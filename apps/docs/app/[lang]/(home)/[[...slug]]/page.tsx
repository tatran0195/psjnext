import type { Metadata } from 'next';
import type { ComponentProps, FC, ReactNode } from 'react';

import Link from 'fumadocs-core/link';
import { findNeighbour } from 'fumadocs-core/page-tree';
import { PathUtils } from 'fumadocs-core/source';
import * as Twoslash from 'fumadocs-twoslash/ui';
import { Banner } from 'fumadocs-ui/components/banner';
import { Callout } from 'fumadocs-ui/components/callout';
import { TypeTable } from 'fumadocs-ui/components/type-table';

import { NotFound } from '@/components/layouts/not-found';
import { getMDXComponents } from '@/components/mdx';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { Mermaid } from '@/components/mdx/mermaid';
import { RibbonPath } from '@/components/mdx/ribbon-path';
import { SymbolLink } from '@/components/mdx/symbol-link';
import * as Preview from '@/components/preview';
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
import { createMetadata, getPageImage } from '@/lib/metadata';
import { source } from '@/lib/source';

function PreviewRenderer({ preview }: { preview: string }): ReactNode {
    if (preview && preview in Preview) {
        const Comp = Preview[preview as keyof typeof Preview];
        return <Comp />;
    }

    return null;
}

export const revalidate = false;
// Always allow dynamic params so all routes resolve on-demand.
export const dynamicParams = true;

// In dev, skip pre-rendering all pages — compile on demand for speed.
// In production, statically generate all pages as normal.
const IS_PROD = process.env.NODE_ENV === 'production';

export default async function Page(props: { params: Promise<{ slug?: string[]; lang: string }> }) {
    const params = await props.params;
    const page = source.getPage(params.slug, params.lang);

    if (!page) return <NotFound getSuggestions={async () => (params.slug ? [] : [])} />;

    // if (page.data.type === 'openapi') {
    //     const { APIPage } = await import('@/components/api-page');
    //     return (
    //         <DocsPage full>
    //             <h1 className="text-[1.75em] font-semibold">{page.data.title}</h1>

    //             <DocsBody>
    //                 <APIPage {...page.data.getAPIPageProps()} />
    //             </DocsBody>
    //         </DocsPage>
    //     );
    // }

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
                {page.data.preview && <PreviewRenderer preview={page.data.preview} />}
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
                            return <DocsCategory url={url ?? page.url} lang={params.lang} />;
                        },
                        DocsSectionOverview: ({ url }) => {
                            return <DocsSectionOverview url={url ?? page.url} lang={params.lang} />;
                        },
                        Installation,
                        Customisation,
                    })}
                />
                {page.data.index ? <DocsCategory url={page.url} lang={params.lang} /> : null}
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
    const page = source.getPage(slug, lang);
    if (!page)
        return createMetadata({
            title: 'Not Found',
        });

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
    if (!IS_PROD) return [];
    return source.generateParams('slug', 'locale');
}
