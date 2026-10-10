// Catalog of generation models. fal.ai hosts many video models behind one key (Seedance, Kling, Hailuo, Veo, Luma...).
// Any other service (e.g. Higgsfield) plugs in via data/providers.json — see providers.example.json.
import fs from 'node:fs/promises';
import path from 'node:path';
import { DATA } from './settings.js';

const near = (d, list) => list.reduce((a, b) => (Math.abs(b - d) < Math.abs(a - d) ? b : a));
const SIZE = { '9:16': 'portrait_16_9', '16:9': 'landscape_16_9', '1:1': 'square_hd' };

export const VIDEO_MODELS = [
  { id: 'seedance-pro', label: 'Seedance 1 Pro (ByteDance)', model: 'bytedance/seedance/v1/pro/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: String(near(o.duration, [5, 10])), aspect_ratio: o.aspect, resolution: '720p' }) },
  { id: 'seedance-lite', label: 'Seedance 1 Lite (faster, cheaper)', model: 'bytedance/seedance/v1/lite/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: String(near(o.duration, [5, 10])), aspect_ratio: o.aspect, resolution: '720p' }) },
  { id: 'kling-master', label: 'Kling 2.1 Master', model: 'fal-ai/kling-video/v2.1/master/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: String(near(o.duration, [5, 10])), aspect_ratio: o.aspect }) },
  { id: 'kling-standard', label: 'Kling 2.1 Standard', model: 'fal-ai/kling-video/v2.1/standard/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: String(near(o.duration, [5, 10])), aspect_ratio: o.aspect }) },
  { id: 'hailuo', label: 'Hailuo 02 (MiniMax)', model: 'fal-ai/minimax/hailuo-02/standard/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: String(near(o.duration, [6, 10])) }) },
  { id: 'veo3', label: 'Veo 3 (Google, with audio) — check fal for current id', model: 'fal-ai/veo3/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, duration: '8s', generate_audio: false }) },
  { id: 'luma', label: 'Luma Ray 2', model: 'fal-ai/luma-dream-machine/ray-2/image-to-video',
    build: (o) => ({ prompt: o.prompt, image_url: o.image, aspect_ratio: o.aspect, duration: o.duration > 5 ? '9s' : '5s' }) },
];

export const IMAGE_MODELS = [
  { id: 'flux-dev', label: 'Flux Dev', model: 'fal-ai/flux/dev', build: (o) => ({ prompt: o.prompt, image_size: SIZE[o.aspect], num_images: 1 }) },
  { id: 'flux-pro', label: 'Flux Pro 1.1', model: 'fal-ai/flux-pro/v1.1', build: (o) => ({ prompt: o.prompt, image_size: SIZE[o.aspect], num_images: 1 }) },
  { id: 'seedream', label: 'Seedream 4 (ByteDance)', model: 'fal-ai/bytedance/seedream/v4/text-to-image', build: (o) => ({ prompt: o.prompt, image_size: SIZE[o.aspect], num_images: 1 }) },
  { id: 'nano-banana', label: 'Nano Banana (Google)', model: 'fal-ai/nano-banana', build: (o) => ({ prompt: `${o.prompt} (${o.aspect} framing)`, num_images: 1 }) },
];

export async function customProviders() {
  try { const l = JSON.parse(await fs.readFile(path.join(DATA, 'providers.json'), 'utf8')); return Array.isArray(l) ? l : []; } catch { return []; }
}

export async function videoChoices() {
  const custom = await customProviders();
  return [...VIDEO_MODELS.map(({ id, label }) => ({ id, label, via: 'fal' })), ...custom.map((c) => ({ id: `custom:${c.id}`, label: `${c.label || c.id} (custom)`, via: 'custom' }))];
}

export async function resolveVideo(id) {
  if (id?.startsWith('custom:')) {
    const c = (await customProviders()).find((x) => `custom:${x.id}` === id);
    if (!c) throw new Error(`custom provider ${id} not found in data/providers.json`);
    return { via: 'custom', cfg: c, id };
  }
  const m = VIDEO_MODELS.find((x) => x.id === id) || VIDEO_MODELS[0];
  return { via: 'fal', ...m };
}
export const resolveImage = (id) => IMAGE_MODELS.find((x) => x.id === id) || IMAGE_MODELS[0];
