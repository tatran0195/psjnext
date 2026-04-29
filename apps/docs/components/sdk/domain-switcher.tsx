'use client';

import { usePathname, useRouter } from 'next/navigation';
import { useMemo } from 'react';

import { Check, ChevronsUpDown, Terminal } from 'lucide-react';

import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { cn } from '@/lib/cn';

export interface DomainItem {
    id: string;
    title: string;
    url: string;
}

export interface DomainSwitcherProps {
    domains: DomainItem[];
    className?: string;
}

export function DomainSwitcher({ domains, className }: DomainSwitcherProps) {
    const pathname = usePathname();
    const router = useRouter();

    const activeDomain = useMemo(() => {
        return domains.find((d) => pathname.startsWith(d.url)) ?? null;
    }, [domains, pathname]);

    function handleSelect(domain: DomainItem) {
        if (domain.id === activeDomain?.id) return;
        router.push(domain.url);
    }

    if (domains.length <= 1) return null;

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
                <div className="flex items-center justify-center rounded-lg size-10 shrink-0 bg-indigo-500/10 text-indigo-600 dark:bg-indigo-500/20 dark:text-indigo-400 group-hover:scale-105 transition-transform">
                    <Terminal className="size-5" />
                </div>
                <div className="flex flex-col items-start flex-1 min-w-0 overflow-hidden text-start">
                    <span className="font-semibold truncate w-full">
                        {activeDomain?.title ?? 'Select domain'}
                    </span>
                    <span className="text-[10px] text-fd-muted-foreground truncate w-full uppercase tracking-wider font-bold">
                        SDK Domain
                    </span>
                </div>
                <ChevronsUpDown className="shrink-0 size-4 text-fd-muted-foreground" />
            </PopoverTrigger>

            <PopoverContent
                align="start"
                className="flex flex-col gap-0.5 p-1.5 min-w-48 rounded-xl shadow-xl border bg-fd-popover fd-scroll-container"
            >
                {domains.map((d) => {
                    const isActive = d.id === activeDomain?.id;
                    return (
                        <button
                            key={d.id}
                            type="button"
                            onClick={() => handleSelect(d)}
                            className={cn(
                                'flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm text-start w-full transition-colors',
                                'hover:bg-fd-accent hover:text-fd-accent-foreground',
                                isActive &&
                                    'bg-fd-accent/60 text-fd-accent-foreground font-semibold',
                            )}
                        >
                            <div
                                className={cn(
                                    'flex items-center justify-center rounded-md size-8 shrink-0 bg-indigo-500/10 text-indigo-600',
                                    isActive && 'bg-indigo-500/20',
                                )}
                            >
                                <Terminal className="size-4" />
                            </div>
                            <span className="flex-1 truncate">{d.title}</span>
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
