/**
 * I18N variant of the docs page.
 *
 * Route: /[lang]/docs/[[...slug]]
 * Examples:
 *   /en/docs/psj-command/Analysis-ADVC-MakeProcess-Static
 *   /ja/docs/psj-command/Analysis-ADVC-MakeProcess-Static
 *
 * How i18n is threaded through:
 *
 *   1. psjSource() emits two virtual files per item:
 *        en/psj-command/Analysis-ADVC-MakeProcess-Static.mdx  → locale baked in as 'en'
 *        ja/psj-command/Analysis-ADVC-MakeProcess-Static.mdx  → locale baked in as 'ja'
 *
 *   2. Fumadocs loader(i18n: { parser: 'dir' }) strips the language prefix and
 *      stores the file in the correct per-locale ContentStorage bucket.
 *
 *   3. psjDocsSource.getPage(slug, lang) retrieves the page from the correct bucket.
 *
 *   4. page.data.getItem(version) resolves the item using the locale that was
 *      baked into the virtual file at source-generation time — no need to pass
 *      lang here.
 *
 *   5. PSJAPIItem renders with the pre-resolved locale — Japanese sidecar YAML
 *      is merged in the loader automatically.
 */

import { psjServer } from '@/lib/psj-server';
import { psjDocsSource } from '@/lib/psj-source';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { createPSJAPIPage } from 'psjapi/ui';

const PSJAPIItem = createPSJAPIPage(psjServer, {});

// ── Static params ──────────────────────────────────────────────────────────

export function generateStaticParams() {
  // getLanguages() returns [{ language: 'en', pages: [...] }, { language: 'ja', pages: [...] }]
  return psjDocsSource.getLanguages().flatMap(({ language, pages }) =>
    pages.map((page) => ({
      lang: language,
      slug: page.slugs,
    })),
  );
}

// ── Metadata ───────────────────────────────────────────────────────────────

export async function generateMetadata({
  params,
}: {
  params: Promise<{ lang: string; slug?: string[] }>;
}): Promise<Metadata> {
  const { lang, slug } = await params;
  const page = psjDocsSource.getPage(slug, lang);
  if (!page) return {};
  return {
    title: page.data.title,
    description: page.data.description,
  };
}

// ── Page ───────────────────────────────────────────────────────────────────

export default async function DocsPage({
  params,
  searchParams,
}: {
  params: Promise<{ lang: string; slug?: string[] }>;
  searchParams: Promise<{ v?: string }>;
}) {
  const { lang, slug } = await params;
  const { v: version } = await searchParams;

  // getPage(slug, lang) looks up the correct locale bucket
  const page = psjDocsSource.getPage(slug, lang);
  if (!page) notFound();

  // Locale is already baked into this page's getItem() — just pass version
  const item = await page.data.getItem(version);
  if (!item) notFound();

  return (
    <div className="container py-12 lg:py-16">
      <PSJAPIItem
        schemaId={psjServer.options.root}
        itemKey={`${item.domain}/${item.id}`}
        version={version}
        // locale prop on PSJAPIItem is optional here — item is already resolved
        // for the correct locale by getItem() above. Pass it anyway so the
        // renderer can use it for any locale-dependent UI labels.
        locale={lang}
      />
    </div>
  );
}
