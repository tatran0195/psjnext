/**
 * PSJ SDK docs page — versioned + i18n URL structure.
 *
 * Route:   /[lang]/sdk/[version]/[[...slug]]
 * Examples:
 *   /en/sdk/5.1.0/psj-command/analysis-advc-makeprocess-static
 *   /ja/sdk/5.0.1/macro/advc-static-process
 *   /en/sdk/5.0.0                               ← index, shows overview
 *
 * How version threads through:
 *   - psjSource emits virtual files keyed as:
 *       en/5.1.0/psj-command/Foo.mdx
 *   - loader(i18n: { parser: 'dir' }) strips the 'en' prefix.
 *   - Fumadocs slug becomes: ['5.1.0', 'psj-command', 'Foo']
 *   - params.version = '5.1.0', params.slug = ['psj-command', 'Foo']
 *   - psjDocs.getPage(['5.1.0', ...slug], lang) finds the file.
 *   - page.data.getItem() uses the baked-in version — no extraction needed.
 */

import { createPSJAPIPage } from 'psjapi/ui';

import { psjServer } from '@/lib/psj-server';
import { ResolvedItem } from 'psjapi';

const PSJAPIItem = createPSJAPIPage(psjServer, {
    // Resolve $ref and see_also links to versioned URLs
    resolveRef: (ref) => {
        // ref is like "psj-command/Analysis-ADVC-MakeProcess-Static" or "macro/AdvcStaticProcess"
        // We can't know the current lang/version from here, so link to canonical path.
        // The middleware will redirect to the correct locale.
        const normalized = ref
            .replace(/([a-z])([A-Z])/g, '$1-$2') // split camelCase/PascalCase boundaries
            .replace(/_/g, '-')
            .toLowerCase();
        return `/sdk/${normalized}`; // resolved at render in layout or middleware
    },
});

export default async function ApiPage({
    item,
    version,
    lang,
}: {
    item: ResolvedItem;
    version?: string;
    lang?: string;
}) {
    return (
        <PSJAPIItem
            schemaId={psjServer.options.root}
            itemKey={`${item.domain}/${item.id}`}
            version={version}
            locale={lang}
        />
    );
}
