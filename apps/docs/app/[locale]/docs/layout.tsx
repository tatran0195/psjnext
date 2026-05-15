import { PsjLogo } from '@/components/icons/psj-logo';
import { DocsLayout } from '@/layouts/docs';
import { navLinks } from '@/lib/nav-links';
import { source } from '@/lib/source';

export default async function Layout({ children, params }: LayoutProps<'/[locale]'>) {
    const { locale } = await params;
    const tree = source.getPageTree(locale);
    return (
        <DocsLayout tree={tree} tabs={[]} links={navLinks} nav={{ mode: 'top', title: <PsjLogo /> }}>
            {children}
        </DocsLayout>
    );
}
