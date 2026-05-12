import { HeroSection } from '@/components/hero-sections';
import { translations } from '@/lib/i18n-translations';
import { changelog } from '@/lib/source';

import PageClient from './page.client';

export default async function Page({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = await params;

    const t = translations[lang as keyof typeof translations]?.changelog || translations.en.changelog;

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

    return (
        <div className="min-h-screen" style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}>
            <HeroSection label={t.platformUpdates} title={t.changelog} description={t.changelogDescription} />

            <div className="psj-container py-10">
                <PageClient lang={lang} entries={sortedEntries} />
            </div>
        </div>
    );
}
