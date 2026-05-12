'use client';

import { usePathname } from 'next/navigation';
import { type ComponentProps, createElement, FC, type ReactNode, useMemo, useState } from 'react';

import { searchPath } from 'fumadocs-core/breadcrumb';
import { useTreeContext } from 'fumadocs-ui/contexts/tree';
import { Languages, Search, SidebarIcon, X } from 'lucide-react';

import { buttonVariants } from '@/components/ui/button';
import { DockRail } from '@/layouts/docs/slots/sidebar/dock-rail';
import { SidebarTabsDropdown } from '@/layouts/docs/slots/sidebar/tabs/dropdown';
import { getFirstUrl, LayoutTab, LinkItem } from '@/layouts/shared';
import { VersionSwitcher } from '@/layouts/shared/slots/version-switch';
import { cn } from '@/lib/cn';
import { sidebarMatch } from '@/lib/tree-filter';

import type { SidebarPageTreeComponents } from './page-tree';

import { useNotebookLayout } from '../../client';
import {
    SidebarCollapseTrigger,
    SidebarContent,
    SidebarDrawer,
    SidebarLinkItem,
    SidebarPageTree,
    SidebarTrigger,
    SidebarViewport,
} from './components';

import type * as PageTree from 'fumadocs-core/page-tree';

export interface NestedTab {
    tabs: LayoutTab[];
    active?: LayoutTab;
}

export interface SidebarProps extends ComponentProps<'aside'> {
    components?: Partial<SidebarPageTreeComponents>;
    banner?: ReactNode | FC<ComponentProps<'div'>>;
    footer?: ReactNode | FC<ComponentProps<'div'>>;
    collapsible?: boolean;
    searchable?: boolean;
}

export function Sidebar({ banner, footer, components, collapsible = true, searchable = true, ...rest }: SidebarProps) {
    const {
        menuItems,
        slots,
        props: { nav, tabs, tabMode },
    } = useNotebookLayout();
    const navMode = nav?.mode ?? 'auto';
    const iconLinks = menuItems.filter((item) => item.type === 'icon');
    const { root: baseRoot, full } = useTreeContext();
    const pathname = usePathname();
    const [filterQuery, setFilterQuery] = useState('');

    const path = useMemo(() => {
        return (
            searchPath(full.children, pathname) ??
            (full.fallback ? searchPath(full.fallback.children, pathname) : null) ??
            []
        );
    }, [full, pathname]);

    const nestedTabs = useMemo(() => {
        const result: NestedTab[] = [];
        for (const node of path) {
            if (node.type === 'folder' && (node as PageTree.Folder & { group: boolean }).group) {
                const options = node.children.filter((n) => n.type === 'folder') as PageTree.Folder[];
                if (options.length === 0) continue;

                const nodeTabs = options.map((folder) => {
                    return {
                        title: folder.name,
                        url: getFirstUrl(folder) ?? '',
                        icon: folder.icon,
                        description: folder.description,
                        $folder: folder,
                    } as LayoutTab;
                });

                const active =
                    nodeTabs.find((t) => path.includes(t.$folder as unknown as PageTree.Node)) ?? nodeTabs[0];
                result.push({ tabs: nodeTabs, active });
            }
        }
        return result;
    }, [path]);

    const lastActiveTab = nestedTabs[nestedTabs.length - 1]?.active;
    const root: PageTree.Root | PageTree.Folder = (lastActiveTab?.$folder ??
        path.findLast((item) => item.type === 'folder' && item.root) ??
        baseRoot) as PageTree.Root | PageTree.Folder;

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
            <div {...props} className={cn('flex flex-col gap-2 p-0 pt-2 pb-0 empty:hidden', props.className)}>
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
        <SidebarViewport>
            {menuItems
                .filter((item) => item.type !== 'icon')
                .map((item, i, arr) => (
                    <SidebarLinkItem key={i} item={item} className={cn('lg:hidden', i === arr.length - 1 && 'mb-3')} />
                ))}
            <SidebarPageTree {...components} list={filteredList} />
        </SidebarViewport>
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
                                                    className: 'mt-px mb-auto text-fd-muted-foreground',
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

                            <DockRail
                                items={nestedTabs[1]?.tabs.map((i) => ({
                                    href: i.url,
                                    text: i.title?.toString() || '',
                                    icon: i.icon,
                                }))}
                                activeHref={lastActiveTab?.url}
                            />
                            <VersionSwitcher />

                            {searchable && (
                                <SearchComposition filterQuery={filterQuery} setFilterQuery={setFilterQuery} />
                            )}

                            {/* {nestedTabs.map((level, i) => (
                                <SidebarTabsDropdown
                                    key={i}
                                    options={level.tabs}
                                    activeItem={level.active}
                                    className={i < nestedTabs.length - 1 ? '-mb-1' : ''}
                                />
                            ))} */}
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
                            {nestedTabs.map((level, i) => (
                                <SidebarTabsDropdown key={i} options={level.tabs} activeItem={level.active} />
                            ))}
                            {searchable && (
                                <SearchComposition filterQuery={filterQuery} setFilterQuery={setFilterQuery} />
                            )}{' '}
                        </>
                    ),
                })}
                {viewport}
                {renderFooter({
                    className: cn(
                        'hidden flex-row text-fd-muted-foreground items-center border-t p-0 pt-2 justify-end',
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

function SearchComposition({
    filterQuery,
    setFilterQuery,
    className,
}: {
    filterQuery: string;
    setFilterQuery: (value: string) => void;
    className?: string;
}) {
    return (
        <div
            className={cn(
                'inline-flex items-center gap-2 rounded-none p-1.5 ps-2 text-sm hover:text-fd-muted-foreground transition-colors focus-within:bg-fd-accent focus-within:text-fd-accent-foreground',
                className,
            )}
        >
            <Search className="size-4 shrink-0 text-fd-muted-foreground" />
            <input
                type="text"
                value={filterQuery}
                onChange={(e) => setFilterQuery(e.target.value)}
                placeholder="Filter..."
                className="w-full min-w-0 bg-transparent outline-none placeholder:text-fd-muted-foreground"
            />
        </div>
    );
}

export * from './components';
export * from './provider';

