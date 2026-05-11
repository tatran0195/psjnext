import { Changelog } from '@/components/changelog';
import { changelog } from '@/lib/source';

export default async function ChangelogPage() {
    const sortedEntries = changelog
        .getPages()
        .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
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
        <div>
            <Changelog entries={sortedEntries} />
        </div>
    );
}

export async function generateMetadata() {
    return {
        title: 'Changelog — New Features, Improvements, and Fixes',
        description:
            'Stay up to date with the latest features, improvements, and fixes in PSJ.',
        openGraph: {
            title: 'Changelog — New Features, Improvements, and Fixes',
            description:
                'Stay up to date with the latest features, improvements, and fixes in PSJ.',
            type: 'website',
        },
        twitter: {
            card: 'summary_large_image',
            title: 'Changelog — New Features, Improvements, and Fixes',
            description:
                'Stay up to date with the latest features, improvements, and fixes in PSJ.',
        },
    };
}
