import { TechnoStarLogo } from '@/components/icons/logo';
import { DocsLayout } from '@/layouts/docs';
import { source } from '@/lib/source';

import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const tree = source.getPageTree(params.lang);

    return (
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
    );
}
