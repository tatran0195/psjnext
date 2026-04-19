// app/[lang]/api/[version]/[[...slug]]/page.tsx
//
// Versioned API docs page.
//
// generateStaticParams:
//   Merge params từ tất cả active versions × tất cả locales.
//   source.generateParams() trả về { lang: string, slug: string[] }.
//   Thêm version vào mỗi entry.
//
// Alias routing:
//   /api/stable/... → resolve → 5.1.0 → apiSources['5.1.0']
//   URL không redirect — cả alias lẫn canonical đều serve nội dung giống nhau.
//   Canonical permalink được expose qua notice banner.

import { getMDXComponents } from '@/components/mdx'
import { i18n } from '@/lib/i18n'
import { apiSources, type ApiVersion } from '@/lib/source'
import {
  ACTIVE_VERSIONS,
  getVersionMeta,
  isVersionActive,
  resolveVersion,
} from '@/lib/versions'
import { PathUtils } from 'fumadocs-core/source'
import * as Twoslash from 'fumadocs-twoslash/ui'
import { Banner } from 'fumadocs-ui/components/banner'
import { Callout } from 'fumadocs-ui/components/callout'
import { TypeTable } from 'fumadocs-ui/components/type-table'
import { DocsBody, DocsDescription, DocsPage, DocsTitle } from 'fumadocs-ui/layouts/docs/page'
import type { Metadata } from 'next'
import { notFound } from 'next/navigation'

import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category'
import { LinkPreview } from '@/components/mdx/link-preview'
import { Mermaid } from '@/components/mdx/mermaid'
import { SymbolLink } from '@/components/mdx/symbol-link'
import { Customisation } from '@/components/preview/customisation'
import { Installation } from '@/components/preview/installation'
import { Wrapper } from '@/components/preview/wrapper'
import Link from 'next/link'
import { ComponentProps, FC } from 'react'
// ── Static params ─────────────────────────────────────────────────────────────

export function generateStaticParams() {
  return ACTIVE_VERSIONS.flatMap((version) => {
    const canonical = resolveVersion(version)
    if (!canonical) return []

    const source = apiSources[canonical as ApiVersion]
    if (!source) return []

    // generateParams() → [{ lang: 'en', slug: [...] }, { lang: 'ja', slug: [...] }, ...]
    return source.generateParams().map((p) => ({ ...p, version }))
  })
}

// ── Metadata ──────────────────────────────────────────────────────────────────

export async function generateMetadata({
  params,
}: {
  params: Promise<{ lang: string; version: string; slug?: string[] }>
}): Promise<Metadata> {
  const { lang, version, slug } = await params
  if (!isVersionActive(version)) return { title: 'Not Found' }

  const canonical = resolveVersion(version)
  if (!canonical) return { title: 'Not Found' }

  const source = apiSources[canonical as ApiVersion]
  const page = source?.getPage(slug, lang)
  if (!page) return { title: 'Not Found' }

  return {
    title: `${page.data.title} — API ${version}`,
    description: page.data.description,
  }
}

// ── Page ──────────────────────────────────────────────────────────────────────

export default async function ApiPage({
  params,
}: {
  params: Promise<{ lang: string; version: string; slug?: string[] }>
}) {
  const { lang, version, slug } = await params

  // 1. Validate
  if (!isVersionActive(version)) notFound()

  const canonical = resolveVersion(version)
  if (!canonical) notFound()

  const source = apiSources[canonical as ApiVersion]
  if (!source) notFound()

  // 2. Load page
  const page = source.getPage(slug, lang)
  if (!page) notFound()

  // 3. Version metadata cho notices
  const meta = getVersionMeta(version)
  const isAlias = version !== canonical
  const prefix = lang === i18n.defaultLanguage ? '' : `/${lang}`
  const slugStr = slug?.join('/') ?? ''

  const { body: Mdx, toc } = await page.data.load();

  return (
    <DocsPage toc={toc}>
      {/* Frozen version banner */}
      {meta?.frozen && (
        <div className="mb-4 rounded-md border border-yellow-200 bg-yellow-50 px-4 py-3 text-sm text-yellow-800 dark:border-yellow-800 dark:bg-yellow-950 dark:text-yellow-300">
          {lang === 'ja' ? (
            <>
              これは凍結バージョンです。最新ドキュメントは{' '}
              <a href={`${prefix}/api/latest/${slugStr}`} className="underline font-medium">
                latest
              </a>{' '}
              をご覧ください。
            </>
          ) : (
            <>
              This is a frozen version. View{' '}
              <a href={`${prefix}/api/latest/${slugStr}`} className="underline font-medium">
                latest
              </a>{' '}
              for current documentation.
            </>
          )}
        </div>
      )}

      {/* Alias notice: /api/stable → /api/5.1.0 */}
      {isAlias && (
        <div className="mb-4 rounded-md border border-fd-border bg-fd-muted px-4 py-3 text-sm text-fd-muted-foreground">
          {lang === 'ja' ? (
            <>
              <code>{version}</code> は{' '}
              <a href={`${prefix}/api/${canonical}/${slugStr}`} className="underline">
                {canonical}
              </a>{' '}
              を参照しています。
            </>
          ) : (
            <>
              <code>{version}</code> resolves to{' '}
              <a href={`${prefix}/api/${canonical}/${slugStr}`} className="underline">
                {canonical}
              </a>
              .
            </>
          )}
        </div>
      )}

      <DocsTitle>{page.data.title}</DocsTitle>
      <DocsDescription>{page.data.description}</DocsDescription>
      <DocsBody>
        <Mdx
          components={getMDXComponents({
            ...Twoslash,
            a({ href, ...props }) {
              if (!href) return <a {...props} />;

              const found = source.getPageByHref(href, {
                dir: PathUtils.dirname(page.path),
              });

              if (!found) return <Link href={href} {...props} />;

              return (
                <LinkPreview
                  href={found.page.url}
                  title={found.page.data.title}
                  description={found.page.data.description}
                >
                  {props.children}
                </LinkPreview>
              );
            },
            Banner,
            Mermaid,
            TypeTable,
            Wrapper,
            SymbolLink,
            LinkPreview,
            blockquote: Callout as unknown as FC<ComponentProps<'blockquote'>>,
            DocsCategory: ({ url }) => {
              return <DocsCategory url={url ?? page.url} lang={lang} />;
            },
            DocsSectionOverview: ({ url }) => {
              return <DocsSectionOverview url={url ?? page.url} lang={lang} />;
            },
            Installation,
            Customisation,
          })}
        />
      </DocsBody>
    </DocsPage>
  )
}
