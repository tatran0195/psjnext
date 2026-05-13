import { HeroSection } from '@/components/hero-sections';
import { getDictionary } from '@/lib/i18n';
import { changelog } from '@/lib/source';

import PageClient from './page.client';

export default async function Page({ params }: LayoutProps<'/[locale]'>) {
    const { locale } = await params;
    const t = getDictionary(locale, 'changelog');

    const allEntries = changelog
        .getPages(locale)
        .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
        .reverse()
        .filter((entry) => !entry?.data.draft)
        .map((entry) => ({
            id: entry.data.id,
            slug: entry.data.slug,
            date: new Date(entry.data.date).toLocaleDateString(locale === 'ja' ? 'ja-JP' : 'en-US', {
                month: 'short',
                day: 'numeric',
                year: 'numeric',
            }),
            version: entry.data.version,
            title: entry.data.title,
            summary: entry.data.summary,
            tags: entry.data.tags,
            image: entry.data.image,
        }));

    return (
        <div className="min-h-screen" style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}>
            <HeroSection label={t.header.label} title={t.header.title} description={t.header.desc} />

            <div className="psj-container py-10">
                <div className="grid lg:grid-cols-[240px_1fr] gap-16 items-start">
                    {/* ─────── VERSION SIDEBAR (RSC) ─────── */}
                    <aside className="hidden lg:block sticky top-36 max-h-[calc(100vh-160px)] overflow-y-auto pr-6 space-y-8 scrollbar-hide border-r border-(--psj-border)">
                        <div className="space-y-4">
                            <div className="text-[11px] uppercase tracking-[0.3em] font-extrabold text-(--psj-text-3)">
                                {t.sidebar.allVersions}
                            </div>
                            <div className="flex flex-col gap-3">
                                {allEntries.map((entry) => (
                                    <a
                                        key={entry.slug}
                                        href={`#${entry.slug}`}
                                        className="group flex flex-col gap-1 transition-all hover:translate-x-1"
                                    >
                                        <span className="text-sm font-bold text-(--psj-text-1) group-hover:text-(--psj-blue) transition-colors">
                                            {entry.version}
                                        </span>
                                        <span className="text-[10px] font-semibold text-(--psj-text-3) uppercase tracking-widest">
                                            {entry.date}
                                        </span>
                                    </a>
                                ))}
                            </div>
                        </div>
                    </aside>

                    {/* ─────── CLIENT-SIDE FILTERING & LIST ─────── */}
                    <PageClient t={t} entries={allEntries} />
                </div>
            </div>
        </div>
    );
}
