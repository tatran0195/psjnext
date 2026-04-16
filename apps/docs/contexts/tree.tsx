'use client';
import { getFirstUrl, type LayoutTab } from '@/layouts/shared';
import { searchPath } from 'fumadocs-core/breadcrumb';
import { usePathname } from 'fumadocs-core/framework';
import type * as PageTree from 'fumadocs-core/page-tree';
import { createContext, type ReactNode, use, useMemo } from 'react';

export interface NestedTab {
    tabs: LayoutTab[];
    active?: LayoutTab;
}

interface TreeContextType {
    root: PageTree.Root | PageTree.Folder;
    full: PageTree.Root;
    nestedTabs: NestedTab[];
}

const TreeContext = createContext<TreeContextType | null>(null);
const PathContext = createContext<PageTree.Node[]>([]);

export function TreeContextProvider({
    tree: rawTree,
    children,
}: {
    tree: PageTree.Root;
    children: ReactNode;
}) {
    const pathname = usePathname();

    const tree = useMemo(() => rawTree, [rawTree.$id ?? rawTree]);

    const path = useMemo(() => {
        return (
            searchPath(tree.children, pathname) ??
            (tree.fallback ? searchPath(tree.fallback.children, pathname) : null) ??
            []
        );
    }, [tree, pathname]);

    const nestedTabs = useMemo(() => {
        const result: NestedTab[] = [];

        for (const node of path) {
            if (node.type === 'folder' && (node as PageTree.Folder & { group: boolean }).group) {
                const options = node.children.filter(
                    (n) => n.type === 'folder',
                ) as PageTree.Folder[];
                if (options.length === 0) continue;

                const tabs = options.map((folder) => {
                    const url = getFirstUrl(folder) ?? '';

                    const tab: LayoutTab = {
                        title: folder.name,
                        url,
                        icon: folder.icon,
                        description: folder.description,
                        $folder: folder,
                    };

                    return tab;
                }) as LayoutTab[];

                const active =
                    tabs.find((t) => path.includes(t.$folder as unknown as PageTree.Node)) ??
                    tabs[0];
                result.push({ tabs, active });
            }
        }

        return result;
    }, [path]);

    const lastActiveTab = nestedTabs[nestedTabs.length - 1]?.active;
    const root =
        lastActiveTab?.$folder ??
        path.findLast((item) => item.type === 'folder' && item.root) ??
        tree;

    return (
        <TreeContext
            value={useMemo(
                () => ({ root, full: tree, nestedTabs }) as TreeContextType,
                [root, tree, nestedTabs],
            )}
        >
            <PathContext value={path}>{children}</PathContext>
        </TreeContext>
    );
}

export function useTreePath(): PageTree.Node[] {
    return use(PathContext);
}

export function useTreeContext(): TreeContextType {
    const ctx = use(TreeContext);

    if (!ctx) throw new Error('You must wrap this component under <DocsLayout />');
    return ctx;
}
