'use client';

import { Fragment, useMemo, type ReactNode } from 'react';
import { usePathname } from 'next/navigation';
import Link from 'next/link';
import { ChevronRight } from 'lucide-react';
import { getBreadcrumbItemsFromPath } from 'fumadocs-core/breadcrumb';
import { useTreeContext, useTreePath } from 'fumadocs-ui/contexts/tree';

import { SiteHeader } from '@/components/layout/site-header';
import { cn } from '@/lib/cn';

export interface GlobalHeaderProps {
    transparent?: boolean;
    sidebarTrigger?: ReactNode;
    className?: string;
}

export function GlobalHeader({ transparent = false, sidebarTrigger, className }: GlobalHeaderProps) {
    const pathname = usePathname();
    const path = useTreePath();
    const { root } = useTreeContext();
    
    // Auto-resolve breadcrumbs via Fumadocs tree
    const breadcrumbItems = useMemo(() => {
        // If we are on landing or showcase, provide hardcoded breadcrumbs to match previous implementation
        if (pathname.includes('/landing')) {
            return [{ name: 'Home', url: '/' }, { name: 'PSJ — Python Scripting for Jupiter' }];
        }
        if (pathname.includes('/showcase')) {
            return [{ name: 'Home', url: '/' }, { name: 'Showcase', url: '/showcase' }, { name: 'CAE Solution Catalog' }];
        }
        
        // Use Fumadocs generic breadcrumbs
        const docsBreadcrumbs = getBreadcrumbItemsFromPath(root, path, {
            includePage: true,
            includeRoot: false,
        });
        
        // Find the top-level section from the path
        const isTutorials = pathname.includes('/docs/tutorials');
        const isApi = pathname.includes('/docs/api');
        
        let sectionName = 'Fundamentals';
        let sectionUrl = '/docs';
        
        if (isTutorials) {
            sectionName = 'Tutorials';
            sectionUrl = '/docs/tutorials';
        } else if (isApi) {
            sectionName = 'API Reference';
            sectionUrl = '/docs/api';
        }

        // We only prepend the section if it's not already the first item in the docsBreadcrumbs
        const hasSection = docsBreadcrumbs.length > 0 && docsBreadcrumbs[0].name === sectionName;
        
        return [
            { name: 'Home', url: '/' },
            ...(hasSection ? [] : [{ name: sectionName, url: sectionUrl }]),
            ...docsBreadcrumbs
        ];
    }, [path, root, pathname]);

    return (
        <header className={cn('flex flex-col z-10 transition-colors', className)}>
            {/* ── Shared top nav ── */}
            <SiteHeader transparent={transparent} />

            {/* ── Breadcrumb Bar ── */}
            <div style={{ background: 'var(--psj-surface-1)', borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container py-2.5 flex items-center gap-2 text-xs overflow-x-auto whitespace-nowrap scrollbar-hide px-4 md:px-6 xl:px-8">
                    {/* Mobile Sidebar Trigger (only passed in Docs layout) */}
                    {sidebarTrigger}

                    {breadcrumbItems.length > 0 ? breadcrumbItems.map((item, i) => {
                        const isLast = i === breadcrumbItems.length - 1;
                        return (
                            <Fragment key={i}>
                                {i !== 0 && <ChevronRight size={11} className="shrink-0" style={{ color: 'var(--psj-text-3)' }} />}
                                {item.url ? (
                                    <Link
                                        href={item.url}
                                        className="transition-colors hover:opacity-80"
                                        style={{ color: isLast ? 'var(--psj-text-2)' : 'var(--psj-text-3)', fontWeight: isLast ? 500 : 400 }}
                                        onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')}
                                        onMouseLeave={e => (e.currentTarget.style.color = isLast ? 'var(--psj-text-2)' : 'var(--psj-text-3)')}
                                    >
                                        {item.name}
                                    </Link>
                                ) : (
                                    <span style={{ color: isLast ? 'var(--psj-text-2)' : 'var(--psj-text-3)', fontWeight: isLast ? 500 : 400 }}>
                                        {item.name}
                                    </span>
                                )}
                            </Fragment>
                        );
                    }) : (
                        <span style={{ color: 'var(--psj-text-3)' }}>Documentation</span>
                    )}
                </div>
            </div>
        </header>
    );
}
