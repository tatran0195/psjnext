import { createPsjd } from 'psjd/server';

export const psjd = createPsjd({
    /** Path to sdk.psjd.yaml */
    input: './content/psjd/sdk.psjd.yaml',
    /**
     * Supported locales. Must match lib/i18n.ts languages.
     * For each locale, sidecar files (<id>.<locale>.yaml) are auto-discovered
     * and merged at load time.
     */
    locales: ['en', 'ja'],
    /**
     * Throw on sidecar validation errors (recommended for CI).
     * Default: false (logs warnings).
     */
    strict: process.env.NODE_ENV === 'production',
});
