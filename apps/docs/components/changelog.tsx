'use client';

import { useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import { Search, Tag as TagIcon, X } from 'lucide-react';

import type { ChangelogFrontmatter } from '@/lib/utils/markdown';

import { ChangelogItem } from '@/components/changelog-item';
import { cn } from '@/lib/cn';
import { translations } from '@/lib/i18n-translations';

interface ChangelogProps {
    entries?: ChangelogFrontmatter[];
    lang?: string;
}

export function Changelog({ entries = [], lang = 'en' }: ChangelogProps) {
    const t =
        translations[lang as keyof typeof translations]?.changelog || translations.en.changelog;
    const [search, setSearch] = useState('');
    const [activeTag, setActiveTag] = useState<string>(t.all);

    // Extract all unique tags
    const allTags = useMemo(() => {
        const tags = new Set<string>();
        entries.forEach((entry) => {
            entry.tags?.forEach((tag) => tags.add(tag));
        });
        return [t.all, ...Array.from(tags).sort()];
    }, [entries, t.all]);

    const filteredEntries = useMemo(() => {
        return entries.filter((entry) => {
            const matchesSearch =
                entry.title.toLowerCase().includes(search.toLowerCase()) ||
                entry.summary.toLowerCase().includes(search.toLowerCase());
            const matchesTag = activeTag === t.all || entry.tags?.includes(activeTag);
            return matchesSearch && matchesTag;
        });
    }, [entries, search, activeTag, t.all]);

    return (
        <div
            className="min-h-screen"
            style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}
        >
            <header
                className="psj-subpage-hero border-b"
                style={{ borderColor: 'var(--psj-border)' }}
            >
                <div className="psj-container py-16 lg:py-20 relative z-10">
                    <div className="max-w-4xl">
                        <div className="flex items-center gap-3 mb-4">
                            <div className="psj-label">{t.platformUpdates}</div>
                        </div>
                        <h1
                            className="psj-h1 mb-6 text-4xl lg:text-5xl"
                            style={{ color: 'var(--psj-text-1)' }}
                        >
                            {t.changelog}
                        </h1>
                        <p
                            className="text-lg leading-relaxed max-w-2xl opacity-80"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            {t.changelogDescription}
                        </p>
                    </div>
                </div>
            </header>

            <main className="psj-container py-12 lg:py-20">
                <div className="grid lg:grid-cols-[240px_1fr] gap-16 items-start">
                    {/* ─────── LEFT SIDEBAR (Filters) ─────── */}
                    <aside className="hidden lg:block sticky top-36 space-y-10">
                        <div className="space-y-4">
                            <div className="text-[11px] uppercase tracking-[0.2em] font-bold text-(--psj-text-3)">
                                {t.searchUpdates}
                            </div>
                            <div
                                className="flex items-center gap-3 px-3 py-2"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={14} className="text-(--psj-text-3)" />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder={t.find}
                                    className="bg-transparent text-sm outline-none w-full text-(--psj-text-1)"
                                />
                                {search && (
                                    <button
                                        onClick={() => setSearch('')}
                                        className="text-(--psj-text-3)"
                                    >
                                        <X size={12} />
                                    </button>
                                )}
                            </div>
                        </div>

                        <div className="space-y-4">
                            <div className="text-[11px] uppercase tracking-[0.2em] font-bold text-(--psj-text-3) flex items-center gap-2">
                                <TagIcon size={12} /> {t.categories}
                            </div>
                            <div className="flex flex-col gap-1">
                                {allTags.map((tag) => (
                                    <button
                                        key={tag}
                                        onClick={() => setActiveTag(tag)}
                                        className={cn(
                                            'text-left px-3 py-2 text-[13px] transition-all border-l-2',
                                            activeTag === tag
                                                ? 'border-(--psj-blue) text-(--psj-blue) font-bold bg-(--psj-blue-subtle)'
                                                : 'border-transparent text-(--psj-text-2) hover:bg-(--psj-surface-1)',
                                        )}
                                    >
                                        {tag}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </aside>

                    {/* ─────── MAIN CONTENT ─────── */}
                    <div className="space-y-24 max-w-4xl">
                        {/* Mobile Filters (Inline) */}
                        <div className="lg:hidden space-y-6 mb-12">
                            <div
                                className="flex items-center gap-3 px-4 py-2.5"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={16} className="text-(--psj-text-3)" />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder={t.searchUpdates}
                                    className="bg-transparent text-sm outline-none flex-1 text-(--psj-text-1)"
                                />
                            </div>
                            <div className="flex flex-wrap gap-2">
                                {allTags.map((tag) => (
                                    <button
                                        key={tag}
                                        onClick={() => setActiveTag(tag)}
                                        className={cn(
                                            'px-4 py-1.5 text-xs font-bold transition-all border',
                                            activeTag === tag
                                                ? 'bg-(--psj-blue) border-(--psj-blue) text-white'
                                                : 'bg-(--psj-surface-1) border-(--psj-border) text-(--psj-text-2)',
                                        )}
                                    >
                                        {tag}
                                    </button>
                                ))}
                            </div>
                        </div>

                        <AnimatePresence mode="popLayout">
                            {filteredEntries.length === 0 ? (
                                <motion.div
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    exit={{ opacity: 0 }}
                                    className="py-20 text-center rounded-lg"
                                    style={{
                                        border: '1px dashed var(--psj-border)',
                                        background: 'var(--psj-surface-1)',
                                    }}
                                >
                                    <p className="text-sm font-medium text-(--psj-text-3)">
                                        {t.noUpdates}
                                    </p>
                                    <button
                                        onClick={() => {
                                            setSearch('');
                                            setActiveTag(t.all);
                                        }}
                                        className="mt-4 text-xs font-bold text-(--psj-blue) underline"
                                    >
                                        {t.clearFilters}
                                    </button>
                                </motion.div>
                            ) : (
                                filteredEntries.map((entry) => (
                                    <ChangelogItem key={entry.id} entry={entry} lang={lang} />
                                ))
                            )}
                        </AnimatePresence>
                    </div>
                </div>
            </main>
        </div>
    );
}
