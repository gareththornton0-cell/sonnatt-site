import fs from 'node:fs/promises';
import path from 'node:path';
import { slug, uid, readJson, writeJson, run, DIMS } from './util.js';
import { DATA } from './settings.js';
import * as real from './providers.js';
import * as demo from './demo.js';
import { resolveVideo, resolveImage } from './registry.js';
import { limiter, retry } from './jobs.js';

export { DATA };
const clientDir = (c) => path.join(DATA, slug(c));
const dirOf = (p) => path.join(clientDir(p.client), p.id);
const rel = (p, f) => `/files/${slug(p.client)}/${p.id}/${f}`;

/* ---------- storage ---------- */
async function entries(dir) { return fs.readdir(dir, { withFileTypes: true }).catch(() => []); }

export async function listProjects() {
  const out = [];
  for (const c of await entries(DATA)) if (c.isDirectory())
    for (const d of await entries(path.join(DATA, c.name))) if (d.isDirectory()) {
      const p = await readJson(path.join(DATA, c.name, d.name, 'project.json'));
      if (p) out.push(p);
    }
  return out.sort((a, b) => b.created.localeCompare(a.created));
}
export async function findProject(id) {
  if (!/^\w+$/.test(id)) throw new Error('bad id');
  for (const c of await entries(DATA)) if (c.isDirectory()) {
    const p = await readJson(path.join(DATA, c.name, id, 'project.json'));
    if (p) return p;
  }
  throw new Error('project not found');
}
const save = (p) => writeJson(path.join(dirOf(p), 'project.json'), p);

// Serialise read-modify-write so parallel shots can't clobber each other.
const locks = new Map();
export function mutate(id, fn) {
  const next = (locks.get(id) || Promise.resolve()).then(async () => { const p = await findProject(id); await fn(p); await save(p); return p; });
  locks.set(id, next.catch(() => {}));
  return next;
}

/* ---------- brand kits (per client) ---------- */
export async function getBrand(client) { return (await readJson(path.join(clientDir(client), 'brand.json'))) || {}; }
export async function setBrand(client, patch) {
  const keys = ['voice', 'notes', 'style', 'outroText', 'outroColor', 'textColor', 'voiceId', 'videoModel', 'imageModel', 'logo', 'music'];
  const b = await getBrand(client);
  for (const k of keys) if (patch[k] !== undefined) b[k] = String(patch[k]).slice(0, 2000);
  await fs.mkdir(clientDir(client), { recursive: true });
  await writeJson(path.join(clientDir(client), 'brand.json'), b);
  return b;
}
export async function listClients() {
  const out = [];
  for (const c of await entries(DATA)) if (c.isDirectory()) out.push({ slug: c.name, brand: await readJson(path.join(DATA, c.name, 'brand.json'), {}) });
  return out;
}

export async function saveUpload({ client, projectId, kind, name, data }) {
  const ext = (path.extname(String(name)).toLowerCase().match(/^\.(png|jpe?g|webp|mp3|wav|m4a)$/) || [])[1];
  if (!ext) throw new Error('unsupported file type (png, jpg, webp, mp3, wav, m4a)');
  const buf = Buffer.from(String(data), 'base64');
  if (!buf.length || buf.length > 40e6) throw new Error('file empty or over 40MB');
  if (kind === 'character') {
    const p = await findProject(projectId);
    const f = `character-${uid()}.${ext}`;
    await fs.writeFile(path.join(dirOf(p), f), buf);
    return mutate(projectId, (x) => { x.character = { ...(x.character || { name: 'Uploaded', description: x.title, imagePrompt: x.title }), image: f }; x.log.push('character: uploaded'); });
  }
  if (kind !== 'logo' && kind !== 'music') throw new Error('bad upload kind');
  const f = `${kind}-${uid()}.${ext}`;
  await fs.mkdir(clientDir(client), { recursive: true });
  await fs.writeFile(path.join(clientDir(client), f), buf);
  return setBrand(client, { [kind]: f });
}

/* ---------- projects ---------- */
export async function createProject({ client, title, brief, aspect = '9:16', style, videoModel, imageModel }) {
  if (!client?.trim() || !title?.trim() || !brief?.trim()) throw new Error('client, title and brief are required');
  if (!DIMS[aspect]) throw new Error('bad aspect');
  const brand = await getBrand(client);
  const p = {
    id: uid(), client: client.trim(), title: title.trim(), brief, aspect,
    style: style || brand.style || 'polished 3D animated mascot, soft studio lighting',
    videoModel: videoModel || brand.videoModel || 'seedance-pro', imageModel: imageModel || brand.imageModel || 'flux-dev',
    voiceId: brand.voiceId || '', created: new Date().toISOString(), character: null, shots: [], final: null, log: [],
  };
  await fs.mkdir(dirOf(p), { recursive: true });
  await save(p);
  return p;
}

export function updateProject(id, patch) {
  return mutate(id, (p) => {
    for (const k of ['title', 'brief', 'aspect', 'style', 'character', 'shots', 'voiceId', 'videoModel', 'imageModel'])
      if (patch[k] !== undefined) p[k] = patch[k];
  });
}

/* ---------- generation steps ---------- */
const SYSTEM = `You are a creative director making short social video ads for brands.
Return ONLY JSON: {"character":{"name":"","description":"","imagePrompt":""},"shots":[{"visual":"","dialogue":"","duration":5}]}.
Rules: 3-6 shots, duration 5 or 10 seconds each, dialogue is spoken to camera (max ~25 words per shot), the visual describes camera + action in one sentence, the imagePrompt describes ONE consistent character in detail (face, clothing, colours, style). Do not claim anything about the brand that the brief does not state (no invented prices, awards, stats or testimonials).`;

export async function makeScript(id, ctx) {
  const p = await findProject(id), brand = await getBrand(p.client);
  const live = (await real.has()).claude;
  ctx?.log(live ? 'Claude is writing the script…' : 'Writing demo script (no Claude key)');
  const r = live
    ? await real.claudeJson(SYSTEM, `Brand/client: ${p.client}\nBrand voice: ${brand.voice || 'friendly, clear'}\nBrand notes: ${brand.notes || '-'}\nVideo title: ${p.title}\nAspect: ${p.aspect}\nStyle: ${p.style}\nBrief:\n${p.brief}`)
    : demo.demoScript(p);
  if (!r?.character || !Array.isArray(r.shots) || !r.shots.length) throw new Error('script came back malformed; try again');
  await mutate(id, (x) => {
    x.character = { ...r.character, image: null };
    x.shots = r.shots.slice(0, 8).map((s, i) => ({ n: i, visual: String(s.visual), dialogue: String(s.dialogue), duration: Number(s.duration) || 5, takes: [], clip: null, voice: null }));
    x.final = null; x.log.push(live ? 'script: claude' : 'script: DEMO');
  });
}

export async function makeCharacter(id, ctx) {
  const p = await findProject(id);
  if (!p.character) throw new Error('write the script first');
  const m = resolveImage(p.imageModel), live = (await real.has()).fal;
  const f = `character-${uid()}.png`, out = path.join(dirOf(p), f);
  const prompt = `${p.character.imagePrompt}. ${p.style}. Full face visible, looking at camera, clean background.`;
  ctx?.log(`Generating character (${live ? m.label : 'demo'})…`);
  if (live) await retry(() => real.falImage(m, { prompt, aspect: p.aspect }, out), ctx); else await demo.demoImage(prompt, p.aspect, out);
  await mutate(id, (x) => { x.character.image = f; x.log.push(`character: ${live ? m.id : 'DEMO'}`); });
}

export async function makeClip(id, n, ctx, { model } = {}) {
  const p = await findProject(id), s = p.shots[n];
  if (!s) throw new Error('no such shot');
  if (!p.character?.image) throw new Error('generate or upload the character first');
  const pick = await resolveVideo(model || s.model || p.videoModel);
  const h = await real.has();
  const live = pick.via === 'fal' ? h.fal : h.custom.includes(pick.cfg.id);
  const f = `shot-${n}-${uid()}.mp4`, out = path.join(dirOf(p), f);
  const o = { prompt: `${p.character.description}. ${s.visual}. The character is speaking naturally to camera.`, imageFile: path.join(dirOf(p), p.character.image), aspect: p.aspect, duration: s.duration };
  ctx?.log(`Shot ${n + 1}: animating with ${live ? pick.label || pick.id : 'demo'}…`);
  if (!live) await demo.demoVideo(o.prompt, o.imageFile, p.aspect, s.duration, out);
  else if (pick.via === 'fal') await retry(() => real.falVideo(pick, o, out), ctx);
  else await retry(() => real.customVideo(pick.cfg, o, out), ctx);
  await mutate(id, (x) => {
    const sh = x.shots[n];
    sh.takes = [...(sh.takes || []), { file: f, model: live ? pick.id : 'DEMO', at: new Date().toISOString() }];
    sh.clip = f; x.final = null; x.log.push(`clip ${n + 1}: ${live ? pick.id : 'DEMO'}`);
  });
}

export const selectTake = (id, n, file) => mutate(id, (x) => {
  const t = x.shots[n]?.takes?.find((k) => k.file === file);
  if (!t) throw new Error('no such take');
  x.shots[n].clip = file; x.final = null;
});

export async function makeVoice(id, n, ctx) {
  const p = await findProject(id), s = p.shots[n];
  if (!s) throw new Error('no such shot');
  const live = (await real.has()).voice;
  const f = `voice-${n}-${uid()}.mp3`, out = path.join(dirOf(p), f);
  ctx?.log(`Shot ${n + 1}: voice (${live ? 'ElevenLabs' : 'demo/silent'})…`);
  if (live) await retry(() => real.elevenVoice(s.dialogue, p.voiceId, out), ctx); else await demo.demoVoice(s.dialogue, out);
  await mutate(id, (x) => { x.shots[n].voice = f; x.final = null; x.log.push(`voice ${n + 1}: ${live ? 'elevenlabs' : 'DEMO (silent)'}`); });
}

/* One click: fills in whatever is missing, then assembles. Safe to re-run; it only generates what's absent. */
export async function autopilot(id, ctx) {
  let p = await findProject(id);
  if (!p.shots.length) { await makeScript(id, ctx); p = await findProject(id); }
  if (!p.character?.image) { await makeCharacter(id, ctx); p = await findProject(id); }
  const gate = limiter(3);
  const work = [];
  p.shots.forEach((s, i) => {
    if (!s.voice) work.push(gate(() => makeVoice(id, i, ctx)));
    if (!s.clip) work.push(gate(() => makeClip(id, i, ctx)));
  });
  const res = await Promise.allSettled(work);
  const bad = res.filter((r) => r.status === 'rejected');
  if (bad.length) throw new Error(`${bad.length} step(s) failed: ${bad[0].reason.message}. Fix and press Autopilot again; finished steps are kept.`);
  await assemble(id, ctx);
}

/* ---------- assembly ---------- */
const dur = async (f) => parseFloat(await run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]));
const ts = (t) => { const h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = (t % 60).toFixed(3).padStart(6, '0'); return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${s.replace('.', ',')}`; };
const hex = (c, d) => (/^#?[0-9a-f]{6}$/i.test(c || '') ? c.replace('#', '') : d);

export async function assemble(id, ctx) {
  const p = await findProject(id), brand = await getBrand(p.client), dir = dirOf(p);
  if (!p.shots.length || p.shots.some((s) => !s.clip)) throw new Error('every shot needs a clip');
  const [w, h] = DIMS[p.aspect];
  ctx?.log('Assembling final video…');
  const parts = []; let srt = '', t = 0;
  for (const s of p.shots) {
    const v = await dur(path.join(dir, s.clip));
    const a = s.voice ? await dur(path.join(dir, s.voice)) : 0;
    const len = Math.max(v, a), part = `_part-${s.n}.mp4`;
    const audio = s.voice ? ['-i', s.voice] : ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo'];
    await run('ffmpeg', ['-y', '-i', s.clip, ...audio,
      '-filter_complex', `[0:v]scale=${w}:${h}:force_original_aspect_ratio=increase,crop=${w}:${h},fps=30,tpad=stop_mode=clone:stop_duration=30,format=yuv420p[v];[1:a]aresample=44100,aformat=channel_layouts=stereo,apad[a]`,
      '-map', '[v]', '-map', '[a]', '-t', len.toFixed(3), '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '160k', part], { cwd: dir });
    srt += `${s.n + 1}\n${ts(t)} --> ${ts(t + len)}\n${s.dialogue}\n\n`;
    parts.push(part); t += len;
  }
  if (brand.outroText || brand.logo) { // branded end card
    await fs.writeFile(path.join(dir, '_outro.txt'), String(brand.outroText || '').replace(/(.{1,24})(\s|$)/g, '$1\n'));
    const logo = brand.logo && path.join(clientDir(p.client), brand.logo);
    const fnt = demo.FONT ? `fontfile=${demo.FONT}:` : '';
    const txt = `drawtext=${fnt}textfile=_outro.txt:fontcolor=0x${hex(brand.textColor, 'FFFFFF')}:fontsize=${Math.round(w / 14)}:x=(w-text_w)/2:y=(h*0.62)`;
    const inputs = ['-f', 'lavfi', '-i', `color=c=0x${hex(brand.outroColor, '0F172A')}:s=${w}x${h}:d=2.5:r=30`];
    let fc = `[0:v]${txt}[bg]`;
    if (logo) { inputs.push('-i', logo); fc += `;[1:v]scale=${Math.round(w * 0.5)}:-1[lg];[bg][lg]overlay=(W-w)/2:(H*0.3)[o]`; } else fc += ';[bg]null[o]';
    await run('ffmpeg', ['-y', ...inputs, '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-filter_complex', `${fc};[o]format=yuv420p[v]`,
      '-map', '[v]', '-map', `${logo ? 2 : 1}:a`, '-t', '2.5', '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '160k', '_outro.mp4'], { cwd: dir });
    parts.push('_outro.mp4');
  }
  await fs.writeFile(path.join(dir, '_list.txt'), parts.map((x) => `file '${x}'`).join('\n'));
  await fs.writeFile(path.join(dir, 'captions.srt'), srt);
  await run('ffmpeg', ['-y', '-f', 'concat', '-safe', '0', '-i', '_list.txt', '-c', 'copy', '_joined.mp4'], { cwd: dir });
  // libass sizes are relative to a 288px-high canvas, so these scale with any aspect ratio
  const style = 'Fontname=DejaVu Sans,Bold=1,FontSize=11,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=1,Outline=1.5,Alignment=2,MarginV=30';
  const f = `final-${uid()}.mp4`;
  const music = brand.music && path.join(clientDir(p.client), brand.music);
  const args = ['-y', '-i', '_joined.mp4'];
  if (music) args.push('-stream_loop', '-1', '-i', music);
  args.push('-filter_complex', `[0:v]subtitles=captions.srt:force_style='${style}'[v]${music ? ';[1:a]volume=0.12[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]' : ''}`,
    '-map', '[v]', '-map', music ? '[a]' : '0:a', '-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', f);
  await run('ffmpeg', args, { cwd: dir });
  await mutate(id, (x) => { x.final = f; x.log.push(`assembled ${t.toFixed(1)}s${music ? ' +music' : ''}${brand.outroText || brand.logo ? ' +outro' : ''}`); });
}

export const view = (p) => ({
  ...p,
  urls: {
    character: p.character?.image && rel(p, p.character.image),
    final: p.final && rel(p, p.final),
    captions: p.final && rel(p, 'captions.srt'),
    clips: p.shots.map((s) => s.clip && rel(p, s.clip)),
    voices: p.shots.map((s) => s.voice && rel(p, s.voice)),
    takes: p.shots.map((s) => (s.takes || []).map((k) => ({ ...k, url: rel(p, k.file) }))),
  },
});
