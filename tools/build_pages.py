#!/usr/bin/env python3
"""Builds the Sonnatt.ai inner pages (services, area and pricing pages).

Run from the repo root:  python3 tools/build_pages.py
Each page is written to <slug>/index.html. Content uses only facts the
homepage already states, so the site never contradicts itself. Edit the
PAGES list below and re-run to change wording; the tools/ folder is not
published.
"""
import html, json, os
from articles import ARTICLES

SITE = "https://sonnattai.com"
UPDATED = "2026-10-10"
BOOKING = ""  # Google Calendar appointment-schedule link; keep in step with index.html

NAV = [("/website-design-leeds/", "Websites"), ("/website-chatbot/", "Chatbots"),
       ("/social-media-marketing-leeds/", "Marketing"), ("/custom-apps-automation/", "Apps & automation"),
       ("/pricing/", "Pricing"), ("/guides/", "Guides"), ("/#contact", "Contact")]

PRICING_FACTS = [("Setup", "£995 one-off"), ("Ongoing", "£995 a month"), ("Contract", "cancel with 30 days' notice")]

STEPS = [("We learn your business", "A short discovery session: your services, your customers, what your site needs to do, and the systems you already use."),
         ("We build your presence", "A real person builds your website, chatbot, any custom apps and your marketing, using AI to work quickly, then checks it all with you."),
         ("We run it with you", "We host it, keep it running and handle your marketing every month, with a review call to plan what's next.")]

PAGES = [
  {
    "slug": "website-design-leeds",
    "title": "Website Design in Leeds | Built, Hosted & Run for You | Sonnatt.ai",
    "desc": "Website design for Leeds businesses, built by a real person around your services, then hosted and kept up to date. £995 setup, £995 a month all-in.",
    "crumb": "Website design in Leeds",
    "service": "Website design and hosting",
    "eyebrow": "Website design · Leeds",
    "h1": "Website design in Leeds, built and run for you",
    "lede": "A real person on our team designs and builds your website around your actual services, not a template with your logo on it. Then we host it, keep it running and make changes whenever you need them.",
    "sections": [
      ("What you get", "cards", [
        ("Designed around your business", "Built for your services and your customers, so it explains what you do and makes it easy to get in touch."),
        ("Hosting and updates included", "Hosting and running costs are in the monthly plan. We monitor the site, fix issues and keep everything up to date."),
        ("Built to be found", "We build your site so search engines understand it, and keep your Google Business Profile active so you show up locally."),
        ("A chatbot on every site", "It answers your most-asked questions and captures enquiries day and night. New leads go straight to your inbox."),
        ("Connected to your tools", "Linked to the calendar, booking tool or CRM you already use, so information is entered once."),
        ("Changes handled for you", "Direct access to the team, not a ticket queue, plus a monthly review call."),
      ]),
      ("Already have a website?", "prose", [
        "No problem. We can rebuild it properly or improve what you've got. Either way, we'll look at your current site on the walkthrough call and tell you honestly what we'd change.",
        "Most small-business websites look fine but don't bring in work: they're slow, hard to read on a phone, never updated, and give people no easy way to ask a question. We fix that, then keep it that way every month.",
      ]),
      ("How it works", "steps", STEPS),
      ("What it costs", "prose", [
        "<b>£995 one-off setup</b>: a discovery and strategy session, your website and chatbot built and live, connected to the tools you already use, and a training session for your team.",
        "<b>£995 a month</b>: hosting and running costs, marketing and social media management, a monthly review call and priority support. There's no long contract; you can cancel with 30 days' notice.",
        'See the full breakdown on our <a href="/pricing/">pricing page</a>.',
      ]),
    ],
    "faq": [
      ("How much does a website cost with Sonnatt.ai?", "The website is part of the £995 one-off setup, together with your chatbot, connection to your existing tools and team training. After that it's £995 a month, which covers hosting, marketing and social media management, a monthly review call and priority support."),
      ("Is hosting included?", "Yes. Hosting and running costs are included in the monthly plan. We monitor your site, fix issues and keep everything up to date, so there's nothing extra for you to manage."),
      ("Can you improve my existing website instead of starting again?", "Yes. We can rebuild it properly or improve what you've got. We'll look at your current site on the free walkthrough call and tell you honestly what we'd change."),
      ("How long does it take to build a website?", "It depends on what you need and how much content you already have. We'll give you a clear timeline on the discovery call, before you commit to anything."),
      ("Do you only work with businesses in Leeds?", "We're based in Leeds, West Yorkshire, and work with businesses in Leeds, Bradford and across Yorkshire. If you're further away, get in touch anyway; most of the work can be done remotely."),
    ],
    "related": ["website-chatbot", "social-media-marketing-leeds", "web-design-bradford", "pricing"],
  },
  {
    "slug": "web-design-bradford",
    "title": "Website Design & Marketing in Bradford | Sonnatt.ai",
    "desc": "Website design, chatbots and marketing for Bradford businesses from a Leeds-based team. One dedicated account manager. £995 setup, £995 a month.",
    "crumb": "Bradford",
    "service": "Website design, chatbots and marketing in Bradford",
    "area": "Bradford",
    "eyebrow": "Bradford · West Yorkshire",
    "h1": "Website design and marketing for Bradford businesses",
    "lede": "Sonnatt.ai is based in Leeds, just down the road, and works with businesses across Bradford. One dedicated account manager builds and runs your website, chatbot and marketing, so you're not juggling six freelancers who don't talk to each other.",
    "sections": [
      ("Everything your business needs online", "cards", [
        ("Website build and hosting", "Built by a real person for your real business, then hosted and kept up to date."),
        ("Chatbot and systems", "A chatbot for your site, connected to the calendar, booking tool or CRM you already use."),
        ("Marketing and social growth", "Content, follow-ups, review requests and your Google profile, run for you every month."),
        ("Custom apps and automation", "Simple apps and dashboards built around how you work, and the admin between systems handled."),
      ]),
      ("Who we work with in Bradford", "prose", [
        "We build for real, local businesses that need a proper online presence and a bit of help running it:",
        "<ul><li><b>Letting and property management</b>: a website and chatbot that handle guest queries and viewing bookings.</li><li><b>Accountants and advisers</b>: a professional site and chatbot for client questions, backed by marketing.</li><li><b>Clinics and practices</b>: appointment enquiries and patient questions handled online, off your reception desk.</li><li><b>Salons, gyms and venues</b>: a booking-ready website and chatbot, plus the social content that keeps you full.</li><li><b>Trades and contractors</b>: a site that wins the job before the phone rings, with the admin handled behind it.</li></ul>",
      ]),
      ("How it works", "steps", STEPS),
      ("Same simple pricing", "prose", [
        "Bradford businesses pay the same as everyone else: <b>£995 one-off</b> to build it and <b>£995 a month</b> to run it, with no long contract (cancel with 30 days' notice). Businesses with several sites or branches can use our Scale plan, from £3,000 a month. <a href=\"/pricing/\">Full pricing</a>.",
      ]),
    ],
    "faq": [
      ("Do you work with businesses in Bradford?", "Yes. We're based in Leeds, West Yorkshire, and work with businesses in Bradford, Leeds and across Yorkshire."),
      ("Is the price different for Bradford?", "No. It's £995 one-off for setup and £995 a month to run it, wherever you are in Yorkshire."),
      ("Do we need to meet in person?", "Most of the work can be done remotely: the free walkthrough, the discovery session and the monthly review calls all work over a video call. If you'd prefer to meet, mention it when you get in touch."),
      ("What happens on the free walkthrough?", "It takes 15 minutes. We'll show you what your new site and chatbot could look like, using your own business, before you commit to anything. There's no obligation."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "website-chatbot",
    "title": "Website Chatbot for Small Businesses | Leeds & Bradford | Sonnatt.ai",
    "desc": "A website chatbot that answers your most-asked questions, captures enquiries day and night and connects to your calendar or CRM. Included in the £995 setup.",
    "crumb": "Website chatbots",
    "service": "Website chatbot and systems",
    "eyebrow": "Chatbots & systems",
    "h1": "A website chatbot that answers questions and captures enquiries",
    "lede": "We add a chatbot to your website that answers your most-asked questions and captures enquiries day and night. New leads go straight to your inbox, so you stop losing customers who visit after hours.",
    "sections": [
      ("What your chatbot does", "cards", [
        ("Answers common questions", "Prices, opening hours, what you offer, how to book: the questions your team answers every day."),
        ("Captures enquiries 24/7", "When someone is ready, it collects their name, contact details and what they need, and sends it straight to you."),
        ("Connects to your tools", "Linked to the calendar, booking tool or CRM you already use, so enquiries and bookings land in the right place."),
        ("Written in your voice", "We set it up around your business and check the wording with you before it goes live."),
      ]),
      ("See one working", "prose", [
        'The assistant on <a href="/">our homepage</a> is built the same way. Ask it about pricing or how we work, or ask it to book a call, and you\'ll see exactly what your customers would get.',
        "Once your website and systems are running well, we can also add a personal AI agent trained on your business to handle bookings and repeat questions. That's the next step, not the starting point.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What can a website chatbot do for a small business?", "It answers your most-asked questions, captures enquiries day and night and sends new leads straight to your inbox. It can also be connected to the calendar, booking tool or CRM you already use."),
      ("Is the chatbot included in the price?", "Yes. Your website and chatbot are both built and put live as part of the £995 one-off setup, and running costs are covered by the £995 monthly plan."),
      ("Where do enquiries from the chatbot go?", "Straight to your inbox, and into your live client dashboard so you can see every lead in one place."),
      ("Can the chatbot take bookings?", "It can be connected to the calendar or booking tool you already use, so customers can get booked in without waiting for a reply."),
      ("Do you build AI agents?", "Yes, as a later step. Once your website and systems are running well, we can add a personal AI agent trained on your business to handle bookings and repeat questions."),
    ],
    "related": ["website-design-leeds", "custom-apps-automation", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "social-media-marketing-leeds",
    "title": "Social Media & Marketing Management in Leeds | Sonnatt.ai",
    "desc": "Social posts, Google Business Profile, follow-ups and review requests, run for Leeds and Bradford businesses every month. Part of the £995 monthly plan.",
    "crumb": "Marketing and social media",
    "service": "Marketing and social media management",
    "eyebrow": "Marketing & social growth · Leeds",
    "h1": "Marketing and social media, run for you every month",
    "lede": "Marketing and social growth are part of the monthly plan. We keep you visible on social media and Google, follow up every enquiry and ask happy customers for reviews, all written in your voice and checked with you first.",
    "sections": [
      ("What's included", "cards", [
        ("Regular social posts", "Content planned and posted for you, so your pages stay active without you finding the time."),
        ("Google Business Profile", "Kept active and up to date, so you show up when people nearby search for what you do."),
        ("Automatic follow-ups", "Every enquiry and quote followed up, so leads don't go cold while you're busy working."),
        ("Review requests", "Sent after each job, to build the reviews that help new customers choose you."),
        ("Plain-English reporting", "A live dashboard showing leads, customers, revenue and the marketing we're running for you."),
        ("Local search", "We build your site so search engines understand it and run content that helps you show up locally."),
      ]),
      ("Why one team works better", "prose", [
        "Most small businesses end up with a web designer, a social media freelancer and someone who \"does Google\", none of whom talk to each other. With Sonnatt.ai, one dedicated account manager runs your website, chatbot and marketing together, so every post, follow-up and page points customers the same way.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What marketing is included in the monthly plan?", "Regular social posts, your Google Business Profile, automatic follow-ups on enquiries and quotes, review requests after each job, and plain-English reporting."),
      ("Do I get to approve posts before they go out?", "Yes. Every message is written in your voice and checked with you first."),
      ("Do you manage Google Business Profiles?", "Yes. We keep your Google Business Profile active and up to date as part of the monthly plan, which helps you show up in local searches and on Google Maps."),
      ("How do I see whether the marketing is working?", "Every client gets a live dashboard showing leads, customers, revenue and the marketing and automated tasks we're running for you, reported in plain English."),
      ("Is marketing an extra cost?", "No. Marketing and social media management are included in the £995 monthly plan, along with hosting, a monthly review call and priority support."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "web-design-bradford", "pricing"],
  },
  {
    "slug": "custom-apps-automation",
    "title": "Custom Apps, Dashboards & Workflow Automation | Leeds | Sonnatt.ai",
    "desc": "Simple apps, client portals and dashboards built around how you work, plus automation that ends double data entry. For Leeds and Bradford businesses.",
    "crumb": "Apps and automation",
    "service": "Custom apps and workflow automation",
    "eyebrow": "Custom apps & automation",
    "h1": "Custom apps and automation built around how you work",
    "lede": "When off-the-shelf software doesn't fit how you work, we build a simple app or dashboard around your actual process, and automate the admin between your systems so information is entered once and updated everywhere.",
    "sections": [
      ("What we build", "cards", [
        ("Client portals", "A simple place for your customers to see what they need, without emailing you for it."),
        ("Booking dashboards", "See and manage bookings in one view, connected to the tools you already use."),
        ("Internal trackers", "Replace the spreadsheet everyone's afraid to touch with a purpose-made tool."),
        ("Workflow automation", "The admin between systems, handled: information entered once and updated everywhere."),
      ]),
      ("Hosted and maintained", "prose", [
        "We host every app we build and keep it maintained, so there's nothing for you to look after. Every client also gets a live dashboard showing leads, customers, revenue and the automated tasks we're running for them.",
        "Apps and automation sit alongside your website, chatbot and marketing, all run by the same dedicated account manager.",
      ]),
      ("How it works", "steps", STEPS),
    ],
    "faq": [
      ("What kind of apps do you build?", "Simple, purpose-made apps and dashboards such as client portals, booking dashboards and internal trackers, built around how you actually work."),
      ("What is workflow automation?", "It's handling the admin between your systems automatically, so information is entered once and updated everywhere instead of being copied by hand."),
      ("Who hosts and maintains the app?", "We do. We host it and keep it maintained as part of your plan."),
      ("How much do custom apps cost?", "For a single-site business, apps are part of the standard £995 setup and £995 a month plan; we confirm exactly what's included on the discovery call. Businesses with several sites or many system integrations use our Scale plan, from £3,000 a month, scoped after discovery."),
    ],
    "related": ["website-chatbot", "website-design-leeds", "social-media-marketing-leeds", "pricing"],
  },
  {
    "slug": "pricing",
    "title": "Pricing: £995 Setup, £995 a Month, Everything Included | Sonnatt.ai",
    "desc": "Simple pricing for your website, chatbot and marketing: £995 one-off setup, then £995 a month with no long contract. Scale plan from £3,000 a month.",
    "crumb": "Pricing",
    "service": None,
    "eyebrow": "Pricing",
    "h1": "Simple for most. Scoped for bigger operations.",
    "lede": "One price covers your website, chatbot, hosting, marketing and support, run by one dedicated account manager. No long contract: cancel any time with 30 days' notice.",
    "sections": [
      ("Plans", "plans", [
        ("Setup", "£995", "One-off, paid once", ["Discovery and strategy session", "Your website and chatbot, built and live", "Connected to your existing systems", "Team training session"], False),
        ("Ongoing", "£995<small>/month</small>", "Cancel any time · single-site businesses", ["Hosting and running costs", "Marketing and social media management", "Monthly review call", "Priority support"], True),
        ("Sonnatt Scale", "£3,000<small>+/month</small>", "Custom setup, scoped after discovery", ["Multiple sites and locations", "Multiple system integrations", "Named account manager", "Same-day priority support", "Quarterly strategy reviews"], False),
      ]),
      ("What £995 a month replaces", "prose", [
        "Instead of paying a web designer, a hosting company, a social media freelancer and someone to set up your systems separately, one team builds and runs the whole thing. You get one point of contact, one monthly bill, and a live dashboard showing what your investment is doing.",
        "The 15-minute walkthrough is free and there's no obligation. We'll show you what your new site and chatbot could look like, using your own business, before you commit to anything.",
      ]),
    ],
    "faq": [
      ("How much does Sonnatt.ai cost?", "£995 one-off to build it, then £995 a month to run it. The monthly plan covers hosting and running costs, marketing and social media management, a monthly review call and priority support."),
      ("Is there a contract?", "There's no long contract. You can cancel any time with 30 days' notice."),
      ("What's included in the £995 setup?", "A discovery and strategy session, your website and chatbot built and live, connection to the tools you already use, and a training session for your team."),
      ("What is the Scale plan?", "For businesses with several sites, branches or systems. It starts from £3,000 a month and includes a named account manager, same-day priority support and quarterly strategy reviews. The setup is quoted after a discovery call."),
      ("Is the first call free?", "Yes. The 15-minute walkthrough is free and there's no obligation."),
    ],
    "related": ["website-design-leeds", "website-chatbot", "social-media-marketing-leeds", "custom-apps-automation"],
  },
]

GA = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-V5KS40EXWS"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  // Analytics stays off until the visitor accepts the cookie banner (UK PECR / GDPR).
  var ckChoice = null;
  try { ckChoice = localStorage.getItem('sonnatt_cookie_consent'); } catch (e) {}
  gtag('consent', 'default', {
    analytics_storage: ckChoice === 'granted' ? 'granted' : 'denied',
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'
  });
  gtag('js', new Date());

  gtag('config', 'G-V5KS40EXWS');
</script>"""

def e(s):
    return html.escape(s, quote=True)

def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

PAGE_BY_SLUG = {p["slug"]: p for p in PAGES}

def nav(current):
    def link(href, label, cls=""):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}{cls}>{label}</a>'
    links = "".join(link(h, l) for h, l in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="/"><img src="/img/logo-64.png" width="30" height="30" alt="" decoding="async"><span>Sonnatt<span class="ai">.ai</span></span></a>
    <nav class="links" aria-label="Main">{links}</nav>
    <div class="nav-right">
      <a class="btn btn-sm" href="/#contact" data-book>Book a call</a>
      <button class="nav-toggle" id="navToggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" aria-label="Menu">
    <a href="/">Home</a>{links}
    <a class="btn" href="/#contact" data-book>Book a free call</a>
  </nav>
</header>"""

FOOTER = """<footer>
  <div class="wrap">
    <div class="cols">
      <div><h2>Sonnatt.ai</h2><ul><li>Websites, chatbots and marketing, built and run for you</li><li>Leeds, West Yorkshire</li><li><a href="mailto:info@sonnattai.com">info@sonnattai.com</a></li><li><a href="https://www.instagram.com/sonnatt.ai/" rel="me noopener" target="_blank">Instagram</a></li></ul></div>
      <div><h2>Services</h2><ul><li><a href="/website-design-leeds/">Website design in Leeds</a></li><li><a href="/website-chatbot/">Website chatbots</a></li><li><a href="/social-media-marketing-leeds/">Marketing and social media</a></li><li><a href="/custom-apps-automation/">Custom apps and automation</a></li></ul></div>
      <div><h2>More</h2><ul><li><a href="/pricing/">Pricing</a></li><li><a href="/web-design-bradford/">Bradford</a></li><li><a href="/guides/">Guides</a></li><li><a href="/#faq">FAQ</a></li><li><a href="/#contact">Contact</a></li></ul></div>
    </div>
    <div class="base"><span>© Sonnatt.ai · <a href="/privacy">Privacy policy</a> · <a href="#" data-cookie-settings>Cookie settings</a></span><span>Smarter Business. Real Results.</span></div>
  </div>
</footer>
<div id="ckBanner" role="dialog" aria-label="Cookie choices" hidden>
  <p>We use Google Analytics cookies to see how people use this site and improve it. They only switch on if you accept. <a href="/privacy">Privacy policy</a></p>
  <div class="ck-row"><button type="button" class="ck-yes" id="ckYes">Accept</button><button type="button" id="ckNo">Decline</button></div>
</div>
<script src="/assets/site.js" defer></script>"""

def section_html(title, kind, body):
    out = [f'<section class="block"><div class="wrap">', f"<h2>{e(title)}</h2>"]
    if kind == "cards":
        out.append('<div class="cards">' + "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in body) + "</div>")
    elif kind == "steps":
        out.append('<ol class="steps">' + "".join(f"<li><b>{e(t)}</b>{e(d)}</li>" for t, d in body) + "</ol>")
    elif kind == "prose":
        out.append('<div class="prose">' + "".join(p if p.startswith("<ul") else f"<p>{p}</p>" for p in body) + "</div>")
    elif kind == "plans":
        cards = []
        for name, price, note, items, lit in body:
            cards.append(f'<div class="card{" lit" if lit else ""}"><h3>{e(name)}</h3><div class="price blue-text">{price}</div><p>{e(note)}</p><ul>' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul></div>")
        out.append('<div class="cards">' + "".join(cards) + "</div>")
    out.append("</div></section>")
    return "\n".join(out)

def jsonld(p):
    url = f"{SITE}/{p['slug']}/"
    org = {"@id": f"{SITE}/#organization"}
    graph = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": strip(p["title"]), "description": p["desc"],
         "inLanguage": "en-GB", "isPartOf": {"@id": f"{SITE}/#website"}, "about": org,
         "breadcrumb": {"@id": url + "#breadcrumb"}, "dateModified": UPDATED,
         "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE}/og-image.png", "width": 1200, "height": 630}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    if p.get("service"):
        area = [{"@type": "City", "name": p["area"]}] if p.get("area") else [{"@type": "City", "name": "Leeds"}, {"@type": "City", "name": "Bradford"}, {"@type": "AdministrativeArea", "name": "West Yorkshire"}]
        graph.append({"@type": "Service", "@id": url + "#service", "name": p["service"], "serviceType": p["service"],
                      "description": strip(p["lede"]), "url": url, "provider": org, "areaServed": area,
                      "offers": [{"@type": "Offer", "name": "Setup", "price": "995", "priceCurrency": "GBP"},
                                 {"@type": "Offer", "name": "Ongoing monthly plan", "priceCurrency": "GBP",
                                  "priceSpecification": {"@type": "UnitPriceSpecification", "price": "995", "priceCurrency": "GBP", "unitText": "MONTH"}}]})
    else:
        graph.append({"@type": "OfferCatalog", "@id": url + "#plans", "name": "Sonnatt.ai plans", "itemListElement": [
            {"@type": "Offer", "name": "Setup", "price": "995", "priceCurrency": "GBP", "seller": org},
            {"@type": "Offer", "name": "Ongoing monthly plan", "seller": org, "priceSpecification": {"@type": "UnitPriceSpecification", "price": "995", "priceCurrency": "GBP", "unitText": "MONTH"}},
            {"@type": "Offer", "name": "Sonnatt Scale", "seller": org, "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": "3000", "priceCurrency": "GBP", "unitText": "MONTH"}}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False).replace("</", "<\\/")

def head(title, desc, url, ld, og_type="website", extra=""):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
{GA}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#05090F">
<meta name="sonnatt-booking" content="{e(BOOKING)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-GB" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Sonnatt.ai">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sonnatt.ai: website, chatbot and marketing for Leeds and Bradford businesses">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
{extra}"""

def build(p):
    url = f"{SITE}/{p['slug']}/"
    facts = "".join(f"<li>{e(k)}: <b>{e(v)}</b></li>" for k, v in PRICING_FACTS)
    sections = "\n".join(section_html(*s) for s in p["sections"])
    faq = "\n".join(f'<details class="faq-i"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p["faq"])
    related = "".join(f'<li><a href="/{s}/">{e(PAGE_BY_SLUG[s]["crumb"])} →</a></li>' for s in p["related"])
    return head(p["title"], p["desc"], url, jsonld(p)) + f"""</head>
<body>
{nav('/' + p['slug'] + '/')}
<main id="main">
  <div class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">{e(p['crumb'])}</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">{e(p['eyebrow'])}</div>
      <h1>{e(p['h1'])}</h1>
      <p class="lede">{e(p['lede'])}</p>
      <ul class="facts">{facts}</ul>
      <div class="cta"><a class="btn" href="/#contact" data-book>Book a free 15-minute call</a><a class="quiet" href="mailto:info@sonnattai.com">Email info@sonnattai.com →</a></div>
    </div>
  </div>
{sections}
  <section class="block" id="faq"><div class="wrap">
    <h2>Frequently asked questions</h2>
    <div class="faq">
{faq}
    </div>
  </div></section>
  <section class="cta-band"><div class="wrap">
    <h2>See what your business could look like online</h2>
    <p>15 minutes, free, no obligation. We'll show you what your new site and chatbot could look like, using your own business, before you commit to anything.</p>
    <div class="cta"><a class="btn" href="/#contact" data-book>Book a free 15-minute call</a><a class="quiet" href="mailto:info@sonnattai.com">Or email info@sonnattai.com →</a></div>
    <ul class="related" aria-label="Related pages">{related}</ul>
  </div></section>
</main>
{FOOTER}
</body>
</html>
"""

def article_ld(a, url):
    org = {"@id": f"{SITE}/#organization"}
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": url + "#article", "headline": a["h1"], "description": a["desc"], "url": url,
         "mainEntityOfPage": url, "inLanguage": "en-GB", "datePublished": a["published"], "dateModified": a["updated"],
         "author": org, "publisher": org, "image": f"{SITE}/og-image.png", "abstract": a["summary"],
         "isPartOf": {"@id": f"{SITE}/guides/#webpage"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{SITE}/guides/"},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
    ]}, indent=1, ensure_ascii=False).replace("</", "<\\/")

def nice_date(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def build_article(a):
    url = f"{SITE}/guides/{a['slug']}/"
    faq = "\n".join(f'<details class="faq-i"><summary>{e(q)}</summary><p>{e(ans)}</p></details>' for q, ans in a["faq"])
    related = "".join(f'<li><a href="/{s}/">{e(PAGE_BY_SLUG[s]["crumb"])} →</a></li>' for s in a["related"])
    more = "".join(f'<li><a href="/guides/{o["slug"]}/">{e(o["h1"])} →</a></li>' for o in ARTICLES if o is not a)
    extra = f'<meta property="article:published_time" content="{a["published"]}">\n<meta property="article:modified_time" content="{a["updated"]}">\n'
    return head(a["title"], a["desc"], url, article_ld(a, url), "article", extra) + f"""</head>
<body>
{nav('/guides/')}
<main id="main">
  <article>
  <div class="page-hero">
    <div class="wrap narrow">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/guides/">Guides</a></li><li aria-current="page">{e(a['h1'])}</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">Guide · {e(a['read'])}</div>
      <h1 class="article-h1">{e(a['h1'])}</h1>
      <p class="byline">By the Sonnatt.ai team, Leeds · Updated <time datetime="{a['updated']}">{nice_date(a['updated'])}</time></p>
      <div class="summary"><b>The short answer</b><p>{e(a['summary'])}</p></div>
    </div>
  </div>
  <section class="block"><div class="wrap narrow prose article-body">
{a['body']}
  </div></section>
  <section class="block" id="faq"><div class="wrap narrow">
    <h2>Frequently asked questions</h2>
    <div class="faq">
{faq}
    </div>
  </div></section>
  </article>
  <section class="cta-band"><div class="wrap">
    <h2>Want this handled for you?</h2>
    <p>Sonnatt.ai builds and runs websites, chatbots and marketing for Leeds and Bradford businesses. The 15-minute walkthrough is free and there's no obligation.</p>
    <div class="cta"><a class="btn" href="/#contact" data-book>Book a free 15-minute call</a><a class="quiet" href="mailto:info@sonnattai.com">Or email info@sonnattai.com →</a></div>
    <ul class="related" aria-label="Related pages">{related}{more}</ul>
  </div></section>
</main>
{FOOTER}
</body>
</html>
"""

def build_guides_index():
    url = f"{SITE}/guides/"
    title = "Guides for Small Business Websites & Marketing | Sonnatt.ai"
    desc = "Plain-English guides for Leeds and Bradford small businesses on websites, chatbots, Google Business Profile and getting found online."
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "en-GB",
         "isPartOf": {"@id": f"{SITE}/#website"}, "publisher": {"@id": f"{SITE}/#organization"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": f"{SITE}/guides/{a['slug']}/", "name": a["h1"]} for i, a in enumerate(ARTICLES)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": url}]},
    ]}, indent=1, ensure_ascii=False).replace("</", "<\\/")
    cards = "".join(f'<a class="card guide-card" href="/guides/{a["slug"]}/"><span class="eyebrow">{e(a["read"])}</span><h2>{e(a["h1"])}</h2><p>{e(a["desc"])}</p><span class="quiet">Read the guide →</span></a>' for a in ARTICLES)
    return head(title, desc, url, ld) + f"""</head>
<body>
{nav('/guides/')}
<main id="main">
  <div class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Guides</li></ol></nav>
      <div class="eyebrow" style="margin-top:28px">Guides</div>
      <h1>Plain-English guides for small businesses</h1>
      <p class="lede">Straight answers on websites, chatbots and getting found on Google, written for small businesses in Leeds, Bradford and across Yorkshire.</p>
    </div>
  </div>
  <section class="block"><div class="wrap"><div class="cards guides">{cards}</div></div></section>
  <section class="cta-band"><div class="wrap">
    <h2>Rather have it done for you?</h2>
    <p>One dedicated account manager builds and runs your website, chatbot and marketing. £995 setup, £995 a month, cancel with 30 days' notice.</p>
    <div class="cta"><a class="btn" href="/#contact" data-book>Book a free 15-minute call</a><a class="quiet" href="/pricing/">See pricing →</a></div>
  </div></section>
</main>
{FOOTER}
</body>
</html>
"""

if __name__ == "__main__":
    for a in ARTICLES:
        os.makedirs(os.path.join("guides", a["slug"]), exist_ok=True)
        with open(os.path.join("guides", a["slug"], "index.html"), "w") as f:
            f.write(build_article(a))
        print("built guides/" + a["slug"])
    with open(os.path.join("guides", "index.html"), "w") as f:
        f.write(build_guides_index())
    print("built guides/")

    for p in PAGES:
        os.makedirs(p["slug"], exist_ok=True)
        with open(os.path.join(p["slug"], "index.html"), "w") as f:
            f.write(build(p))
        print("built", p["slug"])
