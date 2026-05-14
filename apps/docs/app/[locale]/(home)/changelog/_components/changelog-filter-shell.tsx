'use client';

import { useMemo, useState } from 'react';

import { useTranslations } from 'next-intl';

import { ChangelogFilters } from './changelog-filters';
import { ChangelogFrontmatter } from './changelog-item';
import { ChangelogList } from './changelog-list';

type Props = {
    entries: ChangelogFrontmatter[];
};

export function ChangelogFilterShell({ entries }: Props) {
    const t = useTranslations('changelog');
    const allLabel = t('filters.all');

    const [query, setQuery] = useState('');
    const [activeTag, setActiveTag] = useState<string>(allLabel);

    const allTags = useMemo(() => {
        const tags = new Set<string>();
        entries.forEach((entry) => entry.tags?.forEach((tag) => tags.add(tag)));
        return [allLabel, ...Array.from(tags).sort()];
    }, [entries, allLabel]);

    const filteredEntries = useMemo(
        () =>
            entries.filter((entry) => {
                const q = query.toLowerCase();
                const matchesSearch = entry.title.toLowerCase().includes(q) || entry.summary.toLowerCase().includes(q);
                const matchesTag = activeTag === allLabel || entry.tags?.includes(activeTag);
                return matchesSearch && matchesTag;
            }),
        [entries, query, activeTag, allLabel],
    );

    const hasActiveFilters = activeTag !== allLabel || query !== '';

    function clearAll() {
        setQuery('');
        setActiveTag(allLabel);
    }

    return (
        <div className="flex flex-col gap-12 w-full">
            <ChangelogFilters
                query={query}
                onQueryChangeAction={setQuery}
                allTags={allTags}
                activeTag={activeTag}
                onTagChangeAction={setActiveTag}
                totalCount={entries.length}
                filteredCount={filteredEntries.length}
                hasActiveFilters={hasActiveFilters}
                onClearAllAction={clearAll}
            />
            <ChangelogList
                entries={filteredEntries}
                noUpdatesLabel={t('results.noUpdates')}
                clearFiltersLabel={t('filters.clearFilters')}
                onClearAllAction={clearAll}
            />
        </div>
    );
}
