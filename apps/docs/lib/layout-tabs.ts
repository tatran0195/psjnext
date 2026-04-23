import type { LayoutTab } from '@/layouts/shared';

import { ACTIVE_VERSIONS } from '@/lib/versions';

/**
 * Returns a LayoutTab for the "API Reference" navbar tab.
 * Active on any path starting with /<lang>/api/.
 *
 * Used in both the docs layout and the api layout so the full
 * tab row is always visible regardless of which section the user is in.
 */
export function buildApiTab(lang: string): LayoutTab {
    const latest = ACTIVE_VERSIONS[0];
    return {
        title: 'API Reference',
        url: `/${lang}/api/${latest}`,
        // Sentinel ending with '/' → isLayoutTabActive prefix-matches all /lang/api/* paths
        urls: new Set([`/${lang}/api/`]),
    };
}
