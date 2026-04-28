'use client';

import { type ReactNode, useMemo, useState } from 'react';

import type { ResolvedParam } from '../types';

// ─── Params panel with search + deprecated/removed toggles ────────────────────

export interface ParamEntry {
    key: string;
    param: ResolvedParam;
    node: ReactNode;
}

export function ParamsPanel({ entries }: { entries: ParamEntry[] }) {
    const hasDeprecated = entries.some((e) => e.param.deprecated && !e.param.removed);
    const hasRemoved = entries.some((e) => e.param.removed);

    const [search, setSearch] = useState('');
    const [showDeprecated, setShowDeprecated] = useState(true);
    const [showRemoved, setShowRemoved] = useState(false);

    const visible = useMemo(() => {
        const q = search.trim().toLowerCase();
        return entries.filter((e) => {
            // deprecated/removed gates
            if (e.param.removed && !showRemoved) return false;
            if (e.param.deprecated && !e.param.removed && !showDeprecated) return false;
            // search filter
            if (q) {
                const name = (e.param.display_name ?? e.param.name).toLowerCase();
                return name.includes(q);
            }
            return true;
        });
    }, [entries, search, showDeprecated, showRemoved]);

    const total = entries.filter((e) => {
        if (e.param.removed && !showRemoved) return false;
        if (e.param.deprecated && !e.param.removed && !showDeprecated) return false;
        return true;
    }).length;

    return (
        <div className="flex flex-col gap-2">
            {/* ── Search row ──────────────────────────────────────────── */}
            <div className="flex flex-wrap items-center gap-2 not-prose">
                <div className="relative flex-1 min-w-[160px]">
                    {/* magnifier icon */}
                    <svg
                        className="pointer-events-none absolute left-2.5 top-1/2 -translate-y-1/2 size-3.5 text-fd-muted-foreground"
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
                        placeholder="Filter parameters…"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        className="h-8 w-full rounded-md border border-fd-border bg-fd-card pl-8 pr-3 text-xs text-fd-foreground placeholder:text-fd-muted-foreground outline-none focus:ring-1 focus:ring-fd-ring focus:border-fd-ring transition-colors"
                    />
                </div>

                {/* match count */}
                {search.trim() && (
                    <span className="text-xs text-fd-muted-foreground shrink-0 tabular-nums">
                        {visible.length} / {total}
                    </span>
                )}

                {/* deprecated toggle */}
                {hasDeprecated && (
                    <button
                        type="button"
                        onClick={() => setShowDeprecated((v) => !v)}
                        className={[
                            'inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs font-medium transition-colors shrink-0',
                            showDeprecated
                                ? 'border-amber-400/60 bg-amber-50/60 text-amber-700 dark:bg-amber-900/20 dark:text-amber-300'
                                : 'border-fd-border bg-fd-card text-fd-muted-foreground hover:text-fd-foreground',
                        ].join(' ')}
                    >
                        <span className="size-1.5 rounded-full bg-current opacity-70" />
                        {showDeprecated ? 'Hide deprecated' : 'Show deprecated'}
                    </button>
                )}

                {/* removed toggle */}
                {hasRemoved && (
                    <button
                        type="button"
                        onClick={() => setShowRemoved((v) => !v)}
                        className={[
                            'inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs font-medium transition-colors shrink-0',
                            showRemoved
                                ? 'border-red-400/60 bg-red-50/60 text-red-700 dark:bg-red-900/20 dark:text-red-300'
                                : 'border-fd-border bg-fd-card text-fd-muted-foreground hover:text-fd-foreground',
                        ].join(' ')}
                    >
                        <span className="size-1.5 rounded-full bg-current opacity-70" />
                        {showRemoved ? 'Hide removed' : 'Show removed'}
                    </button>
                )}
            </div>

            {/* ── Param list ──────────────────────────────────────────── */}
            {visible.length === 0 ? (
                <p className="text-sm text-fd-muted-foreground italic py-3 text-center">
                    {search.trim()
                        ? `No parameters match "${search.trim()}".`
                        : 'No parameters available for this version.'}
                </p>
            ) : (
                <div className="flex flex-col divide-y divide-fd-border/60 rounded-lg border border-fd-border overflow-hidden">
                    {visible.map((e) => (
                        <div
                            key={e.key}
                            className={[
                                'transition-opacity',
                                e.param.removed
                                    ? 'opacity-40'
                                    : e.param.deprecated
                                      ? 'opacity-70'
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
