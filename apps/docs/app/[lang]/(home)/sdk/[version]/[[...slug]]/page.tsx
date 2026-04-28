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

import type { Metadata } from 'next';
import { notFound } from 'next/navigation';

import { createPSJAPIPage } from 'psjapi/ui';

import { psjServer } from '@/lib/psj-server';
import { psjDocs } from '@/lib/psj-source';

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

// ── Static params — lang × version × slug ──────────────────────────────────

export function generateStaticParams() {
    return psjDocs.getLanguages().flatMap(({ language, pages }) =>
        pages.map((page) => {
            // page.slugs = ['5.1.0', 'psj-command', 'analysis-advc-makeprocess-static']
            const [version, ...slug] = page.slugs;
            return { lang: language, version, slug };
        }),
    );
}

// ── Metadata ───────────────────────────────────────────────────────────────

export async function generateMetadata({
    params,
}: {
    params: Promise<{ lang: string; version: string; slug?: string[] }>;
}): Promise<Metadata> {
    const { lang, version, slug } = await params;
    // Reconstruct the full slug including the version segment
    const fullSlug = [version, ...(slug ?? [])];
    const page = psjDocs.getPage(fullSlug, lang);
    if (!page) return {};
    return {
        title: page.data.title,
        description: page.data.description,
    };
}

// ── Page ───────────────────────────────────────────────────────────────────

export default async function DocsPage({
    params,
}: {
    params: Promise<{ lang: string; version: string; slug?: string[] }>;
}) {
    const { lang, version, slug } = await params;

    // Reconstruct full slug (version is part of the path that psjSource emits)
    const fullSlug = [version, ...(slug ?? [])];

    const page = psjDocs.getPage(fullSlug, lang);
    if (!page) notFound();

    // Version and locale are baked into this page's getItem() — call with no args
    const item = await page.data.getItem();
    if (!item) notFound();

    return (
        <div className="container py-12 lg:py-16">
            <PSJAPIItem
                schemaId={psjServer.options.root}
                itemKey={`${item.domain}/${item.id}`}
                version={page.data.sdkVersion}
                locale={page.data.sdkLocale}
            />
        </div>
    );
}
