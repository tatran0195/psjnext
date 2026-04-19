import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { docsSource } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const tree = docsSource.getPageTree(params.lang);

    return (
        <LinkSidebarProvider>
            <DocsLayout
                tree={tree}
                tabMode="sidebar"
                nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
            >
                {props.children}
            </DocsLayout>
            <LinkSidebar />
        </LinkSidebarProvider>
    );
}
