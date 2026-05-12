import { type Dispatch, type SetStateAction, useState } from 'react';

import { Popover, PopoverContent, PopoverTrigger } from 'fumadocs-ui/components/ui/popover';
import { Check, ChevronsUpDown } from 'lucide-react';

import { cn } from '@/lib/cn';

interface ListMenuItem<T> {
    name: string;
    description?: string;
    value?: T;
}

interface ListMenuProps<T> {
    items: ListMenuItem<T>[];
    label: string;
    selected?: T;
    setSelected: Dispatch<SetStateAction<T | undefined>>;
}

export const ListMenu = <T,>({ items, label, selected, setSelected }: ListMenuProps<T>) => {
    const [open, setOpen] = useState(false);

    const selectedItem = items.find((item) => item.value === selected);

    return (
        <Popover open={open} onOpenChange={setOpen}>
            <PopoverTrigger asChild>
                <button
                    type="button"
                    aria-haspopup="listbox"
                    aria-expanded={open}
                    className={cn(
                        'inline-flex items-center gap-2 rounded-md border px-2.5 py-1.5 text-sm',
                        'border-fd-border bg-fd-background text-fd-foreground',
                        'transition-colors hover:bg-fd-accent hover:text-fd-accent-foreground',
                        'focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-fd-ring',
                        open && 'bg-fd-accent',
                    )}
                >
                    <span className="text-fd-muted-foreground text-xs">{label}:</span>
                    <span className="text-xs font-medium">{selectedItem?.name ?? 'All'}</span>
                    <ChevronsUpDown className="size-3 text-fd-muted-foreground/70 shrink-0" />
                </button>
            </PopoverTrigger>

            <PopoverContent
                align="start"
                sideOffset={6}
                className="w-48 p-0 rounded-md border border-fd-border bg-fd-popover shadow-md overflow-hidden"
            >
                <div role="listbox" className="flex flex-col py-1">
                    {items.map((item) => {
                        const isSelected = item.value === selected;

                        return (
                            <button
                                role="option"
                                aria-selected={isSelected}
                                type="button"
                                key={String(item.value)}
                                onClick={() => {
                                    setSelected(item.value);
                                    setOpen(false);
                                }}
                                className={cn(
                                    'flex items-center gap-2 w-full px-3 py-1.5 text-start',
                                    'text-sm transition-colors',
                                    isSelected
                                        ? 'text-fd-primary bg-fd-primary/5'
                                        : 'text-fd-foreground hover:bg-fd-accent hover:text-fd-accent-foreground',
                                )}
                            >
                                <span className="size-3.5 shrink-0 flex items-center justify-center">
                                    {isSelected && <Check className="size-3.5" strokeWidth={2.5} />}
                                </span>
                                <span className="flex flex-col">
                                    <span className="text-xs font-medium">{item.name}</span>
                                    {item.description && (
                                        <span className="text-xs text-fd-muted-foreground mt-0.5">
                                            {item.description}
                                        </span>
                                    )}
                                </span>
                            </button>
                        );
                    })}
                </div>
            </PopoverContent>
        </Popover>
    );
};
