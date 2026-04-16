/**
 * Resolves tokens appearing in MDX source to SymbolEntry objects.
 * Works across all five symbol categories produced by build-symbol-graph.ts.
 */

import type { SymbolEntry, SymbolGraph } from '@/scripts/build-symbol-graph';

// ── Lazy graph load ───────────────────────────────────────────────────────

let _graph: SymbolGraph | null = null;

function getGraph(): SymbolGraph {
    if (_graph) return _graph;

    try {
        // eslint-disable-next-line @typescript-eslint/no-require-imports
        _graph = require('../content/docs/.generated/symbol-graph.json') as SymbolGraph;
    } catch {
        console.warn(
            '[symbols] symbol-graph.json not found. ' +
                'Run `npm run build:symbols` before `next dev` or `next build`.',
        );
        _graph = { symbols: {}, aliases: {}, version: 1, builtAt: '' };
    }

    return _graph;
}

// ── Token normalisation ───────────────────────────────────────────────────
//
// Handles common usage patterns in PSJ docs:
//   Elastic(...)        → Elastic       (constructor call)
//   Elastic.property    → Elastic       (attribute access)
//   Elastic[]           → Elastic       (list usage)
//   JPT.DItemType.BODY  → BODY          (qualified enum access — keep last segment)
//   JPT.ElemKind.ELEMKIND_2D → ELEMKIND_2D
//   JPT.UnitType.Length_mm   → Length_mm

function normaliseToken(raw: string): string {
    const token = raw.trim();

    // Qualified JPT access: JPT.Xxx.SYMBOL → take last segment
    if (token.startsWith('JPT.')) {
        const parts = token.split('.');
        return parts[parts.length - 1];
    }

    return token
        .replace(/\(.*$/, '') // strip constructor/call parens
        .replace(/<[^>]*>/g, '') // strip generics
        .replace(/\[\]/g, '') // strip list brackets
        .split('.')[0] // take base before attribute access
        .trim();
}

// ── Memoized lookup ───────────────────────────────────────────────────────
//
// Cache is safe to hold for the process lifetime because the graph is
// immutable after build. Call clearSymbolCache() in watch-mode rebuild.

const _cache = new Map<string, SymbolEntry | null>();

export function resolveSymbol(rawToken: string, scope?: string): SymbolEntry | null {
    const cacheKey = scope ? `${scope}:${rawToken}` : rawToken;
    if (_cache.has(cacheKey)) return _cache.get(cacheKey)!;

    const graph = getGraph();
    const base = normaliseToken(rawToken);

    let entry: SymbolEntry | null = null;

    // 1. Try scoped match: scope.base
    if (scope) {
        entry = graph.symbols[`${scope}.${base}`] ?? null;
    }

    // 2. Try direct match (global)
    if (!entry) {
        entry = graph.symbols[base] ?? null;
    }

    // 3. Alias match (e.g. abbreviation "int" -> "Integer")
    if (!entry) {
        const canonical = graph.aliases[base];
        if (canonical) entry = graph.symbols[canonical] ?? null;
    }

    _cache.set(cacheKey, entry);
    return entry;
}

export function clearSymbolCache(): void {
    _cache.clear();
    _graph = null;
}

export function getAllSymbolNames(): string[] {
    return Object.keys(getGraph().symbols);
}

export type { SymbolEntry };
