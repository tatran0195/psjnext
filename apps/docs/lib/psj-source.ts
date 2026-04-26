import { loader } from 'fumadocs-core/source';
import { psjPlugin, psjSource } from 'psjapi/server';

import { i18n } from './i18n';
import { psjServer } from './psj-server';

/**
 * NON-I18N setup — single language, no locale prefix in URLs.
 * Use this if your Fumadocs project does NOT have i18n configured.
 */
// export const psjDocs = loader({
//     source: await psjSource(psjServer, {
//         groupBy: 'domain',
//         per: 'item',
//         // No i18nParser — single virtual file per item
//         // Locale can still be passed explicitly to getItem(version, locale)
//     }),
//     plugins: [psjPlugin()],
//     baseUrl: '/docs',
// });

// ---------------------------------------------------------------------------

/**
 * I18N setup (dir parser) — one URL prefix per language.
 *
 * URL structure:
 *   /en/docs/psj-command/Analysis-ADVC-MakeProcess-Static
 *   /ja/docs/psj-command/Analysis-ADVC-MakeProcess-Static
 *
 * Match this with i18n middleware in middleware.ts:
 *   import { createI18nMiddleware } from 'fumadocs-core/i18n';
 *   export default createI18nMiddleware({
 *     languages: ['en', 'ja'],
 *     defaultLanguage: 'en',
 *   });
 *
 * IMPORTANT: i18nParser must match i18n.parser in loader()
 */
export const psjDocsSource = loader({
    source: await psjSource(psjServer, {
        groupBy: 'domain',
        per: 'item',
        // Tells psjSource to emit en/ and ja/ prefixed files
        i18nParser: 'dir',
    }),
    plugins: [psjPlugin()],
    baseUrl: '/docs',
    i18n,
});
