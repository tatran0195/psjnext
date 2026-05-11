'use client';

import { type ReactNode, useMemo, useState } from 'react';

import type { ResolvedParam } from '../types';

// ─── Params panel with search + inline filters ───────────────────────────────

export interface ParamEntry {
    key: string;
    param: ResolvedParam;
    node: ReactNode;
}

type FilterType = 'all' | 'deprecated' | 'removed';

export function ParamsPanel({ entries }: { entries: ParamEntry[] }) {
    const isDeprecated = (p: ResolvedParam) => p.deprecated || !!p.deprecated_in;
    const isRemoved = (p: ResolvedParam) => p.removed || !!p.removed_in;

    const hasDeprecated = entries.some((e) => isDeprecated(e.param) && !isRemoved(e.param));
    const hasRemoved = entries.some((e) => isRemoved(e.param));

    const [search, setSearch] = useState('');
    const [activeFilter, setActiveFilter] = useState<FilterType>('all');

    const deprecatedCount = entries.filter((e) => isDeprecated(e.param) && !isRemoved(e.param)).length;
    const removedCount = entries.filter((e) => isRemoved(e.param)).length;
    // Total count for 'All' includes all valid (non-removed, non-deprecated) + deprecated params,
    // or you can just show all non-removed params. Let's make 'all' show everything except removed.
    const allCount = entries.filter((e) => !isRemoved(e.param)).length;

    const visible = useMemo(() => {
        const q = search.trim().toLowerCase();
        return entries.filter((e) => {
            // 1. Tag filters
            if (activeFilter === 'all' && isRemoved(e.param)) return false;
            if (activeFilter === 'deprecated' && (!isDeprecated(e.param) || isRemoved(e.param))) return false;
            if (activeFilter === 'removed' && !isRemoved(e.param)) return false;

            // 2. Search filter
            if (q) {
                const name = (e.param.display_name ?? e.param.name).toLowerCase();
                return name.includes(q);
            }
            return true;
        });
    }, [entries, search, activeFilter]);

    return (
        <div className="flex flex-col gap-3">
            {/* ── Search & Filter row ──────────────────────────────────────────── */}
            <div className="flex flex-col sm:flex-row gap-3 items-start sm:items-center justify-between not-prose">
                {/* Search Input */}
                <div className="relative flex-1 min-w-[200px] max-w-sm">
                    <svg
                        className="pointer-events-none absolute left-2.5 top-1/2 -translate-y-1/2 size-4 text-fd-muted-foreground"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth={2}
                        viewBox="0 0 24 24"
                        aria-hidden="true"
                    >
                        <circle cx="11" cy="11" r="8" />
                        <path d="m21 21-4.35-4.35" />
                    </svg>
                    <input
                        type="search"
                        aria-label="Filter parameters"
                        placeholder="Search parameters..."
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        className="h-9 w-full rounded-md border border-fd-border bg-fd-card pl-9 pr-3 text-sm text-fd-foreground placeholder:text-fd-muted-foreground outline-none focus:ring-1 focus:ring-fd-ring focus:border-fd-ring transition-colors"
                    />
                </div>

                {/* Inline filter pills */}
                {(hasDeprecated || hasRemoved) && (
                    <div className="flex bg-fd-secondary/50 p-1 rounded-md border border-fd-border shrink-0 overflow-x-auto">
                        <button
                            type="button"
                            onClick={() => setActiveFilter('all')}
                            className={[
                                'px-3 py-1 text-xs font-semibold rounded-sm transition-colors whitespace-nowrap',
                                activeFilter === 'all'
                                    ? 'bg-fd-background text-fd-foreground shadow-sm'
                                    : 'text-fd-muted-foreground hover:text-fd-foreground',
                            ].join(' ')}
                        >
                            All ({allCount})
                        </button>

                        {hasDeprecated && (
                            <button
                                type="button"
                                onClick={() => setActiveFilter('deprecated')}
                                className={[
                                    'px-3 py-1 text-xs font-semibold rounded-sm transition-colors whitespace-nowrap',
                                    activeFilter === 'deprecated'
                                        ? 'bg-amber-100 text-amber-900 shadow-sm dark:bg-amber-900/30 dark:text-amber-300'
                                        : 'text-fd-muted-foreground hover:text-amber-600 dark:hover:text-amber-400',
                                ].join(' ')}
                            >
                                Deprecated ({deprecatedCount})
                            </button>
                        )}

                        {hasRemoved && (
                            <button
                                type="button"
                                onClick={() => setActiveFilter('removed')}
                                className={[
                                    'px-3 py-1 text-xs font-semibold rounded-sm transition-colors whitespace-nowrap',
                                    activeFilter === 'removed'
                                        ? 'bg-red-100 text-red-900 shadow-sm dark:bg-red-900/30 dark:text-red-300'
                                        : 'text-fd-muted-foreground hover:text-red-600 dark:hover:text-red-400',
                                ].join(' ')}
                            >
                                Removed ({removedCount})
                            </button>
                        )}
                    </div>
                )}
            </div>

            {/* ── Param list ──────────────────────────────────────────── */}
            {visible.length === 0 ? (
                <div className="rounded-lg border border-fd-border bg-fd-card/50 py-12 px-4 text-center">
                    <p className="text-sm text-fd-muted-foreground">
                        {search.trim()
                            ? `No '${activeFilter}' parameters match "${search.trim()}".`
                            : `No parameters found for filter: ${activeFilter}.`}
                    </p>
                </div>
            ) : (
                <div className="flex flex-col divide-y divide-fd-border/50 rounded-lg border border-fd-border overflow-hidden bg-fd-card">
                    {visible.map((e) => (
                        <div
                            key={e.key}
                            className={[
                                'transition-opacity duration-200',
                                e.param.removed
                                    ? 'opacity-50 grayscale-[50%]'
                                    : e.param.deprecated
                                      ? 'bg-amber-50/20 dark:bg-amber-900/5'
                                      : '',
                            ].join(' ')}
                        >
                            {e.node}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
