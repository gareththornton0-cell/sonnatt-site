// End-to-end smoke test in demo mode (no API keys, no network): npm test
import assert from 'node:assert/strict';
import { mkdtemp } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
process.env.STUDIO_DATA = await mkdtemp(path.join(os.tmpdir(), 'studio-'));
for (const k of ['ANTHROPIC_API_KEY', 'FAL_KEY', 'ELEVENLABS_API_KEY']) delete process.env[k];
const P = await import('./lib/pipeline.js');
const { tpl, get } = await import('./lib/providers.js');
const { startJob } = await import('./lib/jobs.js');
const { saveSettings, settingsView } = await import('./lib/settings.js');

// custom-provider templating
assert.equal(tpl('{{duration}}', { duration: 5 }), 5);
assert.equal(tpl('Bearer {{env.CUSTOM_K}}', {}), 'Bearer ');
assert.equal(tpl('{{env.PATH}}', {}), '', 'env templating must not leak arbitrary variables');
assert.equal(get({ a: { b: [{ c: 7 }] } }, 'a.b.0.c'), 7);

// settings never expose secrets
await saveSettings({ FAL_KEY: 'secret123' });
assert.equal((await settingsView()).FAL_KEY, true);
await assert.rejects(saveSettings({ PATH: 'x' }));
delete process.env.FAL_KEY; await saveSettings({ FAL_KEY: '' });

// brand kit + autopilot (demo) -> final video with outro
await P.setBrand('Test Co', { outroText: 'Visit test.co', outroColor: '#112233' });
const p = await P.createProject({ client: 'Test Co', title: 'T', brief: 'We sell widgets. Fast delivery. Call now.' });
const j = startJob(p.id, 'autopilot', (ctx) => P.autopilot(p.id, ctx));
while (j.status === 'running') await new Promise((r) => setTimeout(r, 200));
assert.equal(j.status, 'done', j.error);
const done = await P.findProject(p.id);
assert.ok(done.final && done.shots.every((s) => s.clip && s.takes.length === 1));
// second take + select
await P.makeClip(p.id, 0, null);
const t = (await P.findProject(p.id)).shots[0];
assert.equal(t.takes.length, 2);
await P.selectTake(p.id, 0, t.takes[0].file);
assert.equal((await P.findProject(p.id)).shots[0].clip, t.takes[0].file);
console.log('ok: autopilot, takes, brand outro, settings, templating');
