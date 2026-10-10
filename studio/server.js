import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { has } from './lib/providers.js';
import * as P from './lib/pipeline.js';

const PORT = Number(process.env.PORT || 4747);
const UI = path.resolve(import.meta.dirname, 'ui');
const TYPES = { '.html': 'text/html', '.mp4': 'video/mp4', '.mp3': 'audio/mpeg', '.png': 'image/png', '.srt': 'text/plain' };

const send = (res, code, body, type = 'application/json') => { res.writeHead(code, { 'content-type': type }); res.end(typeof body === 'string' || Buffer.isBuffer(body) ? body : JSON.stringify(body)); };
const body = async (req) => { let s = ''; for await (const c of req) s += c; return s ? JSON.parse(s) : {}; };

async function api(req, res, url) {
  const m = (re) => url.pathname.match(re);
  const method = req.method;
  let r;
  if (url.pathname === '/api/config') return send(res, 200, { providers: has() });
  if (url.pathname === '/api/projects' && method === 'GET') return send(res, 200, (await P.listProjects()).map(P.view));
  if (url.pathname === '/api/projects' && method === 'POST') return send(res, 200, P.view(await P.createProject(await body(req))));
  if ((r = m(/^\/api\/projects\/(\w+)$/))) {
    if (method === 'GET') return send(res, 200, P.view(await P.findProject(r[1])));
    if (method === 'PUT') return send(res, 200, P.view(await P.updateProject(r[1], await body(req))));
  }
  if ((r = m(/^\/api\/projects\/(\w+)\/(script|character|assemble)$/)) && method === 'POST') {
    const fn = { script: P.makeScript, character: P.makeCharacter, assemble: P.assemble }[r[2]];
    return send(res, 200, P.view(await fn(r[1])));
  }
  if ((r = m(/^\/api\/projects\/(\w+)\/shots\/(\d+)\/(clip|voice)$/)) && method === 'POST') {
    const fn = r[3] === 'clip' ? P.makeClip : P.makeVoice;
    return send(res, 200, P.view(await fn(r[1], Number(r[2]))));
  }
  send(res, 404, { error: 'not found' });
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  try {
    if (url.pathname.startsWith('/api/')) return await api(req, res, url);
    if (url.pathname.startsWith('/files/')) {
      const f = path.join(P.DATA, ...decodeURIComponent(url.pathname.slice(7)).split('/').filter((x) => x && x !== '..'));
      return send(res, 200, await fs.readFile(f), TYPES[path.extname(f)] || 'application/octet-stream');
    }
    send(res, 200, await fs.readFile(path.join(UI, 'index.html')), 'text/html');
  } catch (e) {
    console.error(e.message);
    send(res, 500, { error: e.message });
  }
});
server.requestTimeout = 0; // generation calls can take minutes
server.listen(PORT, '127.0.0.1', () => console.log(`Sonnatt Studio on http://localhost:${PORT}`, has()));
