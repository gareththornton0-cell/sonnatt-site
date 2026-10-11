import "jsr:@supabase/functions-js/edge-runtime.d.ts";

// Free website checker for sonnattai.com/check/. Fetches one public web page and scores the basics a
// small business site needs: security, speed, mobile, Google listing and ways to capture enquiries.
// Public (no login), so it only ever fetches public http(s) addresses, never private or internal ones,
// reads at most 2MB, follows at most 3 redirects and returns only the computed checks, never the page.
// Deploy: supabase functions deploy site-check --no-verify-jwt

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "content-type, apikey, authorization, x-client-info",
};
const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...CORS, "Content-Type": "application/json" } });

const MAX_BYTES = 2_000_000;
const hits = new Map<string, number[]>();   // best-effort rate limit per caller IP, per instance

function privateV4(ip: string) {
  const p = ip.split(".").map(Number);
  if (p.length !== 4 || p.some((n) => isNaN(n))) return true;
  const [a, b] = p;
  return a === 0 || a === 10 || a === 127 || a >= 224 || (a === 169 && b === 254) || (a === 172 && b >= 16 && b <= 31) ||
    (a === 192 && b === 168) || (a === 100 && b >= 64 && b <= 127) || (a === 192 && b === 0) || (a === 198 && (b === 18 || b === 19));
}
function privateV6(ip: string) {
  const s = ip.toLowerCase();
  return s === "::" || s === "::1" || s.startsWith("fc") || s.startsWith("fd") || s.startsWith("fe8") || s.startsWith("fe9") ||
    s.startsWith("fea") || s.startsWith("feb") || s.startsWith("::ffff:") || s.startsWith("64:ff9b") || s.startsWith("ff");
}

async function safeUrl(raw: string): Promise<URL> {
  const u = new URL(raw);
  if (u.protocol !== "http:" && u.protocol !== "https:") throw new Error("Only web addresses (http or https) can be checked.");
  if (u.port && u.port !== "80" && u.port !== "443") throw new Error("That address uses an unusual port.");
  if (u.username || u.password) throw new Error("That address can't be checked.");
  const host = u.hostname.replace(/^\[|\]$/g, "");
  if (!host.includes(".") || /^\d+\.\d+\.\d+\.\d+$/.test(host) || host.includes(":") || /\.(local|internal|localhost)$/i.test(host)) {
    throw new Error("Enter your website's public address, like yourbusiness.co.uk.");
  }
  let v4: string[] = [], v6: string[] = [];
  try { v4 = await Deno.resolveDns(host, "A"); } catch (_) { /* none */ }
  try { v6 = await Deno.resolveDns(host, "AAAA"); } catch (_) { /* none */ }
  if (!v4.length && !v6.length) throw new Error("We couldn't find that website. Check the address and try again.");
  if (v4.some(privateV4) || v6.some(privateV6)) throw new Error("That address can't be checked.");
  return u;
}

async function fetchPage(start: URL) {
  let url = start;
  const t0 = Date.now();
  for (let i = 0; i < 4; i++) {
    const res = await fetch(url, {
      redirect: "manual",
      signal: AbortSignal.timeout(10_000),
      headers: { "User-Agent": "Mozilla/5.0 (compatible; SonnattSiteCheck/1.0; +https://sonnattai.com/check/)", Accept: "text/html" },
    });
    if (res.status >= 300 && res.status < 400 && res.headers.get("location")) {
      await res.body?.cancel();
      url = await safeUrl(new URL(res.headers.get("location")!, url).toString());
      continue;
    }
    const reader = res.body?.getReader();
    const chunks: Uint8Array[] = [];
    let size = 0;
    if (reader) {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        size += value.length;
        if (size > MAX_BYTES) { await reader.cancel(); break; }
        chunks.push(value);
      }
    }
    const buf = new Uint8Array(Math.min(size, MAX_BYTES));
    let off = 0;
    for (const c of chunks) { buf.set(c.subarray(0, buf.length - off), off); off += c.length; if (off >= buf.length) break; }
    return { res, url, ms: Date.now() - t0, size, html: new TextDecoder().decode(buf) };
  }
  throw new Error("That website redirects too many times.");
}

const CHAT_VENDORS: [string, RegExp][] = [
  ["Sonnatt.ai", /sonnattai\.com\/widget\.js/i], ["Tidio", /tidio/i], ["Intercom", /intercom/i], ["Crisp", /crisp\.chat/i],
  ["Drift", /drift\.com|js\.driftt/i], ["LiveChat", /livechatinc|cdn\.livechat/i], ["Tawk.to", /tawk\.to/i],
  ["HubSpot chat", /js\.hs-scripts|hubspot.*conversations|usemessages/i], ["Zendesk", /zopim|zdassets|zendesk/i],
  ["Chatbase", /chatbase\.co/i], ["Facebook Messenger", /customerchat/i], ["WhatsApp button", /wa\.me\/|api\.whatsapp\.com/i],
];
// A hand-built chat with no third-party script, recognised by its markup.
const OWN_CHAT = /<(?:div|aside|section|button)[^>]+(?:id|class)=["'][^"']*\b(?:chat-?(?:bot|widget|launcher|panel)|cbLaunch)\b/i;

const decode = (s: string) => s
  .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
  .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(Number(d)))
  .replace(/&quot;/g, '"').replace(/&apos;|&#39;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&");

function analyse(html: string, finalUrl: URL, ms: number, size: number) {
  const head = (html.match(/<head[\s\S]*?<\/head>/i) || [html.slice(0, 60000)])[0];
  const meta = (name: string) => {
    const re = new RegExp(`<meta[^>]+(?:name|property)=["']${name}["'][^>]*>`, "i");
    const tag = head.match(re)?.[0] || "";
    return decode((tag.match(/content=["']([^"']*)["']/i)?.[1] || "").trim());
  };
  const title = decode((head.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1] || "").replace(/\s+/g, " ").trim());
  const desc = meta("description");
  const viewport = /<meta[^>]+name=["']viewport["']/i.test(head);
  const h1 = /<h1[\s>]/i.test(html);
  const ogImage = !!meta("og:image");
  const schema = /application\/ld\+json/i.test(html);
  const localSchema = /"@type"\s*:\s*"(LocalBusiness|[A-Za-z]*(Store|Shop|Salon|Restaurant|Dentist|Clinic|Agent|Accountant|Service|Business|Contractor|Plumber|Electrician|Physician|Hotel))"/i.test(html);
  const chat = CHAT_VENDORS.filter(([, re]) => re.test(html)).map(([n]) => n);
  if (!chat.length && OWN_CHAT.test(html)) chat.push("built-in chat");
  const form = /<form[\s>]/i.test(html);
  const tel = /href=["']tel:/i.test(html);
  const mail = /href=["']mailto:/i.test(html);
  const analytics = /googletagmanager\.com|google-analytics\.com|gtag\(|plausible\.io|fathom|clarity\.ms/i.test(html);
  const https = finalUrl.protocol === "https:";
  const kb = Math.round(size / 1024);
  const scripts = (html.match(/<script[\s>]/gi) || []).length;
  const imgs = html.match(/<img[^>]*>/gi) || [];
  const noAlt = imgs.filter((t) => !/\balt=/i.test(t)).length;
  const speed = ms < 1000 ? `${ms}ms` : `${(ms / 1000).toFixed(1)}s`;

  const checks = [
    { id: "https", group: "Security", pass: https, weight: 12, label: "Secure connection (HTTPS)",
      fix: "Your site isn't served securely. Browsers show 'Not secure', which puts customers off. Add an SSL certificate (often free)." },
    { id: "speed", group: "Speed", pass: ms < 1500, warn: ms < 3000, weight: 12, label: `Page downloaded in ${speed}`,
      fix: "Your page is slow to load. Better hosting or caching usually fixes this; slow sites lose visitors and Google ranking." },
    { id: "weight", group: "Speed", pass: kb < 400, warn: kb < 1200, weight: 6, label: `Page HTML is ${kb}KB`,
      fix: "The page itself is heavy, which slows phones on mobile data. Trimming page builders and inline code helps." },
    { id: "viewport", group: "Mobile", pass: viewport, weight: 12, label: viewport ? "Set up for phones" : "Not set up for phones",
      fix: "Your site isn't set up to fit phone screens. Most local searches happen on a phone, and Google ranks mobile-friendly sites higher." },
    { id: "title", group: "Google", pass: title.length >= 10 && title.length <= 65, warn: title.length > 0, weight: 8,
      label: title ? `Page title (${title.length} characters): "${title.slice(0, 80)}"` : "Page title missing",
      fix: "Your page title is what Google shows as the blue link, and it's cut off after about 60 characters. Keep it to 10–65 characters with your service and town, e.g. 'Hair Salon in Leeds | Studio Name'." },
    { id: "desc", group: "Google", pass: desc.length >= 50 && desc.length <= 170, warn: desc.length > 0, weight: 8,
      label: desc ? `Google description is ${desc.length} characters` : "Google description missing",
      fix: "Add a meta description of 50–160 characters. It's the text under your link on Google, and a good one gets more clicks." },
    { id: "h1", group: "Google", pass: h1, weight: 4, label: h1 ? "Main heading on the page" : "No main heading",
      fix: "The page has no main (H1) heading, so Google has less to go on about what you do." },
    { id: "schema", group: "Google", pass: localSchema, warn: schema, weight: 6, label: localSchema ? "Business details marked up for Google" : "No business details for Google",
      fix: "Add 'LocalBusiness' structured data (address, hours, phone) so Google can show your details directly in search and Maps." },
    { id: "social", group: "Google", pass: ogImage, weight: 3, label: ogImage ? "Preview image when shared" : "No preview image when shared",
      fix: "When someone shares your site on WhatsApp or Facebook there's no preview image. Add an og:image." },
    { id: "chat", group: "Enquiries", pass: chat.length > 0, weight: 12, label: chat.length ? `Chat on site: ${chat.join(", ")}` : "No chat or instant-reply option",
      fix: "Visitors can't get an instant answer. A website chatbot answers common questions 24/7 and captures enquiries while you're busy or closed." },
    { id: "contact", group: "Enquiries", pass: form && (tel || mail), warn: form || tel || mail, weight: 10,
      label: [form && "enquiry form", tel && "tap-to-call", mail && "email link"].filter(Boolean).join(", ") || "No enquiry form or tap-to-call",
      fix: "Make it easy to get in touch from the homepage: an enquiry form plus a tap-to-call phone link." },
    { id: "analytics", group: "Enquiries", pass: analytics, weight: 4, label: analytics ? "Visitor analytics installed" : "No visitor analytics",
      fix: "You can't see how many people visit or where they come from. Add Google Analytics (free) so you know what's working." },
    { id: "alt", group: "Mobile", pass: imgs.length === 0 || noAlt === 0, warn: noAlt <= 3, weight: 3,
      label: imgs.length ? `${imgs.length - noAlt} of ${imgs.length} images described` : "No images to check",
      fix: "Some images have no description (alt text). It helps blind visitors and helps Google understand your pictures." },
  ];
  let got = 0, total = 0;
  for (const c of checks) { total += c.weight; got += c.pass ? c.weight : (c as { warn?: boolean }).warn ? c.weight / 2 : 0; }
  return {
    url: finalUrl.toString(), score: Math.round((got / total) * 100), ms, kb, scripts,
    checks: checks.map((c) => ({ id: c.id, group: c.group, label: c.label, status: c.pass ? "pass" : (c as { warn?: boolean }).warn ? "warn" : "fail", fix: c.pass ? "" : c.fix })),
  };
}

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
  if (req.method !== "POST") return json({ error: "Use POST." }, 405);
  const ip = (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() || "unknown";
  const now = Date.now(), recent = (hits.get(ip) || []).filter((t) => now - t < 60 * 60 * 1000);
  if (recent.length >= 20) return json({ error: "You've run a lot of checks. Please try again in an hour." }, 429);
  recent.push(now); hits.set(ip, recent);

  let raw = "";
  try { raw = String((await req.json())?.url || "").trim().slice(0, 300); } catch (_) { /* ignore */ }
  if (!raw) return json({ error: "Enter your website address." }, 400);
  if (!/^https?:\/\//i.test(raw)) raw = "https://" + raw;
  try {
    const start = await safeUrl(raw);
    let page;
    try { page = await fetchPage(start); }
    catch (e) {
      if (start.protocol === "https:" && !(e instanceof Error && /redirect/.test(e.message))) {
        start.protocol = "http:";   // the site may not support HTTPS at all; that's itself a finding
        page = await fetchPage(start);
      } else throw e;
    }
    if (page.res.status >= 400) return json({ error: `That website returned an error (${page.res.status}). Check the address.` }, 422);
    if (!/text\/html|application\/xhtml/i.test(page.res.headers.get("content-type") || "text/html")) {
      return json({ error: "That address isn't a web page." }, 422);
    }
    return json(analyse(page.html, page.url, page.ms, page.size));
  } catch (e) {
    const msg = e instanceof Error ? e.message : "";
    const friendly = /couldn't|can't|Enter|unusual|Only|redirects/.test(msg) ? msg : "We couldn't reach that website. Check the address and try again.";
    return json({ error: friendly }, 422);
  }
});
