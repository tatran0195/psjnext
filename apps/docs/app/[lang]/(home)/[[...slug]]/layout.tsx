import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { getLayoutTabs } from '@/layouts/shared';
import { source } from '@/lib/source';


export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const { lang } = params;

    const tree = source.getPageTree(lang);

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <DocsLayout
                    tree={tree}
                    tabs={getLayoutTabs(tree)}
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
