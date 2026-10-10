import { uid, sleep } from './util.js';

const jobs = new Map();

export function startJob(projectId, label, fn) {
  const j = { id: uid(), projectId, label, status: 'running', steps: [], error: null, started: Date.now(), ended: null };
  jobs.set(j.id, j);
  if (jobs.size > 200) jobs.delete(jobs.keys().next().value);
  Promise.resolve().then(() => fn({ log: (m) => j.steps.push(m) }))
    .then(() => { j.status = 'done'; }, (e) => { j.status = 'error'; j.error = e.message; })
    .finally(() => { j.ended = Date.now(); });
  return j;
}
export const listJobs = (projectId) => [...jobs.values()].filter((j) => !projectId || j.projectId === projectId).slice(-20);

export function limiter(n) {
  let active = 0; const q = [];
  const next = () => {
    if (active >= n || !q.length) return;
    active++;
    const { fn, res, rej } = q.shift();
    fn().then(res, rej).finally(() => { active--; next(); });
  };
  return (fn) => new Promise((res, rej) => { q.push({ fn, res, rej }); next(); });
}

export async function retry(fn, ctx, n = 2) {
  for (let i = 0; ; i++) {
    try { return await fn(); } catch (e) {
      if (i >= n) throw e;
      ctx?.log(`retrying (${i + 1}/${n}): ${e.message.slice(0, 120)}`);
      await sleep(2000 * (i + 1));
    }
  }
}
