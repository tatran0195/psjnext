import { visit } from 'unist-util-visit';

import type { Root, Link, Parent, PhrasingContent } from 'mdast';
import type { MdxJsxAttribute } from 'mdast-util-mdx';
import type { Plugin } from 'unified';

export interface RemarkLinkPreviewOptions {
    tag?: string;
    internalPrefix?: string[];
}

export const remarkLinkPreview: Plugin<[RemarkLinkPreviewOptions?], Root> = (options) => {
    const { tag = 'LinkPreview', internalPrefix = ['/docs', '../', './'] } = options ?? {};

    return (tree) => {
        visit(tree, 'link', (node: Link, index, parent: Parent | null) => {
            const isInternal =
                internalPrefix.some((prefix) => node.url === prefix || node.url.startsWith(prefix)) ||
                node.url.startsWith('/');
            const isNotPreview = node.url.endsWith('.zip') || node.url.endsWith('.step');
            if (!isInternal || isNotPreview) return;
            if (parent === null || index === undefined) return;

            const attributes: MdxJsxAttribute[] = [
                {
                    type: 'mdxJsxAttribute',
                    name: 'href',
                    value: node.url,
                },
            ];

            // Object.assign(node, {
            //     type: 'mdxJsxTextElement',
            //     name: tag,
            //     attributes,
            //     children: node.children as PhrasingContent[],
            // } satisfies MdxJsxTextElement);
            parent.children[index] = {
                type: 'mdxJsxTextElement',
                name: tag,
                attributes,
                children: node.children as PhrasingContent[],
            };
        });
    };
};
