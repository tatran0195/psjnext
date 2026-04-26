import path from 'node:path';
import { createPSJAPI } from 'psjapi';

/**
 * PSJAPIServer singleton.
 *
 * `root` points to the directory containing sdk.psjapi.yaml.
 * In development, disable caching so YAML edits hot-reload without restart.
 */
export const psjServer = createPSJAPI({
    root: path.join(process.cwd(), 'content/psj-sdk'),
    defaultLocale: 'en',
    disableCache: process.env.NODE_ENV === 'development',
});
