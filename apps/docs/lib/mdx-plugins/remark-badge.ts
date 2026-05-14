import { visit } from 'unist-util-visit';

// lib/remark-badge.ts
import type { Root } from 'mdast';
import type { Plugin } from 'unified';

export type BadgeVariant = 'feature' | 'fix' | 'api' | 'utility' | 'macro' | 'data' | 'highlight' | 'default';

const SHORTHAND_VARIANTS = [
    'feature',
    'fix',
    'api',
    'utility',
    'macro',
    'data',
    'highlight',
] as const satisfies ReadonlyArray<BadgeVariant>;

const SHORTHAND_PATTERN = SHORTHAND_VARIANTS.join('|');

/**
 * Matches:
 *   ::badge[Label](variant=feature)   — full syntax with variant
 *   ::badge[Label]                    — full syntax, default variant
 *   ::feature[Label]                  — shorthand
 */
const BADGE_REGEX = new RegExp(
    `::(?:badge\\[([^\\]]+)\\](?:\\(variant=(${SHORTHAND_PATTERN}|default)\\))?|(${SHORTHAND_PATTERN})\\[([^\\]]+)\\])`,
    'g',
);

// -----------------------------------------------------------------
// AST node types
// -----------------------------------------------------------------
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

function createBadgeNode(label: string, variant: BadgeVariant = 'default'): MdxJsxTextElement {
    return {
        type: 'mdxJsxTextElement',
        name: 'Badge',
        attributes: [
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
        ],
        children: [],
        data: { _mdxExplicitJsx: true },
    };
}

/**
 * Remark plugin to convert badge directives to Badge components.
 */
export const remarkBadge: Plugin<[], Root> = () => {
    return (tree) => {
        visit(tree, (node, index, parent) => {
            if (!parent || index === undefined) return;
            const n = node as unknown as {
                type: string;
                name?: string;
                children?: Array<{ type: string; value?: string }>;
                attributes?: Record<string, string>;
            };
            if (n.type === 'leafDirective' || n.type === 'textDirective') {
                const { name, children, attributes } = n;
                if (
                    name === 'badge' ||
                    (typeof name === 'string' && (SHORTHAND_VARIANTS as readonly string[]).includes(name))
                ) {
                    let text = '';
                    if (children && children[0] && children[0].type === 'text' && children[0].value) {
                        text = children[0].value;
                    }
                    const variant = name === 'badge' ? (attributes?.variant ?? 'default') : name;
                    (parent.children as unknown[])[index] = createBadgeNode(text, variant as BadgeVariant);
                }
            }
        });

        visit(tree, 'paragraph', (paragraph) => {
            const children = paragraph.children as unknown as Array<{
                type: string;
                value?: string;
                url?: string;
                children?: Array<{ type: string; value?: string }>;
            }>;
            let i = 0;
            while (i < children.length) {
                const node = children[i];

                if (node.type === 'text') {
                    const value = node.value as string;

                    if (value.endsWith('::badge')) {
                        const nextNode = children[i + 1];
                        if (nextNode && nextNode.type === 'link') {
                            const url = nextNode.url as string;
                            if (url.startsWith('variant=') || url === 'default') {
                                const variant = url.replace('variant=', '');
                                let label = '';
                                if (nextNode.children && nextNode.children[0] && nextNode.children[0].type === 'text') {
                                    label = nextNode.children[0].value ?? '';
                                }

                                if (value === '::badge') {
                                    children.splice(
                                        i,
                                        2,
                                        createBadgeNode(
                                            label,
                                            variant as BadgeVariant,
                                        ) as unknown as (typeof children)[0],
                                    );
                                } else {
                                    // Slicing out `::badge` from the text
                                    node.value = value.slice(0, -7);
                                    children.splice(
                                        i + 1,
                                        1,
                                        createBadgeNode(
                                            label,
                                            variant as BadgeVariant,
                                        ) as unknown as (typeof children)[0],
                                    );
                                }
                                i++; // Move past the new badge node
                                continue;
                            }
                        }
                    }

                    // For all other cases, try our regex
                    // Reset lastIndex
                    BADGE_REGEX.lastIndex = 0;
                    if (BADGE_REGEX.test(value)) {
                        BADGE_REGEX.lastIndex = 0;
                        const newNodes = [];
                        let lastIndex = 0;
                        let match: RegExpExecArray | null;

                        while ((match = BADGE_REGEX.exec(value)) !== null) {
                            const [fullMatch, badgeLabel, badgeVariant, shorthandVariant, shorthandLabel] = match;
                            const matchStart = match.index;

                            if (matchStart > lastIndex) {
                                newNodes.push({ type: 'text', value: value.slice(lastIndex, matchStart) });
                            }

                            const label = badgeLabel ?? shorthandLabel ?? '';
                            const variant = (badgeVariant ?? shorthandVariant ?? 'default') as BadgeVariant;

                            newNodes.push(createBadgeNode(label, variant));
                            lastIndex = matchStart + fullMatch.length;
                        }

                        if (lastIndex < value.length) {
                            newNodes.push({ type: 'text', value: value.slice(lastIndex) });
                        }

                        children.splice(i, 1, ...(newNodes as unknown as typeof children));
                        i += newNodes.length; // skip the newly inserted nodes
                        continue;
                    }
                }

                i++;
            }
        });
    };
};
