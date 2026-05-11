import NextImage from 'next/image';

import { motion } from 'framer-motion';
import Link from 'fumadocs-core/link';
import { ChevronRight, Link2 } from 'lucide-react';
import Markdown from 'markdown-to-jsx';

import type { ChangelogFrontmatter } from '@/lib/utils/markdown';

import { Grid } from '@/components/grid-pattern';
import { translations } from '@/lib/i18n-translations';

interface ChangelogItemProps {
    entry: ChangelogFrontmatter;
    lang?: string;
}

export function ChangelogItem({ entry, lang = 'en' }: ChangelogItemProps) {
    const t =
        translations[lang as keyof typeof translations]?.changelog || translations.en.changelog;
    const dateLocale = lang === 'ja' ? 'ja-JP' : 'en-US';

    const handleCopyLink = (slug: string) => {
        const url = `${window.location.origin}/${lang}/changelog/${slug}`;
        if (navigator.clipboard) {
            navigator.clipboard.writeText(url);
        }
    };

    return (
        <motion.article
            layout
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.98 }}
            className="grid md:grid-cols-[180px_1fr] items-start gap-x-12 gap-y-6 group"
        >
            {/* Date & Version */}
            <div className="md:sticky md:top-36 md:self-start z-10">
                <div className="flex flex-col md:items-end gap-2">
                    {entry.version ? (
                        <div
                            className="inline-block translate-y-[0.08em] px-2.5 py-1 text-[11px] font-black tracking-wider uppercase bg-(--psj-blue) text-white"
                            style={{
                                boxShadow: '4px 4px 0 var(--psj-blue-subtle)',
                            }}
                        >
                            {entry.version}
                        </div>
                    ) : (
                        <div className="text-[10px] text-red-500">{t.missingVersion}</div>
                    )}
                    <time
                        dateTime={entry.date}
                        className="text-xs font-bold text-(--psj-text-3) tracking-widest uppercase"
                    >
                        {new Date(entry.date).toLocaleDateString(dateLocale, {
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
                        <h2 className="psj-h2 text-2xl group-hover:text-(--psj-blue) transition-colors">
                            <Link href={`/changelog/${entry.slug}`}>{entry.title}</Link>
                        </h2>
                        <button
                            onClick={() => handleCopyLink(entry.slug)}
                            className="translate-y-[0.08em] p-2 hover:bg-(--psj-surface-2) rounded-full transition-colors shrink-0"
                            title={t.copyLink}
                        >
                            <Link2 size={16} className="text-(--psj-text-3)" />
                        </button>
                    </div>

                    <div className="text-base leading-relaxed opacity-90 prose prose-sm sm:prose-base dark:prose-invert max-w-none psj-prose text-(--psj-text-2)">
                        <Markdown options={{ wrapper: 'div' }}>{entry.summary}</Markdown>
                    </div>

                    {entry.highlights && entry.highlights.length > 0 && (
                        <div className="mt-4 mb-4">
                            <ul className="space-y-1.5 border-l-2 pl-4 border-(--psj-surface-2)">
                                {entry.highlights.slice(0, 3).map((h, i) => (
                                    <li
                                        key={i}
                                        className="text-sm leading-relaxed prose prose-sm dark:prose-invert max-w-none text-(--psj-text-2)"
                                    >
                                        <Markdown options={{ forceInline: true, wrapper: 'span' }}>
                                            {'• ' + h}
                                        </Markdown>
                                    </li>
                                ))}
                                {entry.highlights.length > 3 && (
                                    <li className="text-xs font-bold uppercase tracking-widest mt-2 text-(--psj-blue)">
                                        + {entry.highlights.length - 3} {t.moreUpdates}
                                    </li>
                                )}
                            </ul>
                        </div>
                    )}

                    <div className="psj-card overflow-hidden">
                        <Link
                            href={`/changelog/${entry.slug}`}
                            className="block overflow-hidden relative group/image"
                        >
                            {entry.image ? (
                                <div className="w-full aspect-[2.5/1] sm:aspect-[3.5/1] transition-transform duration-700 group-hover:scale-105 relative overflow-hidden">
                                    <NextImage
                                        src={entry.image}
                                        alt={entry.title}
                                        fill
                                        className="object-cover"
                                    />
                                </div>
                            ) : (
                                <div
                                    className="w-full aspect-[2.5/1] sm:aspect-[3.5/1] flex flex-col justify-center transition-transform duration-700 group-hover:scale-105 relative overflow-hidden"
                                    style={{
                                        background:
                                            'linear-gradient(135deg, var(--psj-surface-1) 0%, var(--psj-surface-2) 100%)',
                                    }}
                                >
                                    <Grid size={20} />
                                    <div className="absolute right-4 top-4 text-[80px] sm:text-[100px] font-black tracking-tighter opacity-10 leading-none select-none max-w-[50%] text-(--psj-text-1)">
                                        {entry.version || 'PSJ'}
                                    </div>
                                    <div className="relative z-10 px-12 flex flex-col gap-3">
                                        <div className="inline-flex items-center w-fit border rounded-full px-3 py-1 text-xs font-bold uppercase tracking-widest text-(--psj-blue) border-(--psj-border) bg-(--psj-surface-0)">
                                            {t.releaseNote}
                                        </div>
                                        <div className="text-4xl lg:text-5xl font-black tracking-tight text-(--psj-text-1)">
                                            {entry.version || t.defaultUpdateTitle}
                                        </div>
                                        <div className="h-1 w-12 bg-(--psj-blue) mt-2"></div>
                                    </div>
                                </div>
                            )}
                        </Link>
                    </div>

                    <div className="flex flex-wrap items-center justify-between gap-4 pt-4">
                        <div className="flex flex-wrap gap-1.5">
                            {entry.tags?.map((tag) => (
                                <span
                                    key={tag}
                                    className="text-[10px] uppercase tracking-widest font-bold px-2 py-0.5 bg-(--psj-surface-2) text-(--psj-text-2) border border-(--psj-border)"
                                >
                                    {tag}
                                </span>
                            ))}
                        </div>

                        <Link
                            href={`/changelog/${entry.slug}`}
                            className="inline-flex items-center gap-2 text-xs font-extrabold uppercase tracking-widest text-(--psj-blue) group/link"
                        >
                            {t.readFullRelease}
                            <ChevronRight
                                size={14}
                                className="transition-transform group-hover/link:translate-x-1"
                            />
                        </Link>
                    </div>
                </div>
            </div>
        </motion.article>
    );
}
