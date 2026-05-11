'use client';
import { type ComponentProps, createContext, type FC, use } from 'react';

import { useIsScrollTop } from 'fumadocs-ui/utils/use-is-scroll-top';

import { type LinkItemType } from '@/layouts/shared';

import { type DocsLayoutProps } from '.';
import { baseSlots, type BaseSlots, type BaseSlotsProps, type LayoutTab, useLinkItems } from '../shared';
import { Container } from './slots/container';
import { Header } from './slots/header';
import {
    Sidebar,
    SidebarCollapseTrigger,
    SidebarProvider,
    SidebarTrigger,
    useSidebar,
    type SidebarProps,
    type SidebarProviderProps,
} from './slots/sidebar';

export interface DocsSlots extends BaseSlots {
    container: FC<ComponentProps<'div'>>;
    header: FC<ComponentProps<'header'>>;
    sidebar: {
        provider: FC<SidebarProviderProps>;
        root: FC<SidebarProps>;
        trigger: FC<ComponentProps<'button'>>;
        collapseTrigger: FC<ComponentProps<'button'>>;
        useSidebar: () => { collapsed: boolean; open: boolean; setOpen: (V: boolean) => void };
    };
}

const { useProvider } = baseSlots({
    useProps() {
        return useNotebookLayout().props;
    },
});

interface SlotsProps extends BaseSlotsProps<DocsLayoutProps> {
    sidebar: SidebarProps;
    tabMode: NonNullable<DocsLayoutProps['tabMode']>;
    tabs: LayoutTab[];
}

const LayoutContext = createContext<{
    props: SlotsProps;
    isNavTransparent: boolean;
    navItems: LinkItemType[];
    menuItems: LinkItemType[];
    slots: DocsSlots;
} | null>(null);

export function useNotebookLayout() {
    const context = use(LayoutContext);
    if (!context)
        throw new Error(
            'Please use <DocsPage /> (`fumadocs-ui/layouts/notebook/page`) under <DocsLayout /> (`fumadocs-ui/layouts/notebook`).',
        );
    return context;
}

export function LayoutBody(
    props: Omit<DocsLayoutProps, 'tabs'> & {
        tabs: LayoutTab[];
    },
) {
    const {
        nav: { enabled: navEnabled = true, transparentMode: navTransparentMode = 'none' } = {},
        sidebar: { defaultOpenLevel, prefetch, ...sidebarProps } = {},
        slots: defaultSlots,
        tabMode = 'sidebar',
        tabs,
        containerProps,
        children,
    } = props;
    const isTop = useIsScrollTop({ enabled: navTransparentMode === 'top' }) ?? true;
    const isNavTransparent = navTransparentMode === 'top' ? isTop : navTransparentMode === 'always';
    const { baseSlots, baseProps } = useProvider(props);
    const linkItems = useLinkItems(props);
    const slots: DocsSlots = {
        ...baseSlots,
        header: defaultSlots?.header ?? Header,
        container: defaultSlots?.container ?? Container,
        sidebar: defaultSlots?.sidebar ?? {
            provider: SidebarProvider,
            root: Sidebar,
            trigger: SidebarTrigger,
            collapseTrigger: SidebarCollapseTrigger,
            useSidebar,
        },
    };

    return (
        <LayoutContext
            value={{
                props: {
                    tabs,
                    tabMode,
                    sidebar: sidebarProps,
                    ...baseProps,
                },
                isNavTransparent,
                slots,
                ...linkItems,
            }}
        >
            <SidebarProvider defaultOpenLevel={defaultOpenLevel} prefetch={prefetch}>
                <slots.container {...containerProps}>
                    {navEnabled && <slots.header />}
                    <slots.sidebar.root {...sidebarProps} />
                    {children}
                </slots.container>
            </SidebarProvider>
        </LayoutContext>
    );
}
