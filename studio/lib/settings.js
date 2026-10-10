// API keys live in data/settings.json (mode 600, git-ignored), never in the UI bundle or API responses.
import fs from 'node:fs/promises';
import path from 'node:path';

export const DATA = process.env.STUDIO_DATA ? path.resolve(process.env.STUDIO_DATA) : path.resolve(import.meta.dirname, '..', 'data');
const FILE = path.join(DATA, 'settings.json');
const ALLOWED = /^(ANTHROPIC_API_KEY|FAL_KEY|ELEVENLABS_API_KEY|ELEVENLABS_VOICE_ID|(CUSTOM|HIGGSFIELD)_[A-Z0-9_]+)$/;
const SECRET = (k) => k !== 'ELEVENLABS_VOICE_ID';

async function read() { try { return JSON.parse(await fs.readFile(FILE, 'utf8')); } catch { return {}; } }

export async function loadSettings() {
  for (const [k, v] of Object.entries(await read())) if (ALLOWED.test(k) && v && !process.env[k]) process.env[k] = v;
}

export async function saveSettings(patch) {
  const cur = await read();
  for (const [k, v] of Object.entries(patch)) {
    if (!ALLOWED.test(k)) throw new Error(`setting not allowed: ${k}`);
    if (typeof v !== 'string' || v.length > 500) throw new Error(`bad value for ${k}`);
    if (v.trim()) { cur[k] = v.trim(); process.env[k] = v.trim(); } else { delete cur[k]; delete process.env[k]; }
  }
  await fs.mkdir(DATA, { recursive: true });
  await fs.writeFile(FILE, JSON.stringify(cur, null, 2), { mode: 0o600 });
  await fs.chmod(FILE, 0o600);
}

// Booleans for secrets; plain value only for non-secret ids.
export async function settingsView() {
  const cur = await read(); const out = {};
  for (const k of Object.keys({ ...cur, ...Object.fromEntries(['ANTHROPIC_API_KEY', 'FAL_KEY', 'ELEVENLABS_API_KEY', 'ELEVENLABS_VOICE_ID'].map((x) => [x, 1])) }))
    out[k] = SECRET(k) ? !!process.env[k] : process.env[k] || '';
  return out;
}
