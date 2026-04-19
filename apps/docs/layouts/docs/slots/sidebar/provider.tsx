'use client';
import {
    createContext,
    type ReactNode,
    type RefObject,
    use,
    useMemo,
    useRef,
    useState,
} from 'react';

import { usePathname } from 'fumadocs-core/framework';
import { useMediaQuery } from 'fumadocs-core/utils/use-media-query';
import { useOnChange } from 'fumadocs-core/utils/use-on-change';

interface SidebarContext {
    open: boolean;
    setOpen: React.Dispatch<React.SetStateAction<boolean>>;
    collapsed: boolean;
    setCollapsed: React.Dispatch<React.SetStateAction<boolean>>;

    /**
     * When set to false, don't close the sidebar when navigate to another page
     */
    closeOnRedirect: RefObject<boolean>;
    defaultOpenLevel: number;
    prefetch?: boolean;
    mode: Mode;
}

export interface SidebarProviderProps {
    /**
     * Open folders by default if their level is lower or equal to a specific level
     * (Starting from 1)
     *
     * @defaultValue 0
     */
    defaultOpenLevel?: number;

    /**
     * Prefetch links, default behaviour depends on your React.js framework.
     */
    prefetch?: boolean;

    children?: ReactNode;
}

export type Mode = 'drawer' | 'full';

export const SidebarContext = createContext<SidebarContext | null>(null);

export const FolderContext = createContext<{
    open: boolean;
    setOpen: React.Dispatch<React.SetStateAction<boolean>>;
    depth: number;
    collapsible: boolean;
} | null>(null);

export function SidebarProvider({
    defaultOpenLevel = 0,
    prefetch,
    children,
}: SidebarProviderProps) {
    const closeOnRedirect = useRef(true);
    const [open, setOpen] = useState(false);
    const [collapsed, setCollapsed] = useState(false);
    const pathname = usePathname();
    const mode: Mode = useMediaQuery('(width < 768px)') ? 'drawer' : 'full';

    useOnChange(pathname, () => {
        if (closeOnRedirect.current) {
            setOpen(false);
        }
        closeOnRedirect.current = true;
    });

    return (
        <SidebarContext
            value={useMemo(
                () => ({
                    open,
                    setOpen,
                    collapsed,
                    setCollapsed,
                    closeOnRedirect,
                    defaultOpenLevel,
                    prefetch,
                    mode,
                }),
                [open, collapsed, defaultOpenLevel, prefetch, mode],
            )}
        >
            {children}
        </SidebarContext>
    );
}

export function useSidebar(): SidebarContext {
    const ctx = use(SidebarContext);
    if (!ctx)
        throw new Error(
            'Missing SidebarContext, make sure you have wrapped the component in <DocsLayout /> and the context is available.',
        );

    return ctx;
}

export function useFolder() {
    return use(FolderContext);
}

export function useFolderDepth() {
    return use(FolderContext)?.depth ?? 0;
}
