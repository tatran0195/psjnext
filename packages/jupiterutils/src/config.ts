/**
 * Configuration loader.
 *
 * Reads environment variables (via dotenv) and returns a validated Config.
 * Throws a descriptive error if required variables are missing.
 */

import { config as loadDotenv } from 'dotenv';
import { resolve } from 'node:path';

import type { Config } from './types/index.js';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Load configuration from the `.env` file located in `projectRoot`
 * (defaults to `process.cwd()`).
 */
export function loadConfig(projectRoot?: string): Config {
    const root = projectRoot ?? process.cwd();

    // Load .env relative to the project root
    loadDotenv({ path: resolve(root, '.env') });

    const webRoot = requireEnv('WEB_ROOT');
    const macroRoot = requireEnv('MACRO_ROOT');
    console.log('webRoot', webRoot);
    console.log('root', root);
    console.log('macroRoot', macroRoot);
    return {
        webRoot,
        macroRoot,
        projectRoot: root,
    };
}

// ---------------------------------------------------------------------------
// Internal
// ---------------------------------------------------------------------------

function requireEnv(key: string): string {
    const value = process.env[key];
    if (!value) {
        throw new Error(
            `Environment variable "${key}" is required but not set.\n` +
                `Make sure it is defined in your .env file.`,
        );
    }
    return value;
}
