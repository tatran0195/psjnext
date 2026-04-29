import type { Folder, Node } from 'fumadocs-core/page-tree';
import { type LoaderPlugin } from 'fumadocs-core/source';
import React from 'react';

import { getSection } from '@/lib/source/navigation';

type FolderWithGroup = Folder & { group?: boolean; groupLevel?: number };

export function pageTreeFoldersPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            folder(node, _dir, metaFile) {
                let groupLevel: number | undefined;
                let isRoot = false;

                if (metaFile) {
                    const meta = this.storage.read(metaFile);
                    const data = meta?.data as {
                        group?: boolean;
                        groupLevel?: number;
                        root?: boolean;
                    };
                    if (data?.groupLevel !== undefined) groupLevel = data.groupLevel;
                    else if (data?.group === true) groupLevel = 0;

                    if (data?.root === true) isRoot = true;
                }

                if ((node as FolderWithGroup).groupLevel !== undefined) {
                    groupLevel = (node as FolderWithGroup).groupLevel;
                } else if ((node as FolderWithGroup).group === true) {
                    groupLevel = 0;
                }

                if ((node as unknown as Record<string, unknown>).root === true) isRoot = true;

                const isGroup = (node as FolderWithGroup).group === true;

                if (groupLevel !== undefined || isRoot || isGroup) {
                    if (groupLevel !== undefined) {
                        node.children = applyGroupLevel(node.children, groupLevel);
                    }

                    // Apply styles
                    applyFolderStyles(node, metaFile);
                }

                return node;
            },
        },
    };
}

function applyGroupLevel(nodes: Node[], level: number): Node[] {
    if (level < 0) return nodes;

    if (level === 0) {
        // This folder itself should be a group (handled by the caller setting group: true)
        return nodes;
    }

    if (level === 1) {
        const result: Node[] = [];
        const flatItems: Node[] = [];

        for (const child of nodes) {
            if (child.type === 'folder') {
                (child as FolderWithGroup).group = true;
                result.push(child);
            } else {
                flatItems.push(child);
            }
        }

        if (flatItems.length > 0) {
            result.push({
                type: 'folder',
                name: 'Other',
                children: flatItems,
                group: true,
            } as FolderWithGroup);
        }

        return result;
    }

    // level > 1: Recurse down
    return nodes.map((node) => {
        if (node.type === 'folder') {
            return {
                ...node,
                children: applyGroupLevel(node.children, level - 1),
            };
        }
        return node;
    });
}

function applyFolderStyles(node: Folder, metaFile: string | undefined) {
    const isGroup = (node as FolderWithGroup).group === true;
    const isRoot = (node as unknown as Record<string, unknown>).root === true;

    if (!isGroup && !isRoot) return;

    // Derive color from metaFile if available, fallback to extracting from url
    let pathForColor = metaFile ? metaFile : undefined;
    const folderUrl =
        (node as unknown as Record<string, unknown>).url ||
        (node.index as unknown as Record<string, unknown>)?.url;

    if (!pathForColor && typeof folderUrl === 'string') {
        const segments = folderUrl.split('/').filter(Boolean);
        const section = segments.find((s: string) => ['api', 'guides', 'data-type', 'sdk'].includes(s));
        if (section) pathForColor = section;
    }

    const color = `var(--${getSection(pathForColor)}-color, var(--color-fd-foreground))`;

    const Box = ({ children }: { children: React.ReactNode }) => (
        <div
            className="flex items-center justify-center [&_svg]:size-[18px] rounded-lg size-8 shrink-0 text-(--tab-color) bg-(--tab-color)/10 border border-(--tab-color)/20 p-1.5"
            style={{ '--tab-color': color } as object}
        >
            {children}
        </div>
    );

    if (node.icon) {
        node.icon = <Box key={node.name?.toString()}>{node.icon}</Box>;
    }

    if (isGroup) {
        const styleChildren = (nodes: Node[]) => {
            for (const child of nodes) {
                if (child.type === 'folder') {
                    if (child.icon) {
                        child.icon = <Box key={child.name?.toString()}>{child.icon}</Box>;
                    }
                    styleChildren(child.children);
                }
            }
        };
        styleChildren(node.children);
    }
}
