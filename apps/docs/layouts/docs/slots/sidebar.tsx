'use client';

import * as Base from '@/components/sidebar/base';
import { createLinkItemRenderer } from '@/components/sidebar/link-item';
import {
    createPageTreeRenderer,
    type SidebarPageTreeComponents,
} from '@/components/sidebar/page-tree';
import { buttonVariants } from '@/components/ui/button';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { useTreeContext } from '@/contexts/tree';
import { isLayoutTabActive, type LayoutTab, LinkItem } from '@/layouts/shared';
import { cn } from '@/lib/cn';
import { mergeRefs } from '@/lib/merge-refs';
import { sidebarMatch } from '@/lib/tree-filter';
import { cva } from 'class-variance-authority';
import { usePathname } from 'fumadocs-core/framework';
import Link from 'fumadocs-core/link';
import type * as PageTree from 'fumadocs-core/page-tree';
import { Check, ChevronsUpDown, Languages, Search, SidebarIcon, X } from 'lucide-react';
import {
    type ComponentProps,
    createElement,
    type FC,
    type ReactNode,
    useMemo,
    useRef,
    useState,
} from 'react';
import { useNotebookLayout } from '../client';

const itemVariants = cva(
    'relative flex flex-row items-center gap-2 rounded-lg p-2 text-start text-fd-muted-foreground wrap-anywhere [&_svg]:size-4 [&_svg]:shrink-0',
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

export interface SidebarProps extends ComponentProps<'aside'> {
    components?: Partial<SidebarPageTreeComponents>;
    banner?: ReactNode | FC<ComponentProps<'div'>>;
    footer?: ReactNode | FC<ComponentProps<'div'>>;
    /**
     * Support collapsing the sidebar on desktop mode
     *
     * @defaultValue true
     */
    collapsible?: boolean;
}

export type SidebarProviderProps = Base.SidebarProviderProps;

export const { useSidebar } = Base;

export function SidebarProvider(props: SidebarProviderProps) {
    return <Base.SidebarProvider {...props} />;
}

export function SidebarTrigger(props: ComponentProps<'button'>) {
    return <Base.SidebarTrigger {...props} />;
}

export function SidebarCollapseTrigger(props: ComponentProps<'button'>) {
    return <Base.SidebarCollapseTrigger {...props} />;
}

function SidebarContent({ ref: refProp, className, children, ...props }: ComponentProps<'aside'>) {
    const {
        props: { nav },
    } = useNotebookLayout();
    const navMode = nav?.mode ?? 'auto';
    const ref = useRef<HTMLElement>(null);

    return (
        <Base.SidebarContent>
            {({ collapsed, hovered, ref: asideRef, ...rest }) => (
                <div
                    data-sidebar-placeholder=""
                    className={cn(
                        'sticky z-20 [grid-area:sidebar] pointer-events-none *:pointer-events-auto md:layout:[--fd-sidebar-width:268px] max-md:hidden',
                        navMode === 'auto'
                            ? 'top-(--fd-docs-row-1) h-[calc(var(--fd-docs-height)-var(--fd-docs-row-1))]'
                            : 'top-(--fd-docs-row-2) h-[calc(var(--fd-docs-height)-var(--fd-docs-row-2))]',
                    )}
                >
                    {collapsed && <div className="absolute inset-s-0 inset-y-0 w-4" {...rest} />}
                    <aside
                        id="nd-sidebar"
                        ref={mergeRefs(ref, refProp, asideRef)}
                        data-collapsed={collapsed}
                        data-hovered={collapsed && hovered}
                        className={cn(
                            'absolute flex flex-col w-full inset-s-0 inset-y-0 items-end text-sm duration-250 *:w-(--fd-sidebar-width)',
                            navMode === 'auto' && 'bg-fd-card border-e',
                            collapsed && [
                                'inset-y-2 rounded-xl bg-fd-card transition-transform border w-(--fd-sidebar-width)',
                                hovered
                                    ? 'shadow-lg translate-x-2 rtl:-translate-x-2'
                                    : '-translate-x-(--fd-sidebar-width) rtl:translate-x-full',
                            ],
                            ref.current &&
                                (ref.current.getAttribute('data-collapsed') === 'true') !==
                                    collapsed &&
                                'transition-[width,inset-block,translate,background-color]',
                            className,
                        )}
                        {...props}
                        {...rest}
                    >
                        {children}
                    </aside>
                </div>
            )}
        </Base.SidebarContent>
    );
}

function SidebarDrawer({
    children,
    className,
    ...props
}: ComponentProps<typeof Base.SidebarDrawerContent>) {
    return (
        <>
            <Base.SidebarDrawerOverlay className="fixed z-40 inset-0 backdrop-blur-xs data-[state=open]:animate-fd-fade-in data-[state=closed]:animate-fd-fade-out" />
            <Base.SidebarDrawerContent
                className={cn(
                    'fixed text-[0.9375rem] flex flex-col shadow-lg border-s inset-e-0 inset-y-0 w-[85%] max-w-[380px] z-40 bg-fd-background data-[state=open]:animate-fd-sidebar-in data-[state=closed]:animate-fd-sidebar-out',
                    className,
                )}
                {...props}
            >
                {children}
            </Base.SidebarDrawerContent>
        </>
    );
}

function SidebarFolder(props: ComponentProps<typeof Base.SidebarFolder>) {
    return <Base.SidebarFolder {...props} />;
}

function SidebarSeparator({ className, style, children, ...props }: ComponentProps<'p'>) {
    const depth = Base.useFolderDepth();

    return (
        <Base.SidebarSeparator
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
        </Base.SidebarSeparator>
    );
}

function SidebarItem({
    className,
    style,
    children,
    ...props
}: ComponentProps<typeof Base.SidebarItem>) {
    const depth = Base.useFolderDepth();

    return (
        <Base.SidebarItem
            className={cn(itemVariants({ variant: 'link', highlight: depth >= 1 }), className)}
            style={{
                paddingInlineStart: getItemOffset(depth),
                ...style,
            }}
            {...props}
        >
            {children}
        </Base.SidebarItem>
    );
}

function SidebarFolderTrigger({
    className,
    style,
    ...props
}: ComponentProps<typeof Base.SidebarFolderTrigger>) {
    const { depth, collapsible } = Base.useFolder()!;

    return (
        <Base.SidebarFolderTrigger
            className={cn(
                itemVariants({ variant: collapsible ? 'button' : null }),
                'w-full',
                className,
            )}
            style={{
                paddingInlineStart: getItemOffset(depth - 1),
                ...style,
            }}
            {...props}
        >
            {props.children}
        </Base.SidebarFolderTrigger>
    );
}

function SidebarFolderLink({
    className,
    style,
    ...props
}: ComponentProps<typeof Base.SidebarFolderLink>) {
    const depth = Base.useFolderDepth();

    return (
        <Base.SidebarFolderLink
            className={cn(
                itemVariants({ variant: 'link', highlight: depth > 1 }),
                'w-full',
                className,
            )}
            style={{
                paddingInlineStart: getItemOffset(depth - 1),
                ...style,
            }}
            {...props}
        >
            {props.children}
        </Base.SidebarFolderLink>
    );
}

function SidebarFolderContent({
    className,
    children,
    ...props
}: ComponentProps<typeof Base.SidebarFolderContent>) {
    const depth = Base.useFolderDepth();

    return (
        <Base.SidebarFolderContent
            className={cn(
                'relative',
                depth === 1 &&
                    "before:content-[''] before:absolute before:w-px before:inset-y-1 before:bg-fd-border before:inset-s-2.5",
                className,
            )}
            {...props}
        >
            <div className="flex flex-col gap-0.5 pt-0.5">{children}</div>
        </Base.SidebarFolderContent>
    );
}

const SidebarPageTree = createPageTreeRenderer({
    SidebarFolder,
    SidebarFolderContent,
    SidebarFolderLink,
    SidebarFolderTrigger,
    SidebarItem,
    SidebarSeparator,
});

const SidebarLinkItem = createLinkItemRenderer({
    SidebarFolder,
    SidebarFolderContent,
    SidebarFolderLink,
    SidebarFolderTrigger,
    SidebarItem,
});

export function Sidebar({ banner, footer, components, collapsible = true, ...rest }: SidebarProps) {
    const {
        menuItems,
        slots,
        props: { nav, tabs, tabMode },
    } = useNotebookLayout();
    const navMode = nav?.mode ?? 'auto';
    const iconLinks = menuItems.filter((item) => item.type === 'icon');
    const { nestedTabs, root } = useTreeContext();
    const [filterQuery, setFilterQuery] = useState('');

    const filteredList = useMemo(() => {
        if (!filterQuery) return root.children;

        function filterNodes(nodes: PageTree.Node[]): PageTree.Node[] {
            return nodes
                .map((node) => {
                    const isMatch = sidebarMatch(filterQuery, node.name);
                    if (node.type === 'separator') return isMatch ? node : null;
                    if (node.type === 'folder') {
                        const filtered = filterNodes(node.children);
                        if (filtered.length > 0 || isMatch) {
                            return {
                                ...node,
                                defaultOpen: true,
                                children: isMatch ? node.children : filtered,
                            };
                        }
                        return null;
                    }
                    if (isMatch) {
                        return node;
                    }
                    return null;
                })
                .filter(Boolean) as PageTree.Node[];
        }
        return filterNodes(root.children);
    }, [filterQuery, root.children]);

    function renderHeader(props: ComponentProps<'div'>) {
        if (typeof banner === 'function') return createElement(banner, props);

        return (
            <div
                {...props}
                className={cn('flex flex-col gap-2 p-4 pb-0 empty:hidden', props.className)}
            >
                {props.children}
                {banner}
            </div>
        );
    }

    function renderFooter(props: ComponentProps<'div'>) {
        if (typeof footer === 'function') return createElement(footer, props);

        return (
            <div {...props}>
                {props.children}
                {footer}
            </div>
        );
    }

    const viewport = (
        <Base.SidebarViewport>
            {menuItems
                .filter((item) => item.type !== 'icon')
                .map((item, i, arr) => (
                    <SidebarLinkItem
                        key={i}
                        item={item}
                        className={cn('lg:hidden', i === arr.length - 1 && 'mb-3')}
                    />
                ))}
            <SidebarPageTree {...components} list={filteredList} />
        </Base.SidebarViewport>
    );

    return (
        <>
            <SidebarContent {...rest}>
                {renderHeader({
                    children: (
                        <>
                            {navMode === 'auto' && (
                                <div className="flex justify-between">
                                    {slots.navTitle && (
                                        <slots.navTitle className="inline-flex items-center gap-2.5 font-medium" />
                                    )}
                                    {nav?.children}
                                    {collapsible && (
                                        <SidebarCollapseTrigger
                                            className={cn(
                                                buttonVariants({
                                                    color: 'ghost',
                                                    size: 'icon-sm',
                                                    className:
                                                        'mt-px mb-auto text-fd-muted-foreground',
                                                }),
                                            )}
                                        >
                                            <SidebarIcon />
                                        </SidebarCollapseTrigger>
                                    )}
                                </div>
                            )}

                            {tabs.length > 0 && (
                                <SidebarTabsDropdown
                                    options={tabs}
                                    className={cn(tabMode === 'navbar' && 'lg:hidden')}
                                />
                            )}

                            <SearchInput
                                filterQuery={filterQuery}
                                setFilterQuery={setFilterQuery}
                            />

                            {nestedTabs.map((level, i) => (
                                <SidebarTabsDropdown
                                    key={i}
                                    options={level.tabs}
                                    activeItem={level.active}
                                    className={i < nestedTabs.length - 1 ? '-mb-1' : ''}
                                />
                            ))}
                        </>
                    ),
                })}
                {viewport}
                {renderFooter({
                    className: cn(
                        'hidden flex-row text-fd-muted-foreground items-center border-t px-4 py-2.5',
                        iconLinks.length > 0 && 'max-lg:flex',
                    ),
                    children: iconLinks.map((item, i) => (
                        <LinkItem
                            key={i}
                            item={item}
                            className={cn(
                                buttonVariants({
                                    size: 'icon-sm',
                                    color: 'ghost',
                                    className: 'lg:hidden',
                                }),
                            )}
                            aria-label={item.label}
                        >
                            {item.icon}
                        </LinkItem>
                    )),
                })}
            </SidebarContent>
            <SidebarDrawer {...rest}>
                {renderHeader({
                    children: (
                        <>
                            <SidebarTrigger
                                className={cn(
                                    buttonVariants({
                                        size: 'icon-sm',
                                        color: 'ghost',
                                        className: 'ms-auto text-fd-muted-foreground',
                                    }),
                                )}
                            >
                                <X />
                            </SidebarTrigger>
                            {tabs.length > 0 && <SidebarTabsDropdown options={tabs} />}
                            <SearchInput
                                filterQuery={filterQuery}
                                setFilterQuery={setFilterQuery}
                            />
                            {nestedTabs.map((level, i) => (
                                <SidebarTabsDropdown
                                    key={i}
                                    options={level.tabs}
                                    activeItem={level.active}
                                />
                            ))}
                        </>
                    ),
                })}
                {viewport}
                {renderFooter({
                    className: cn(
                        'hidden flex-row text-fd-muted-foreground items-center border-t p-4 pt-2 justify-end',
                        (slots.languageSelect || slots.themeSwitch) && 'flex',
                        iconLinks.length > 0 && 'max-lg:flex',
                    ),
                    children: (
                        <>
                            {iconLinks.map((item, i) => (
                                <LinkItem
                                    key={i}
                                    item={item}
                                    className={cn(
                                        buttonVariants({
                                            size: 'icon-sm',
                                            color: 'ghost',
                                        }),
                                        'text-fd-muted-foreground lg:hidden',
                                        i === iconLinks.length - 1 && 'me-auto',
                                    )}
                                    aria-label={item.label}
                                >
                                    {item.icon}
                                </LinkItem>
                            ))}
                            {slots.languageSelect && (
                                <slots.languageSelect.root>
                                    <Languages className="size-4.5 text-fd-muted-foreground" />
                                </slots.languageSelect.root>
                            )}
                            {slots.themeSwitch && <slots.themeSwitch />}
                        </>
                    ),
                })}
            </SidebarDrawer>
        </>
    );
}

function SearchInput({
    filterQuery,
    setFilterQuery,
}: {
    filterQuery: string;
    setFilterQuery: (value: string) => void;
}) {
    return (
        <div className="inline-flex items-center gap-2 rounded-lg p-1.5 ps-2 text-sm hover:text-fd-muted-foreground transition-colors focus-within:bg-fd-accent focus-within:text-fd-accent-foreground">
            <Search className="size-4 shrink-0" />
            <input
                type="text"
                value={filterQuery}
                onChange={(e) => setFilterQuery(e.target.value)}
                placeholder="Filter composition..."
                className="w-full min-w-0 bg-transparent outline-none placeholder:text-fd-muted-foreground"
            />
        </div>
    );
}

function SidebarTabsDropdown({
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
            {selected.icon}
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
                            {item.icon}
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
