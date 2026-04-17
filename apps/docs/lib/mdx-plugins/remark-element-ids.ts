import { visit } from 'unist-util-visit';

import type { Root } from 'mdast';
import type { Transformer } from 'unified';

/**
 * Remark plugin that extracts `id` attributes from MDX JSX elements.
 *
 * This plugin traverses the MDX AST and collects all static `id` attribute
 * values from JSX block elements (`mdxJsxFlowElement`). The collected IDs
 * are stored in `file.data.elementIds` for later use (e.g. linting, validation,
 * or metadata processing).
 *
 * @returns A unified transformer that augments `file.data` with an `elementIds` array.
 *
 * @example
 * Input (MDX):
 * ```mdx
 * <Card id="intro" />
 * <Callout id="warning" />
 * ```
 *
 * Output:
 * ```ts
 * file.data.elementIds = ['intro', 'warning'];
 * ```
 *
 * @remarks
 * - Only supports JSX block elements (`mdxJsxFlowElement`)
 * - Ignores inline JSX (`mdxJsxTextElement`)
 * - Only extracts static string values (`id="..."`)
 * - Dynamic values (e.g. `id={value}`) are ignored
 *
 * @see file.data.elementIds
 */
export function remarkElementIds(): Transformer<Root, Root> {
    return (tree, file) => {
        file.data ??= {};
        file.data.elementIds ??= [];

        visit(tree, 'mdxJsxFlowElement', (element) => {
            if (!element.name || !element.attributes) return;

            const idAttr = element.attributes.find(
                (attr) => attr.type === 'mdxJsxAttribute' && attr.name === 'id',
            );

            if (idAttr && typeof idAttr.value === 'string') {
                (file.data.elementIds as string[]).push(idAttr.value);
            }
        });
    };
}
