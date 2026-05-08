'use client';
import { type ComponentProps, type ReactNode, useMemo } from 'react';

import { usePathname } from 'fumadocs-core/framework';
import Link from 'fumadocs-core/link';
import { Check, ChevronsUpDown } from 'lucide-react';

import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { isLayoutTabActive, type LayoutTab } from '@/layouts/shared';
import { cn } from '@/lib/cn';

import { useSidebar } from '..';

const IconBox = ({ children, className, ...props }: ComponentProps<'div'>) => (
    <div
        className={cn(
            'flex items-center justify-center [&_svg]:size-[18px] rounded-lg size-8 shrink-0 text-(--tab-color) bg-(--tab-color)/10 border border-(--tab-color)/20 p-1.5',
            className,
        )}
        style={{ '--tab-color': 'var(--color-fd-primary, var(--color-fd-foreground))' } as object}
        {...props}
    >
        {children}
    </div>
);

export function SidebarTabsDropdown({
    options,
    placeholder,
    activeItem,
    ...props
}: {
    placeholder?: ReactNode;
    options: LayoutTab[];
    activeItem?: LayoutTab;
} & ComponentProps<'button'>) {
    const { closeOnRedirect } = useSidebar();
    const pathname = usePathname();

    const selected = useMemo(() => {
        return activeItem ?? options.findLast((item) => isLayoutTabActive(item, pathname));
    }, [activeItem, options, pathname]);

    const onClick = () => {
        closeOnRedirect.current = false;
    };

    const item = selected ? (
        <>
            <IconBox>{selected.icon}</IconBox>
            <div>
                <p className="text-sm font-medium leading-5">{selected.title}</p>
                <p className="text-xs text-fd-muted-foreground leading-4 empty:hidden">
                    {selected.description !== selected.title ? selected.description : null}
                </p>
            </div>
        </>
    ) : (
        placeholder
    );

    return (
        <Popover>
            {item && (
                <PopoverTrigger
                    {...props}
                    className={cn(
                        'flex items-center gap-2 rounded-lg p-2 text-start text-fd-secondary-foreground transition-colors hover:bg-fd-accent/15 data-[state=open]:bg-fd-accent/15 data-[state=open]:text-fd-accent-foreground',
                        props.className,
                    )}
                >
                    {item}
                    <ChevronsUpDown className="shrink-0 ms-auto size-4 text-fd-muted-foreground" />
                </PopoverTrigger>
            )}
            <PopoverContent className="flex flex-col gap-1 w-(--radix-popover-trigger-width) p-1 fd-scroll-container">
                {options.map((item) => {
                    const active = isLayoutTabActive(item, pathname);
                    if (!active && item.unlisted) return;

                    return (
                        <Link
                            key={item.url}
                            href={item.url}
                            onClick={onClick}
                            {...item.props}
                            className={cn(
                                'flex items-center gap-2 rounded-lg p-1.5 hover:bg-fd-accent/15 hover:text-fd-accent-foreground',
                                active && 'bg-fd-accent/15 text-fd-accent-foreground',
                            )}
                        >
                            <IconBox>{item.icon}</IconBox>
                            <div>
                                <p className="text-sm font-medium leading-5">{item.title}</p>
                                <p className="text-[0.8125rem] text-fd-muted-foreground leading-4 empty:hidden">
                                    {item.description !== item.title ? item.description : null}
                                </p>
                            </div>

                            <Check
                                className={cn(
                                    'shrink-0 ms-auto size-3.5 text-fd-primary',
                                    !active && 'invisible',
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
