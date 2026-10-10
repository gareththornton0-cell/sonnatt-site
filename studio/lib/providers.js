// Live provider calls. pipeline.js falls back to demo.js when a provider's key is missing.
import fs from 'node:fs/promises';
import { sleep, download } from './util.js';
import { customProviders } from './registry.js';

const env = (k, d = '') => process.env[k] || d;
export async function has() {
  return {
    claude: !!env('ANTHROPIC_API_KEY'),
    fal: !!env('FAL_KEY'),
    voice: !!env('ELEVENLABS_API_KEY'),
    custom: (await customProviders()).map((c) => c.id),
  };
}

export async function claudeJson(system, user) {
  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': env('ANTHROPIC_API_KEY'), 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: env('CLAUDE_MODEL', 'claude-sonnet-5-5'), max_tokens: 4000, system, messages: [{ role: 'user', content: user }] }),
  });
  const j = await r.json();
  if (!r.ok) throw new Error(`Claude: ${j.error?.message || r.status}`);
  const text = j.content.map((c) => c.text || '').join('');
  try { return JSON.parse(text.slice(text.indexOf('{'), text.lastIndexOf('}') + 1)); }
  catch { throw new Error('Claude returned something that was not valid JSON; try again'); }
}

async function fal(model, input) {
  const H = { Authorization: `Key ${env('FAL_KEY')}`, 'content-type': 'application/json' };
  const sub = await fetch(`https://queue.fal.run/${model}`, { method: 'POST', headers: H, body: JSON.stringify(input) });
  const job = await sub.json().catch(() => ({}));
  if (!sub.ok) throw new Error(`fal ${model}: ${JSON.stringify(job).slice(0, 300)}`);
  for (let i = 0; i < 180; i++) { // ~15 min
    await sleep(5000);
    const s = await (await fetch(job.status_url, { headers: H })).json();
    if (s.status === 'COMPLETED') {
      const res = await fetch(job.response_url, { headers: H });
      const out = await res.json();
      if (!res.ok) throw new Error(`fal result: ${JSON.stringify(out).slice(0, 300)}`);
      return out;
    }
    if (s.status && !['IN_QUEUE', 'IN_PROGRESS'].includes(s.status)) throw new Error(`fal status ${s.status}`);
  }
  throw new Error('fal timed out');
}

export async function falImage(m, o, outFile) {
  const out = await fal(m.model, m.build(o));
  await download(out.images[0].url, outFile);
}

export const dataUri = async (file) => `data:image/png;base64,${(await fs.readFile(file)).toString('base64')}`;

export async function falVideo(m, o, outFile) {
  const out = await fal(m.model, m.build({ ...o, image: await dataUri(o.imageFile) }));
  await download((out.video || out.videos?.[0]).url, outFile);
}

// ---- custom HTTP provider (Higgsfield or anything else), described in data/providers.json
const get = (o, p) => String(p).split('.').reduce((a, k) => (a == null ? a : a[k]), o);
const envName = (n) => (/^(CUSTOM|HIGGSFIELD)_/.test(n) ? process.env[n] || '' : '');
function tpl(v, vars) {
  if (typeof v === 'string') {
    const whole = v.match(/^\{\{(\w+)\}\}$/);
    if (whole && typeof vars[whole[1]] === 'number') return vars[whole[1]];
    return v.replace(/\{\{(env\.)?(\w+)\}\}/g, (_, e, k) => String(e ? envName(k) : vars[k] ?? ''));
  }
  if (Array.isArray(v)) return v.map((x) => tpl(x, vars));
  if (v && typeof v === 'object') return Object.fromEntries(Object.entries(v).map(([k, x]) => [k, tpl(x, vars)]));
  return v;
}
export { tpl, get };

export async function customVideo(cfg, o, outFile) {
  const vars = { prompt: o.prompt, image: await dataUri(o.imageFile), duration: o.duration, aspect: o.aspect };
  const s = tpl(cfg.submit, vars);
  const r = await fetch(s.url, { method: s.method || 'POST', headers: s.headers, body: JSON.stringify(s.body) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(`${cfg.id}: ${JSON.stringify(j).slice(0, 300)}`);
  let result = get(j, cfg.resultPath);
  vars.id = get(j, cfg.idPath);
  for (let i = 0; !result && i < 180; i++) {
    await sleep(5000);
    const p = tpl(cfg.poll, vars);
    const pj = await (await fetch(p.url, { headers: p.headers })).json();
    const st = String(get(pj, p.statusPath)).toLowerCase();
    if ((p.failValues || []).includes(st)) throw new Error(`${cfg.id} failed: ${JSON.stringify(pj).slice(0, 200)}`);
    if ((p.doneValues || []).includes(st)) result = get(pj, cfg.resultPath);
  }
  if (!result) throw new Error(`${cfg.id}: no result URL (check resultPath in providers.json)`);
  await download(result, outFile);
}

export async function elevenVoice(text, voiceId, outFile) {
  const r = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId || env('ELEVENLABS_VOICE_ID', '21m00Tcm4TlvDq8ikWAM')}`, {
    method: 'POST',
    headers: { 'xi-api-key': env('ELEVENLABS_API_KEY'), 'content-type': 'application/json', accept: 'audio/mpeg' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2' }),
  });
  if (!r.ok) throw new Error(`ElevenLabs ${r.status}: ${(await r.text()).slice(0, 200)}`);
  await fs.writeFile(outFile, Buffer.from(await r.arrayBuffer()));
}
