import { buttonVariants } from 'fumadocs-ui/components/ui/button';
import { Popover, PopoverContent, PopoverTrigger } from 'fumadocs-ui/components/ui/popover';
import { ChevronDown } from 'lucide-react';
import { type Dispatch, type SetStateAction, useState } from 'react';

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
    return (
        <Popover open={open} onOpenChange={setOpen}>
            <PopoverTrigger
                className={buttonVariants({
                    size: 'sm',
                    color: 'ghost',
                    className: '-m-1.5 me-2',
                })}
            >
                <span className="text-fd-muted-foreground/80 me-2">{label}</span>
                {items.find((item) => item.value === selected)?.name}
                <ChevronDown className="size-3.5 text-fd-muted-foreground" />
            </PopoverTrigger>
            <PopoverContent className="flex flex-col p-1 gap-1" align="start">
                {items.map((item) => {
                    const isSelected = item.value === selected;

                    return (
                        <button
                            type="button"
                            key={String(item.value)}
                            onClick={() => {
                                setSelected(item.value);
                                setOpen(false);
                            }}
                            className={cn(
                                'rounded-lg text-start px-2 py-1.5',
                                isSelected
                                    ? 'text-fd-primary bg-fd-primary/10'
                                    : 'hover:text-fd-accent-foreground hover:bg-fd-accent',
                            )}
                        >
                            <p className="text-xs font-medium mb-0.5">{item.name}</p>
                            <p className="text-xs opacity-70">{item.description}</p>
                        </button>
                    );
                })}
            </PopoverContent>
        </Popover>
    );
};
