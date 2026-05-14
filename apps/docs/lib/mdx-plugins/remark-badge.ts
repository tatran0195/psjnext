import { visit } from 'unist-util-visit';

import type { Root } from 'mdast';
import type { Plugin } from 'unified';

export type BadgeVariant = 'feature' | 'fix' | 'api' | 'utility' | 'macro' | 'data' | 'highlight' | 'default';

export type BadgeIcon = 'zap' | 'bug' | 'code2' | 'wrench' | 'braces' | 'database' | 'sparkles' | 'tag';

const SHORTHAND_VARIANTS = [
    'feature',
    'fix',
    'api',
    'utility',
    'macro',
    'data',
    'highlight',
] as const satisfies ReadonlyArray<BadgeVariant>;

// AST node types
interface MdxJsxAttribute {
    type: 'mdxJsxAttribute';
    name: string;
    value: string;
}

interface MdxJsxTextElement {
    type: 'mdxJsxTextElement';
    name: string;
    attributes: MdxJsxAttribute[];
    children: [];
    data: { _mdxExplicitJsx: true };
}

interface TextDirectiveNode {
    type: 'textDirective';
    name: string;
    // remark-directive stores parsed attributes here
    attributes?: Record<string, string>;
    children: Array<{ type: string; value?: string }>;
}

function createBadgeNode(label: string, variant: BadgeVariant = 'default', icon?: string): MdxJsxTextElement {
    const attributes: MdxJsxAttribute[] = [
        {
            type: 'mdxJsxAttribute',
            name: 'variant',
            value: variant,
        },
        {
            type: 'mdxJsxAttribute',
            name: 'label',
            value: label,
        },
    ];

    if (icon) {
        attributes.push({
            type: 'mdxJsxAttribute',
            name: 'icon',
            value: icon,
        });
    }

    return {
        type: 'mdxJsxTextElement',
        name: 'Badge',
        attributes,
        children: [],
        data: { _mdxExplicitJsx: true },
    };
}

/**
 * Remark plugin to convert text directives into Badge components.
 * Supports both full syntax and shorthand variants.
 */
export const remarkBadge: Plugin<[], Root> = () => {
    return (tree) => {
        visit(tree, 'textDirective', (node, index, parent) => {
            if (!parent || index === undefined) return;

            const directive = node as unknown as TextDirectiveNode;
            const { name, attributes, children } = directive;

            const isShorthand = (SHORTHAND_VARIANTS as readonly string[]).includes(name);
            const isBadge = name === 'badge';

            if (!isBadge && !isShorthand) return;

            // Extract label from directive children text nodes
            const label = children
                .filter((c) => c.type === 'text')
                .map((c) => c.value ?? '')
                .join('');

            // attributes is a flat key-value object from remark-directive
            const variant = isBadge ? ((attributes?.variant ?? 'default') as BadgeVariant) : (name as BadgeVariant);

            const icon = attributes?.icon as BadgeIcon | undefined;

            (parent.children as unknown[])[index] = createBadgeNode(label, variant, icon);
        });
    };
};
