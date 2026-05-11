import { ReactNode } from 'react';

import * as PageTree from 'fumadocs-core/page-tree';
import { findSiblings } from 'fumadocs-core/page-tree';
import { Card, Cards } from 'fumadocs-ui/components/card';

import { source } from '@/lib/source';

export function DocsCategory({
    url,
    lang,
    resolveUrl = (u) => u,
}: {
    url: string;
    lang: string;
    resolveUrl?: (url: string) => string;
}) {
    return (
        <Cards>
            {findSiblings(source.getPageTree(lang), url).map((item) => {
                if (item.type === 'separator') return null;
                const node = item.type === 'folder' ? item.index : item;
                if (!node || node.type !== 'page') return null;

                return (
                    <Card key={node.url} title={node.name} href={resolveUrl(node.url)}>
                        {node.description}
                    </Card>
                );
            })}
        </Cards>
    );
}

export function DocsSectionOverview({
    url,
    lang,
    resolveUrl = (u) => u,
}: {
    url: string;
    lang: string;
    resolveUrl?: (url: string) => string;
}) {
    function folderContainsPath(node: PageTree.Folder, path: string): boolean {
        if (node.index?.url === path) return true;
        return node.children.some((child) => {
            if (child.type === 'page' && child.url === path) return true;
            if (child.type === 'folder') return folderContainsPath(child, path);
            return false;
        });
    }

    function findNodeWithUrl(tree: PageTree.Node[], path: string): PageTree.Folder | null {
        for (const node of tree) {
            if (node.type === 'folder') {
                if (node.index?.url === path) return node;
                if (folderContainsPath(node, path)) {
                    const found = findNodeWithUrl(node.children, path);
                    return found ?? node;
                }
            }
        }
        return null;
    }

    const node = findNodeWithUrl(source.getPageTree(lang).children, url);
    const items = node?.children ?? [];

    return (
        <Cards>
            {items.map((item, i) => {
                if (item.type !== 'folder' && item.type !== 'page') return null;
                const title = String(item.name);
                let description: ReactNode = '';
                let href = '';

                if (item.type === 'folder') {
                    if (!item.index) return null;
                    description = item.index.description ?? '';
                    href = item.index.url;
                } else {
                    description = item.description ?? '';
                    href = item.url;
                }

                return (
                    <Card key={i} title={title.replace('PSJ ', '')} href={resolveUrl(href)} description={description} />
                );
            })}
        </Cards>
    );
}
