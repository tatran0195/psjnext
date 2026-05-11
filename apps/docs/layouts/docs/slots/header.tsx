'use client';

import type { ComponentProps } from 'react';

import { Sidebar as SidebarIcon } from 'lucide-react';

import { GlobalHeader } from '@/components/layout/global-header';
import { cn } from '@/lib/cn';

import { useNotebookLayout } from '../client';

export function Header(props: ComponentProps<'header'>) {
    const { slots, isNavTransparent } = useNotebookLayout();
    const { open } = slots.sidebar?.useSidebar?.() ?? {};
    const SidebarTrigger = slots.sidebar?.trigger;

    return (
        <GlobalHeader
            transparent={isNavTransparent && !open}
            className={cn(
                'sticky [grid-area:header] top-(--fd-docs-row-1) layout:[--fd-header-height:104px]',
                props.className,
            )}
            sidebarTrigger={
                SidebarTrigger ? (
                    <SidebarTrigger className="md:hidden mr-2 -ml-2 flex items-center justify-center rounded-md p-1.5 hover:bg-fd-accent text-fd-muted-foreground">
                        <SidebarIcon className="size-4" />
                    </SidebarTrigger>
                ) : null
            }
        />
    );
}
