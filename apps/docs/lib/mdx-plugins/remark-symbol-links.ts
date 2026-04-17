/**
 * plugins/remark-symbol-links.ts
 *
 * Transforms inline code nodes whose value resolves to a known PSJ symbol
 * into <SymbolLink> MDX JSX elements.
 *
 * Also handles common PSJ qualified-access patterns in inline code:
 *   `BODY`                   → links to entity-types
 *   `ELEMKIND_2D`            → links to element-types
 *   `JPT.DItemType.BODY`     → links to entity-types (resolver strips prefix)
 *   `Elastic`                → links to material-property/Class_Elastic
 *   `BASIC`                  → links to parameter-types/Data-Type_JPT_BASIC
 *   `YOUNGS_MODULUS`         → links to material-types
 *
 * Plain-text linking is opt-in (linkPlainText: true) because PSJ docs
 * contain many identifiers in prose that should NOT all be auto-linked.
 */

import { Link } from 'mdast';
import { SKIP, visit } from 'unist-util-visit';

import type { SymbolEntry } from '../symbol-resolver';

import { resolveSymbol } from '../symbol-resolver';

import type { Root, RootContent } from 'mdast';
import type { Plugin } from 'unified';

// ── MDX JSX node shapes ───────────────────────────────────────────────────

interface MdxJsxAttribute {
    type: 'mdxJsxAttribute';
    name: string;
    value: string;
}

interface MdxJsxTextElement {
    type: 'mdxJsxTextElement';
    name: string;
    attributes: MdxJsxAttribute[];
    children: { type: 'text'; value: string }[];
    data: { _mdxExplicitJsx: true };
}

function makeSymbolNode(displayText: string, sym: SymbolEntry): MdxJsxTextElement {
    return {
        type: 'mdxJsxTextElement',
        name: 'SymbolLink',
        attributes: [
            { type: 'mdxJsxAttribute', name: 'name', value: sym.name },
            { type: 'mdxJsxAttribute', name: 'href', value: sym.href },
            {
                type: 'mdxJsxAttribute',
                name: 'description',
                value: sym.description,
            },
            { type: 'mdxJsxAttribute', name: 'category', value: sym.category },
        ],
        children: [{ type: 'text', value: displayText }],
        data: { _mdxExplicitJsx: true },
    };
}

// ── Contexts where we must never inject links ─────────────────────────────

const SKIP_PARENT_TYPES = new Set([
    'heading', // anchor-in-anchor = invalid HTML
    'link', // anchor-in-anchor = invalid HTML
    'code', // fenced code block
    'inlineCode', // already the source node type — guard for text pass
    'mdxJsxTextElement', // author-written <SymbolLink> — don't re-process
]);

// ── Plugin options ────────────────────────────────────────────────────────

export interface RemarkSymbolLinksOptions {
    /**
     * Also scan plain-text prose for symbol names.
     * Default: false — PSJ docs have many bare identifiers in explanatory
     * prose that should NOT all become links.
     */
    linkPlainText?: boolean;

    /**
     * Minimum token length for plain-text linking.
     * Prevents linking very short tokens like "A", "In", "To".
     * Default: 4
     */
    minTokenLength?: number;

    /**
     * Only link symbols from these categories.
     * When omitted, all categories are linked.
     * Useful to start with just parameter-types and classes,
     * then gradually enable enum categories.
     *
     * @example ["parameter-type", "class"]
     */
    allowCategories?: SymbolEntry['category'][];

    /** Custom per-token filter. Return false to skip. */
    filter?: (token: string, entry: SymbolEntry) => boolean;
}

// ── Plugin ────────────────────────────────────────────────────────────────

export const remarkSymbolLinks: Plugin<[RemarkSymbolLinksOptions?], Root> = (options = {}) => {
    const { linkPlainText = false, minTokenLength = 4, allowCategories, filter } = options;

    const categorySet = allowCategories ? new Set(allowCategories) : null;

    function shouldLink(token: string, entry: SymbolEntry): boolean {
        if (categorySet && !categorySet.has(entry.category)) return false;
        if (filter && !filter(token, entry)) return false;
        return true;
    }

    return (tree, file) => {
        const frontmatter = (file.data as any).frontmatter;
        const scope = frontmatter?.id;

        // ── Pass 1: inline code nodes `` `Elastic` `` ──────────────────────
        visit(tree, 'inlineCode', (node, index, parent) => {
            if (index === undefined || !parent) return;
            if (SKIP_PARENT_TYPES.has(parent.type as string)) return;

            const sym = resolveSymbol(node.value, scope);
            if (!sym) return;
            if (!shouldLink(node.value, sym)) return;

            parent.children.splice(index, 1, makeSymbolNode(node.value, sym) as unknown as Link);
            return SKIP;
        });

        // ── Pass 2: plain text nodes (opt-in) ──────────────────────────────
        if (!linkPlainText) return;

        visit(tree, 'text', (node, index, parent) => {
            if (index === undefined || !parent) return;
            if (SKIP_PARENT_TYPES.has(parent.type as string)) return;

            // Tokenise on \b word boundaries, preserving delimiters so
            // the rebuilt text is byte-identical when no symbols match.
            const parts = node.value.split(/\b/);
            let modified = false;
            const newNodes: RootContent[] = [];

            for (const part of parts) {
                // Skip tokens that are too short
                if (part.length < minTokenLength) {
                    pushText(newNodes, part);
                    continue;
                }

                const sym = resolveSymbol(part, scope);

                if (sym && shouldLink(part, sym)) {
                    newNodes.push(makeSymbolNode(part, sym) as unknown as Link);
                    modified = true;
                } else {
                    pushText(newNodes, part);
                }
            }

            if (!modified) return;

            parent.children.splice(index, 1, ...newNodes);
            return SKIP;
        });
    };
};

// Merge adjacent text nodes to keep the AST clean
function pushText(nodes: RootContent[], value: string): void {
    const last = nodes.at(-1);
    if (last?.type === 'text') {
        last.value += value;
    } else {
        nodes.push({ type: 'text', value });
    }
}
