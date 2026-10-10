import fs from 'node:fs/promises';
import path from 'node:path';
import { slug, uid, readJson, writeJson, run, DIMS } from './util.js';
import * as real from './providers.js';
import * as demo from './demo.js';

export const DATA = path.resolve(import.meta.dirname, '..', 'data');
const dirOf = (p) => path.join(DATA, slug(p.client), p.id);

export async function listProjects() {
  const out = [];
  for (const c of await fs.readdir(DATA).catch(() => []))
    for (const id of await fs.readdir(path.join(DATA, c)).catch(() => [])) {
      const p = await readJson(path.join(DATA, c, id, 'project.json'));
      if (p) out.push(p);
    }
  return out.sort((a, b) => b.created.localeCompare(a.created));
}

export async function findProject(id) {
  const p = (await listProjects()).find((x) => x.id === id);
  if (!p) throw new Error('project not found');
  return p;
}

const save = (p) => writeJson(path.join(dirOf(p), 'project.json'), p);
const rel = (p, f) => `/files/${slug(p.client)}/${p.id}/${f}`;

export async function createProject({ client, title, brief, aspect = '9:16', style = 'polished 3D animated mascot, soft studio lighting' }) {
  if (!client || !title || !brief) throw new Error('client, title and brief are required');
  const p = { id: uid(), client, title, brief, aspect, style, created: new Date().toISOString(), character: null, shots: [], final: null, log: [] };
  await fs.mkdir(dirOf(p), { recursive: true });
  await save(p);
  return p;
}

export async function updateProject(id, patch) {
  const p = await findProject(id);
  for (const k of ['title', 'brief', 'aspect', 'style', 'character', 'shots', 'voiceId'])
    if (patch[k] !== undefined) p[k] = patch[k];
  await save(p);
  return p;
}

const SYSTEM = `You are a creative director making short social video ads for brands.
Return ONLY JSON: {"character":{"name":"","description":"","imagePrompt":""},"shots":[{"visual":"","dialogue":"","duration":5}]}.
Rules: 3-6 shots, duration 5 or 10 seconds each, dialogue is spoken to camera (max ~25 words per shot), the visual describes camera + action in one sentence, the imagePrompt describes ONE consistent character in detail (face, clothing, colours, style). Do not claim anything about the brand that the brief does not state.`;

export async function makeScript(id) {
  const p = await findProject(id);
  let r;
  if (real.has().claude) r = await real.claudeJson(SYSTEM, `Brand/client: ${p.client}\nVideo title: ${p.title}\nAspect: ${p.aspect}\nStyle: ${p.style}\nBrief:\n${p.brief}`);
  else r = demo.demoScript(p);
  p.character = { ...r.character, image: null };
  p.shots = r.shots.map((s, i) => ({ n: i, ...s, clip: null, voice: null }));
  p.final = null;
  p.log.push(real.has().claude ? 'script: claude' : 'script: DEMO');
  await save(p);
  return p;
}

export async function makeCharacter(id) {
  const p = await findProject(id);
  if (!p.character) throw new Error('write the script first');
  const f = `character-${uid()}.png`;
  const out = path.join(dirOf(p), f);
  const prompt = `${p.character.imagePrompt}. ${p.style}. Full face visible, looking at camera, clean background.`;
  if (real.has().fal) await real.falImage(prompt, p.aspect, out);
  else await demo.demoImage(prompt, p.aspect, out);
  p.character.image = f;
  p.log.push(real.has().fal ? 'character: fal' : 'character: DEMO');
  await save(p);
  return p;
}

export async function makeClip(id, n) {
  const p = await findProject(id);
  const s = p.shots[n];
  if (!s) throw new Error('no such shot');
  if (!p.character?.image) throw new Error('generate the character first');
  const f = `shot-${n}-${uid()}.mp4`;
  const img = path.join(dirOf(p), p.character.image);
  const prompt = `${p.character.description}. ${s.visual}. The character is speaking naturally to camera.`;
  if (real.has().fal) await real.falVideo(prompt, img, p.aspect, s.duration, path.join(dirOf(p), f));
  else await demo.demoVideo(prompt, img, p.aspect, s.duration, path.join(dirOf(p), f));
  s.clip = f;
  p.final = null;
  p.log.push(`clip ${n}: ${real.has().fal ? 'fal' : 'DEMO'}`);
  await save(p);
  return p;
}

export async function makeVoice(id, n) {
  const p = await findProject(id);
  const s = p.shots[n];
  if (!s) throw new Error('no such shot');
  const f = `voice-${n}-${uid()}.mp3`;
  const out = path.join(dirOf(p), f);
  if (real.has().voice) await real.elevenVoice(s.dialogue, p.voiceId, out);
  else await demo.demoVoice(s.dialogue, out);
  s.voice = f;
  p.final = null;
  p.log.push(`voice ${n}: ${real.has().voice ? 'elevenlabs' : 'DEMO (silent)'}`);
  await save(p);
  return p;
}

const dur = async (f) => parseFloat(await run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]));
const ts = (t) => { const h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = (t % 60).toFixed(3).padStart(6, '0'); return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${s.replace('.', ',')}`; };

export async function assemble(id) {
  const p = await findProject(id);
  const dir = dirOf(p);
  if (!p.shots.length || p.shots.some((s) => !s.clip)) throw new Error('every shot needs a clip');
  const [w, h] = DIMS[p.aspect];
  const parts = []; let srt = '', t = 0;
  for (const s of p.shots) {
    const v = await dur(path.join(dir, s.clip));
    const a = s.voice ? await dur(path.join(dir, s.voice)) : 0;
    const len = Math.max(v, a);
    const part = `_part-${s.n}.mp4`;
    const audio = s.voice ? ['-i', s.voice] : ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo'];
    await run('ffmpeg', ['-y', '-i', s.clip, ...audio,
      '-filter_complex', `[0:v]scale=${w}:${h}:force_original_aspect_ratio=increase,crop=${w}:${h},fps=30,tpad=stop_mode=clone:stop_duration=30,format=yuv420p[v];[1:a]aresample=44100,aformat=channel_layouts=stereo,apad[a]`,
      '-map', '[v]', '-map', '[a]', '-t', len.toFixed(3), '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '160k', part], { cwd: dir });
    srt += `${s.n + 1}\n${ts(t)} --> ${ts(t + len)}\n${s.dialogue}\n\n`;
    parts.push(part); t += len;
  }
  await fs.writeFile(path.join(dir, '_list.txt'), parts.map((x) => `file '${x}'`).join('\n'));
  await fs.writeFile(path.join(dir, 'captions.srt'), srt);
  await run('ffmpeg', ['-y', '-f', 'concat', '-safe', '0', '-i', '_list.txt', '-c', 'copy', '_joined.mp4'], { cwd: dir });
  // libass sizes are relative to a 288px-high canvas, so these scale with any aspect ratio
  const style = 'Fontname=DejaVu Sans,Bold=1,FontSize=11,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=1,Outline=1.5,Alignment=2,MarginV=30';
  const f = `final-${uid()}.mp4`;
  await run('ffmpeg', ['-y', '-i', '_joined.mp4', '-vf', `subtitles=captions.srt:force_style='${style}'`, '-c:v', 'libx264', '-crf', '20', '-c:a', 'copy', '-movflags', '+faststart', f], { cwd: dir });
  p.final = f;
  p.log.push(`assembled ${t.toFixed(1)}s`);
  await save(p);
  return p;
}

export const view = (p) => ({
  ...p,
  urls: {
    character: p.character?.image && rel(p, p.character.image),
    final: p.final && rel(p, p.final),
    captions: p.final && rel(p, 'captions.srt'),
    clips: p.shots.map((s) => s.clip && rel(p, s.clip)),
    voices: p.shots.map((s) => s.voice && rel(p, s.voice)),
  },
});
