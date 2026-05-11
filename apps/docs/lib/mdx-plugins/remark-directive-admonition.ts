import { visit } from 'unist-util-visit';

import type { BlockContent, DefinitionContent, Root } from 'mdast';
import type { MdxJsxAttribute, MdxJsxFlowElement } from 'mdast-util-mdx';
import type { Transformer } from 'unified';

export interface RemarkDirectiveAdmonitionOptions {
    /**
     * the tag names of Callout component.
     */
    tags?: Record<string, string>;

    /**
     * All supported admonition types and their linked Callout type.
     *
     * When specified, all defaults will be cleared.
     */
    types?: Record<string, string>;
}

/**
 * Remark Plugin to support Admonition syntax in Docusaurus, useful for migrating from Docusaurus.
 *
 * Requires [`remark-directive`](https://github.com/remarkjs/remark-directive) to be configured.
 */
export function remarkDirectiveAdmonition({
    types = {
        note: 'info',
        tip: 'idea',
        info: 'info',
        warn: 'warning',
        warning: 'warning',
        danger: 'error',
        success: 'success',
    },
}: RemarkDirectiveAdmonitionOptions = {}): Transformer<Root, Root> {
    return (tree) => {
        visit(tree, 'containerDirective', (node) => {
            if (!(node.name in types)) return;

            const attributes: MdxJsxAttribute[] = [
                {
                    type: 'mdxJsxAttribute',
                    name: 'type',
                    value: types[node.name],
                },
            ];

            for (const [k, v] of Object.entries(node.attributes ?? {})) {
                if (k === 'title') continue; // Skip title if already handled
                attributes.push({
                    type: 'mdxJsxAttribute',
                    name: k,
                    value: v,
                });
            }

            let title: string | undefined;
            const children: (BlockContent | DefinitionContent)[] = [];

            for (const item of node.children) {
                if (item.type === 'paragraph' && item.data?.directiveLabel) {
                    // Extract text content from title nodes
                    title = item.children.map((child) => ('value' in child ? child.value : '')).join('');
                } else {
                    children.push(item);
                }
            }

            if (title) {
                attributes.push({
                    type: 'mdxJsxAttribute',
                    name: 'title',
                    value: title,
                });
            }

            Object.assign(node, {
                type: 'mdxJsxFlowElement',
                attributes,
                name: 'Callout',
                children,
            } satisfies MdxJsxFlowElement);
        });
    };
}
