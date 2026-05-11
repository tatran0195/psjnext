import { fromMarkdown } from 'mdast-util-from-markdown';
import { visit } from 'unist-util-visit';

import type { BlockContent, DefinitionContent, Html, Root } from 'mdast';
import type { MdxJsxAttribute, MdxJsxFlowElement } from 'mdast-util-mdx';
import type { Transformer } from 'unified';
import type { Node, Parent } from 'unist';

export interface RemarkDetailsAccordionOptions {
    accordionsTag?: string;
    accordionTag?: string;
    defaultType?: string;
}

export function remarkDetailsAccordion({
    accordionsTag = 'Accordions',
    accordionTag = 'Accordion',
    defaultType = 'single',
}: RemarkDetailsAccordionOptions = {}): Transformer<Root, Root> {
    return (tree) => {
        // ── Strategy 1: no blank lines → mdxJsxFlowElement ──
        visit(tree, 'mdxJsxFlowElement', (node) => {
            if ((node as MdxJsxFlowElement).name !== 'details') return;

            let title = '';
            const contentChildren: (BlockContent | DefinitionContent)[] = [];

            for (const child of (node as MdxJsxFlowElement).children) {
                if (child.type === 'mdxJsxFlowElement' && (child as MdxJsxFlowElement).name === 'summary') {
                    title = extractTextFromNode(child as Node);
                } else {
                    contentChildren.push(child as BlockContent | DefinitionContent);
                }
            }

            Object.assign(node, buildAccordionsNode(title, contentChildren, accordionsTag, accordionTag, defaultType));
        });

        // ── Strategy 2: blank lines → scattered html nodes ──
        processChildren(tree, accordionsTag, accordionTag, defaultType);
    };
}

// ─────────────────────
// Raw HTML transformer
// ─────────────────────

function processChildren(parent: Parent, accordionsTag: string, accordionTag: string, defaultType: string): void {
    const children = parent.children as Node[];
    let i = 0;

    while (i < children.length) {
        const node = children[i];

        // Recurse into non-html block containers
        if (node.type !== 'html' && 'children' in node) {
            processChildren(node as Parent, accordionsTag, accordionTag, defaultType);
            i++;
            continue;
        }

        if (node.type !== 'html') {
            i++;
            continue;
        }

        const htmlNode = node as Html;

        if (!isDetailsOpen(htmlNode.value)) {
            i++;
            continue;
        }

        const openIndex = i;
        let closeIndex = -1;
        let summaryTitle = '';
        const bodyNodes: (BlockContent | DefinitionContent)[] = [];

        for (let j = openIndex + 1; j < children.length; j++) {
            const sibling = children[j] as Node;

            if (sibling.type === 'html') {
                const sibHtml = sibling as Html;

                if (isDetailsClose(sibHtml.value)) {
                    closeIndex = j;
                    break;
                }

                if (isSummaryNode(sibHtml.value)) {
                    summaryTitle = extractSummaryTitle(sibHtml.value);

                    // ── KEY FIX: re-parse trailing markdown content ──
                    const trailing = extractContentAfterSummary(sibHtml.value);
                    if (trailing) {
                        const parsed = parseMarkdown(trailing);
                        bodyNodes.push(...parsed);
                    }
                    continue;
                }
            }

            bodyNodes.push(sibling as BlockContent | DefinitionContent);
        }

        if (closeIndex === -1) {
            i++;
            continue;
        }

        const accordionsNode = buildAccordionsNode(summaryTitle, bodyNodes, accordionsTag, accordionTag, defaultType);

        children.splice(openIndex, closeIndex - openIndex + 1, accordionsNode as Node);
        i++;
    }
}

// ─────────────────────
// Markdown re-parser
// ─────────────────────

/**
 * Re-parse a raw markdown string into mdast BlockContent nodes.
 * Used to recover markdown content that was trapped inside an html node.
 *
 * e.g. "  - `foo`: bar\n  - `baz`: qux"
 *   → [list node with two items]
 */
function parseMarkdown(markdown: string): (BlockContent | DefinitionContent)[] {
    if (!markdown.trim()) return [];

    const ast = fromMarkdown(markdown);
    return ast.children as (BlockContent | DefinitionContent)[];
}

// ─────────────────────
// HTML matchers
// ─────────────────────

function isDetailsOpen(value: string): boolean {
    return /^\s*<details(\s[^>]*)?\s*>\s*$/.test(value.trim());
}

function isDetailsClose(value: string): boolean {
    return /^\s*<\/details>\s*$/.test(value.trim());
}

function isSummaryNode(value: string): boolean {
    return /<summary[\s\S]*?>[\s\S]*?<\/summary>/.test(value);
}

function extractSummaryTitle(value: string): string {
    const match = value.match(/<summary[^>]*>([\s\S]*?)<\/summary>/);
    if (!match) return '';

    return match[1]
        .replace(/<[^>]+>/g, '')
        .replace(/&amp;/g, '&')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&quot;/g, '"')
        .trim();
}

/**
 * Extract raw markdown string that appears after </summary> in the same html node.
 *
 * Input:  `<summary id="x">Title</summary>\n  - item1\n  - item2`
 * Output: `  - item1\n  - item2`
 */
function extractContentAfterSummary(value: string): string {
    const match = value.match(/<\/summary>([\s\S]*)$/);
    if (!match) return '';
    return match[1].trim();
}

// ─────────────────────
// Shared node builder
// ─────────────────────

function buildAccordionsNode(
    title: string,
    children: (BlockContent | DefinitionContent)[],
    accordionsTag: string,
    accordionTag: string,
    defaultType: string,
): MdxJsxFlowElement {
    const accordionNode: MdxJsxFlowElement = {
        type: 'mdxJsxFlowElement',
        name: accordionTag,
        attributes: [
            {
                type: 'mdxJsxAttribute',
                name: 'title',
                value: title,
            } satisfies MdxJsxAttribute,
        ],
        children,
    };

    return {
        type: 'mdxJsxFlowElement',
        name: accordionsTag,
        attributes: [
            {
                type: 'mdxJsxAttribute',
                name: 'type',
                value: defaultType,
            } satisfies MdxJsxAttribute,
        ],
        children: [accordionNode],
    };
}

// ─────────────────────
// Generic text extractor (mdxJsxFlowElement path)
// ─────────────────────

function extractTextFromNode(node: Node): string {
    if ('value' in node && typeof (node as { value: unknown }).value === 'string') {
        return (node as { value: string }).value;
    }
    if ('children' in node && Array.isArray((node as { children: unknown }).children)) {
        return (node as { children: Node[] }).children.map(extractTextFromNode).join('').trim();
    }
    return '';
}
