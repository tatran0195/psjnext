'use client';

import { useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import { Search, X } from 'lucide-react';

import type { ChangelogFrontmatter } from '@/lib/utils/markdown';

import { ChangelogItem } from '@/components/changelog-item';
import { cn } from '@/lib/cn';
import { type TranslationDict } from '@/lib/i18n';

type Props = {
    entries: ChangelogFrontmatter[];
    t: TranslationDict['changelog'];
};

export default function PageClient({ entries, t }: Props) {
    const { filters, results, search } = t;

    const [query, setQuery] = useState('');
    const [activeTag, setActiveTag] = useState<string>(filters.all);

    // Extract all unique tags from entries
    const allTags = useMemo(() => {
        const tags = new Set<string>();
        entries.forEach((entry) => entry.tags?.forEach((tag) => tags.add(tag)));
        return [filters.all, ...Array.from(tags).sort()];
    }, [entries, filters.all]);

    const filteredEntries = useMemo(() => {
        return entries.filter((entry) => {
            const matchesSearch =
                entry.title.toLowerCase().includes(query.toLowerCase()) ||
                entry.summary.toLowerCase().includes(query.toLowerCase());
            const matchesTag = activeTag === filters.all || entry.tags?.includes(activeTag);
            return matchesSearch && matchesTag;
        });
    }, [entries, query, activeTag, filters.all]);

    return (
        <div className="flex flex-col gap-12 w-full">
            {/* ─────── INLINE FILTER BAR ─────── */}
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
                            onChange={(e) => setQuery(e.target.value)}
                            placeholder={search.find}
                            className="bg-transparent text-sm outline-none flex-1 text-(--psj-text-1)"
                        />
                        {query && (
                            <button
                                onClick={() => setQuery('')}
                                className="text-(--psj-text-3) hover:text-(--psj-text-1) transition-colors"
                            >
                                <X size={16} />
                            </button>
                        )}
                    </div>
                </div>

                {/* Category chips */}
                <div className="flex flex-wrap items-center gap-2">
                    {allTags.map((tag) => {
                        const active = activeTag === tag;
                        return (
                            <button
                                key={tag}
                                onClick={() => setActiveTag(tag)}
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
                        {results.showing
                            .replace('{count}', filteredEntries.length.toString())
                            .replace('{total}', entries.length.toString())}
                    </div>
                    {(activeTag !== filters.all || query) && (
                        <button
                            onClick={() => {
                                setActiveTag(filters.all);
                                setQuery('');
                            }}
                            className="text-[11px] uppercase tracking-widest font-bold text-(--psj-blue) underline hover:opacity-80 transition-opacity"
                        >
                            {filters.clearFilters}
                        </button>
                    )}
                </div>
            </div>

            {/* ─────── CHANGELOG LIST ─────── */}
            <div className="space-y-24">
                <AnimatePresence mode="popLayout">
                    {filteredEntries.length === 0 ? (
                        <motion.div
                            key="empty"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="py-24 text-center rounded-lg"
                            style={{
                                border: '1px dashed var(--psj-border)',
                                background: 'var(--psj-surface-1)',
                            }}
                        >
                            <Search size={32} className="mx-auto mb-4 text-(--psj-text-3)" />
                            <p className="text-sm font-medium text-(--psj-text-2)">{results.noUpdates}</p>
                            <button
                                onClick={() => {
                                    setQuery('');
                                    setActiveTag(filters.all);
                                }}
                                className="mt-4 text-xs font-bold text-(--psj-blue) underline"
                            >
                                {filters.clearFilters}
                            </button>
                        </motion.div>
                    ) : (
                        filteredEntries.map((entry) => <ChangelogItem key={entry.id} entry={entry} t={t} />)
                    )}
                </AnimatePresence>
            </div>
        </div>
    );
}
