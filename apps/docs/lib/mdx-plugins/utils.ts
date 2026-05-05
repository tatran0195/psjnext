import { valueToEstree } from 'estree-util-value-to-estree';

import type { Expression } from 'estree';
import type Hast from 'hast';
import type { RootContent } from 'mdast';
import type { MdxjsEsm } from 'mdast-util-mdx';

export function flattenNode(node: RootContent): string {
    if ('children' in node) return node.children.map(flattenNode).join('');
    if ('value' in node && typeof node.value === 'string') return node.value;
    return '';
}

export function flattenNodeHast(node: Hast.RootContent): string {
    if ('children' in node) return node.children.map(flattenNodeHast).join('');
    return 'value' in node && typeof node.value === 'string' ? node.value : '';
}

export function toMdxExport(name: string, value: unknown): MdxjsEsm {
    return toMdxExportRaw(name, valueToEstree(value));
}

export function toMdxExportRaw(name: string, expression: Expression): MdxjsEsm {
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
                                    init: expression,
                                },
                            ],
                        },
                    },
                ],
            },
        },
    };
}

export function parseDecorators(text: string) {
    const decorators: { key: string; value?: string }[] = [];
    const regex = /@(\w+)(?:\(([^)]*)\))?/g;
    let match;
    while ((match = regex.exec(text)) !== null) {
        decorators.push({ key: match[1], value: match[2] });
    }
    return decorators;
}

export function stripDecorators(text: string): string {
    return text.replace(/@\w+(\([^)]*\))?/g, '').trim();
}

export function semverGte(a: string, b: string): boolean {
    const pa = a.split('.').map(Number);
    const pb = b.split('.').map(Number);
    for (let i = 0; i < 3; i++) {
        if ((pa[i] || 0) > (pb[i] || 0)) return true;
        if ((pa[i] || 0) < (pb[i] || 0)) return false;
    }
    return true;
}

export function semverLt(a: string, b: string): boolean {
    return !semverGte(a, b);
}

export type VersionStatus = 'available' | 'unavailable' | 'deprecated' | 'removed';

export function getVersionStatus(
    current: string,
    introduced?: string,
    deprecated?: string,
    removed?: string,
): VersionStatus {
    if (removed && semverGte(current, removed)) return 'removed';
    if (introduced && !semverGte(current, introduced)) return 'unavailable';
    if (deprecated && semverGte(current, deprecated)) return 'deprecated';
    return 'available';
}
