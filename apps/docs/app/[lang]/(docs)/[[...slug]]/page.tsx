import type { Metadata } from 'next';
import type { ComponentProps, FC } from 'react';

import Link from 'fumadocs-core/link';
import { findNeighbour } from 'fumadocs-core/page-tree';
import { PathUtils } from 'fumadocs-core/source';
import * as Twoslash from 'fumadocs-twoslash/ui';
import { Banner } from 'fumadocs-ui/components/banner';
import { Callout } from 'fumadocs-ui/components/callout';
import { TypeTable } from 'fumadocs-ui/components/type-table';

import type { ApiVersion } from '@/lib/api-versions';

import { NotFound } from '@/components/layouts/not-found';
import { getMDXComponents } from '@/components/mdx';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { Mermaid } from '@/components/mdx/mermaid';
import { ParamHeader, ParamSection } from '@/components/mdx/param-badge';
import { RibbonPath } from '@/components/mdx/ribbon-path';
import { SymbolLink } from '@/components/mdx/symbol-link';
import {
    DocsBody,
    DocsDescription,
    DocsPage,
    DocsTitle,
    PageLastUpdate,
} from '@/layouts/docs/page';
import { DocsPager } from '@/layouts/shared/docs-pager';
import { API_VERSIONS } from '@/lib/api-versions';
import { createMetadata, getPageImage } from '@/lib/metadata';
import { source } from '@/lib/source';

import { getSuggestions } from './suggestions';

/**
 * Resolve [version, ...pageSlug] from catch-all segments after stripping the
 * route prefix ('api').
 *
 * /api/5.1.0/getting-started → { version: '5.1.0', pageSlug: ['getting-started'] }
 * /api/getting-started       → { version: '5.1.0', pageSlug: ['getting-started'] }
 * /api                       → { version: '5.1.0', pageSlug: [] }
 */
function resolveVersion(slug: string[]): { version: string; pageSlug: string[] } {
    const [maybeVersion, ...rest] = slug;
    const isVersionSegment = (API_VERSIONS as readonly string[]).includes(maybeVersion);
    return isVersionSegment
        ? { version: maybeVersion, pageSlug: rest }
        : { version: API_VERSIONS[0], pageSlug: slug };
}

export default async function Page(props: {
    params: Promise<{ slug?: string[]; lang: string }>;
    searchParams: Promise<{ v?: string }>;
}) {
    const params = await props.params;
    const { slug = [], lang } = params;

    // Resolve page + optional API-specific MDX component overrides.
    // let page: ReturnType<typeof source.getPage>;
    let apiMdxComponents: Partial<Parameters<typeof getMDXComponents>[0]> | undefined;
    const page = source.getPage(slug, lang);
    if (!page)
        return (
            <NotFound
                getSuggestions={async () =>
                    params.slug ? getSuggestions(params.slug.join(' ')) : []
                }
            />
        );
    if (slug[0] === 'api') {
        const { version } = resolveVersion(slug.slice(1));
        apiMdxComponents = {
            h3: (props: ComponentProps<'h3'>) => <ParamHeader {...props} />,
            ParamSection: (props: Omit<ComponentProps<typeof ParamSection>, 'currentVersion'>) => (
                <ParamSection {...props} currentVersion={version as ApiVersion} />
            ),
        };
    }

    const { body: Mdx, toc, lastModified } = await page.data.load();
    const { ribbon, shortcut } = page.data;

    const neighbours = findNeighbour(source.getPageTree(lang), page.url);
    const footerPrevious = neighbours.previous
        ? { name: neighbours.previous.name, url: neighbours.previous.url }
        : undefined;
    const footerNext = neighbours.next
        ? { name: neighbours.next.name, url: neighbours.next.url }
        : undefined;
    const markdownUrl = `${page.url}.mdx`;

    return (
        <DocsPage toc={toc} breadcrumb={{ enabled: false }}>
            <div>
                <div className="flex flex-wrap items-start justify-between gap-4">
                    <DocsTitle className="mb-0">{page.data.title}</DocsTitle>
                    <DocsPager
                        {...(footerPrevious && { previous: { url: footerPrevious.url } })}
                        {...(footerNext && { next: { url: footerNext.url } })}
                        markdownUrl={markdownUrl}
                    />
                </div>

                {ribbon && <RibbonPath ribbon={ribbon} shortcut={shortcut} variant="inline" />}

                {page.data.description && (
                    <DocsDescription className="mt-3">{page.data.description}</DocsDescription>
                )}
            </div>
            <DocsBody>
                <Mdx
                    components={getMDXComponents({
                        ...Twoslash,
                        a({ href, ...props }: ComponentProps<'a'>) {
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
                        SymbolLink,
                        LinkPreview,
                        blockquote: Callout as unknown as FC<ComponentProps<'blockquote'>>,
                        DocsCategory: ({ url }: { url?: string }) => (
                            <DocsCategory url={url ?? page.url} lang={lang} />
                        ),
                        DocsSectionOverview: ({ url }: { url?: string }) => (
                            <DocsSectionOverview url={url ?? page.url} lang={lang} />
                        ),
                        ...apiMdxComponents,
                    })}
                />
                {page.data.index ? <DocsCategory url={page.url} lang={lang} /> : null}
            </DocsBody>
            {lastModified && <PageLastUpdate date={lastModified} />}
        </DocsPage>
    );
}

export async function generateMetadata(props: {
    params: Promise<{ slug?: string[]; lang: string }>;
}): Promise<Metadata> {
    const params = await props.params;
    const { slug = [], lang } = params;

    let querySlug = slug;
    if (slug[0] === 'api' && (API_VERSIONS as readonly string[]).includes(slug[1])) {
        // Strip the version segment so source.getPage can resolve the canonical page.
        querySlug = ['api', ...slug.slice(2)];
    }

    const page = source.getPage(querySlug, lang);
    if (!page) {
        return createMetadata({ title: 'Not Found' });
    }

    const description = page.data.description ?? 'The library for building documentation sites';
    const image = {
        url: getPageImage(page).url,
        width: 1200,
        height: 630,
    };

    return createMetadata({
        title: page.data.title,
        description,
        openGraph: {
            url: `/docs/${page.slugs.join('/')}`,
            images: [image],
        },
        twitter: {
            images: [image],
        },
    });
}

export function generateStaticParams() {
    // Standard docs params (all non-api pages, emitted with lang).
    const docsParams = source.generateParams('slug', 'lang');

    // API pages require versioned canonical paths: /api/[version]/[...pageSlug].
    // Versionless /api/... URLs are handled at runtime — must NOT be pre-rendered
    // since the target version changes when a new version is released.
    const apiParams = source
        .getPages()
        .filter((p) => p.slugs[0] === 'api' && p.slugs[1] !== undefined)
        .flatMap((p) =>
            API_VERSIONS.map((version) => ({
                slug: ['api', version, ...p.slugs.slice(1)],
                lang: 'en',
            })),
        );

    return [...docsParams, ...apiParams];
}
