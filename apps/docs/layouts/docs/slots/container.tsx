'use client';

import { useEffect, useState, type ComponentProps } from 'react';

import { cn } from '@/lib/cn';

import { useNotebookLayout } from '../client';

const PAGE_COLS = 'calc(var(--fd-layout-width,97rem) - var(--fd-sidebar-col) - var(--fd-toc-width))';

const LAYOUT_TEMPLATES = {
    fluid: {
        top: `"header header header"
            "sidebar toc-popover toc-popover"
            "sidebar main toc" 1fr / var(--fd-sidebar-col) 1fr var(--fd-toc-width)`,
        side: `"sidebar header header"
            "sidebar toc-popover toc-popover"
            "sidebar main toc" 1fr / var(--fd-sidebar-col) 1fr var(--fd-toc-width)`,
    },
    container: {
        top: `". header header header ."
"sidebar sidebar toc-popover toc-popover ."
"sidebar sidebar main toc ." 1fr / minmax(min-content, 1fr) var(--fd-sidebar-col) minmax(0, ${PAGE_COLS}) var(--fd-toc-width) minmax(min-content, 1fr)`,
        side: `"sidebar sidebar header header ."
"sidebar sidebar toc-popover toc-popover ."
"sidebar sidebar main toc ." 1fr / minmax(min-content, 1fr) var(--fd-sidebar-col) minmax(0, ${PAGE_COLS}) var(--fd-toc-width) minmax(min-content, 1fr)`,
    },
};

const layout: keyof typeof LAYOUT_TEMPLATES = 'fluid';

export function Container(props: ComponentProps<'div'>) {
    const {
        props: { nav },
        slots,
    } = useNotebookLayout();
    const { collapsed } = slots.sidebar?.useSidebar?.() ?? {};
    const [previousCollapsed, setPreviousCollapsed] = useState(collapsed);
    const isCollapseChanged = previousCollapsed !== collapsed;

    useEffect(() => {
        if (isCollapseChanged) setPreviousCollapsed(collapsed);
    }, [collapsed, isCollapseChanged]);

    return (
        <div
            id="nd-notebook-layout"
            data-sidebar-collapsed={collapsed}
            data-column-changed={isCollapseChanged}
            {...props}
            style={
                {
                    gridTemplate: nav?.mode === 'top' ? LAYOUT_TEMPLATES[layout].top : LAYOUT_TEMPLATES[layout].side,
                    '--fd-docs-row-1': 'var(--fd-banner-height, 0px)',
                    '--fd-docs-row-2': 'calc(var(--fd-docs-row-1) + var(--fd-header-height))',
                    '--fd-docs-row-3': 'calc(var(--fd-docs-row-2) + var(--fd-toc-popover-height))',
                    '--fd-sidebar-col': collapsed ? '0px' : 'var(--fd-sidebar-width)',
                    ...props.style,
                } as object
            }
            className={cn(
                'grid overflow-x-clip min-h-(--fd-docs-height) auto-cols-auto auto-rows-auto [--fd-docs-height:100dvh] [--fd-header-height:0px] [--fd-toc-popover-height:0px] [--fd-sidebar-width:0px] [--fd-toc-width:0px] data-[column-changed=true]:transition-[grid-template-columns]',
                props.className,
            )}
        >
            {props.children}
        </div>
    );
}
