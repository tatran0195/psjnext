'use client';

import { useCallback, useId, useMemo, useState } from 'react';
import type { ResolvedParam } from '../types.js';
import { en, type PsjdLocale } from './i18n.js';

// ─── Types ────────────────────────────────────────────────────────────────────

export interface ParamSearchProps {
  params: ResolvedParam[];
  style: 'named' | 'positional';
  onFilter?: (filtered: ResolvedParam[]) => void;
}

export interface UseParamSearchResult {
  query: string;
  setQuery: (q: string) => void;
  filteredParams: ResolvedParam[];
  matchCount: number;
  totalCount: number;
}

// ─── Core search hook ─────────────────────────────────────────────────────────

export function useParamSearch(params: ResolvedParam[]): UseParamSearchResult {
  const [query, setQueryRaw] = useState('');
  const setQuery = useCallback((q: string) => setQueryRaw(q), []);

  const filteredParams = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return params;
    return params.filter((p) => {
      if (p.name?.toLowerCase().includes(q)) return true;
      if (p.display_name?.toLowerCase().includes(q)) return true;
      if (p.type.toLowerCase().includes(q)) return true;
      if (p.description?.toLowerCase().includes(q)) return true;
      if (p.enum_values?.some(
        (e) =>
          e.label.toLowerCase().includes(q) ||
          String(e.id).toLowerCase().includes(q) ||
          e.description?.toLowerCase().includes(q),
      )) return true;
      return false;
    });
  }, [params, query]);

  return { query, setQuery, filteredParams, matchCount: filteredParams.length, totalCount: params.length };
}

// ─── Search input component ───────────────────────────────────────────────────

export function ParamSearchInput({
  query,
  setQuery,
  matchCount,
  totalCount,
  locale = en,
}: {
  query: string;
  setQuery: (q: string) => void;
  matchCount: number;
  totalCount: number;
  locale?: PsjdLocale;
}) {
  const inputId = useId();
  const isFiltered = query.trim().length > 0;

  return (
    <div className="psjd-search-wrapper">
      <div className="psjd-search-input-row">
        <svg className="psjd-search-icon" width="14" height="14" viewBox="0 0 24 24"
          fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
          <circle cx="11" cy="11" r="8" />
          <line x1="21" y1="21" x2="16.65" y2="16.65" />
        </svg>
        <input
          id={inputId}
          type="search"
          className="psjd-search-input"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={locale.filterPlaceholder}
          autoComplete="off"
          spellCheck={false}
          aria-label={locale.filterAriaLabel}
          aria-describedby={`${inputId}-status`}
        />
        {isFiltered && (
          <button className="psjd-search-clear" onClick={() => setQuery('')}
            aria-label={locale.clearFilter} title={locale.clearFilter}>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        )}
      </div>
      <span id={`${inputId}-status`} className="psjd-search-status" aria-live="polite">
        {isFiltered && (
          matchCount === 0
            ? locale.noMatchingParams
            : matchCount === totalCount
              ? null
              : locale.matchCount(matchCount, totalCount)
        )}
      </span>
    </div>
  );
}

// ─── Highlighted text helper ──────────────────────────────────────────────────

export function HighlightMatch({ text, query }: { text: string; query: string }) {
  const q = query.trim();
  if (!q) return <>{text}</>;
  const idx = text.toLowerCase().indexOf(q.toLowerCase());
  if (idx === -1) return <>{text}</>;
  return (
    <>
      {text.slice(0, idx)}
      <mark className="psjd-search-highlight">{text.slice(idx, idx + q.length)}</mark>
      {text.slice(idx + q.length)}
    </>
  );
}
