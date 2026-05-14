'use client';

import { AnimatePresence, motion } from 'framer-motion';
import { Search } from 'lucide-react';

import { ChangelogItem, type ChangelogFrontmatter } from './changelog-item';

type Props = {
    entries: ChangelogFrontmatter[];
    noUpdatesLabel: string;
    clearFiltersLabel: string;
    onClearAllAction: () => void;
};

export function ChangelogList({ entries, noUpdatesLabel, clearFiltersLabel, onClearAllAction }: Props) {
    return (
        <div className="space-y-24">
            <AnimatePresence mode="popLayout">
                {entries.length === 0 ? (
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
                        <p className="text-sm font-medium text-(--psj-text-2)">{noUpdatesLabel}</p>
                        <button
                            onClick={onClearAllAction}
                            className="mt-4 text-xs font-bold text-(--psj-blue) underline"
                        >
                            {clearFiltersLabel}
                        </button>
                    </motion.div>
                ) : (
                    entries.map((entry) => <ChangelogItem key={entry.id} entry={entry} />)
                )}
            </AnimatePresence>
        </div>
    );
}
