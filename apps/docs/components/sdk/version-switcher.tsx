'use client';

import { usePathname, useRouter } from 'next/navigation';
import { useMemo } from 'react';

import { Check, ChevronsUpDown } from 'lucide-react';
import { switchVersion } from 'psjapi/versions';

import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { cn } from '@/lib/cn';

import type { SdkVersion } from 'psjapi';

export interface VersionSwitcherProps {
    versions: SdkVersion[];
    /** Extra class applied to the trigger button. */
    className?: string;
}

export function VersionSwitcher({ versions, className }: VersionSwitcherProps) {
    const pathname = usePathname();
    const router = useRouter();

    const activeId = useMemo(() => {
        const parts = pathname.split('/');
        return parts[3] ?? null;
    }, [pathname]);

    const active = useMemo(
        () => versions.find((v) => v.id === activeId) ?? null,
        [versions, activeId],
    );

    function handleSelect(version: SdkVersion) {
        if (version.id === activeId) return;
        const next = switchVersion(pathname, version.id);
        router.push(next);
    }

    return (
        <Popover>
            <PopoverTrigger
                className={cn(
                    'flex items-center gap-2 rounded-lg px-2.5 py-1.5 text-sm font-medium',
                    'border bg-fd-background text-fd-secondary-foreground',
                    'transition-colors hover:bg-fd-accent hover:text-fd-accent-foreground',
                    'data-[state=open]:bg-fd-accent data-[state=open]:text-fd-accent-foreground',
                    'outline-none ring-fd-ring focus-visible:ring-2',
                    className,
                )}
            >
                <span className="truncate">{active?.label ?? activeId ?? 'Select version'}</span>
                <ChevronsUpDown className="shrink-0 size-3.5 text-fd-muted-foreground" />
            </PopoverTrigger>

            <PopoverContent className="flex flex-col gap-0.5 p-1.5 min-w-40 rounded-xl shadow-md border bg-fd-popover fd-scroll-container">
                {versions.map((v) => {
                    const isActive = v.id === activeId;
                    return (
                        <button
                            key={v.id}
                            type="button"
                            onClick={() => handleSelect(v)}
                            className={cn(
                                'flex items-center gap-2 rounded-lg px-2.5 py-1.5 text-sm text-start w-full',
                                'transition-colors hover:bg-fd-accent hover:text-fd-accent-foreground',
                                isActive && 'bg-fd-accent/60 text-fd-accent-foreground font-medium',
                            )}
                        >
                            <span className="flex-1 truncate">{v.label}</span>
                            <Check
                                className={cn(
                                    'shrink-0 size-3.5 text-fd-primary',
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
