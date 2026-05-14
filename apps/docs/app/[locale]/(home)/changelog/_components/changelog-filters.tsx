import { Search, X } from 'lucide-react';
import { useTranslations } from 'next-intl';

import { cn } from '@/lib/cn';

type Props = {
    query: string;
    onQueryChangeAction: (v: string) => void;
    allTags: string[];
    activeTag: string;
    onTagChangeAction: (tag: string) => void;
    totalCount: number;
    filteredCount: number;
    hasActiveFilters: boolean;
    onClearAllAction: () => void;
};

export function ChangelogFilters({
    query,
    onQueryChangeAction,
    allTags,
    activeTag,
    onTagChangeAction,
    totalCount,
    filteredCount,
    hasActiveFilters,
    onClearAllAction,
}: Props) {
    const t = useTranslations('changelog');
    const showingText = t('results.showing', { count: filteredCount, total: totalCount });

    return (
        <div className="flex flex-col gap-6">
            {/* Search input */}
            <div className="flex flex-wrap items-center gap-4">
                <div
                    className="flex items-center gap-3 px-4 py-2.5 flex-1 min-w-[280px]"
                    style={{
                        border: '1px solid var(--psj-border)',
                        background: 'var(--psj-surface-1)',
                    }}
                >
                    <Search size={18} className="text-(--psj-text-3)" />
                    <input
                        value={query}
                        onChange={(e) => onQueryChangeAction(e.target.value)}
                        placeholder={t('search.find')}
                        className="bg-transparent text-sm outline-none flex-1 text-(--psj-text-1)"
                    />
                    {query && (
                        <button
                            onClick={() => onQueryChangeAction('')}
                            className="text-(--psj-text-3) hover:text-(--psj-text-1) transition-colors"
                        >
                            <X size={16} />
                        </button>
                    )}
                </div>
            </div>

            {/* Tag chips */}
            <div className="flex flex-wrap items-center gap-2">
                {allTags.map((tag) => {
                    const active = activeTag === tag;
                    return (
                        <button
                            key={tag}
                            onClick={() => onTagChangeAction(tag)}
                            className={cn(
                                'flex items-center gap-2 px-4 py-2 text-xs font-bold transition-all border whitespace-nowrap',
                                active
                                    ? 'bg-(--psj-blue) border-(--psj-blue) text-white shadow-lg shadow-blue-500/20'
                                    : 'bg-(--psj-surface-1) border-(--psj-border) text-(--psj-text-2) hover:border-(--psj-text-3)',
                            )}
                        >
                            {tag}
                        </button>
                    );
                })}
            </div>

            {/* Results summary */}
            <div className="flex items-center justify-between">
                <div className="text-[10px] uppercase tracking-[0.15em] font-bold text-(--psj-text-3)">
                    {showingText}
                </div>
                {hasActiveFilters && (
                    <button
                        onClick={onClearAllAction}
                        className="text-[11px] uppercase tracking-widest font-bold text-(--psj-blue) underline hover:opacity-80 transition-opacity"
                    >
                        {t('filters.clearFilters')}
                    </button>
                )}
            </div>
        </div>
    );
}
