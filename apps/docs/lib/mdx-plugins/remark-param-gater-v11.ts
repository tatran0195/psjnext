import { flattenNode, getVersionStatus } from './utils';

import type { Content, Heading, Root, RootContent } from 'mdast';
import type { Plugin, Transformer } from 'unified';

// ─── Public API ──────────────────────────────────────────────────────────────

export interface VersionFilterOptions {
    /** Active API version, e.g. "5.2.0".  Falls back to file path / file.data._version if omitted. */
    version?: string;
    /** Minimum heading depth that starts a param section.  Default: 3. */
    minHeadingDepth?: number;
}

export interface ParamMetaExport {
    name: string;
    since?: string;
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

// ─── Defaults ────────────────────────────────────────────────────────────────

const DEFAULTS = {
    minHeadingDepth: 3,
} satisfies Partial<VersionFilterOptions>;

// ─── Helpers ─────────────────────────────────────────────────────────────────

function isHeading(node: Content): node is Heading {
    return node.type === 'heading';
}

/**
 * Extract a version annotation like `@since:5.1.0` or `@removed:5.3.0` from
 * a raw comment / html string.  Trailing punctuation (hyphens, > characters)
 * is stripped to handle patterns like `@since:5.1.0-->`.
 */
function extractAnnotation(value: string, key: string, isVersionUrl = true): string | undefined {
    const pattern = isVersionUrl ? '([\\d.]+)' : '([^\\s;>]+)';
    const regex = new RegExp(`@${key}[:\\s]+${pattern}`, 'i');
    const match = value.match(regex);
    if (!match) return undefined;
    return match[1].replace(/[->;]+$/, '').trim();
}

/**
 * Detect the `kind` of the annotation block:
 * - `@input` / `@inputs`  → 'input'
 * - anything else with `@`  → 'param'
 * Returns `null` when the value does not look like a meta comment at all.
 */
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

    const meta: ParamMeta = {
        kind,
        since: extractAnnotation(value, 'since'),
        deprecated: extractAnnotation(value, 'deprecated'),
        removed: extractAnnotation(value, 'removed'),
        type: extractAnnotation(value, 'type', false),
        required: /@required/i.test(value),
    };

    return meta;
}

/**
 * Given a ParamMeta and an active version string, decide whether the param
 * block should be included in the rendered output.
 *
 * Rules:
 *  - `removed`     → hide for current version ≥ removed version
 *  - `unavailable` → hide for current version < since version
 *  - `available` / `deprecated` → show (deprecated still renders, just styled)
 */
function isParamVisible(meta: ParamMeta, version: string): boolean {
    const status = getVersionStatus(version, meta.since, meta.deprecated, meta.removed);
    return status !== 'removed' && status !== 'unavailable';
}

/**
 * Skip whitespace-only text nodes and html nodes that are blank.
 * Used to bridge the gap between a meta comment and its following heading.
 */
function skipBlankNodes(nodes: Content[], start: number): number {
    let j = start;
    while (j < nodes.length) {
        const n = nodes[j];
        // Allow blank html and empty text through; stop on meaningful content
        const val = (n as { value?: string }).value ?? '';
        const isBlankHtml = n.type === 'html' && val.trim() === '';
        const isEmptyText = n.type === 'text' && val.trim() === '';
        if (!isBlankHtml && !isEmptyText) break;
        j++;
    }
    return j;
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

/**
 * `remarkParamGaterV11`
 *
 * Scans the MDX AST for inline comment nodes that carry version annotations
 * (`@since`, `@removed`, `@deprecated`, `@type`, `@required`, `@input`).
 * Each such comment is expected to immediately precede a heading (of depth ≥
 * `minHeadingDepth`) that starts a parameter section.
 *
 * When a `version` is active:
 *  - Parameters not yet introduced (`@since`) are removed from the AST.
 *  - Parameters that have been removed (`@removed`) are removed from the AST.
 *  - Deprecated parameters are kept but the `deprecated` prop is passed to the
 *    wrapping `<PSJParamSection>` element.
 *
 * Input params (`@input` / `@inputs`) follow the same rules and are wrapped in
 * `<PSJParamSection kind="input" …>` for downstream styling.
 *
 * When no `version` is provided (e.g. during static generation without a
 * version context), all blocks are preserved so that nothing is accidentally
 * hidden.
 */
export const remarkParamGaterV11: Plugin<[VersionFilterOptions?], Root> = (options) => {
    const opts = { ...DEFAULTS, ...options };

    const transformer: Transformer<Root> = (tree, file) => {
        // ── Resolve version ───────────────────────────────────────────────────
        let version =
            opts.version ||
            ((file.data as Record<string, unknown>)._version as string | undefined);

        if (!version && typeof file.path === 'string') {
            const m = file.path.match(/[/\\](\d+\.\d+\.\d+)([/\\]|$)/);
            if (m) version = m[1];
        }

        // ── Walk nodes ────────────────────────────────────────────────────────
        const nodes = tree.children;
        const out: Content[] = [];
        let i = 0;

        while (i < nodes.length) {
            const node = nodes[i];
            const rawValue = (node as { value?: string }).value ?? '';
            const meta = parseParamMeta(rawValue);

            if (meta) {
                // Skip any blank separators between the comment and the heading
                const headingIdx = skipBlankNodes(nodes, i + 1);
                const headingNode = nodes[headingIdx];

                if (
                    headingNode &&
                    isHeading(headingNode) &&
                    headingNode.depth >= opts.minHeadingDepth
                ) {
                    const depth = headingNode.depth;

                    // Collect the whole block: heading + everything until the
                    // next sibling heading at the same (or shallower) depth.
                    const block: Content[] = [headingNode];
                    let k = headingIdx + 1;
                    while (k < nodes.length) {
                        const n = nodes[k];
                        if (isHeading(n) && n.depth <= depth) break;
                        
                        // Break if we hit another param comment to avoid swallowing it into this block
                        const nValue = (n as { value?: string }).value ?? '';
                        if (parseParamMeta(nValue)) break;

                        block.push(n);
                        k++;
                    }

                    // If we have a version context, apply visibility filtering.
                    // Without a version, we keep everything (safe default).
                    const keep = !version || isParamVisible(meta, version);

                    if (keep) {
                        const attributes = [
                            meta.kind === 'input' && {
                                type: 'mdxJsxAttribute',
                                name: 'kind',
                                value: 'input',
                            },
                            meta.since && {
                                type: 'mdxJsxAttribute',
                                name: 'since',
                                value: meta.since,
                            },
                            meta.removed && {
                                type: 'mdxJsxAttribute',
                                name: 'removed',
                                value: meta.removed,
                            },
                            meta.deprecated && {
                                type: 'mdxJsxAttribute',
                                name: 'deprecated',
                                value: meta.deprecated,
                            },
                            meta.type && {
                                type: 'mdxJsxAttribute',
                                name: 'type',
                                value: meta.type,
                            },
                            meta.required && {
                                type: 'mdxJsxAttribute',
                                name: 'required',
                                value: 'true',
                            },
                        ].filter(Boolean);

                        out.push({
                            type: 'mdxJsxFlowElement',
                            name: 'PSJParamSection',
                            attributes,
                            children: block,
                        } as unknown as Content);

                        // Export param metadata for search indexing
                        const docData = file.data as { paramMeta?: ParamMetaExport[] };
                        const exportedMeta = docData.paramMeta || [];
                        const headingText = flattenNode(headingNode as unknown as RootContent);
                        exportedMeta.push({
                            name: headingText.trim(),
                            since: meta.since,
                            removed: meta.removed
                        });
                        docData.paramMeta = exportedMeta;
                    }
                    // Whether kept or filtered, advance past the entire block.
                    i = k;
                    continue;
                }
            }

            // Default: pass node through unchanged.
            out.push(node);
            i++;
        }

        tree.children = out;
    };

    return transformer;
};
