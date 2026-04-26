import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { psjDocsSource } from '@/lib/psj-source';
import { source } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const tree = source.getPageTree(params.lang);
    console.log(psjDocsSource.getPageTree(params.lang));

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
