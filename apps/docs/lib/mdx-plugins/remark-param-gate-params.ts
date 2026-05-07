import { valueToEstree } from 'estree-util-value-to-estree';

import { API_VERSIONS, semverGte } from '@/lib/api-versions';

import { flattenNode, getVersionStatus } from './utils';

import type { Heading, Root, RootContent } from 'mdast';
import type { MdxjsEsm } from 'mdast-util-mdx';
import type { Plugin, Transformer } from 'unified';

// ─── Public API ───────────────────────────────────────────────────────────────

export interface VersionGateOptions {
    /** Minimum heading depth that starts a param section. Default: 3. */
    minHeadingDepth?: number;
    /** Export `paramMeta` alongside `versionedStructuredData`. Default: true. */
    exportParamMeta?: boolean;
}

export interface VersionRange {
    since?: string;
    deprecated?: string;
    removed?: string;
    required?: boolean;
}

export interface ParamMetaExport {
    name: string;
    ranges: VersionRange[];
}

// ─── Internal types ───────────────────────────────────────────────────────────

interface ParamMeta {
    ranges: VersionRange[];
    type?: string;
}

interface ParsedParamBlock {
    meta: ParamMeta;
    headingId: string;
    headingContent: string;
    bodyContents: string[];
    astNodes: RootContent[];
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

// ─── Constants ────────────────────────────────────────────────────────────────

const DEFAULTS = {
    minHeadingDepth: 3,
    exportParamMeta: true,
} satisfies Required<VersionGateOptions>;

const ANNOTATION_RE = /@(?:since|removed|deprecated|type|required|optional|inputs?)/i;

// ─── Helpers ──────────────────────────────────────────────────────────────────

function isHeading(node: RootContent): node is Heading {
    return node.type === 'heading';
}

function isBlankNode(node: RootContent): boolean {
    const v = (node as { value?: string }).value ?? '';
    return (node.type === 'html' || node.type === 'text') && v.trim() === '';
}

function isAnnotationComment(node: RootContent): boolean {
    return node.type === 'html' && ANNOTATION_RE.test((node as { value?: string }).value ?? '');
}

function extractAnnotation(value: string, key: string, isVersion = true): string | undefined {
    const pattern = isVersion ? '([\\d.]+)' : '([^\\s;>]+)';
    const match = value.match(new RegExp(`@${key}[:\\s]+${pattern}`, 'i'));
    return match?.[1].replace(/[->;]+$/, '').trim();
}

function parseRange(value: string): VersionRange {
    const range: VersionRange = {
        since: extractAnnotation(value, 'since'),
        deprecated: extractAnnotation(value, 'deprecated'),
        removed: extractAnnotation(value, 'removed'),
        required: /@required/i.test(value) ? true : undefined,
    };
    // strip undefined keys for a clean serialisation
    for (const k of Object.keys(range) as (keyof VersionRange)[]) {
        if (range[k] === undefined) delete range[k];
    }
    return range;
}

function isVisibleAt(meta: ParamMeta, version: string): boolean {
    for (const r of meta.ranges) {
        const status = getVersionStatus(version, r.since, r.deprecated, r.removed);
        if (status === 'removed') return false;
    }
    for (const r of meta.ranges) {
        const status = getVersionStatus(version, r.since, r.deprecated, r.removed);
        if (status !== 'unavailable') return true;
    }
    return false;
}

// ─── AST scanner ─────────────────────────────────────────────────────────────

/**
 * Consume a run of annotation comments (skipping blank nodes between them)
 * starting at `start`. Returns null if the run isn't followed by a heading.
 */
function consumeAnnotationRun(
    nodes: RootContent[],
    start: number,
    minDepth: number,
): { meta: ParamMeta; headingIdx: number; headingNode: Heading } | null {
    const ranges: VersionRange[] = [];
    let type: string | undefined;
    let i = start;

    while (i < nodes.length) {
        if (isAnnotationComment(nodes[i])) {
            const value = (nodes[i] as { value: string }).value;
            ranges.push(parseRange(value));
            type ??= extractAnnotation(value, 'type', false);
            i++;
        } else if (isBlankNode(nodes[i]) && ranges.length > 0) {
            i++;
        } else {
            break;
        }
    }

    if (ranges.length === 0) return null;

    // skip trailing blanks before heading
    while (i < nodes.length && isBlankNode(nodes[i])) i++;

    const heading = nodes[i];
    if (!heading || !isHeading(heading) || heading.depth < minDepth) return null;

    return { meta: { ranges, ...(type && { type }) }, headingIdx: i, headingNode: heading };
}

// ─── ESM builder ─────────────────────────────────────────────────────────────

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

// Add to internal types
export interface ResolvedParam {
    visible: boolean;
    since?: string;
    deprecated?: string;
    required?: boolean;
    type?: string;
}

// Replace resolveActiveRange (was only in the React component before)
function resolveActiveRange(ranges: VersionRange[], version: string): VersionRange | undefined {
    let active: VersionRange | undefined;
    for (const r of ranges) {
        if (!r.since || semverGte(version, r.since)) active = r;
    }
    return active;
}

// Replace wrapInParamSection
function wrapInParamSection(block: RootContent[], meta: ParamMeta): RootContent {
    const versionMap: Record<string, ResolvedParam> = Object.fromEntries(
        API_VERSIONS.map((version) => {
            if (!isVisibleAt(meta, version)) {
                return [version, { visible: false }];
            }
            const active = resolveActiveRange(meta.ranges, version);
            return [
                version,
                {
                    visible: true,
                    ...(active?.since && { since: active.since }),
                    ...(active?.deprecated && { deprecated: active.deprecated }),
                    ...(active?.required && { required: true }),
                    ...(meta.type && { type: meta.type }),
                } satisfies ResolvedParam,
            ];
        }),
    );

    return {
        type: 'mdxJsxFlowElement',
        name: 'PSJParamSection',
        attributes: [
            {
                type: 'mdxJsxAttribute',
                name: 'versionMap',
                value: JSON.stringify(versionMap),
            },
        ],
        children: block,
    } as unknown as RootContent;
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

export const remarkVersionGateParams: Plugin<[VersionGateOptions?], Root> = (options) => {
    const { minHeadingDepth, exportParamMeta } = { ...DEFAULTS, ...options };

    const transformer: Transformer<Root> = (tree) => {
        const nodes = tree.children;

        type PassthroughSlot = { kind: 'passthrough'; node: RootContent };
        type ParamSlot = { kind: 'param'; block: ParsedParamBlock };
        type Slot = PassthroughSlot | ParamSlot;

        const slots: Slot[] = [];
        const sharedHeadings: StructuredDataHeading[] = [];
        const sharedContents: StructuredDataContent[] = [];

        // ── Pass 1: classify nodes into param blocks vs passthrough ──────────

        let i = 0;
        while (i < nodes.length) {
            const node = nodes[i];

            if (isAnnotationComment(node)) {
                const run = consumeAnnotationRun(nodes, i, minHeadingDepth);

                if (run) {
                    const { meta, headingIdx, headingNode } = run;
                    const depth = headingNode.depth;

                    const block: RootContent[] = [headingNode];
                    let k = headingIdx + 1;
                    while (k < nodes.length) {
                        const n = nodes[k];
                        if (isHeading(n) && n.depth <= depth) break;
                        if (isAnnotationComment(n)) break;
                        block.push(n);
                        k++;
                    }

                    const hId =
                        (headingNode.data as { hProperties?: { id?: string } })?.hProperties?.id ??
                        '';
                    const hContent = flattenNode(headingNode as unknown as RootContent).trim();

                    const bodyContents: string[] = block
                        .slice(1)
                        .filter((n) => n.type !== 'code' && n.type !== 'mdxJsxFlowElement')
                        .map((n) => flattenNode(n as unknown as RootContent).trim())
                        .filter(Boolean);

                    slots.push({
                        kind: 'param',
                        block: {
                            meta,
                            headingId: hId,
                            headingContent: hContent,
                            bodyContents,
                            astNodes: block,
                        },
                    });
                    i = k;
                    continue;
                }
            }

            // passthrough: track shared structural headings/content for structured data
            if (node.type === 'heading') {
                const id = (node.data as { hProperties?: { id?: string } })?.hProperties?.id ?? '';
                const content = flattenNode(node as unknown as RootContent).trim();
                if (id && content) sharedHeadings.push({ id, content });
            } else {
                const text = flattenNode(node as unknown as RootContent).trim();
                if (text)
                    sharedContents.push({ heading: sharedHeadings.at(-1)?.id, content: text });
            }

            slots.push({ kind: 'passthrough', node });
            i++;
        }

        // ── Pass 2: build versionedStructuredData ────────────────────────────

        const paramSlots = slots.filter((s): s is ParamSlot => s.kind === 'param');

        const versionedStructuredData = Object.fromEntries(
            API_VERSIONS.map((version) => {
                const headings = [...sharedHeadings];
                const contents = [...sharedContents];

                for (const { block } of paramSlots) {
                    if (!isVisibleAt(block.meta, version)) continue;
                    if (block.headingId && block.headingContent) {
                        headings.push({ id: block.headingId, content: block.headingContent });
                    }
                    for (const text of block.bodyContents) {
                        contents.push({ heading: block.headingId || undefined, content: text });
                    }
                }

                return [version, { headings, contents } satisfies StructuredData];
            }),
        );

        // ── Pass 3: rewrite AST ───────────────────────────────────────────────

        tree.children = slots.map((s) =>
            s.kind === 'passthrough' ? s.node : wrapInParamSection(s.block.astNodes, s.block.meta),
        );

        // ── Inject exports ────────────────────────────────────────────────────

        const esm: MdxjsEsm[] = [
            buildEsmExport('versionedStructuredData', versionedStructuredData),
            ...(exportParamMeta
                ? [
                      buildEsmExport(
                          'paramMeta',
                          paramSlots.map(
                              ({ block }) =>
                                  ({
                                      name: block.headingContent.replace(/`/g, '').trim(),
                                      ranges: block.meta.ranges,
                                  }) satisfies ParamMetaExport,
                          ),
                      ),
                  ]
                : []),
        ];

        for (const node of esm.reverse()) {
            tree.children.unshift(node as unknown as RootContent);
        }
    };

    return transformer;
};
