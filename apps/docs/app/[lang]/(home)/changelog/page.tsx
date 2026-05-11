'use client';

import { use, useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import { Search, X } from 'lucide-react';

import { ChangelogItem } from '@/components/changelog-item';
import { HeroSection } from '@/components/hero-sections';
import { cn } from '@/lib/cn';
import { translations } from '@/lib/i18n-translations';
import { changelog } from '@/lib/source';

export default function ChangelogPage({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = use(params);

    const t = translations[lang as keyof typeof translations]?.changelog || translations.en.changelog;
    const [search, setSearch] = useState('');
    const [activeTag, setActiveTag] = useState<string>(t.all);

    const sortedEntries = changelog
        .getPages(lang)
        .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
        .reverse()
        .filter((entry) => !entry?.data.draft)
        .map((entry) => ({
            id: entry.data.id,
            slug: entry.data.slug,
            date: entry.data.date,
            version: entry.data.version,
            title: entry.data.title,
            summary: entry.data.summary,
            tags: entry.data.tags,
            image: entry.data.image,
        }));

    // Extract all unique tags
    const allTags = useMemo(() => {
        const tags = new Set<string>();
        sortedEntries.forEach((entry) => {
            entry.tags?.forEach((tag) => tags.add(tag));
        });
        return [t.all, ...Array.from(tags).sort()];
    }, [sortedEntries, t.all]);

    const filteredEntries = useMemo(() => {
        return sortedEntries.filter((entry) => {
            const matchesSearch =
                entry.title.toLowerCase().includes(search.toLowerCase()) ||
                entry.summary.toLowerCase().includes(search.toLowerCase());
            const matchesTag = activeTag === t.all || entry.tags?.includes(activeTag);
            return matchesSearch && matchesTag;
        });
    }, [sortedEntries, search, activeTag, t.all]);

    return (
        <div className="min-h-screen" style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}>
            <HeroSection label={t.platformUpdates} title={t.changelog} description={t.changelogDescription} />

            <main className="psj-container py-10">
                <div className="max-w-7xl mx-auto">
                    {/* ─────── INLINE FILTER BAR ─────── */}
                    <div className="flex flex-col gap-6 mb-4 lg:mb-8">
                        {/* Primary Filter Row */}
                        <div className="flex flex-wrap items-center gap-4">
                            {/* Search */}
                            <div
                                className="flex items-center gap-3 px-4 py-2.5 flex-1 min-w-[280px]"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={18} className="text-(--psj-text-3)" />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder={t.find}
                                    className="bg-transparent text-sm outline-none flex-1 text-(--psj-text-1)"
                                />
                                {search && (
                                    <button
                                        onClick={() => setSearch('')}
                                        className="text-(--psj-text-3) hover:text-(--psj-text-1) transition-colors"
                                    >
                                        <X size={16} />
                                    </button>
                                )}
                            </div>
                        </div>

                        {/* Category Chips Row */}
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

                        {/* Summary Row */}
                        <div className="flex items-center justify-between">
                            <div className="text-[10px] uppercase tracking-[0.15em] font-bold text-(--psj-text-3)">
                                {t.showingResults
                                    .replace('{count}', filteredEntries.length.toString())
                                    .replace('{total}', sortedEntries.length.toString())}
                            </div>
                            {(activeTag !== t.all || search) && (
                                <button
                                    onClick={() => {
                                        setActiveTag(t.all);
                                        setSearch('');
                                    }}
                                    className="text-[11px] uppercase tracking-widest font-bold text-(--psj-blue) underline hover:opacity-80 transition-opacity"
                                >
                                    {t.clearFilters}
                                </button>
                            )}
                        </div>
                    </div>

                    <div className="grid lg:grid-cols-[240px_1fr] gap-16 items-start">
                        {/* ─────── VERSION SIDEBAR ─────── */}
                        <aside className="hidden lg:block sticky top-36 max-h-[calc(100vh-160px)] overflow-y-auto pr-6 space-y-8 scrollbar-hide border-r border-(--psj-border)">
                            <div className="space-y-4">
                                <div className="text-[11px] uppercase tracking-[0.3em] font-extrabold text-(--psj-text-3)">
                                    {t.allVersions}
                                </div>
                                <div className="flex flex-col gap-3">
                                    {filteredEntries.map((entry) => (
                                        <a
                                            key={entry.slug}
                                            href={`#${entry.slug}`}
                                            className="group flex flex-col gap-1 transition-all hover:translate-x-1"
                                        >
                                            <span className="text-sm font-bold text-(--psj-text-1) group-hover:text-(--psj-blue) transition-colors">
                                                {entry.version}
                                            </span>
                                            <span className="text-[10px] font-semibold text-(--psj-text-3) uppercase tracking-widest">
                                                {new Date(entry.date).toLocaleDateString(
                                                    lang === 'ja' ? 'ja-JP' : 'en-US',
                                                    {
                                                        month: 'short',
                                                        day: 'numeric',
                                                        year: 'numeric',
                                                    },
                                                )}
                                            </span>
                                        </a>
                                    ))}
                                </div>
                            </div>
                        </aside>

                        {/* ─────── CHANGELOG LIST ─────── */}
                        <div className="space-y-24 max-w-4xl">
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
                                        <p className="text-sm font-medium text-(--psj-text-2)">{t.noUpdates}</p>
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
                </div>
            </main>
        </div>
    );
}
