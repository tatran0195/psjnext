import { isValidElement, type ReactNode } from 'react';

type PayloadNode = {
    _payload?: { value?: unknown };
};

type PropsNode = {
    props?: { children?: unknown };
};

function hasPayload(node: unknown): node is PayloadNode {
    return typeof node === 'object' && node !== null && '_payload' in node;
}

function hasProps(node: unknown): node is PropsNode {
    return typeof node === 'object' && node !== null && 'props' in node;
}

function extractText(node: unknown): string {
    if (typeof node === 'string') return node;
    if (typeof node === 'number') return String(node);
    if (!node) return '';
    if (isValidElement<{ children?: ReactNode }>(node)) {
        const children = node.props.children;
        if (Array.isArray(children)) {
            return children.map(extractText).join('');
        }
        return extractText(children);
    }

    // Handle RSC/Lazy payloads
    if (typeof node === 'object') {
        if (Array.isArray(node)) {
            return node.map(extractText).join('');
        }
        if (hasPayload(node) && node._payload?.value) {
            return extractText(node._payload.value);
        }

        if (hasProps(node) && node.props?.children) {
            return extractText(node.props.children);
        }
    }

    return String(node);
}

/**
 * Precise substring matching for technical names.
 * Handles dots and segments by ensuring all query terms are present in the target.
 */
export function sidebarMatch(query: string, target: string | unknown): boolean {
    const q = query.toLowerCase().trim();
    if (q === '') return true;

    // Handle potential object names or missing names gracefully
    const extracted = extractText(target);
    const t = extracted.toLowerCase();

    // 1. Direct substring match (e.g., "XXX.Create" matches "JPT.XXX.Create()")
    if (t.includes(q)) return true;

    // 2. Multi-term match (handles "XXX Create" matching "XXX.Create")
    // Split by spaces and dots to get individual terms
    const terms = q.split(/[\s.]+/).filter(Boolean);
    if (terms.length === 0) return true;

    // Every term in the query must be found in the target as a substring
    return terms.every((term) => t.includes(term));
}
