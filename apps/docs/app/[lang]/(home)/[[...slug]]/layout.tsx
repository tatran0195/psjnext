import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DocsLayout } from '@/layouts/docs';
import { getLayoutTabs } from '@/layouts/shared';
import { APP_VERSIONS, source } from '@/lib/source';
import { VersionSwitcher } from '@/components/sdk/version-switcher';
import { compareSemver } from '@/lib/semver';

import type * as PageTree from 'fumadocs-core/page-tree';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const { slug = [], lang } = params;

    const fullTree = source.getPageTree(lang);
    let tree = fullTree;
    let navTree = fullTree;

    const isApp = slug[0] === 'app' && APP_VERSIONS.includes(slug[1]);
    const activeVersionId = isApp ? slug[1] : undefined;

    if (isApp && activeVersionId) {
        navTree = filterAppTree(fullTree, activeVersionId, lang);

        // Find the "app" folder in the already filtered tree
        const appFolder = navTree.children.find(
            (child) =>
                child.type === 'folder' &&
                (child.name === 'Application Programming Guide' ||
                    (child.index && child.index.url.includes('/app')) ||
                    child.children.some((c) => 'url' in c && c.url.includes('/app'))),
        ) as PageTree.Folder;

        if (appFolder) {
            tree = {
                ...navTree,
                children: appFolder.children,
            };
        }
    }

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <DocsLayout
                    tree={tree}
                    tabs={getLayoutTabs(navTree)}
                    tabMode="navbar"
                    nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
                    sidebar={{
                        banner: isApp && activeVersionId ? (
                            <div className="flex flex-col gap-2 px-3 py-2 -mx-2">
                                <VersionSwitcher
                                    activeId={activeVersionId}
                                    versions={APP_VERSIONS.map((v, i) => ({
                                        id: v,
                                        label: v,
                                        isCurrent: i === 0,
                                    }))}
                                />
                            </div>
                        ) : undefined,
                    }}
                >
                    {props.children}
                </DocsLayout>
                <LinkSidebar />
            </LinkSidebarProvider>
        </TreeContextProvider>
    );
}

function filterAppTree(tree: PageTree.Root, versionId: string, lang: string): PageTree.Root {
    function walkNode<T extends PageTree.Node>(node: T): T | null {
        if (node.type === 'page' && typeof node.url === 'string') {
            // Robust slug extraction: remove lang prefix if exists
            const urlParts = node.url.split('/').filter(Boolean);
            if (urlParts[0] && urlParts[0].length === 2) {
                urlParts.shift();
            }
            const slugs = urlParts;
            const page = source.getPage(slugs, lang);
            if (page) {
                const introduced = page.data.version_introduced;
                if (typeof introduced === 'string') {
                    if (compareSemver(versionId, introduced) < 0) {
                        return null; // Not introduced yet
                    }
                }
            }
        }

        const newNode = { ...node };
        if ('url' in newNode && typeof newNode.url === 'string') {
            newNode.url = newNode.url.replace(/\/app(\/|$)/, `/app/${versionId}$1`);
        }
        if ('index' in newNode && newNode.index) {
            newNode.index = walkNode(newNode.index as unknown as PageTree.Item) as any;
        }
        if ('children' in newNode) {
            (newNode as any).children = (newNode as any).children
                .map(walkNode)
                .filter(Boolean);
        }
        return newNode;
    }

    return {
        ...tree,
        children: tree.children.map(walkNode).filter(Boolean) as PageTree.Node[],
    };
}
