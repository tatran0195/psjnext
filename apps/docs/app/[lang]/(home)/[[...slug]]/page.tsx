import type { Metadata } from 'next';
import type { ComponentProps, FC } from 'react';

import Link from 'fumadocs-core/link';
import * as PageTree from 'fumadocs-core/page-tree';
import { findNeighbour } from 'fumadocs-core/page-tree';
import { PathUtils } from 'fumadocs-core/source';
import * as Twoslash from 'fumadocs-twoslash/ui';
import { Banner } from 'fumadocs-ui/components/banner';
import { Callout } from 'fumadocs-ui/components/callout';
import { TypeTable } from 'fumadocs-ui/components/type-table';

import { NotFound } from '@/components/layouts/not-found';
import { getMDXComponents } from '@/components/mdx';
import { compareSemver } from '@/lib/semver';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { Mermaid } from '@/components/mdx/mermaid';
import { RibbonPath } from '@/components/mdx/ribbon-path';
import { SymbolLink } from '@/components/mdx/symbol-link';
import { FolderIndex } from '@/components/sdk/folder-index';
import {
    DocsBody,
    DocsDescription,
    DocsPage,
    DocsTitle,
    PageLastUpdate,
} from '@/layouts/docs/page';
import { DocsPager } from '@/layouts/shared/docs-pager';
import { createMetadata, getPageImage } from '@/lib/metadata';
import { APP_VERSIONS, source } from '@/lib/source';

export default async function Page(props: {
    params: Promise<{ slug?: string[]; lang: string; version?: string }>;
    searchParams: Promise<{ v?: string }>;
}) {
    const params = await props.params;
    const { slug = [], lang } = params;

    let querySlug = slug;
    let isAppVersion = false;
    let activeVersion: string | undefined;

    if (slug[0] === 'app' && APP_VERSIONS.includes(slug[1])) {
        isAppVersion = true;
        activeVersion = slug[1];
        querySlug = ['app', ...slug.slice(2)];
    }

    let page = source.getPage(querySlug, lang);
    let indexFolder: PageTree.Folder | undefined;

    if (!page) {
        // Try to find if it's a folder to show a category index
        const tree = source.getPageTree(lang);
        let current: PageTree.Node[] = tree.children;
        let foundFolder: PageTree.Folder | undefined;

        for (const segment of querySlug) {
            const node = current.find(
                (n): n is PageTree.Folder =>
                    n.type === 'folder' && n.name.toLowerCase() === segment.toLowerCase(),
            );

            if (node) {
                foundFolder = node;
                current = node.children;
            } else {
                foundFolder = undefined;
                break;
            }
        }

        if (foundFolder) {
            indexFolder = foundFolder;
            // Create a virtual page for the folder
            page = {
                slugs: querySlug,
                url: `/${lang}/${querySlug.join('/')}`,
                data: {
                    title: foundFolder.name,
                    description: '',
                    index: true,
                    // Folders are always considered compatible with all versions for routing purposes
                    // (They just show the compatible children)
                    load: async () => ({
                        body: (() => null) as any,
                        toc: [],
                        lastModified: undefined,
                    }),
                },
            } as any;
        }
    }

    if (!page) {
        return <NotFound getSuggestions={async () => (params.slug ? [] : [])} />;
    }

    if (isAppVersion && activeVersion) {
        const introduced = page.data.version_introduced;
        if (typeof introduced === 'string') {
            if (compareSemver(activeVersion, introduced) < 0) {
                return <NotFound getSuggestions={async () => (params.slug ? [] : [])} />;
            }
        }
    }

    // Resolve folder for index pages if not already found
    if (page.data.index && !indexFolder) {
        const tree = source.getPageTree(lang);
        let current: PageTree.Node[] = tree.children;
        for (const segment of querySlug) {
            const next = current.find(
                (n): n is PageTree.Folder =>
                    n.type === 'folder' && n.name.toLowerCase() === segment.toLowerCase(),
            );
            if (!next) {
                indexFolder = undefined;
                break;
            }
            indexFolder = next;
            current = next.children;
        }
    }

    const { body: Mdx, toc, lastModified } = await page.data.load();
    const { ribbon } = page.data;

    const neighbours = findNeighbour(source.getPageTree(lang), page.url);
    const resolveUrl = (url: string) => {
        if (!isAppVersion || !activeVersion) return url;
        return url.replace(/\/app(\/|$)/, `/app/${activeVersion}$1`);
    };

    const footerPrevious = neighbours.previous
        ? { name: neighbours.previous.name, url: resolveUrl(neighbours.previous.url) }
        : undefined;
    const footerNext = neighbours.next
        ? { name: neighbours.next.name, url: resolveUrl(neighbours.next.url) }
        : undefined;
    const markdownUrl = `${page.url}.mdx`;

    return (
        <DocsPage toc={toc}>
            <div>
                {/* Title row — clean, no competition */}
                <div className="flex flex-wrap items-start justify-between gap-4">
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
                        a({ href, ...props }: ComponentProps<'a'>) {
                            if (!href) return <a {...props} />;

                            const found = source.getPageByHref(href, {
                                dir: PathUtils.dirname(page.path),
                            });

                            if (!found) return <Link href={resolveUrl(href)} {...props} />;

                            return (
                                <LinkPreview
                                    href={resolveUrl(found.page.url)}
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
                        DocsCategory: ({ url }: { url?: string }) => {
                            return <DocsCategory url={url ?? page.url} lang={lang} resolveUrl={resolveUrl} />;
                        },
                        DocsSectionOverview: ({ url }: { url?: string }) => {
                            return <DocsSectionOverview url={url ?? page.url} lang={lang} resolveUrl={resolveUrl} />;
                        },
                    })}
                />
                {indexFolder ? (
                    <FolderIndex folder={indexFolder} resolveUrl={resolveUrl} />
                ) : page.data.index ? (
                    <DocsCategory url={page.url} lang={lang} resolveUrl={resolveUrl} />
                ) : null}
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
    if (slug[0] === 'app' && APP_VERSIONS.includes(slug[1])) {
        querySlug = ['app', ...slug.slice(2)];
    }

    const page = source.getPage(querySlug, lang);
    if (!page) {
        return createMetadata({
            title: 'Not Found',
        });
    }

    if (slug[0] === 'app' && APP_VERSIONS.includes(slug[1])) {
        const activeVersion = slug[1];
        const introduced = page.data.version_introduced;
        if (typeof introduced === 'string') {
            if (compareSemver(activeVersion, introduced) < 0) {
                return createMetadata({
                    title: 'Not Found',
                });
            }
        }
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
    const params = source.generateParams('slug', 'lang');
    const fannedParams: unknown[] = [];
    for (const param of params) {
        if (param.slug && param.slug[0] === 'app') {
            const page = source.getPage(param.slug as string[], param.lang as string);
            for (const version of APP_VERSIONS) {
                let skip = false;
                if (page) {
                    const introduced = page.data.version_introduced;
                    if (typeof introduced === 'string') {
                        if (compareSemver(version, introduced) < 0) {
                            skip = true;
                        }
                    }
                }
                if (!skip) {
                    fannedParams.push({
                        ...param,
                        slug: ['app', version, ...param.slug.slice(1)],
                    });
                }
            }
        } else {
            fannedParams.push(param);
        }
    }
    return fannedParams;
}
