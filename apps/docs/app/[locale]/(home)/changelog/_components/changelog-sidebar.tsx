// _components/changelog-sidebar.tsx  — Server Component (no 'use client')

type Entry = {
    slug: string;
    version: string;
    date: string;
};

type Props = {
    entries: Entry[];
    allVersionsLabel: string;
};

export function ChangelogSidebar({ entries, allVersionsLabel }: Props) {
    return (
        <aside className="hidden lg:block sticky top-36 max-h-[calc(100vh-160px)] overflow-y-auto pr-6 space-y-8 scrollbar-hide border-r border-(--psj-border)">
            <div className="space-y-4">
                <div className="text-[11px] uppercase tracking-[0.3em] font-extrabold text-(--psj-text-3)">
                    {allVersionsLabel}
                </div>
                <div className="flex flex-col gap-3">
                    {entries.map((entry) => (
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
    );
}
