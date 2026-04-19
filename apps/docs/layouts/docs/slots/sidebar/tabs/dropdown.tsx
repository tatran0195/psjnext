'use client';
import { type ComponentProps, type ReactNode, useMemo, useState } from 'react';

import { usePathname } from 'fumadocs-core/framework';
import Link from 'fumadocs-core/link';
import { Check, ChevronsUpDown } from 'lucide-react';

import { useSidebar } from '@/components/sidebar/base';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { isLayoutTabActive, type LayoutTab } from '@/layouts/shared';
import { cn } from '@/lib/cn';

export type SidebarTabWithProps = LayoutTab;

export function SidebarTabsDropdown({
    options,
    placeholder,
    ...props
}: {
    placeholder?: ReactNode;
    options: LayoutTab[];
} & ComponentProps<'button'>) {
    const [open, setOpen] = useState(false);
    const { closeOnRedirect } = useSidebar();
    const pathname = usePathname();

    const selected = useMemo(() => {
        return options.findLast((item) => isLayoutTabActive(item, pathname));
    }, [options, pathname]);

    const onClick = () => {
        closeOnRedirect.current = false;
        setOpen(false);
    };

    const item = selected ? (
        <div className="flex items-center gap-3">
            <div className="flex items-center justify-center rounded-md border text-fd-primary bg-fd-primary/10 border-fd-primary/20 p-1 shadow-sm size-8 shrink-0 empty:hidden">
                {selected.icon}
            </div>
            <div className="flex flex-col text-left">
                <p className="text-sm font-medium text-fd-foreground">{selected.title}</p>
                {selected.description && (
                    <p className="text-[13px] font-normal text-fd-muted-foreground hidden md:block">
                        {selected.description}
                    </p>
                )}
            </div>
        </div>
    ) : (
        placeholder
    );

    return (
        <Popover open={open} onOpenChange={setOpen}>
            {item && (
                <PopoverTrigger
                    {...props}
                    className={cn(
                        'flex items-center gap-2 rounded-xl p-2.5 border bg-fd-background text-start text-fd-secondary-foreground transition-all hover:bg-fd-accent hover:shadow-sm data-[state=open]:bg-fd-accent data-[state=open]:shadow-sm outline-none ring-fd-ring focus-visible:ring-2',
                        props.className,
                    )}
                >
                    {item}
                    <ChevronsUpDown className="shrink-0 ms-auto size-4 text-fd-muted-foreground" />
                </PopoverTrigger>
            )}
            <PopoverContent className="flex flex-col gap-1 w-(--radix-popover-trigger-width) p-1.5 rounded-xl shadow-md border bg-fd-popover fd-scroll-container">
                {options.map((item) => {
                    const isActive = selected && item.url === selected.url;
                    if (!isActive && item.unlisted) return;

                    return (
                        <Link
                            key={item.url}
                            href={item.url}
                            onClick={onClick}
                            {...item.props}
                            className={cn(
                                'flex items-center gap-3 rounded-lg p-2 transition-all hover:bg-fd-accent hover:text-fd-accent-foreground',
                                item.props?.className,
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
                                {item.icon}
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
                                    {item.title}
                                </p>
                                {item.description && (
                                    <p className="text-[13px] font-normal text-fd-muted-foreground truncate">
                                        {item.description}
                                    </p>
                                )}
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

export const isTabActive = isLayoutTabActive;
