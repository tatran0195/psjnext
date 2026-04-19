import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { ComponentProps, FC } from 'react';

import { findNeighbour } from 'fumadocs-core/page-tree';
import { PathUtils } from 'fumadocs-core/source';
import * as Twoslash from 'fumadocs-twoslash/ui';
import { Banner } from 'fumadocs-ui/components/banner';
import { Callout } from 'fumadocs-ui/components/callout';
import { TypeTable } from 'fumadocs-ui/components/type-table';

import { getMDXComponents } from '@/components/mdx';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { Mermaid } from '@/components/mdx/mermaid';
import { RibbonPath } from '@/components/mdx/ribbon-path';
import { SymbolLink } from '@/components/mdx/symbol-link';
import { Customisation } from '@/components/preview/customisation';
import { Installation } from '@/components/preview/installation';
import { Wrapper } from '@/components/preview/wrapper';
import {
    DocsBody,
    DocsDescription,
    DocsPage,
    DocsTitle,
    PageLastUpdate,
} from '@/layouts/docs/page';
import { DocsPager } from '@/layouts/shared/docs-pager';
import { apiSources, type ApiVersion } from '@/lib/source';
import { ACTIVE_VERSIONS, isVersionActive } from '@/lib/versions';
// ── Static params ─────────────────────────────────────────────────────────────

export function generateStaticParams() {
    return ACTIVE_VERSIONS.flatMap((version) => {
        const source = apiSources[version];
        if (!source) return [];

        // generateParams() → [{ lang: 'en', slug: [...] }, { lang: 'ja', slug: [...] }, ...]
        return source.generateParams().map((p) => ({ ...p, version }));
    });
}

// ── Metadata ──────────────────────────────────────────────────────────────────

export async function generateMetadata({
    params,
}: {
    params: Promise<{ lang: string; version: string; slug?: string[] }>;
}): Promise<Metadata> {
    const { lang, version, slug } = await params;
    if (!isVersionActive(version)) return { title: 'Not Found' };

    const source = apiSources[version as ApiVersion];
    const page = source?.getPage(slug, lang);
    if (!page) return { title: 'Not Found' };

    return {
        title: `${page.data.title} — API ${version}`,
        description: page.data.description,
    };
}

// ── Page ──────────────────────────────────────────────────────────────────────

export default async function ApiPage({
    params,
}: {
    params: Promise<{ lang: string; version: string; slug?: string[] }>;
}) {
    const { lang, version, slug } = await params;

    if (!isVersionActive(version)) notFound();

    const source = apiSources[version as ApiVersion];
    if (!source) notFound();

    const page = source.getPage(slug, lang);
    if (!page) notFound();

    const { body: Mdx, toc, lastModified } = await page.data.load();
    const { ribbon } = page.data;

    const neighbours = findNeighbour(source.getPageTree(), page.url);
    const footerPrevious = neighbours.previous
        ? { name: neighbours.previous.name, url: neighbours.previous.url }
        : undefined;
    const footerNext = neighbours.next
        ? { name: neighbours.next.name, url: neighbours.next.url }
        : undefined;
    const markdownUrl = `${page.url}.mdx`;

    return (
        <DocsPage toc={toc}>
            <div>
                {/* Title row — clean, no competition */}
                <div className="flex items-start justify-between gap-4">
                    <DocsTitle className="mb-0">{page.data.title}</DocsTitle>
                    {/* <div className="flex items-center gap-2 not-prose shrink-0">
                        <MarkdownCopyButton markdownUrl={markdownUrl} /> */}
                    <DocsPager
                        {...(footerPrevious && {
                            previous: { url: footerPrevious.url },
                        })}
                        {...(footerNext && {
                            next: { url: footerNext.url },
                        })}
                        markdownUrl={markdownUrl}
                    />
                    {/* </div> */}
                </div>

                {/* Ribbon path — sits quietly below the title */}
                {ribbon && <RibbonPath ribbon={ribbon} />}

                {/* Description below ribbon */}
                {page.data.description && (
                    <DocsDescription className="mt-3">{page.data.description}</DocsDescription>
                )}
            </div>
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
                {page.data.index ? <DocsCategory url={page.url} lang={lang} /> : null}
            </DocsBody>
            {lastModified && <PageLastUpdate date={lastModified} />}
        </DocsPage>
    );
}
