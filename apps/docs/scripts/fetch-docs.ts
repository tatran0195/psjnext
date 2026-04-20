#!/usr/bin/env bun
/**
 * CI script: fetch versioned docs from GitHub org/repos → content/api/X.Y.Z
 *
 * Usage:
 *   bun scripts/fetch-docs.ts
 *   FORCE_FETCH=1 bun scripts/fetch-docs.ts     # skip cache check
 *   DRY_RUN=1 bun scripts/fetch-docs.ts         # preview without writing
 *   CONCURRENCY=4 bun scripts/fetch-docs.ts     # parallel downloads
 *
 * Env vars:
 *   GITHUB_TOKEN   - Required for org private repos & higher rate limits
 *   GITHUB_ORG     - Default org (overrides per-target org)
 *   FORCE_FETCH    - '1' to re-fetch even if output dir exists
 *   DRY_RUN        - '1' to preview without writing files
 *   CONCURRENCY    - Max parallel downloads (default: 3)
 */

import fs from 'node:fs/promises';
import path from 'node:path';

// ── Types ─────────────────────────────────────────────────────────────────────

type FetchTarget = {
    /** Canonical version key, e.g. '5.1.0' */
    version: string;
    /** 'org/repo' — org can be omitted if GITHUB_ORG env is set */
    repo: string;
    /** Exact branch name OR a glob pattern like 'release/*' */
    branch: string;
    /** Subdirectory inside the repo to copy, e.g. 'docs/api'. Empty = root */
    subdir: string;
    /** Override output directory, relative to project root */
    outputDir?: string;
};

type ResolvedTarget = FetchTarget & {
    resolvedBranch: string;
    resolvedRepo: string; // always 'org/repo'
    resolvedOutput: string; // absolute path
};

type FetchResult =
    | { status: 'ok'; target: ResolvedTarget }
    | { status: 'skipped'; target: ResolvedTarget }
    | { status: 'error'; target: FetchTarget; error: Error };

// ── Config ────────────────────────────────────────────────────────────────────

const FETCH_TARGETS: FetchTarget[] = [
    {
        version: '5.0.1',
        repo: 'your-org/your-repo',
        branch: 'release/5.0.1',
        subdir: 'docs/api',
    },
    {
        version: '5.1.0',
        repo: 'your-repo', // short form — uses GITHUB_ORG env var
        branch: 'release/5.1.*', // pattern — resolves to latest match
        subdir: 'docs/api',
    },
    {
        version: '6.0.0',
        repo: 'another-org/another-repo',
        branch: 'main',
        subdir: '', // fetch entire repo root
        outputDir: 'content/api/v6', // custom output path
    },
];

// ── Constants ─────────────────────────────────────────────────────────────────

// FIX #1: derive PROJECT_ROOT from cwd(), not import.meta.dir —
// import.meta.dir is the *script's* directory, which breaks if the script
// is invoked from a subdirectory or symlinked. cwd() is always the workspace root
// when run via `bun run` / package.json scripts.
const PROJECT_ROOT = process.cwd();

// FIX #10: register tmp dir globally so we can clean it up on fatal exit
const TMP_DIR = path.join(PROJECT_ROOT, '.tmp-fetch-docs');

const GITHUB_API = 'https://api.github.com';
const TIMEOUT_MS = 60_000;
const MAX_RETRIES = 3;
// Maximum open file descriptors for parallel copies (FIX #4)
const MAX_OPEN_FDS = 64;

const FORCE_FETCH = process.env.FORCE_FETCH === '1';
const DRY_RUN = process.env.DRY_RUN === '1';
const CONCURRENCY = Math.max(1, parseInt(process.env.CONCURRENCY ?? '3', 10));
const DEFAULT_ORG = process.env.GITHUB_ORG ?? '';

// ── Logging ───────────────────────────────────────────────────────────────────

const log = {
    info: (msg: string) => console.log(`  ${msg}`),
    ok: (msg: string) => console.log(`  ✓ ${msg}`),
    skip: (msg: string) => console.log(`  ⊘ ${msg}`),
    warn: (msg: string) => console.warn(`  ⚠ ${msg}`),
    error: (msg: string) => console.error(`  ✗ ${msg}`),
    section: (msg: string) => console.log(`\n${msg}`),
};

// ── HTTP helpers ──────────────────────────────────────────────────────────────

// Build once per run; token presence is logged only once via the warning below.
let _headersBuilt = false;
let _tokenWarned = false;

function buildHeaders(): Record<string, string> {
    const headers: Record<string, string> = {
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'bun-docs-fetch/2.0',
    };

    const token = process.env.GITHUB_TOKEN;
    if (token) {
        headers.Authorization = `Bearer ${token}`;
    } else if (!_tokenWarned) {
        log.warn('GITHUB_TOKEN not set — rate limit: 60 req/h (unauthenticated)');
        _tokenWarned = true;
    }

    _headersBuilt = true;
    return headers;
}

class FetchError extends Error {
    constructor(
        message: string,
        public readonly status: number,
        public readonly url: string,
        public readonly body: string,
    ) {
        super(message);
        this.name = 'FetchError';
    }
}

function sleep(ms: number) {
    return new Promise<void>((resolve) => setTimeout(resolve, ms));
}

async function fetchWithRetry(
    url: string,
    attempt: number = 1,
    options: RequestInit = {},
): Promise<Response> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);

    try {
        const res = await fetch(url, {
            ...options,
            headers: { ...buildHeaders(), ...((options.headers as Record<string, string>) ?? {}) },
            signal: controller.signal,
            redirect: 'follow',
        });

        if (res.status === 429 && attempt <= MAX_RETRIES) {
            const retryAfter = parseInt(res.headers.get('retry-after') ?? '10', 10);
            log.warn(`Rate limited — waiting ${retryAfter}s (attempt ${attempt}/${MAX_RETRIES})`);
            await sleep(retryAfter * 1_000);
            return fetchWithRetry(url, attempt + 1, options);
        }

        if (res.status >= 500 && attempt <= MAX_RETRIES) {
            const delay = 1_000 * 2 ** (attempt - 1);
            log.warn(
                `HTTP ${res.status} — retrying in ${delay / 1000}s ` +
                    `(attempt ${attempt}/${MAX_RETRIES})`,
            );
            await sleep(delay);
            return fetchWithRetry(url, attempt + 1, options);
        }

        if (!res.ok) {
            const body = await res.text().catch(() => '');
            throw new FetchError(
                `HTTP ${res.status} ${res.statusText} — ${url}`,
                res.status,
                url,
                body,
            );
        }

        return res;
    } finally {
        clearTimeout(timer);
    }
}

// ── GitHub API helpers ────────────────────────────────────────────────────────

async function listOrgRepos(org: string): Promise<string[]> {
    const repos: string[] = [];
    let page = 1;

    while (true) {
        const url = `${GITHUB_API}/orgs/${org}/repos?per_page=100&page=${page}&sort=full_name`;
        const res = await fetchWithRetry(url);
        const data = (await res.json()) as Array<{ name: string }>;
        if (data.length === 0) break;
        repos.push(...data.map((r) => r.name));
        page++;
    }

    return repos;
}

async function listBranches(repo: string): Promise<string[]> {
    const branches: string[] = [];
    let page = 1;

    while (true) {
        const url = `${GITHUB_API}/repos/${repo}/branches?per_page=100&page=${page}`;
        const res = await fetchWithRetry(url);
        const data = (await res.json()) as Array<{ name: string }>;
        if (data.length === 0) break;
        branches.push(...data.map((b) => b.name));
        page++;
    }

    return branches;
}

// FIX #3: GitHub REST API does NOT support URL-encoded slashes in branch names
// for the /branches/{branch} endpoint — it returns 404 even with correct encoding.
// The only reliable approach is to list all branches and match by name.
// We always go through listBranches() for both exact and pattern matches.
async function resolveBranch(repo: string, pattern: string): Promise<string> {
    const branches = await listBranches(repo);

    const isGlob = pattern.includes('*') || pattern.includes('?');
    const matched = isGlob
        ? branches.filter((b) => globToRegex(pattern).test(b))
        : branches.filter((b) => b === pattern);

    if (matched.length === 0) {
        // Provide actionable feedback: show first 15 available branches
        const preview = branches.slice(0, 15).join(', ');
        const more = branches.length > 15 ? ` … (${branches.length - 15} more)` : '';
        throw new Error(
            `Branch '${pattern}' not found in ${repo}.\n` + `  Available: ${preview}${more}`,
        );
    }

    // Sort descending so the semantically "latest" branch comes first.
    // For version branches like release/5.1.2, lexicographic desc is correct.
    const sorted = matched.slice().sort().reverse();

    if (matched.length > 1) {
        log.info(
            `Pattern '${pattern}' matched ${matched.length} branches — ` + `using: '${sorted[0]}'`,
        );
    }

    return sorted[0]!;
}

// FIX #8: previous version was missing proper character-class handling.
// This version only escapes the minimal set needed and avoids touching
// characters that are valid inside branch name globs.
function globToRegex(pattern: string): RegExp {
    // Escape all regex special chars except * and ? which we handle below
    const escaped = pattern
        .replace(/[\\^$.|+()[\]{}]/g, '\\$&') // escape regex metacharacters
        .replace(/\*/g, '.*') // * → match anything
        .replace(/\?/g, '[^/]'); // ? → match single non-slash char
    return new RegExp(`^${escaped}$`);
}

function resolveRepo(repo: string): string {
    if (repo.includes('/')) return repo;
    if (!DEFAULT_ORG) {
        throw new Error(
            `Repo '${repo}' has no org prefix and GITHUB_ORG is not set.\n` +
                `  Use 'org/repo' format or set GITHUB_ORG=<your-org>`,
        );
    }
    return `${DEFAULT_ORG}/${repo}`;
}

// ── Download + extract (Bun-native) ──────────────────────────────────────────

// FIX #5: stream zip directly to disk instead of buffering the entire
// response as an ArrayBuffer — avoids OOM on large repos.
async function downloadZip(repo: string, branch: string, destPath: string): Promise<void> {
    const url = `${GITHUB_API}/repos/${repo}/zipball/${encodeURIComponent(branch)}`;
    log.info(`Downloading ${repo}@${branch}…`);

    if (DRY_RUN) {
        log.info(`[dry-run] Would GET ${url}`);
        return;
    }

    const res = await fetchWithRetry(url);
    if (!res.body) throw new Error('Response body is null — cannot download zip');

    // Write the raw bytes straight to disk via Bun's streaming writer
    await Bun.write(destPath, res);

    const stat = await fs.stat(destPath);
    const sizeKb = (stat.size / 1024).toFixed(1);
    log.info(`Saved ${sizeKb} KB → ${path.relative(PROJECT_ROOT, destPath)}`);
}

async function extractZip(zipPath: string, destDir: string): Promise<void> {
    await fs.mkdir(destDir, { recursive: true });

    const proc = Bun.spawn(['unzip', '-q', '-o', zipPath, '-d', destDir], {
        stdout: 'ignore',
        stderr: 'pipe',
    });

    const exitCode = await proc.exited;

    if (exitCode !== 0) {
        const stderr = await new Response(proc.stderr).text();
        throw new Error(
            `unzip failed (exit ${exitCode})${stderr ? `: ${stderr.trim()}` : ''}.\n` +
                `  Install with: apt-get install unzip   or   brew install unzip`,
        );
    }
}

// FIX #4: semaphore-based fd limiter prevents "too many open files" errors
// when recursively copying large directory trees in parallel.
class Semaphore {
    private _queue: Array<() => void> = [];
    private _active: number = 0;

    constructor(private readonly limit: number) {}

    async acquire(): Promise<void> {
        if (this._active < this.limit) {
            this._active++;
            return;
        }
        await new Promise<void>((resolve) => this._queue.push(resolve));
        this._active++;
    }

    release(): void {
        this._active--;
        this._queue.shift()?.();
    }
}

async function copyDir(src: string, dest: string, sem: Semaphore): Promise<void> {
    await fs.mkdir(dest, { recursive: true });
    const entries = await fs.readdir(src, { withFileTypes: true });

    await Promise.all(
        entries.map(async (entry) => {
            const srcPath = path.join(src, entry.name);
            const destPath = path.join(dest, entry.name);

            if (entry.isDirectory()) {
                await copyDir(srcPath, destPath, sem);
            } else {
                // Acquire a slot before opening the file to cap concurrent fd usage
                await sem.acquire();
                try {
                    await Bun.write(destPath, Bun.file(srcPath));
                } finally {
                    sem.release();
                }
            }
        }),
    );
}

async function extractSubdir(zipPath: string, subdir: string, outputDir: string): Promise<void> {
    const tmpExtractDir = `${zipPath}-extracted`;

    try {
        await extractZip(zipPath, tmpExtractDir);

        const entries = await fs.readdir(tmpExtractDir, { withFileTypes: true });
        const topDir = entries.find((e) => e.isDirectory());

        if (!topDir) {
            throw new Error('Zipball has no top-level directory — unexpected archive format');
        }

        const repoRoot = path.join(tmpExtractDir, topDir.name);
        const srcDir = subdir ? path.join(repoRoot, subdir) : repoRoot;

        // Verify the requested subdirectory actually exists before wiping outputDir
        try {
            const stat = await fs.stat(srcDir);
            if (!stat.isDirectory()) {
                throw new Error(`'${subdir}' exists in the repo but is not a directory`);
            }
        } catch (err: unknown) {
            if ((err as NodeJS.ErrnoException).code === 'ENOENT') {
                const topContents = (await fs.readdir(repoRoot)).join(', ');
                throw new Error(
                    `Subdirectory '${subdir}' not found in repo.\n` +
                        `  Top-level contents: ${topContents}`,
                    { cause: err },
                );
            }
            throw err;
        }

        // FIX #9: remove any partial outputDir *before* copying so a failed
        // previous run doesn't leave a corrupt-but-present directory that
        // tricks the cache check into thinking it's valid.
        await fs.rm(outputDir, { recursive: true, force: true });

        const sem = new Semaphore(MAX_OPEN_FDS);
        await copyDir(srcDir, outputDir, sem);
    } finally {
        // Always remove the extraction temp dir, even on error
        await fs.rm(tmpExtractDir, { recursive: true, force: true });
    }
}

// ── Resolution ────────────────────────────────────────────────────────────────

async function resolveTarget(target: FetchTarget): Promise<ResolvedTarget> {
    const resolvedRepo = resolveRepo(target.repo);
    const resolvedBranch = await resolveBranch(resolvedRepo, target.branch);

    // FIX #6: honour custom outputDir when building the absolute output path
    const outputRel = target.outputDir ?? `content/api/${target.version}`;
    const resolvedOutput = path.isAbsolute(outputRel)
        ? outputRel
        : path.join(PROJECT_ROOT, outputRel);

    return { ...target, resolvedRepo, resolvedBranch, resolvedOutput };
}

// ── Per-target fetch ──────────────────────────────────────────────────────────

async function fetchTarget(target: FetchTarget): Promise<FetchResult> {
    let resolved: ResolvedTarget;

    try {
        resolved = await resolveTarget(target);
    } catch (err) {
        return {
            status: 'error',
            target,
            error: err instanceof Error ? err : new Error(String(err)),
        };
    }

    // Cache check
    if (!FORCE_FETCH) {
        try {
            const stat = await fs.stat(resolved.resolvedOutput);
            if (stat.isDirectory()) {
                log.skip(
                    `${target.version} — already at ` +
                        path.relative(PROJECT_ROOT, resolved.resolvedOutput),
                );
                return { status: 'skipped', target: resolved };
            }
            // Path exists but isn't a directory — fall through and overwrite
        } catch {
            /* ENOENT — not cached, proceed */
        }
    }

    const zipPath = path.join(TMP_DIR, `${target.version}.zip`);

    try {
        await downloadZip(resolved.resolvedRepo, resolved.resolvedBranch, zipPath);

        if (!DRY_RUN) {
            log.info(
                `Extracting ${target.version}` +
                    (resolved.subdir ? ` (subdir: ${resolved.subdir})` : '') +
                    '…',
            );
            await extractSubdir(zipPath, resolved.subdir, resolved.resolvedOutput);
        }

        log.ok(
            `${target.version} → ` +
                path.relative(PROJECT_ROOT, resolved.resolvedOutput) +
                (resolved.resolvedBranch !== target.branch
                    ? `  (resolved branch: ${resolved.resolvedBranch})`
                    : ''),
        );

        return { status: 'ok', target: resolved };
    } catch (err) {
        return {
            status: 'error',
            target: resolved,
            error: err instanceof Error ? err : new Error(String(err)),
        };
    } finally {
        // Always clean up zip file, even on error
        await fs.rm(zipPath, { force: true });
    }
}

// ── Concurrency pool ──────────────────────────────────────────────────────────

// FIX #2: replaced the mutable-shared-array approach with an index-based
// counter incremented atomically (single-threaded JS event loop guarantees
// this is safe — no true concurrent mutation can occur between awaits).
async function runWithConcurrency(targets: FetchTarget[], limit: number): Promise<FetchResult[]> {
    if (targets.length === 0) return [];

    const results: FetchResult[] = new Array(targets.length);
    let nextIndex = 0;

    async function worker(): Promise<void> {
        while (true) {
            // Grab next index atomically (safe: JS is single-threaded between awaits)
            const idx = nextIndex++;
            if (idx >= targets.length) return;
            results[idx] = await fetchTarget(targets[idx]!);
        }
    }

    const workerCount = Math.min(limit, targets.length);
    await Promise.all(Array.from({ length: workerCount }, worker));

    return results;
}

// ── Org discovery mode ────────────────────────────────────────────────────────

async function listOrgReposMode(): Promise<void> {
    const org = DEFAULT_ORG || process.argv[2];
    if (!org) {
        console.error('Set GITHUB_ORG=<org> or pass org name as first argument');
        process.exit(1);
    }

    console.log(`\nListing repos for org: ${org}\n`);
    const repos = await listOrgRepos(org);
    for (const name of repos) console.log(`  ${org}/${name}`);
    console.log(`\nTotal: ${repos.length} repos`);
}

// ── Main ──────────────────────────────────────────────────────────────────────

// FIX #10: clean up TMP_DIR on any unhandled exit so orphaned temp files
// don't accumulate across failed CI runs.
async function cleanupTmpDir(): Promise<void> {
    await fs.rm(TMP_DIR, { recursive: true, force: true });
}

process.on('exit', () => {
    /* sync — nothing async possible here */
});
process.on('SIGINT', async () => {
    await cleanupTmpDir();
    process.exit(130);
});
process.on('SIGTERM', async () => {
    await cleanupTmpDir();
    process.exit(143);
});

async function main(): Promise<void> {
    if (process.env.LIST_ORG_REPOS === '1') {
        await listOrgReposMode();
        return;
    }

    console.log('[fetch-docs] Starting…');
    if (DRY_RUN) log.warn('DRY RUN — no files will be written');
    if (FORCE_FETCH) log.warn('FORCE_FETCH — ignoring cached output dirs');
    if (DEFAULT_ORG) log.info(`Default GitHub org: ${DEFAULT_ORG}`);
    log.info(`Targets: ${FETCH_TARGETS.length} | Concurrency: ${CONCURRENCY}`);

    if (FETCH_TARGETS.length === 0) {
        log.warn('No targets configured — nothing to do.');
        return;
    }

    await fs.mkdir(TMP_DIR, { recursive: true });

    let results: FetchResult[];
    try {
        results = await runWithConcurrency(FETCH_TARGETS, CONCURRENCY);
    } finally {
        // FIX #10: guaranteed cleanup even when runWithConcurrency throws
        await cleanupTmpDir();
    }

    // ── Summary ────────────────────────────────────────────────────────────────
    const ok = results.filter((r) => r.status === 'ok');
    const skipped = results.filter((r) => r.status === 'skipped');
    const errors = results.filter((r) => r.status === 'error');

    log.section('[fetch-docs] Summary:');
    console.log(`  ✓ Fetched:  ${ok.length}`);
    console.log(`  ⊘ Skipped:  ${skipped.length}`);
    console.log(`  ✗ Errors:   ${errors.length}`);

    if (errors.length > 0) {
        log.section('[fetch-docs] Failed targets:');
        for (const r of errors) {
            if (r.status === 'error') {
                log.error(`${r.target.version} (${r.target.repo}@${r.target.branch})`);
                // Indent the error message for readability
                for (const line of r.error.message.split('\n')) {
                    console.error(`      ${line}`);
                }
            }
        }
        process.exit(1);
    }

    console.log('\n[fetch-docs] Done.');
}

main().catch(async (err: unknown) => {
    console.error('[fetch-docs] Fatal:', err);
    await cleanupTmpDir();
    process.exit(1);
});
