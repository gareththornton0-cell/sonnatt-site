// Offline stand-ins so the whole pipeline runs without any API keys.
import fs from 'node:fs/promises';
import path from 'node:path';
import { run, DIMS } from './util.js';

import { existsSync } from 'node:fs';
export const FONT = ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf', 'C:/Windows/Fonts/arialbd.ttf'].find(existsSync) || '';

export function demoScript(p) {
  const base = p.brief.split(/[.!?]\s/).filter(Boolean);
  const lines = [
    `Hey! Quick question: ${base[0] || p.title}?`,
    `Here is what ${p.client} does differently. ${base[1] || ''}`.trim(),
    `Ready to try it? Tap the link and say hello to ${p.client}.`,
  ];
  return {
    character: { name: 'Demo Mascot', description: `Friendly brand mascot for ${p.client}`, imagePrompt: `Friendly mascot for ${p.client}, ${p.style}` },
    shots: lines.map((dialogue, i) => ({ visual: `Mascot speaks to camera, scene ${i + 1}`, dialogue, duration: 5 })),
  };
}

async function card(text, aspect, outFile, dir) {
  const [w, h] = DIMS[aspect];
  const tf = path.join(dir, '_card.txt');
  await fs.writeFile(tf, text.replace(/(.{1,28})(\s|$)/g, '$1\n'));
  await run('ffmpeg', ['-y', '-f', 'lavfi', '-i', `color=c=0x0f172a:s=${w}x${h}`, '-vf', `drawtext=${FONT ? `fontfile=${FONT}:` : ''}textfile=${tf}:fontcolor=white:fontsize=${Math.round(w / 18)}:x=(w-text_w)/2:y=(h-text_h)/2`, '-frames:v', '1', outFile]);
}

export const demoImage = (prompt, aspect, outFile) => card(`[DEMO IMAGE]\n${prompt}`, aspect, outFile, path.dirname(outFile));

export async function demoVideo(prompt, imageFile, aspect, duration, outFile) {
  const [w, h] = DIMS[aspect];
  await run('ffmpeg', ['-y', '-loop', '1', '-i', imageFile, '-vf', `zoompan=z='min(zoom+0.0015,1.3)':d=${duration * 30}:s=${w}x${h}:fps=30,format=yuv420p`, '-t', String(duration), '-c:v', 'libx264', outFile]);
}

export async function demoVoice(text, outFile) {
  const secs = Math.max(2, text.split(/\s+/).length * 0.4);
  await run('ffmpeg', ['-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', String(secs), '-c:a', 'libmp3lame', outFile]);
}
