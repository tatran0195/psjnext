import { getVersionStatus } from './utils';

import type { Content, Heading, Root } from 'mdast';
import type { Plugin, Transformer } from 'unified';

export interface VersionFilterOptions {
    version?: string;
    minHeadingDepth?: number;
}

type Meta = {
    since?: string;
    deprecated?: string;
    removed?: string;
    type?: string;
    required?: boolean;
};

const DEFAULTS = {
    minHeadingDepth: 3,
};

function isHeading(node: any): node is Heading {
    return node.type === 'heading';
}

function parseCommentMeta(value: string): Meta | null {
    const meta: Meta = {};

    const find = (key: string) => {
        const regex = new RegExp(`@${key}:([^\\s;>]+)`, 'i');
        const match = value.match(regex);
        if (!match) return undefined;
        let val = match[1].trim();
        val = val.replace(/-+$/, '');
        return val;
    };

    meta.since = find('since');
    meta.deprecated = find('deprecated');
    meta.removed = find('removed');
    meta.type = find('type');
    meta.required = /@required/i.test(value);

    return Object.keys(meta).length > 0 ? meta : null;
}

function isVisible(meta: Meta, version: string): boolean {
    const status = getVersionStatus(version, meta.since, meta.deprecated, meta.removed);
    return status !== 'removed' && status !== 'unavailable';
}

export const remarkParamGaterV11: Plugin<[VersionFilterOptions], Root> = (options) => {
    const opts = { ...DEFAULTS, ...options };

    const transformer: Transformer<Root> = (tree, file) => {
        let version =
            opts.version || ((file.data as Record<string, unknown>)._version as string | undefined);

        if (!version && typeof file.path === 'string') {
            const matches = file.path.match(/[/\\](\d+\.\d+\.\d+)([/\\]|$)/);
            if (matches) version = matches[1];
        }

        const nodes = tree.children;

        if (file.path?.includes('ACModeling.ACBoundary.FirstMethod')) {
            console.error(`[PARAM-GATER-V11] Processing ${file.path}, version: ${version}`);
            nodes.forEach((n, idx) => {
                const val = (n as any).value || (n as any).name || '';
                console.error(`  [${idx}] ${n.type}: ${val.substring(0, 30)}...`);
            });
        }

        const out: Content[] = [];
        let i = 0;

        while (i < nodes.length) {
            const node = nodes[i];

            // Match ANY node that looks like our metadata comment
            const val = (node as any).value || '';
            const meta =
                typeof val === 'string' && val.includes('@') ? parseCommentMeta(val) : null;

            if (meta) {
                let j = i + 1;
                while (
                    j < nodes.length &&
                    (nodes[j].type === 'text' ||
                        nodes[j].type === 'break' ||
                        nodes[j].type === 'html')
                ) {
                    const textVal = (nodes[j] as any).value || '';
                    if (textVal.trim() !== '' && nodes[j].type !== 'html') break;
                    j++;
                }

                const next = nodes[j];
                if (next && isHeading(next) && next.depth >= opts.minHeadingDepth) {
                    const depth = next.depth;
                    const block: Content[] = [next];
                    let k = j + 1;
                    while (k < nodes.length) {
                        const n = nodes[k];
                        if (isHeading(n) && n.depth <= depth) break;
                        block.push(n);
                        k++;
                    }

                    if (!version || isVisible(meta, version)) {
                        const attributes = [
                            {
                                type: 'mdxJsxAttribute',
                                name: 'debugId',
                                value: 'BINGO-V11-ULTRA-3',
                            },
                            { type: 'mdxJsxAttribute', name: 'name', value: '' },
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
                        ].filter(Boolean) as any[];

                        out.push({
                            type: 'mdxJsxFlowElement',
                            name: 'PSJParamSection',
                            attributes,
                            children: block,
                        } as any);
                    }

                    i = k;
                    continue;
                }
            }

            out.push(node);
            i++;
        }

        tree.children = out;
    };

    return transformer;
};
