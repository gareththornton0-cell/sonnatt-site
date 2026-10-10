// Real providers: Anthropic (script), fal.ai (image + image-to-video), ElevenLabs (voice).
// Each returns null/throws clearly; pipeline.js falls back to demo.js when a key is missing.
import fs from 'node:fs/promises';
import { sleep, download } from './util.js';

const env = (k, d = '') => process.env[k] || d;
export const has = () => ({
  claude: !!env('ANTHROPIC_API_KEY'),
  fal: !!env('FAL_KEY'),
  voice: !!env('ELEVENLABS_API_KEY'),
});

export async function claudeJson(system, user) {
  const r = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'x-api-key': env('ANTHROPIC_API_KEY'), 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
    body: JSON.stringify({ model: env('CLAUDE_MODEL', 'claude-sonnet-5-5'), max_tokens: 4000, system, messages: [{ role: 'user', content: user }] }),
  });
  const j = await r.json();
  if (!r.ok) throw new Error(`Claude: ${j.error?.message || r.status}`);
  const text = j.content.map((c) => c.text || '').join('');
  const a = text.indexOf('{'), b = text.lastIndexOf('}');
  return JSON.parse(text.slice(a, b + 1));
}

async function fal(model, input) {
  const H = { Authorization: `Key ${env('FAL_KEY')}`, 'content-type': 'application/json' };
  const sub = await fetch(`https://queue.fal.run/${model}`, { method: 'POST', headers: H, body: JSON.stringify(input) });
  const job = await sub.json();
  if (!sub.ok) throw new Error(`fal submit: ${JSON.stringify(job).slice(0, 300)}`);
  for (let i = 0; i < 180; i++) { // up to ~15 min
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

const IMAGE_SIZE = { '9:16': 'portrait_16_9', '16:9': 'landscape_16_9', '1:1': 'square_hd' };

export async function falImage(prompt, aspect, outFile) {
  const out = await fal(env('FAL_IMAGE_MODEL', 'fal-ai/flux/dev'), { prompt, image_size: IMAGE_SIZE[aspect], num_images: 1 });
  await download(out.images[0].url, outFile);
}

export async function falVideo(prompt, imageFile, aspect, duration, outFile) {
  const b64 = (await fs.readFile(imageFile)).toString('base64');
  const out = await fal(env('FAL_VIDEO_MODEL', 'fal-ai/kling-video/v2.1/standard/image-to-video'), {
    prompt,
    image_url: `data:image/png;base64,${b64}`,
    duration: String(duration <= 5 ? 5 : 10),
    aspect_ratio: aspect,
  });
  await download(out.video.url, outFile);
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
