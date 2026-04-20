/**
 * Configuration loader.
 *
 * Bun natively loads `.env` files from the working directory —
 * no dotenv package required. Environment variables are available
 * directly via `Bun.env` / `process.env` at startup.
 *
 * CLI override: `bun --env-file=other/.env run index.ts`
 *
 * Throws a descriptive error if required variables are missing.
 */

import type { Config } from '@/types/index.js';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Load configuration from environment variables.
 *
 * Bun automatically sources `.env`, `.env.local`, `.env.production`, etc.
 * from `process.cwd()` before the process starts — no explicit dotenv call needed.
 */
export function loadConfig(projectRoot?: string): Config {
    const root = projectRoot ?? process.cwd();

    const webRoot = requireEnv('WEB_ROOT');
    const macroRoot = requireEnv('MACRO_ROOT');

    return { webRoot, macroRoot, projectRoot: root };
}

// ---------------------------------------------------------------------------
// Internal
// ---------------------------------------------------------------------------

function requireEnv(key: string): string {
    // Bun.env is the idiomatic accessor — same backing store as process.env
    const value = Bun.env[key];
    if (!value) {
        throw new Error(
            `Environment variable "${key}" is required but not set.\n` +
                `Make sure it is defined in your .env file.`,
        );
    }
    return value;
}
