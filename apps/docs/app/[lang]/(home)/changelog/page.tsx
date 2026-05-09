import { Changelog } from '@/components/changelog';
import { changelog } from '@/lib/source';

export default async function ChangelogPage() {
    const sortedEntries = changelog
        .getPages()
        .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
        .filter((entry) => !entry?.data.draft)
        .map(({ ...entry }) => entry.data);

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
            'Stay up to date with the latest features, improvements, and fixes in LLM Gateway.',
        openGraph: {
            title: 'Changelog — New Features, Improvements, and Fixes',
            description:
                'Stay up to date with the latest features, improvements, and fixes in LLM Gateway.',
            type: 'website',
        },
        twitter: {
            card: 'summary_large_image',
            title: 'Changelog — New Features, Improvements, and Fixes',
            description:
                'Stay up to date with the latest features, improvements, and fixes in LLM Gateway.',
        },
    };
}
