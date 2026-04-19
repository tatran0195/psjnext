// CI script: fetch old version content from GitHub branches → content/api/X.Y.Z
// Run before `next build` (see prebuild in package.json).
//
// Usage:
//   npx tsx scripts/fetch-docs.ts
//   FORCE_FETCH=1 npx tsx scripts/fetch-docs.ts   # skip cache check
//
// Requires: GITHUB_TOKEN (optional but strongly recommended)
//   Unauthenticated: 60 req/h | Authenticated: 5000 req/h

import { createWriteStream } from 'node:fs';
import fs from 'node:fs/promises';
import path from 'node:path';
import { pipeline } from 'node:stream/promises';

const PROJECT_ROOT = process.cwd();
const TIMEOUT_MS = 30_000;
const MAX_RETRIES = 3;

// ── Config ────────────────────────────────────────────────────────────────────
//
// Only declare versions with sourceType: 'github' in lib/versions.ts.
// Key must match canonical version key.

type FetchTarget = {
    version: string; // canonical key, e.g. '5.1.0'
    repo: string; // 'org/repo'
    branch: string; // 'release/5.1.0'
    subdir: string; // subdirectory in branch, e.g. 'docs/api'
};

const FETCH_TARGETS: FetchTarget[] = [
    {
        version: '5.1.0',
        repo: 'your-org/your-repo',
        branch: 'release/5.1.0',
        subdir: 'docs/api',
    },
    {
        version: '5.0.1',
        repo: 'your-org/your-repo',
        branch: 'release/5.0.1',
        subdir: 'docs/api',
    },
];

// ── HTTP helpers ──────────────────────────────────────────────────────────────

function buildHeaders(): Record<string, string> {
    const headers: Record<string, string> = {
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'docs-fetch-script/1.0',
    };
    const token = process.env['GITHUB_TOKEN'];
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    } else {
        console.warn('  [warn] GITHUB_TOKEN not set — rate limit: 60 req/h');
    }
    return headers;
}

async function fetchWithRetry(url: string, attempt = 1): Promise<Response> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
    try {
        const res = await fetch(url, {
            headers: buildHeaders(),
            signal: controller.signal,
            redirect: 'follow',
        });
        if (!res.ok) {
            if (res.status === 429 && attempt < MAX_RETRIES) {
                const after = parseInt(res.headers.get('retry-after') ?? '5', 10);
                console.warn(`  [warn] Rate limited, retry after ${after}s`);
                await sleep(after * 1000);
                return fetchWithRetry(url, attempt + 1);
            }
            if (res.status >= 500 && attempt < MAX_RETRIES) {
                await sleep(1000 * attempt);
                return fetchWithRetry(url, attempt + 1);
            }
            throw new Error(`HTTP ${res.status} ${res.statusText}`);
        }
        return res;
    } finally {
        clearTimeout(timer);
    }
}

function sleep(ms: number) {
    return new Promise<void>((r) => setTimeout(r, ms));
}

// ── ZIP extraction ────────────────────────────────────────────────────────────

async function downloadZip(repo: string, branch: string, dest: string) {
    const url = `https://api.github.com/repos/${repo}/zipball/${branch}`;
    console.log(`  Downloading ${repo}@${branch}...`);
    const res = await fetchWithRetry(url);
    if (!res.body) throw new Error('No response body');
    const ws = createWriteStream(dest);
    await pipeline(res.body as unknown as NodeJS.ReadableStream, ws);
}

async function copyDir(src: string, dest: string) {
    await fs.mkdir(dest, { recursive: true });
    for (const entry of await fs.readdir(src, { withFileTypes: true })) {
        const s = path.join(src, entry.name);
        const d = path.join(dest, entry.name);
        if (entry.isDirectory()) await copyDir(s, d);
        else await fs.copyFile(s, d);
    }
}

async function extractSubdir(zipPath: string, subdir: string, outputDir: string) {
    const { execFile } = await import('child_process');
    const { promisify } = await import('util');
    const exec = promisify(execFile);

    const tmpDir = zipPath + '-extracted';
    await fs.mkdir(tmpDir, { recursive: true });

    try {
        await exec('unzip', ['-q', '-o', zipPath, '-d', tmpDir]);
    } catch {
        throw new Error('unzip not found — install unzip or use a Node.js ZIP library');
    }

    // GitHub zipball có top-level dir in format "org-repo-{sha}/"
    const entries = await fs.readdir(tmpDir, { withFileTypes: true });
    const topDir = entries.find((e) => e.isDirectory());
    if (!topDir) throw new Error('No top-level directory in zipball');

    const srcDir = subdir ? path.join(tmpDir, topDir.name, subdir) : path.join(tmpDir, topDir.name);

    const absOutput = path.join(PROJECT_ROOT, outputDir);
    await copyDir(srcDir, absOutput);
    await fs.rm(tmpDir, { recursive: true, force: true });
}

// ── Main ──────────────────────────────────────────────────────────────────────

async function fetchTarget(target: FetchTarget) {
    const outputDir = `content/api/${target.version}`;
    const absOutput = path.join(PROJECT_ROOT, outputDir);
    const forceFetch = process.env['FORCE_FETCH'] === '1';

    if (!forceFetch) {
        try {
            await fs.access(absOutput);
            console.log(`  [skip] ${target.version} — already at ${outputDir}`);
            return;
        } catch {
            /* not present, proceed */
        }
    }

    const tmpDir = path.join(PROJECT_ROOT, '.tmp-fetch');
    await fs.mkdir(tmpDir, { recursive: true });
    const zipPath = path.join(tmpDir, `${target.version}.zip`);

    try {
        await downloadZip(target.repo, target.branch, zipPath);
        console.log(`  Extracting ${target.version}...`);
        await extractSubdir(zipPath, target.subdir, outputDir);
        console.log(`  ✓ ${target.version} → ${outputDir}`);
    } finally {
        await fs.rm(zipPath, { force: true });
    }
}

async function main() {
    console.log('[fetch-docs] Starting...\n');

    if (FETCH_TARGETS.length === 0) {
        console.log('[fetch-docs] No GitHub targets configured.');
        return;
    }

    for (const target of FETCH_TARGETS) {
        try {
            await fetchTarget(target);
        } catch (err) {
            console.error(`  [error] ${target.version}:`, err);
            process.exit(1);
        }
    }

    await fs.rm(path.join(PROJECT_ROOT, '.tmp-fetch'), { recursive: true, force: true });
    console.log('\n[fetch-docs] Done.');
}

main().catch((err) => {
    console.error('[fetch-docs] Fatal:', err);
    process.exit(1);
});
