import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LinkSidebar, LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { DomainSwitcher } from '@/components/sdk/domain-switcher';
import { VersionSwitcher } from '@/components/sdk/version-switcher';
import { DocsLayout } from '@/layouts/docs';
import { getLayoutTabs } from '@/layouts/shared';
import { getSdk, source } from '@/lib/source';

import type * as PageTree from 'fumadocs-core/page-tree';

export default async function Layout(props: LayoutProps<'/[lang]/[[...slug]]'>) {
    const params = await props.params;
    const { slug = [], lang } = params;
    const isSdk = slug[0] === 'sdk';

    const { manifest } = await getSdk();
    const effectiveVersionId = isSdk ? slug[1] || manifest.current_version : undefined;
    const activeDomainId = isSdk ? slug[2] : undefined;

    const fullTree = source.getPageTree(lang);
    let tree = fullTree;

    if (isSdk && effectiveVersionId) {
        tree = filterTree(fullTree, effectiveVersionId, activeDomainId);
    }

    const domainItems =
        isSdk && effectiveVersionId
            ? manifest.domains.map((d) => ({
                  id: d.id,
                  title: d.title,
                  url: `/${lang}/sdk/${effectiveVersionId}/${d.id}`,
              }))
            : [];

    return (
        <TreeContextProvider tree={tree}>
            <LinkSidebarProvider>
                <DocsLayout
                    tree={tree}
                    tabs={getLayoutTabs(fullTree)}
                    tabMode="navbar"
                    nav={{ mode: 'top', title: <TechnoStarLogo variant="inline" height={34} /> }}
                    sidebar={{
                        banner:
                            isSdk && effectiveVersionId ? (
                                <div className="flex flex-col gap-2 px-3 py-2 -mx-2">
                                    <VersionSwitcher
                                        activeId={effectiveVersionId}
                                        versions={manifest.versions.map((v) => ({
                                            ...v,
                                            label: v.id,
                                            isCurrent: v.id === manifest.current_version,
                                        }))}
                                    />
                                    <DomainSwitcher domains={domainItems} />
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

function filterTree(tree: PageTree.Root, versionId: string, domainId?: string): PageTree.Root {
    // Find the SDK root folder accurately.
    const findSdk = (nodes: PageTree.Node[]): PageTree.Folder | undefined => {
        // First pass: try to find by title/name directly in roots
        for (const node of nodes) {
            if (node.type !== 'folder') continue;
            const title = (node as unknown as Record<string, unknown>).title || node.name;
            const url = (node as unknown as Record<string, unknown>).url || node.index?.url;

            // Strict exclusion of API Reference
            if (title === 'API Reference' || node.name === 'api') continue;
            if (typeof url === 'string' && (url === '/api' || url.startsWith('/api/'))) continue;

            const isSdk = 
                title === 'SDK' || 
                node.name === 'sdk' || 
                (typeof url === 'string' && (url === '/sdk' || url.startsWith('/sdk/')));

            if (isSdk) return node;
        }

        // Second pass: deep search
        for (const node of nodes) {
            if (node.type !== 'folder') continue;
            const sub = node.children.find(c => {
                if (c.type !== 'folder') return false;
                const cTitle = (c as unknown as Record<string, unknown>).title || c.name;
                const cUrl = (c as unknown as Record<string, unknown>).url || c.index?.url;
                if (cTitle === 'API Reference' || c.name === 'api') return false;
                return cTitle === 'SDK' || c.name === 'sdk' || (typeof cUrl === 'string' && (cUrl === '/sdk' || cUrl.startsWith('/sdk/')));
            });
            if (sub) return sub as PageTree.Folder;
        }
        return undefined;
    };

    const sdkFolder = findSdk(tree.children);
    if (!sdkFolder) return tree;

    const versionFolder = sdkFolder.children.find(
        (child): child is PageTree.Folder => child.type === 'folder' && child.name === versionId,
    );

    if (versionFolder) {
        if (domainId) {
            const domainFolder = versionFolder.children.find(
                (child): child is PageTree.Folder => child.type === 'folder' && child.name === domainId,
            );
            if (domainFolder) {
                return {
                    ...tree,
                    children: domainFolder.children,
                };
            }
        }

        return {
            ...tree,
            children: versionFolder.children,
        };
    }

    return tree;
}
