import { getTranslations } from 'next-intl/server';

import { HeroSection } from '@/components/hero-sections';
import { changelog } from '@/lib/source';

import { ChangelogFilterShell } from './_components/changelog-filter-shell';
import { ChangelogSidebar } from './_components/changelog-sidebar';

export default async function Page({ params }: LayoutProps<'/[locale]'>) {
    const { locale } = await params;
    const t = await getTranslations('changelog');

    const entries = changelog
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
            <HeroSection label={t('header.label')} title={t('header.title')} description={t('header.desc')} />
            <div className="psj-container py-10">
                <div className="grid lg:grid-cols-[240px_1fr] gap-16 items-start">
                    <ChangelogSidebar entries={entries} allVersionsLabel={t('sidebar.allVersions')} />
                    <ChangelogFilterShell entries={entries} />
                </div>
            </div>
        </div>
    );
}
