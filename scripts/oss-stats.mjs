// Collects Felix's contributions to repositories he does not own from the
// GitHub search API and writes them to src/data/oss.json, which the
// OpenSourceCard renders at build time (no API call from the browser).
//
// Usage: GITHUB_TOKEN=... node scripts/oss-stats.mjs
import { readFileSync, writeFileSync } from 'node:fs';

const USER = 'felix-helleckes';
const OUT = new URL('../src/data/oss.json', import.meta.url);
const LATEST = 5;

async function search(query) {
  const items = [];
  let total = 0;
  for (let page = 1; page <= 10; page++) {
    const url = `https://api.github.com/search/issues?q=${encodeURIComponent(query)}&per_page=100&page=${page}`;
    const res = await fetch(url, {
      headers: {
        Accept: 'application/vnd.github+json',
        'User-Agent': `${USER}-oss-stats`,
        ...(process.env.GITHUB_TOKEN && {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
        }),
      },
    });
    if (!res.ok) {
      throw new Error(`${res.status} ${res.statusText} for "${query}"`);
    }
    const data = await res.json();
    total = data.total_count;
    items.push(...data.items);
    if (items.length >= total || data.items.length < 100) break;
  }
  return { total, items };
}

const repoName = (item) => item.repository_url.split('/repos/')[1];
const base = `author:${USER} -user:${USER}`;

const [merged, open, issues] = await Promise.all([
  search(`${base} type:pr is:merged`),
  search(`${base} type:pr is:open`),
  search(`${base} type:issue`),
]);

const repos = new Map();
const repo = (name) => {
  if (!repos.has(name)) {
    repos.set(name, {
      name,
      url: `https://github.com/${name}`,
      merged: 0,
      open: 0,
    });
  }
  return repos.get(name);
};
merged.items.forEach((item) => repo(repoName(item)).merged++);
open.items.forEach((item) => repo(repoName(item)).open++);

const stats = {
  merged: merged.total,
  open: open.total,
  issues: issues.total,
  repos: [...repos.values()].sort(
    (a, b) =>
      b.merged - a.merged || b.open - a.open || a.name.localeCompare(b.name),
  ),
  latestMerged: merged.items
    .map((item) => ({
      title: item.title,
      url: item.html_url,
      repo: repoName(item),
      mergedAt: item.pull_request.merged_at ?? item.closed_at,
    }))
    .sort(
      (a, b) =>
        b.mergedAt.localeCompare(a.mergedAt) || b.url.localeCompare(a.url),
    )
    .slice(0, LATEST),
};

// Only touch the file (and its date) when the numbers or PRs changed, so the
// daily run does not commit and redeploy for nothing.
let previous = null;
try {
  previous = JSON.parse(readFileSync(OUT, 'utf8'));
} catch {
  // first run
}
const { updatedAt: _, ...previousStats } = previous ?? {};
if (previous && JSON.stringify(previousStats) === JSON.stringify(stats)) {
  console.log('oss.json unchanged');
} else {
  const updatedAt = new Date().toISOString().slice(0, 10);
  writeFileSync(OUT, JSON.stringify({ updatedAt, ...stats }, null, 2) + '\n');
  console.log(
    `oss.json written: ${stats.merged} merged, ${stats.open} open, ${stats.issues} issues`,
  );
}
