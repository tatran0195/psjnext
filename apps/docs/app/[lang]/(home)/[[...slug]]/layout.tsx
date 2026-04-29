import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { source } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const tree = source.getPageTree(params.lang);

    console.log(source.getPages())

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <DocsLayout
                    tree={tree}
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
