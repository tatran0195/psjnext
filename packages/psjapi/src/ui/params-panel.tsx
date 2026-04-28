'use client';

import { type ReactNode, useState } from 'react';
import type { ResolvedParam } from '../types';

// ─── Params panel with deprecated/removed toggles ─────────────────────────────

export interface ParamEntry {
  key: string;
  param: ResolvedParam;
  node: ReactNode;
}

export function ParamsPanel({ entries }: { entries: ParamEntry[] }) {
  const hasDeprecated = entries.some((e) => e.param.deprecated && !e.param.removed);
  const hasRemoved    = entries.some((e) => e.param.removed);

  const [showDeprecated, setShowDeprecated] = useState(true);
  const [showRemoved,    setShowRemoved]    = useState(false);

  const visible = entries.filter((e) => {
    if (e.param.removed)    return showRemoved;
    if (e.param.deprecated) return showDeprecated;
    return true;
  });

  return (
    <div className="flex flex-col">
      {/* Toggle bar */}
      {(hasDeprecated || hasRemoved) && (
        <div className="flex flex-wrap items-center gap-2 mb-3 not-prose">
          {hasDeprecated && (
            <button
              type="button"
              onClick={() => setShowDeprecated((v) => !v)}
              className={[
                'inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-xs font-medium transition-colors',
                showDeprecated
                  ? 'border-amber-400/60 bg-amber-50/60 text-amber-700 dark:bg-amber-900/20 dark:text-amber-300'
                  : 'border-fd-border bg-fd-card text-fd-muted-foreground hover:text-fd-foreground',
              ].join(' ')}
            >
              <span className="size-1.5 rounded-full bg-current opacity-70" />
              {showDeprecated ? 'Hide deprecated' : 'Show deprecated'}
            </button>
          )}
          {hasRemoved && (
            <button
              type="button"
              onClick={() => setShowRemoved((v) => !v)}
              className={[
                'inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-xs font-medium transition-colors',
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
      )}

      {/* Params */}
      {visible.length === 0 ? (
        <p className="text-sm text-fd-muted-foreground italic py-2">
          No parameters available for this version.
        </p>
      ) : (
        <div className="flex flex-col">
          {visible.map((e) => (
            <div
              key={e.key}
              className={[
                'transition-opacity',
                e.param.removed
                  ? 'opacity-50 [&>*]:line-through-param' // dim removed
                  : e.param.deprecated
                  ? 'opacity-70'                          // slightly dim deprecated
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
