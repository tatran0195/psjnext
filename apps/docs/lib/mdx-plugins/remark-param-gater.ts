import { valueToEstree } from 'estree-util-value-to-estree';

import { API_VERSIONS } from '@/lib/api-versions';
import { flattenNode, getVersionStatus } from './utils';

import type { Content, Heading, Root, RootContent } from 'mdast';
import type { MdxjsEsm } from 'mdast-util-mdx';
import type { Plugin, Transformer } from 'unified';

// ─── Public API ──────────────────────────────────────────────────────────────

export interface VersionFilterOptions {
    /** Minimum heading depth that starts a param section. Default: 3. */
    minHeadingDepth?: number;
    /**
     * Export `paramMeta` alongside `versionedStructuredData`.
     * @defaultValue true
     */
    exportParamMeta?: boolean;
}

export interface ParamMetaExport {
    name: string;
    since?: string;
    deprecated?: string;
    removed?: string;
}

// ─── Internal types ───────────────────────────────────────────────────────────

type ParamKind = 'param' | 'input';

interface ParamMeta {
    kind: ParamKind;
    since?: string;
    deprecated?: string;
    removed?: string;
    type?: string;
    required?: boolean;
}

/**
 * A parsed param block: the annotation metadata + the flat heading text that
 * remarkStructure would have produced for this heading node.
 */
interface ParsedParamBlock {
    meta: ParamMeta;
    /** Normalised heading id (hProperties.id), e.g. "bismergepart" */
    headingId: string;
    /** Display text of the heading, e.g. "`bIsMergePart`" */
    headingContent: string;
    /** Body paragraphs belonging to this param */
    bodyContents: string[];
    /** The full block of AST nodes (heading + body) to splice into the tree */
    astNodes: Content[];
}

// ─── Defaults ────────────────────────────────────────────────────────────────

const DEFAULTS = {
    minHeadingDepth: 3,
    exportParamMeta: true,
} satisfies Partial<VersionFilterOptions>;

// ─── Helpers ─────────────────────────────────────────────────────────────────

function isHeading(node: Content): node is Heading {
    return node.type === 'heading';
}

function extractAnnotation(value: string, key: string, isVersionUrl = true): string | undefined {
    const pattern = isVersionUrl ? '([\\d.]+)' : '([^\\s;>]+)';
    const regex = new RegExp(`@${key}[:\\s]+${pattern}`, 'i');
    const match = value.match(regex);
    if (!match) return undefined;
    return match[1].replace(/[->;]+$/, '').trim();
}

function parseParamMeta(value: string): ParamMeta | null {
    if (typeof value !== 'string' || !value.includes('@')) return null;

    const hasVersionAnnotation =
        /@since/i.test(value) ||
        /@removed/i.test(value) ||
        /@deprecated/i.test(value) ||
        /@type/i.test(value) ||
        /@required/i.test(value) ||
        /@inputs?/i.test(value);

    if (!hasVersionAnnotation) return null;

    const kind: ParamKind = /@inputs?/i.test(value) ? 'input' : 'param';

    return {
        kind,
        since: extractAnnotation(value, 'since'),
        deprecated: extractAnnotation(value, 'deprecated'),
        removed: extractAnnotation(value, 'removed'),
        type: extractAnnotation(value, 'type', false),
        required: /@required/i.test(value),
    };
}

function isParamVisible(meta: ParamMeta, version: string): boolean {
    const status = getVersionStatus(version, meta.since, meta.deprecated, meta.removed);
    return status !== 'removed' && status !== 'unavailable';
}

function skipBlankNodes(nodes: Content[], start: number): number {
    let j = start;
    while (j < nodes.length) {
        const n = nodes[j];
        const val = (n as { value?: string }).value ?? '';
        const isBlankHtml = n.type === 'html' && val.trim() === '';
        const isEmptyText = n.type === 'text' && val.trim() === '';
        if (!isBlankHtml && !isEmptyText) break;
        j++;
    }
    return j;
}

/**
 * Stringify the plain-text content of a non-heading, non-code block node.
 * We only need the text that remarkStructure would have captured.
 */
function extractNodeText(node: Content): string {
    return flattenNode(node as unknown as RootContent).trim();
}

// ─── ESM export builders ──────────────────────────────────────────────────────

function buildEsmExport(name: string, value: unknown): MdxjsEsm {
    return {
        type: 'mdxjsEsm',
        value: '',
        data: {
            estree: {
                type: 'Program',
                sourceType: 'module',
                body: [
                    {
                        type: 'ExportNamedDeclaration',
                        attributes: [],
                        specifiers: [],
                        declaration: {
                            type: 'VariableDeclaration',
                            kind: 'let',
                            declarations: [
                                {
                                    type: 'VariableDeclarator',
                                    id: { type: 'Identifier', name },
                                    init: valueToEstree(value),
                                },
                            ],
                        },
                    },
                ],
            },
        },
    } as MdxjsEsm;
}

// ─── PSJParamSection wrapper ──────────────────────────────────────────────────

function wrapInParamSection(block: Content[], meta: ParamMeta): Content {
    const attributes = [
        meta.kind === 'input' && { type: 'mdxJsxAttribute', name: 'kind', value: 'input' },
        meta.since && { type: 'mdxJsxAttribute', name: 'since', value: meta.since },
        meta.removed && { type: 'mdxJsxAttribute', name: 'removed', value: meta.removed },
        meta.deprecated && { type: 'mdxJsxAttribute', name: 'deprecated', value: meta.deprecated },
        meta.type && { type: 'mdxJsxAttribute', name: 'type', value: meta.type },
        meta.required && { type: 'mdxJsxAttribute', name: 'required', value: 'true' },
    ].filter(Boolean);

    return {
        type: 'mdxJsxFlowElement',
        name: 'PSJParamSection',
        attributes,
        children: block,
    } as unknown as Content;
}

interface StructuredDataHeading {
  id: string;
  content: string;
}

interface StructuredDataContent {
  heading: string | undefined;
  content: string;
}

interface StructuredData {
  headings: StructuredDataHeading[];
  contents: StructuredDataContent[];
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

/**
 * `remarkParamGater`
 *
 * In addition to the original rendering behaviour (wrapping visible param
 * blocks in `<PSJParamSection>`), this version also emits a compile-time
 * `versionedStructuredData` export — a `Record<version, StructuredData>` map
 * covering every entry in `API_VERSIONS`.
 *
 * Because `API_VERSIONS` is a static constant known at build time, we can
 * iterate every version once per source file and compute exactly which
 * headings and content blocks are visible for each version.  The map is baked
 * into the compiled MDX module so `buildIndex` pays zero runtime cost:
 *
 * ```ts
 * // search/route.ts
 * const structuredData = page.data.versionedStructuredData?.[version]
 *                     ?? page.data.structuredData;          // non-versioned fallback
 * ```
 *
 * ## Execution order (unchanged)
 *
 * Must run AFTER `remarkHeading` (heading ids must exist) and BEFORE
 * `remarkStructure` (so removed headings are absent from the AST that
 * remarkStructure walks for the default `structuredData` export).
 *
 * The plugin filters the live AST for the *latest* version in API_VERSIONS
 * (preserving the existing render-time behaviour) while computing the full
 * version map purely from the collected metadata — no second AST walk needed.
 */
export const remarkParamGater: Plugin<[VersionFilterOptions?], Root> = (options) => {
    const opts = { ...DEFAULTS, ...options };

    const transformer: Transformer<Root> = (tree) => {
        const nodes = tree.children;

        // ── Pass 1: collect all param blocks ─────────────────────────────────
        //
        // Walk the AST once.  For each annotation comment + following heading,
        // record:
        //   a) the full ParsedParamBlock (for versionedStructuredData)
        //   b) the AST splice info (for rendering)
        //
        // Non-param nodes are collected as-is into `nonParamRanges`.

        interface AstSlot {
            kind: 'passthrough';
            node: Content;
        }
        interface ParamSlot {
            kind: 'param';
            block: ParsedParamBlock;
        }
        type Slot = AstSlot | ParamSlot;

        const slots: Slot[] = [];
        // Structural (non-param) headings and their body content — shared across
        // all versions since they are never gated.
        const sharedHeadings: StructuredDataHeading[] = [];
        const sharedContents: StructuredDataContent[] = [];

        let i = 0;
        while (i < nodes.length) {
            const node = nodes[i];
            const rawValue = (node as { value?: string }).value ?? '';
            const meta = parseParamMeta(rawValue);

            if (meta) {
                const headingIdx = skipBlankNodes(nodes, i + 1);
                const headingNode = nodes[headingIdx];

                if (
                    headingNode &&
                    isHeading(headingNode) &&
                    headingNode.depth >= opts.minHeadingDepth
                ) {
                    const depth = headingNode.depth;

                    // Collect block nodes (heading + body until next same/shallower heading or annotation)
                    const block: Content[] = [headingNode];
                    let k = headingIdx + 1;
                    while (k < nodes.length) {
                        const n = nodes[k];
                        if (isHeading(n) && n.depth <= depth) break;
                        if (parseParamMeta((n as { value?: string }).value ?? '')) break;
                        block.push(n);
                        k++;
                    }

                    // Extract heading id (set by remarkHeading)
                    const hProps = (headingNode.data as { hProperties?: { id?: string } })
                        ?.hProperties;
                    const headingId = hProps?.id ?? '';

                    // Plain-text heading content (same logic as remarkStructure's stringify)
                    const headingContent = flattenNode(headingNode as unknown as RootContent).trim();

                    // Body content lines (paragraphs, blockquotes — skip code blocks)
                    const bodyContents: string[] = [];
                    for (const n of block.slice(1)) {
                        if (n.type === 'code' || n.type === 'mdxJsxFlowElement') continue;
                        const text = extractNodeText(n);
                        if (text.length > 0) bodyContents.push(text);
                    }

                    slots.push({
                        kind: 'param',
                        block: { meta, headingId, headingContent, bodyContents, astNodes: block },
                    });

                    i = k;
                    continue;
                }
            }

            // Non-param node: capture structural headings for shared data
            if (node.type === 'heading') {
                const hProps = (node.data as { hProperties?: { id?: string } })?.hProperties;
                const id = hProps?.id ?? '';
                const content = flattenNode(node as unknown as RootContent).trim();
                if (id && content) {
                    sharedHeadings.push({ id, content });
                }
            } else {
                const text = extractNodeText(node);
                if (text.length > 0) {
                    // Associate with last shared heading (mirrors remarkStructure behaviour)
                    const lastHeading = sharedHeadings[sharedHeadings.length - 1]?.id;
                    sharedContents.push({ heading: lastHeading, content: text });
                }
            }

            slots.push({ kind: 'passthrough', node });
            i++;
        }

        // ── Pass 2: build versionedStructuredData ────────────────────────────
        //
        // For each version in API_VERSIONS, filter param slots and assemble a
        // StructuredData object.  O(|API_VERSIONS| × |paramSlots|) — negligible.

        const paramSlots = slots.filter((s): s is ParamSlot => s.kind === 'param');

        const versionedStructuredData: Record<string, StructuredData> = {};

        for (const version of API_VERSIONS) {
            const headings: StructuredDataHeading[] = [...sharedHeadings];
            const contents: StructuredDataContent[] = [...sharedContents];

            for (const slot of paramSlots) {
                if (!isParamVisible(slot.block.meta, version)) continue;

                if (slot.block.headingId && slot.block.headingContent) {
                    headings.push({
                        id: slot.block.headingId,
                        content: slot.block.headingContent,
                    });
                }

                for (const text of slot.block.bodyContents) {
                    contents.push({
                        heading: slot.block.headingId || undefined,
                        content: text,
                    });
                }
            }

            versionedStructuredData[version] = { headings, contents };
        }

        // ── Pass 3: rewrite AST for rendering ────────────────────────────────
        //
        // The rendered page is version-agnostic at compile time (version plugin
        // stamps _version at runtime).  Preserve all param blocks so every
        // versioned page route can render the correct subset at request time via
        // the existing PSJParamSection / CSS visibility approach.
        //
        // This preserves the original behaviour: no AST nodes are dropped here.

        const out: Content[] = [];
        for (const slot of slots) {
            if (slot.kind === 'passthrough') {
                out.push(slot.node);
            } else {
                out.push(wrapInParamSection(slot.block.astNodes, slot.block.meta));
            }
        }
        tree.children = out;

        // ── Inject exports ────────────────────────────────────────────────────

        const exports: MdxjsEsm[] = [];

        exports.push(
            buildEsmExport('versionedStructuredData', versionedStructuredData) as MdxjsEsm,
        );

        if (opts.exportParamMeta) {
            const paramMeta: ParamMetaExport[] = paramSlots.map((s) => ({
                name: s.block.headingContent.replace(/`/g, '').trim(),
                ...(s.block.meta.since && { since: s.block.meta.since }),
                ...(s.block.meta.deprecated && { deprecated: s.block.meta.deprecated }),
                ...(s.block.meta.removed && { removed: s.block.meta.removed }),
            }));
            exports.push(buildEsmExport('paramMeta', paramMeta) as MdxjsEsm);
        }

        // Prepend all exports at top of module (same convention as remarkStructure)
        for (const node of exports.reverse()) {
            tree.children.unshift(node as unknown as Content);
        }
    };

    return transformer;
};