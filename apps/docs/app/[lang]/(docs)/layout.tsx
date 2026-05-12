import { PsjLogo } from '@/components/icons/psj-logo';
import { DocsLayout } from '@/layouts/docs';
import { navLinks } from '@/lib/nav-links';
import { source } from '@/lib/source';

export default async function Layout(props: LayoutProps<'/[lang]'>) {
    const params = await props.params;
    const { lang } = params;
    const tree = source.getPageTree(lang);
    return (
        <DocsLayout tree={tree} tabs={[]} links={navLinks} nav={{ mode: 'top', title: <PsjLogo /> }}>
            {props.children}
        </DocsLayout>
    );
}
