import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { PsjLogo } from '@/components/icons/psj-logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { ClientDocsLayout } from '@/components/layout/client-docs-layout';
import { navLinks } from '@/lib/nav-links';
import { source } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]'>) {
    const params = await props.params;
    const { lang } = params;

    const tree = source.getPageTree(lang);

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <ClientDocsLayout
                    tree={tree}
                    links={navLinks}
                    nav={{ mode: 'top', title: <PsjLogo /> }}
                >
                    {props.children}
                </ClientDocsLayout>
                <LinkSidebar />
            </LinkSidebarProvider>
        </TreeContextProvider>
    );
}
