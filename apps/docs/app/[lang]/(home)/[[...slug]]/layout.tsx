import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { getApiLayoutTab, getLayoutTabs } from '@/layouts/shared';
import { docsSource } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const tree = docsSource.getPageTree(params.lang);
    const tabs = [...getLayoutTabs(tree), getApiLayoutTab(tree, params.lang)];

    console.log(tabs)
    console.log(docsSource.getPageTree())

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <DocsLayout
                    tree={tree}
                    tabs={tabs}
                    tabMode="navbar"
                    nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
                >
                    {props.children}
                </DocsLayout>
                <LinkSidebar />
            </LinkSidebarProvider>
        </TreeContextProvider>
    );
}
