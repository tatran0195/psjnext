import { TechnoStarLogo } from '@/components/icons/logo';
import { DocsLayout } from '@/layouts/docs';
import { getLayoutTabs } from '@/layouts/shared';
import { source } from '@/lib/source';

export default async function ApiVersionLayout(
    props: LayoutProps<'/[lang]/app/[version]/[[...slug]]'>,
) {
    const params = await props.params;
    const tree = source.getPageTree();
    const appFolder = tree.children.find(
        (n) => n.type === 'folder' && typeof n.name === 'string' && n.name.toLowerCase() === 'app',
    );
    const versionSubtree =
        appFolder && appFolder.type === 'folder'
            ? appFolder.children.find((n) => n.type === 'folder' && n.name === params.version)
            : undefined;

    const filteredTree = versionSubtree ? { ...tree, children: [versionSubtree] } : tree;

    return (
        <DocsLayout
            tree={filteredTree}
            tabs={getLayoutTabs(tree)}
            tabMode="navbar"
            nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
        >
            {props.children}
        </DocsLayout>
    );
}
