import type { Metadata } from 'next';
import type { ComponentProps, FC } from 'react';

import Link from 'fumadocs-core/link';
import { findNeighbour } from 'fumadocs-core/page-tree';
import { PathUtils } from 'fumadocs-core/source';
import * as Twoslash from 'fumadocs-twoslash/ui';
import { Callout } from 'fumadocs-ui/components/callout';
import { Locale } from 'next-intl';

import { NotFound } from '@/components/layouts/not-found';
import { getMDXComponents } from '@/components/mdx';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { ParamHeader, ParamSection } from '@/components/mdx/param-section';
import { RibbonPath } from '@/components/mdx/ribbon-path';
import { DeprecatedBadge, VersionBadge } from '@/components/mdx/version-badge';
import { env } from '@/env';
import { DocsBody, DocsDescription, DocsPage, DocsTitle, PageLastUpdate } from '@/layouts/docs/page';
import { DocsPageActions } from '@/layouts/shared/page-actions';
import { getVersionStatus } from '@/lib/api-versions';
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
    const isVersionSegment = (env.API_VERSIONS as readonly string[]).includes(maybeVersion);
    return isVersionSegment
        ? { version: maybeVersion, pageSlug: rest }
        : { version: env.API_VERSIONS[0], pageSlug: slug };
}

export default async function Page(props: {
    params: Promise<{ slug?: string[]; locale: Locale }>;
    searchParams: Promise<{ v?: string }>;
}) {
    const params = await props.params;
    const { slug = [], locale } = params;

    let apiMdxComponents: Partial<Parameters<typeof getMDXComponents>[0]> | undefined;
    const page = source.getPage(slug, locale);
    if (!page) {
        const query = slug.join(' ');
        return <NotFound getSuggestions={() => getSuggestions(query)} />;
    }

    let version: string | undefined;
    let isDeprecated = false;

    if (slug[0] === 'api') {
        const resolved = resolveVersion(slug.slice(1));
        version = resolved.version;

        const status = getVersionStatus(version, page.data.since, page.data.deprecated, page.data.removed);
        isDeprecated = status === 'deprecated';

        apiMdxComponents = {
            h3: (props: ComponentProps<'h3'>) => <ParamHeader {...props} />,
            ParamSection: (props: Omit<ComponentProps<typeof ParamSection>, 'currentVersion'>) => (
                <ParamSection {...props} currentVersion={version!} />
            ),
        };
    }

    const { body: Mdx, toc, lastModified } = await page.data.load();
    const { ribbon, shortcut } = page.data;

    const neighbours = findNeighbour(source.getPageTree(locale), page.url);
    const footerPrevious = neighbours.previous
        ? { name: neighbours.previous.name, url: neighbours.previous.url }
        : undefined;
    const footerNext = neighbours.next ? { name: neighbours.next.name, url: neighbours.next.url } : undefined;
    const markdownUrl = `${page.url}.mdx`;

    return (
        <DocsPage toc={toc} breadcrumb={{ enabled: false }}>
            <div>
                <div className="space-y-2">
                    {page.data.since && <VersionBadge version={page.data.since} />}
                    <div className="flex flex-wrap items-center justify-between gap-4">
                        <div className="relative inline-block">
                            <DocsTitle className="mb-0">{page.data.title}</DocsTitle>

                            {isDeprecated && (
                                <div className="absolute left-full top-1 ml-4 whitespace-nowrap">
                                    <DeprecatedBadge />
                                </div>
                            )}
                        </div>

                        <DocsPageActions
                            {...(footerPrevious && { previous: { url: footerPrevious.url } })}
                            {...(footerNext && { next: { url: footerNext.url } })}
                            markdownUrl={markdownUrl}
                        />
                    </div>
                </div>

                {ribbon && <RibbonPath ribbon={ribbon} shortcut={shortcut} variant="inline" />}

                {page.data.description && <DocsDescription className="mt-3">{page.data.description}</DocsDescription>}
            </div>
            <DocsBody>
                <Mdx
                    components={getMDXComponents({
                        ...Twoslash,
                        a({ href, ...props }: ComponentProps<'a'>) {
                            if (!href) return <Link href={href} {...props} />;
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
                        LinkPreview,
                        blockquote: Callout as unknown as FC<ComponentProps<'blockquote'>>,
                        DocsCategory: ({ url }: { url?: string }) => (
                            <DocsCategory url={url ?? page.url} lang={locale} />
                        ),
                        DocsSectionOverview: ({ url }: { url?: string }) => (
                            <DocsSectionOverview url={url ?? page.url} lang={locale} />
                        ),
                        ...apiMdxComponents,
                    })}
                />
                {page.data.index ? <DocsCategory url={page.url} lang={locale} /> : null}
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
    if (slug[1] === 'api' && (env.API_VERSIONS as readonly string[]).includes(slug[2])) {
        querySlug = ['api', ...slug.slice(2)];
    }

    const page = source.getPage(querySlug, lang);
    if (!page) {
        return createMetadata({ title: 'Not Found' });
    }
    const description = page.data.description ?? 'Python Scripting for Jupiter';
    const image = {
        url: getPageImage(page).url,
        width: 1200,
        height: 630,
    };

    return createMetadata({
        title: page.data.title,
        description,
        openGraph: {
            url: page.url,
            images: [image],
        },
        twitter: {
            images: [image],
        },
    });
}

export function generateStaticParams() {
    const docsParams = source.generateParams('slug', 'locale');
    const apiParams = source
        .getPages()
        .filter((p) => p.slugs[1] === 'api' && p.slugs[2] !== undefined)
        .flatMap((p) =>
            env.API_VERSIONS.map((version) => ({
                slug: ['api', version, ...p.slugs.slice(2)],
                lang: 'en',
            })),
        );

    return [...docsParams, ...apiParams];
}
