'use client';
import {
    type ComponentProps,
    CSSProperties,
    type PointerEvent,
    type ReactNode,
    type RefObject,
    use,
    useEffect,
    useMemo,
    useRef,
    useState,
} from 'react';

import { Presence } from '@radix-ui/react-presence';
import { cva } from 'class-variance-authority';
import Link, { type LinkProps } from 'fumadocs-core/link';
import { useOnChange } from 'fumadocs-core/utils/use-on-change';
import { ChevronDown, ExternalLink } from 'lucide-react';
import scrollIntoView from 'scroll-into-view-if-needed';

import {
    Collapsible,
    CollapsibleContent,
    type CollapsibleContentProps,
    CollapsibleTrigger,
    type CollapsibleTriggerProps,
} from '@/components/ui/collapsible';
import { ScrollArea, ScrollViewport } from '@/components/ui/scroll-area';
import { cn } from '@/lib/cn';
import { isFolderExpanded, setFolderExpanded } from '@/lib/sidebar-state';

import { useNotebookLayout } from '../../client';
import { createLinkItemRenderer } from './link-item';
import { createPageTreeRenderer } from './page-tree';
import { FolderContext, type Mode, useFolderDepth, useSidebar } from './provider';

const itemVariants = cva(
    'relative flex flex-row items-center gap-2 rounded-none p-2 text-start text-fd-muted-foreground wrap-anywhere [&_svg]:size-4 [&_svg]:shrink-0',
    {
        variants: {
            variant: {
                link: 'transition-colors hover:bg-fd-accent/50 hover:text-fd-accent-foreground/80 hover:transition-none data-[active=true]:bg-fd-primary/10 data-[active=true]:text-fd-primary data-[active=true]:hover:transition-colors',
                button: 'transition-colors hover:bg-fd-accent/50 hover:text-fd-accent-foreground/80 hover:transition-none',
            },
            highlight: {
                true: "data-[active=true]:before:content-[''] data-[active=true]:before:bg-fd-primary data-[active=true]:before:absolute data-[active=true]:before:w-px data-[active=true]:before:inset-y-2.5 data-[active=true]:before:inset-s-2.5",
            },
        },
    },
);

function getItemOffset(depth: number) {
    return `calc(${2 + 3 * depth} * var(--spacing))`;
}

export function SidebarContent({ mode: allowedMode = 'full', children }: { mode?: Mode | true; children: ReactNode }) {
    const { collapsed, mode } = useSidebar();
    const [hover, setHover] = useState(false);
    const ref = useRef<HTMLElement | null>(null);
    const timerRef = useRef(0);
    const {
        props: { nav },
    } = useNotebookLayout();
    const navMode = nav?.mode ?? 'auto';

    useOnChange(collapsed, () => {
        if (collapsed) setHover(false);
    });

    if (allowedMode !== true && allowedMode !== mode) return;

    function shouldIgnoreHover(e: PointerEvent): boolean {
        const element = ref.current;
        if (!element) return true;

        return !collapsed || e.pointerType === 'touch' || element.getAnimations().length > 0;
    }

    return (
        <div
            data-sidebar-placeholder=""
            className={cn(
                'sticky z-20 [grid-area:sidebar] pointer-events-none *:pointer-events-auto md:layout:[--fd-sidebar-width:268px] max-md:hidden',
                navMode === 'auto'
                    ? 'top-(--fd-docs-row-1) h-[calc(var(--fd-docs-height)-var(--fd-docs-row-1))]'
                    : 'top-(--fd-docs-row-2) h-[calc(var(--fd-docs-height)-var(--fd-docs-row-2))]',
            )}
        >
            {collapsed && <div className="absolute inset-s-0 inset-y-0 w-4" />}
            <aside
                id="nd-sidebar"
                ref={ref}
                data-collapsed={collapsed}
                data-hovered={collapsed && hover}
                className={cn(
                    'absolute flex flex-col w-full inset-s-1 inset-y-0 items-end text-sm duration-250 *:w-(--fd-sidebar-width)',
                    navMode === 'auto' && 'bg-fd-card border-e',
                    collapsed && [
                        'inset-y-2 rounded-none bg-fd-card transition-transform border w-(--fd-sidebar-width)',
                        hover
                            ? 'shadow-lg translate-x-2 rtl:-translate-x-2'
                            : '-translate-x-(--fd-sidebar-width) rtl:translate-x-full',
                    ],
                    ref.current &&
                        (ref.current.getAttribute('data-collapsed') === 'true') !== collapsed &&
                        'transition-[width,inset-block,translate,background-color]',
                )}
                onPointerEnter={(e) => {
                    if (shouldIgnoreHover(e)) return;
                    window.clearTimeout(timerRef.current);
                    setHover(true);
                }}
                onPointerLeave={(e) => {
                    if (shouldIgnoreHover(e)) return;
                    window.clearTimeout(timerRef.current);

                    timerRef.current = window.setTimeout(
                        () => setHover(false),
                        // if mouse is leaving the viewport, add a close delay
                        Math.min(e.clientX, document.body.clientWidth - e.clientX) > 100 ? 0 : 500,
                    );
                }}
            >
                {children}
            </aside>
        </div>
    );
}

export function SidebarViewport({
    area,
    viewport,
    children,
}: {
    area?: ComponentProps<typeof ScrollArea>;
    viewport?: ComponentProps<typeof ScrollViewport>;
    children: ReactNode;
}) {
    return (
        <ScrollArea {...area} className={cn('min-h-0 flex-1', area?.className)}>
            <ScrollViewport
                {...viewport}
                className={cn(
                    '*:flex! *:flex-col! *:gap-0.5! p-0 overscroll-contain mask-[linear-gradient(to_bottom,transparent,white_12px,white_calc(100%-12px),transparent)]',
                    viewport?.className,
                )}
            >
                {children}
            </ScrollViewport>
        </ScrollArea>
    );
}

export function SidebarDrawerOverlay(props: ComponentProps<'div'>) {
    const { open, setOpen, mode } = useSidebar();

    if (mode !== 'drawer') return;
    return (
        <Presence present={open}>
            <div data-state={open ? 'open' : 'closed'} onClick={() => setOpen(false)} {...props} />
        </Presence>
    );
}

export function SidebarDrawerContent({ className, children, ...props }: ComponentProps<'aside'>) {
    const { open, mode } = useSidebar();
    const state = open ? 'open' : 'closed';

    if (mode !== 'drawer') return;
    return (
        <Presence present={open}>
            {({ present }) => (
                <aside
                    id="nd-sidebar-mobile"
                    data-state={state}
                    className={cn(!present && 'invisible', className)}
                    {...props}
                >
                    {children}
                </aside>
            )}
        </Presence>
    );
}

export function SidebarDrawer({ children, className, ...props }: ComponentProps<typeof SidebarDrawerContent>) {
    return (
        <>
            <SidebarDrawerOverlay className="fixed z-40 inset-0 backdrop-blur-xs data-[state=open]:animate-fd-fade-in data-[state=closed]:animate-fd-fade-out" />
            <SidebarDrawerContent
                className={cn(
                    'fixed text-[0.9375rem] flex flex-col shadow-lg border-s inset-e-0 inset-y-0 w-[85%] max-w-[380px] z-40 bg-fd-background data-[state=open]:animate-fd-sidebar-in data-[state=closed]:animate-fd-sidebar-out',
                    className,
                )}
                {...props}
            >
                {children}
            </SidebarDrawerContent>
        </>
    );
}

export function SidebarSeparator({ className, style, children, ...props }: ComponentProps<'p'>) {
    const depth = useFolderDepth();
    return (
        <p
            className={cn(
                'inline-flex items-center gap-2 mb-1.5 px-2 mt-6 empty:mb-0 [&_svg]:size-4 [&_svg]:shrink-0',
                depth === 0 && 'first:mt-0',
                className,
            )}
            style={{
                paddingInlineStart: getItemOffset(depth),
                ...style,
            }}
            {...props}
        >
            {children}
        </p>
    );
}

export function SidebarItem({
    icon,
    active = false,
    children,
    className,
    style,
    ...props
}: LinkProps & {
    active?: boolean;
    icon?: ReactNode;
    style?: CSSProperties;
}) {
    const ref = useRef<HTMLAnchorElement>(null);
    const { prefetch } = useSidebar();
    const depth = useFolderDepth();

    useAutoScroll(active, ref);

    return (
        <Link
            ref={ref}
            data-active={active}
            prefetch={prefetch}
            className={cn(itemVariants({ variant: 'link', highlight: /*depth >= 1*/ false }), className)}
            style={{
                paddingInlineStart: getItemOffset(depth),
                ...style,
            }}
            title={children?.toString()}
            {...props}
        >
            {icon ?? (props.external ? <ExternalLink /> : null)}
            {children}
        </Link>
    );
}

export function SidebarFolder({
    id,
    defaultOpen: defaultOpenProp,
    collapsible = true,
    active = false,
    children,
    ...props
}: ComponentProps<'div'> & {
    id?: string;
    active?: boolean;
    defaultOpen?: boolean;
    collapsible?: boolean;
}) {
    const { defaultOpenLevel } = useSidebar();
    const depth = useFolderDepth() + 1;
    const defaultOpen = collapsible === false || active || (defaultOpenProp ?? defaultOpenLevel >= depth);

    const [open, setOpen] = useState(() => {
        if (id && isFolderExpanded(id)) return true;
        return defaultOpen;
    });

    useOnChange(defaultOpen, (v) => {
        if (v) {
            setOpen(true);
            if (id) setFolderExpanded(id, true);
        }
    });

    return (
        <Collapsible
            open={open}
            onOpenChange={(v) => {
                setOpen(v);
                if (id) setFolderExpanded(id, v);
            }}
            disabled={!collapsible}
            {...props}
        >
            <FolderContext value={useMemo(() => ({ open, setOpen, depth, collapsible }), [collapsible, depth, open])}>
                {children}
            </FolderContext>
        </Collapsible>
    );
}

export function SidebarFolderTrigger({ children, ...props }: CollapsibleTriggerProps) {
    const { open, collapsible, depth } = use(FolderContext)!;

    if (collapsible) {
        return (
            <CollapsibleTrigger
                className={cn(itemVariants({ variant: collapsible ? 'button' : null }), 'w-full')}
                style={{
                    paddingInlineStart: getItemOffset(depth - 1),
                }}
                {...props}
            >
                {children}
                <ChevronDown
                    data-icon
                    className={cn('ms-auto transition-transform', !open && '-rotate-90 rtl:rotate-90')}
                />
            </CollapsibleTrigger>
        );
    }

    return <div {...(props as ComponentProps<'div'>)}>{children}</div>;
}

export function SidebarFolderLink({
    children,
    active = false,
    ...props
}: LinkProps & {
    active?: boolean;
}) {
    const ref = useRef<HTMLAnchorElement>(null);
    const { open, setOpen, collapsible, depth } = use(FolderContext)!;
    const { prefetch } = useSidebar();

    useAutoScroll(active, ref);

    return (
        <Link
            ref={ref}
            data-active={active}
            onClick={(e) => {
                if (!collapsible) return;

                if (e.target instanceof Element && e.target.matches('[data-icon], [data-icon] *')) {
                    setOpen(!open);
                    e.preventDefault();
                } else {
                    setOpen(active ? !open : true);
                }
            }}
            prefetch={prefetch}
            className={cn(itemVariants({ variant: 'link', highlight: depth > 1 }), 'w-full')}
            style={{
                paddingInlineStart: getItemOffset(depth - 1),
            }}
            {...props}
        >
            {children}
            {collapsible && (
                <ChevronDown
                    data-icon
                    className={cn('ms-auto transition-transform', !open && '-rotate-90 rtl:rotate-90')}
                />
            )}
        </Link>
    );
}

export function SidebarFolderContent({ children, ...props }: CollapsibleContentProps) {
    const depth = useFolderDepth();

    return (
        <CollapsibleContent
            className={cn(
                'relative',
                depth === 1 &&
                    "before:content-[''] before:absolute before:w-0 before:inset-y-1 before:bg-fd-border before:inset-s-2.5",
                // "before:content-[''] before:absolute before:w-px before:inset-y-1 before:bg-fd-border before:inset-s-2.5",
            )}
            {...props}
        >
            <div className="flex flex-col gap-0.5 pt-0.5">{children}</div>
        </CollapsibleContent>
    );
}

export function SidebarTrigger({ children, ...props }: ComponentProps<'button'>) {
    const { setOpen } = useSidebar();

    return (
        <button aria-label="Open Sidebar" onClick={() => setOpen((prev) => !prev)} {...props}>
            {children}
        </button>
    );
}

export function SidebarCollapseTrigger(props: ComponentProps<'button'>) {
    const { collapsed, setCollapsed } = useSidebar();

    return (
        <button
            type="button"
            aria-label="Collapse Sidebar"
            data-collapsed={collapsed}
            onClick={() => {
                setCollapsed((prev) => !prev);
            }}
            {...props}
        >
            {props.children}
        </button>
    );
}

/**
 * scroll to the element if `active` is true
 */
export function useAutoScroll(active: boolean, ref: RefObject<HTMLElement | null>) {
    const { mode } = useSidebar();

    useEffect(() => {
        if (active && ref.current) {
            scrollIntoView(ref.current, {
                boundary: document.getElementById(mode === 'drawer' ? 'nd-sidebar-mobile' : 'nd-sidebar'),
                scrollMode: 'if-needed',
            });
        }
    }, [active, mode, ref]);
}

export const SidebarPageTree = createPageTreeRenderer({
    SidebarFolder,
    SidebarFolderContent,
    SidebarFolderLink,
    SidebarFolderTrigger,
    SidebarItem,
    SidebarSeparator,
});

export const SidebarLinkItem = createLinkItemRenderer({
    SidebarFolder,
    SidebarFolderContent,
    SidebarFolderLink,
    SidebarFolderTrigger,
    SidebarItem,
});
