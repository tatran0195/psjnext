'use client';

import { usePathname, useRouter } from 'next/navigation';
import { useMemo } from 'react';

import { Check, ChevronsUpDown, Tag } from 'lucide-react';
import { type SdkVersion } from 'psjapi';

import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { cn } from '@/lib/cn';

export interface VersionSwitcherProps {
    versions: SdkVersion[];
    /** Extra class applied to the trigger button. */
    className?: string;
    /** Current active version ID (optional override) */
    activeId?: string;
}

function switchVersion(currentPath: string | null | undefined, newVersionId: string): string {
    if (!currentPath) return '';
    const parts = currentPath.split('/');
    if (parts.length >= 4 && parts[2] === 'sdk') {
        parts[3] = newVersionId;
        return parts.join('/');
    }
    return currentPath;
}

export function VersionSwitcher({ versions, className, activeId: propsActiveId }: VersionSwitcherProps) {
    const pathname = usePathname();
    const router = useRouter();

    const activeId = useMemo(() => {
        if (propsActiveId) return propsActiveId;
        const parts = pathname.split('/');
        return parts[3] ?? null;
    }, [pathname, propsActiveId]);

    const active = useMemo(
        () => versions.find((v) => v.id === activeId) ?? null,
        [versions, activeId],
    );

    const isLatest = active?.isCurrent;

    function handleSelect(version: SdkVersion) {
        if (version.id === activeId) return;
        const next = switchVersion(pathname, version.id);
        router.push(next);
    }

    return (
        <Popover>
            <PopoverTrigger
                className={cn(
                    'flex items-center gap-3 rounded-xl p-2 text-sm font-medium transition-colors group',
                    'hover:bg-fd-accent/50 data-[state=open]:bg-fd-accent/50',
                    'outline-none ring-fd-ring focus-visible:ring-2',
                    className,
                )}
            >
                <div className="flex items-center justify-center rounded-lg size-10 shrink-0 bg-blue-500/10 text-blue-600 dark:bg-blue-500/20 dark:text-blue-400 group-hover:scale-105 transition-transform">
                    <Tag className="size-5" />
                </div>
                <div className="flex flex-col items-start flex-1 min-w-0 overflow-hidden text-start">
                    <span className="font-semibold truncate w-full">
                        {active?.label ?? activeId ?? 'Select version'}
                    </span>
                    <span className="text-[10px] text-fd-muted-foreground truncate w-full uppercase tracking-wider font-bold">
                        {isLatest ? 'Latest version' : 'SDK Version'}
                    </span>
                </div>
                <ChevronsUpDown className="shrink-0 size-4 text-fd-muted-foreground" />
            </PopoverTrigger>

            <PopoverContent
                align="start"
                className="flex flex-col gap-0.5 p-1.5 min-w-48 rounded-xl shadow-xl border bg-fd-popover fd-scroll-container"
            >
                {versions.map((v) => {
                    const isActive = v.id === activeId;
                    return (
                        <button
                            key={v.id}
                            type="button"
                            onClick={() => handleSelect(v)}
                            className={cn(
                                'flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm text-start w-full transition-colors',
                                'hover:bg-fd-accent hover:text-fd-accent-foreground',
                                isActive && 'bg-fd-accent/60 text-fd-accent-foreground font-semibold',
                            )}
                        >
                            <div
                                className={cn(
                                    'flex items-center justify-center rounded-md size-8 shrink-0 bg-blue-500/10 text-blue-600',
                                    isActive && 'bg-blue-500/20',
                                )}
                            >
                                <Tag className="size-4" />
                            </div>
                            <div className="flex flex-col flex-1 min-w-0">
                                <span className="truncate">{v.id}</span>
                                {v.isCurrent && (
                                    <span className="text-[9px] text-fd-muted-foreground uppercase tracking-widest font-bold">
                                        Latest
                                    </span>
                                )}
                            </div>
                            <Check
                                className={cn(
                                    'shrink-0 size-4 text-fd-primary',
                                    !isActive && 'invisible',
                                )}
                            />
                        </button>
                    );
                })}
            </PopoverContent>
        </Popover>
    );
}
