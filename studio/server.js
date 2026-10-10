import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { loadSettings, saveSettings, settingsView, DATA } from './lib/settings.js';
import { has } from './lib/providers.js';
import { videoChoices } from './lib/registry.js';
import { IMAGE_MODELS } from './lib/registry.js';
import { startJob, listJobs } from './lib/jobs.js';
import * as P from './lib/pipeline.js';

await loadSettings();
const PORT = Number(process.env.PORT || 4747);
const UI = path.resolve(import.meta.dirname, 'ui');
const TYPES = { '.html': 'text/html; charset=utf-8', '.mp4': 'video/mp4', '.mp3': 'audio/mpeg', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.wav': 'audio/wav', '.m4a': 'audio/mp4', '.srt': 'text/plain; charset=utf-8' };
const LOCAL = new Set([`localhost:${PORT}`, `127.0.0.1:${PORT}`]);

const send = (res, code, b, type = 'application/json') => { res.writeHead(code, { 'content-type': type, 'x-content-type-options': 'nosniff' }); res.end(typeof b === 'string' || Buffer.isBuffer(b) ? b : JSON.stringify(b)); };
const readBody = async (req, max = 60e6) => {
  let n = 0; const chunks = [];
  for await (const c of req) { n += c.length; if (n > max) throw new Error('request too large'); chunks.push(c); }
  const s = Buffer.concat(chunks).toString();
  return s ? JSON.parse(s) : {};
};

// This server holds API keys and spends money: refuse anything not from the local UI (blocks DNS-rebinding and cross-site POSTs).
function guard(req) {
  if (!LOCAL.has(req.headers.host)) return 'bad host';
  const o = req.headers.origin;
  if (o && !LOCAL.has(new URL(o).host)) return 'bad origin';
  if (req.method !== 'GET' && !o && req.headers['sec-fetch-site'] && req.headers['sec-fetch-site'] !== 'same-origin') return 'bad origin';
  return null;
}

const job = (res, projectId, label, fn) => send(res, 202, { job: startJob(projectId, label, fn) });

async function api(req, res, url) {
  const m = (re) => url.pathname.match(re), method = req.method;
  let r;
  if (url.pathname === '/api/config') return send(res, 200, { providers: await has(), videoModels: await videoChoices(), imageModels: IMAGE_MODELS.map(({ id, label }) => ({ id, label })), settings: await settingsView() });
  if (url.pathname === '/api/settings' && method === 'PUT') { await saveSettings(await readBody(req)); return send(res, 200, { ok: true }); }
  if (url.pathname === '/api/jobs') return send(res, 200, listJobs(url.searchParams.get('project')));
  if (url.pathname === '/api/clients') return send(res, 200, await P.listClients());
  if ((r = m(/^\/api\/brand\/([^/]+)$/))) {
    const client = decodeURIComponent(r[1]);
    if (method === 'GET') return send(res, 200, await P.getBrand(client));
    if (method === 'PUT') return send(res, 200, await P.setBrand(client, await readBody(req)));
  }
  if (url.pathname === '/api/upload' && method === 'POST') {
    const b = await readBody(req);
    const out = await P.saveUpload(b);
    return send(res, 200, b.kind === 'character' ? P.view(out) : out);
  }
  if (url.pathname === '/api/projects' && method === 'GET') return send(res, 200, (await P.listProjects()).map(P.view));
  if (url.pathname === '/api/projects' && method === 'POST') return send(res, 200, P.view(await P.createProject(await readBody(req))));
  if ((r = m(/^\/api\/projects\/(\w+)$/))) {
    if (method === 'GET') return send(res, 200, P.view(await P.findProject(r[1])));
    if (method === 'PUT') return send(res, 200, P.view(await P.updateProject(r[1], await readBody(req))));
  }
  if ((r = m(/^\/api\/projects\/(\w+)\/(script|character|autopilot|assemble)$/)) && method === 'POST') {
    const [, id, what] = r;
    await P.findProject(id);
    const fn = { script: P.makeScript, character: P.makeCharacter, autopilot: P.autopilot, assemble: P.assemble }[what];
    return job(res, id, what, (ctx) => fn(id, ctx));
  }
  if ((r = m(/^\/api\/projects\/(\w+)\/shots\/(\d+)\/(clip|voice|select)$/)) && method === 'POST') {
    const [, id, n, what] = r, i = Number(n), b = await readBody(req);
    await P.findProject(id);
    if (what === 'select') return send(res, 200, P.view(await P.selectTake(id, i, b.file)));
    return job(res, id, `${what} ${i + 1}`, (ctx) => (what === 'clip' ? P.makeClip(id, i, ctx, { model: b.model }) : P.makeVoice(id, i, ctx)));
  }
  send(res, 404, { error: 'not found' });
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  const bad = guard(req);
  if (bad) return send(res, 403, { error: bad });
  try {
    if (url.pathname.startsWith('/api/')) return await api(req, res, url);
    if (url.pathname.startsWith('/files/')) {
      const f = path.join(DATA, ...decodeURIComponent(url.pathname.slice(7)).split('/').filter((x) => x && x !== '..' && x !== 'settings.json'));
      if (path.basename(f) === 'settings.json' || !TYPES[path.extname(f)]) return send(res, 404, { error: 'not found' });
      return send(res, 200, await fs.readFile(f), TYPES[path.extname(f)]);
    }
    send(res, 200, await fs.readFile(path.join(UI, 'index.html')), 'text/html; charset=utf-8');
  } catch (e) {
    console.error(e.message);
    send(res, e.code === 'ENOENT' ? 404 : 400, { error: e.message });
  }
});
server.requestTimeout = 0;
server.listen(PORT, '127.0.0.1', async () => console.log(`Sonnatt Studio on http://localhost:${PORT}`, await has()));
