import type { ReactNode } from 'react';

import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { DocsLayout } from '@/layouts/docs';
import { psjDocs } from '@/lib/psj-source';

export default async function DocsI18nLayout({
    params,
    children,
}: {
    params: Promise<{ lang: string }>;
    children: ReactNode;
}) {
    const { lang } = await params;
    const tree = psjDocs.getPageTree(lang);

    return (
        <TreeContextProvider tree={tree}>
            <DocsLayout
                tree={tree}
                tabMode="navbar"
                nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
            >
                {children}
            </DocsLayout>
        </TreeContextProvider>
    );
}
