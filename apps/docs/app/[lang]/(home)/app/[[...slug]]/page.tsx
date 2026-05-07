import { notFound, redirect } from 'next/navigation';

import type { ApiVersion, VersionStatus } from '@/lib/api-versions';
import type { VersionedPageFrontmatter } from '@/lib/source/plugins/version-plugin';

import { getMDXComponents } from '@/components/mdx';
import { DocsBody, DocsPage, DocsTitle } from '@/layouts/docs/page';
import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';
import { source } from '@/lib/source';

import { PSJParamHeader, PSJParamSection } from './psj-param-badge';
import { VersionDropdown } from './version-dropdown';

interface PageParams {
    slug?: string[];
}

interface VersionedPageData extends VersionedPageFrontmatter {
    _status: VersionStatus;
    load: () => Promise<{ body: React.ComponentType<{ components: unknown }> }>;
}

/**
 * Resolve [version, ...pageSlug] from the raw catch-all segments.
 *
 * /app/5.1.0/getting-started → { version: '5.1.0', pageSlug: ['getting-started'], versionless: false }
 * /app/getting-started       → { version: '5.1.0', pageSlug: ['getting-started'], versionless: true }
 * /app                       → { version: '5.1.0', pageSlug: [],                  versionless: true }
 */
function resolveVersion(slug: string[]): {
    version: string;
    pageSlug: string[];
    versionless: boolean;
} {
    const [maybeVersion, ...rest] = slug;
    const isVersionSegment = (API_VERSIONS as readonly string[]).includes(maybeVersion);

    return isVersionSegment
        ? { version: maybeVersion, pageSlug: rest, versionless: false }
        : { version: API_VERSIONS[0], pageSlug: slug, versionless: true };
}

export async function generateStaticParams(): Promise<PageParams[]> {
    // Emit only the versioned canonical paths. Versionless URLs are handled
    // at runtime via redirect — they must not be statically pre-rendered since
    // the target version could change when a new version is released.
    return source
        .getPages()
        .filter((p) => p.slugs[0] === 'app' && p.slugs[1] !== undefined)
        .map((p) => ({
            ...(p.slugs.length > 2 && { slug: p.slugs.slice(1) }),
        }));
}

export default async function ApiPage({ params }: { params: PageParams }) {
    const { slug = [] } = await params;
    const { version, pageSlug, versionless } = resolveVersion(slug);

    // Redirect versionless URLs to their canonical versioned form so crawlers
    // and shared links always point at a stable, version-pinned URL.
    if (!versionless) {
        const target =
            pageSlug.length > 0 ? `/app/${version}/${pageSlug.join('/')}` : `/app/${version}`;
        redirect(target);
    }

    const page = source.getPage(['app', ...pageSlug]);
    if (!page) notFound();

    const fm = page.data as unknown as VersionedPageData;

    if (fm._status === 'removed') notFound();

    const versionMeta = API_VERSIONS.map((v) => ({
        version: v,
        status: getVersionStatus(v, fm.introduced, fm.deprecated, fm.removed),
    })).filter(({ status }) => status !== 'unavailable' && status !== 'removed');

    const { body: Mdx } = await fm.load();

    return (
        <DocsPage>
            <DocsTitle>{fm.title}</DocsTitle>
            <VersionDropdown
                currentVersion={version as ApiVersion}
                baseSlug={pageSlug}
                versionMeta={versionMeta}
                status={fm._status}
            />
            <DocsBody>
                <Mdx
                    components={getMDXComponents({
                        h3: (props) => <PSJParamHeader {...props} />,
                        PSJParamSection: (props) => (
                            <PSJParamSection currentVersion={version as ApiVersion} {...props} />
                        ),
                    })}
                />
            </DocsBody>
        </DocsPage>
    );
}
