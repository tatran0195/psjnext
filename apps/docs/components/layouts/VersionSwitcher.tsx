'use client';

import { useParams } from 'next/navigation';

import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { cn } from '@/lib/cn';
import { ACTIVE_VERSIONS } from '@/lib/versions';
import { Archive, Check, ChevronsUpDown, Link, Tag } from 'lucide-react';
import { useState } from 'react';

export function VersionSwitcher() {
    const [open, setOpen] = useState(false);
    const params = useParams();

    const lang = (params['lang'] as string | undefined) ?? 'en';
    const currentVersion = (params['version'] as string | undefined) ?? ACTIVE_VERSIONS[0];

    const isLatest = ACTIVE_VERSIONS.indexOf(currentVersion as typeof ACTIVE_VERSIONS[number]) === 0;

    const item = lang ? (
        <div className="flex items-center gap-3">
            <div className="flex items-center justify-center rounded-md border text-fd-primary bg-fd-primary/10 border-fd-primary/20 p-1 shadow-sm size-8 shrink-0 empty:hidden">
                <Tag />
            </div>
            <div className="flex flex-col text-left">
                <p className="text-sm font-medium text-fd-foreground">{currentVersion}</p>
                <p className="text-[13px] font-normal text-fd-muted-foreground hidden md:block">
                    {isLatest ? "Latest" : "Previous"}
                </p>
            </div>
        </div>
    ) : (
        "Select version"
    );

    return (
        <Popover open={open} onOpenChange={setOpen}>
            {item && (
                <PopoverTrigger
                    className={cn(
                        'flex items-center gap-2 rounded-xl p-2.5 border bg-fd-background text-start text-fd-secondary-foreground transition-all hover:bg-fd-accent hover:shadow-sm data-[state=open]:bg-fd-accent data-[state=open]:shadow-sm outline-none ring-fd-ring focus-visible:ring-2',
                    )}
                >
                    {item}
                    <ChevronsUpDown className="shrink-0 ms-auto size-4 text-fd-muted-foreground" />
                </PopoverTrigger>
            )}
            <PopoverContent className="flex flex-col gap-1 w-(--radix-popover-trigger-width) p-1.5 rounded-xl shadow-md border bg-fd-popover fd-scroll-container">
                {ACTIVE_VERSIONS.map((version, idx) => {
                    const isActive = currentVersion === version;
                    return (
                        <Link
                            key={version}
                            href={`/${lang}/api/${version}`}
                            className={cn(
                                'flex items-center gap-3 rounded-lg p-2 transition-all hover:bg-fd-accent hover:text-fd-accent-foreground',
                            )}
                        >
                            <div
                                className={cn(
                                    'flex items-center justify-center rounded-md border p-1 shadow-[0_1px_2px_rgba(0,0,0,0.05)] size-8 shrink-0 empty:hidden',
                                    isActive
                                        ? 'bg-fd-primary/10 border-fd-primary/20 text-fd-primary'
                                        : 'bg-fd-background border-fd-border text-fd-muted-foreground',
                                )}
                            >
                                {idx === 0 ? <Tag /> : <Archive />}
                            </div>
                            <div className="flex flex-col text-left min-w-0">
                                <p
                                    className={cn(
                                        'text-sm font-medium leading-tight truncate',
                                        isActive
                                            ? 'text-fd-foreground'
                                            : 'text-fd-muted-foreground',
                                    )}
                                >
                                    {"adasdasdas"}
                                </p>
                                <p className="text-[13px] font-normal text-fd-muted-foreground truncate">
                                    {idx === 0 ? 'Latest' : 'Previous'}
                                </p>
                            </div>

                            <Check
                                className={cn(
                                    'shrink-0 ms-auto size-4',
                                    isActive ? 'text-emerald-500' : 'invisible',
                                )}
                            />
                        </Link>
                    );
                })}
            </PopoverContent>
        </Popover>
    );
}
