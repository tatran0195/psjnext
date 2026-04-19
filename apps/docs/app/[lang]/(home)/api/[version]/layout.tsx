import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';

import { TechnoStarLogo } from '@/components/icons/logo';
import { VersionSwitcher } from '@/components/layouts/VersionSwitcher';
import { LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { apiSources, type ApiVersion } from '@/lib/source';
import { isVersionActive } from '@/lib/versions';

export default async function ApiVersionLayout({
    params,
    children,
}: {
    params: Promise<{ lang: string; version: string }>;
    children: ReactNode;
}) {
    const { lang, version } = await params;
    if (!isVersionActive(version)) notFound();

    const source = apiSources[version as ApiVersion];
    if (!source) notFound();

    const tree = source.getPageTree(lang);

    return (
        <LinkSidebarProvider>
            <DocsLayout
                tree={tree}
                tabMode="navbar"
                nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
                sidebar={{
                    banner: <VersionSwitcher key={version} />,
                }}
            >
                {children}
            </DocsLayout>
        </LinkSidebarProvider>
    );
}
