'use client';

import { useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import {
    ChevronRight,
    Link2,
    Search,
    Tag as TagIcon,
    X,
} from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';

import { cn } from '@/lib/cn';
import type { ChangelogFrontmatter } from '@/lib/utils/markdown';

interface ChangelogProps {
    entries?: ChangelogFrontmatter[];
}

export function Changelog({ entries }: ChangelogProps = {}) {
    const changelogEntries = entries ?? [];
    const [search, setSearch] = useState('');
    const [activeTag, setActiveTag] = useState('All');

    // Extract all unique tags
    const allTags = useMemo(() => {
        const tags = new Set<string>();
        changelogEntries.forEach((entry) => {
            entry.tags?.forEach((tag) => tags.add(tag));
        });
        return ['All', ...Array.from(tags).sort()];
    }, [changelogEntries]);

    const filteredEntries = useMemo(() => {
        return changelogEntries.filter((entry) => {
            const matchesSearch =
                entry.title.toLowerCase().includes(search.toLowerCase()) ||
                entry.summary.toLowerCase().includes(search.toLowerCase());
            const matchesTag = activeTag === 'All' || entry.tags?.includes(activeTag);
            return matchesSearch && matchesTag;
        });
    }, [changelogEntries, search, activeTag]);

    const handleCopyLink = (slug: string) => {
        const url = `${window.location.origin}/changelog/${slug}`;
        navigator.clipboard.writeText(url);
    };

    return (
        <div className="min-h-screen" style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}>
            <header className="psj-subpage-hero border-b" style={{ borderColor: 'var(--psj-border)' }}>
                <div className="psj-container py-16 lg:py-20 relative z-10">
                    <div className="max-w-4xl">
                        <div className="flex items-center gap-3 mb-4">
                            <div className="psj-label">Platform Updates</div>
                        </div>
                        <h1 className="psj-h1 mb-6 text-4xl lg:text-5xl" style={{ color: 'var(--psj-text-1)' }}>
                            Product Changelog
                        </h1>
                        <p
                            className="text-lg leading-relaxed max-w-2xl opacity-80"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            Explore the latest features, performance improvements, and technical updates 
                            to the PSJ Engineering Automation Platform.
                        </p>
                    </div>
                </div>
            </header>

            <main className="psj-container py-12 lg:py-20">
                <div className="grid lg:grid-cols-[240px_1fr] gap-16 items-start">
                    {/* ─────── LEFT SIDEBAR (Filters) ─────── */}
                    <aside className="hidden lg:block sticky top-24 space-y-10">
                        <div className="space-y-4">
                            <div className="text-[11px] uppercase tracking-[0.2em] font-bold text-[var(--psj-text-3)]">
                                Search Updates
                            </div>
                            <div
                                className="flex items-center gap-3 px-3 py-2"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={14} style={{ color: 'var(--psj-text-3)' }} />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder="Find..."
                                    className="bg-transparent text-sm outline-none w-full"
                                    style={{ color: 'var(--psj-text-1)' }}
                                />
                                {search && (
                                    <button onClick={() => setSearch('')} style={{ color: 'var(--psj-text-3)' }}>
                                        <X size={12} />
                                    </button>
                                )}
                            </div>
                        </div>

                        <div className="space-y-4">
                            <div className="text-[11px] uppercase tracking-[0.2em] font-bold text-[var(--psj-text-3)] flex items-center gap-2">
                                <TagIcon size={12} /> Categories
                            </div>
                            <div className="flex flex-col gap-1">
                                {allTags.map((tag) => (
                                    <button
                                        key={tag}
                                        onClick={() => setActiveTag(tag)}
                                        className={cn(
                                            "text-left px-3 py-2 text-[13px] transition-all border-l-2",
                                            activeTag === tag 
                                                ? "border-[var(--psj-blue)] text-[var(--psj-blue)] font-bold bg-[var(--psj-blue-subtle)]" 
                                                : "border-transparent text-[var(--psj-text-2)] hover:bg-[var(--psj-surface-1)]"
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
                                <Search size={16} style={{ color: 'var(--psj-text-3)' }} />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder="Search updates..."
                                    className="bg-transparent text-sm outline-none flex-1"
                                    style={{ color: 'var(--psj-text-1)' }}
                                />
                            </div>
                            <div className="flex flex-wrap gap-2">
                                {allTags.map((tag) => (
                                    <button
                                        key={tag}
                                        onClick={() => setActiveTag(tag)}
                                        className={cn(
                                            "px-4 py-1.5 text-xs font-bold transition-all border",
                                            activeTag === tag 
                                                ? "bg-[var(--psj-blue)] border-[var(--psj-blue)] text-white" 
                                                : "bg-[var(--psj-surface-1)] border-[var(--psj-border)] text-[var(--psj-text-2)]"
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
                                    style={{ border: '1px dashed var(--psj-border)', background: 'var(--psj-surface-1)' }}
                                >
                                    <p className="text-sm font-medium" style={{ color: 'var(--psj-text-3)' }}>
                                        No updates match your criteria
                                    </p>
                                    <button 
                                        onClick={() => {setSearch(''); setActiveTag('All');}}
                                        className="mt-4 text-xs font-bold text-[var(--psj-blue)] underline"
                                    >
                                        Clear all filters
                                    </button>
                                </motion.div>
                            ) : (
                                filteredEntries.map((entry) => (
                                    <motion.article
                                        key={entry.id}
                                        layout
                                        initial={{ opacity: 0, y: 30 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0, scale: 0.98 }}
                                        className="grid md:grid-cols-[180px_1fr] gap-x-12 gap-y-6 group"
                                    >
                                        {/* Date & Version */}
                                        <div className="md:sticky md:top-24 md:self-start z-10">
                                            <div className="flex flex-col md:items-end gap-2">
                                                {entry.version ? (
                                                    <div 
                                                        className="inline-block px-2.5 py-1 text-[11px] font-black tracking-wider uppercase bg-[var(--psj-blue)] text-white"
                                                        style={{ boxShadow: '4px 4px 0 var(--psj-blue-subtle)' }}
                                                    >
                                                        {entry.version}
                                                    </div>
                                                ) : (
                                                    <div className="text-[10px] text-red-500">Missing Version</div>
                                                )}
                                                <time
                                                    dateTime={entry.date}
                                                    className="text-xs font-bold text-[var(--psj-text-3)] tracking-widest uppercase"
                                                >
                                                    {new Date(entry.date).toLocaleDateString('en-US', {
                                                        month: 'short',
                                                        day: 'numeric',
                                                        year: 'numeric',
                                                    })}
                                                </time>
                                            </div>
                                        </div>

                                        {/* Content Area */}
                                        <div className="space-y-8">
                                            <div className="space-y-4">
                                                <div className="flex items-start justify-between gap-4">
                                                    <h2 className="psj-h2 text-2xl group-hover:text-[var(--psj-blue)] transition-colors">
                                                        <Link href={`/changelog/${entry.slug}`} prefetch={true}>
                                                            {entry.title}
                                                        </Link>
                                                    </h2>
                                                    <button 
                                                        onClick={() => handleCopyLink(entry.slug)}
                                                        className="mt-1 p-2 hover:bg-[var(--psj-surface-2)] rounded-full transition-colors shrink-0"
                                                        title="Copy direct link"
                                                    >
                                                        <Link2 size={16} style={{ color: 'var(--psj-text-3)' }} />
                                                    </button>
                                                </div>
                                                
                                                <p className="text-base leading-relaxed opacity-90" style={{ color: 'var(--psj-text-2)' }}>
                                                    {entry.summary}
                                                </p>

                                                <div className="psj-card overflow-hidden">
                                                    <Link href={`/changelog/${entry.slug}`} prefetch={true} className="block overflow-hidden">
                                                        <Image
                                                            src={entry.image.src}
                                                            alt={entry.image.alt}
                                                            width={entry.image.width}
                                                            height={entry.image.height}
                                                            className="w-full h-[360px] object-cover transition-transform duration-700 group-hover:scale-105 object-top"
                                                        />
                                                    </Link>
                                                </div>

                                                <div className="flex flex-wrap items-center justify-between gap-4 pt-4">
                                                    {/* Tags displayed above "Read full" link as requested */}
                                                    <div className="flex flex-wrap gap-1.5">
                                                        {entry.tags?.map((tag) => (
                                                            <span
                                                                key={tag}
                                                                className="text-[10px] uppercase tracking-widest font-bold px-2 py-0.5"
                                                                style={{ 
                                                                    background: 'var(--psj-surface-2)', 
                                                                    color: 'var(--psj-text-2)',
                                                                    border: '1px solid var(--psj-border)' 
                                                                }}
                                                            >
                                                                {tag}
                                                            </span>
                                                        ))}
                                                    </div>

                                                    <Link
                                                        href={`/changelog/${entry.slug}`}
                                                        className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-widest text-[var(--psj-blue)] group/link"
                                                        prefetch={true}
                                                    >
                                                        Read full release
                                                        <ChevronRight size={14} className="transition-transform group-hover/link:translate-x-1" />
                                                    </Link>
                                                </div>
                                            </div>
                                        </div>
                                    </motion.article>
                                ))
                            )}
                        </AnimatePresence>
                    </div>
                </div>

            </main>
        </div>
    );
}
