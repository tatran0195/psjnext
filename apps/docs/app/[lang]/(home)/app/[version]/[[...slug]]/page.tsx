import { notFound } from 'next/navigation';

import type { ApiVersion, VersionStatus } from '@/lib/api-versions';
import type { VersionedPageFrontmatter } from '@/lib/source/plugins/version-plugin';

import { getMDXComponents } from '@/components/mdx';
import { DocsBody, DocsPage, DocsTitle } from '@/layouts/docs/page';
import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';
import { source } from '@/lib/source';

import { PSJParamHeader, PSJParamSection } from './psj-param-badge';
import { TombstonePage } from './tombstone-page';
import { VersionDropdown } from './version-dropdown';

interface Props {
    params: { version: string; slug: string[] };
}

export async function generateStaticParams() {
    // source.getPages() already contains the versioned virtual pages
    return source
        .getPages()
        .filter((p) => p.slugs[0] === 'app' && p.slugs[1] !== undefined)
        .map((p) => ({
            version: p.slugs[1],
            slug: p.slugs.slice(2),
        }));
}

export default async function ApiVersionPage({ params }: Props) {
    const { version, slug = [] } = await params;

    if (!(API_VERSIONS as readonly string[]).includes(version)) notFound();

    // Versioned slugs are ['app', version, ...slug]
    const page = source.getPage(['app', version, ...slug]);
    if (!page) notFound();

    const fm = page.data as unknown as VersionedPageFrontmatter & {
        _status: VersionStatus;
        body: unknown;
    };

    const status = fm._status;

    // Build version availability map (iterate all versions, check status from frontmatter)
    const versionMeta = API_VERSIONS.map((v) => ({
        version: v,
        status: getVersionStatus(v, fm.introduced, fm.deprecated, fm.removed),
    })).filter(({ status }) => status !== 'unavailable');

    if (status === 'removed') {
        return (
            <DocsPage>
                <TombstonePage
                    title={fm.title}
                    version={version as ApiVersion}
                    removedIn={fm.removed!}
                    versionMeta={versionMeta}
                />
            </DocsPage>
        );
    }

    const { body: Mdx } = await page.data.load();

    return (
        <DocsPage>
            <DocsTitle>{fm.title}</DocsTitle>
            <VersionDropdown
                currentVersion={version as ApiVersion}
                baseSlug={slug}
                versionMeta={versionMeta as unknown as { version: string; status: string }[]}
                status={status as unknown as ApiVersion}
            />
            <DocsBody>
                <Mdx
                    components={getMDXComponents({
                        h3: (props) => (
                            <PSJParamHeader
                                currentVersion={version as ApiVersion}
                                {...(props as any)}
                            />
                        ),
                        PSJParamHeader: (props) => (
                            <PSJParamHeader
                                currentVersion={version as ApiVersion}
                                {...(props as any)}
                            />
                        ),
                        PSJParamSection: (props) => (
                            <PSJParamSection
                                currentVersion={version as ApiVersion}
                                {...(props as any)}
                            />
                        ),
                    })}
                />
            </DocsBody>
        </DocsPage>
    );
}
