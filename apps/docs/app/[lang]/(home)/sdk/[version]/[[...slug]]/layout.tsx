import type { ReactNode } from 'react';

import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { VersionSwitcher } from '@/components/sdk/version-switcher';
import { DocsLayout } from '@/layouts/docs';
import { getSdkVersions, psjDocs } from '@/lib/psj-source';

import type * as PageTree from 'fumadocs-core/page-tree';

export default async function DocsI18nLayout({
    params,
    children,
}: {
    params: Promise<{ lang: string; version: string }>;
    children: ReactNode;
}) {
    const { lang, version } = await params;
    const fullTree = psjDocs.getPageTree(lang);
    const versions = await getSdkVersions();

    const versionFolder = fullTree.children.find(
        (node) => node.type === 'folder' && node.name === version,
    );

    const versionedTree: PageTree.Root = {
        ...fullTree,
        children: versionFolder?.type === 'folder' ? versionFolder.children : [],
    };

    return (
        <TreeContextProvider tree={versionedTree}>
            <DocsLayout
                tree={versionedTree}
                tabMode="navbar"
                nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
                sidebar={{
                    banner: <VersionSwitcher key="version" versions={versions.all} />,
                }}
            >
                {children}
            </DocsLayout>
        </TreeContextProvider>
    );
}
