'use client';

import { usePathname } from 'next/navigation';

import { Code2, Database } from 'lucide-react';

import type { DocsLayoutProps } from '@/layouts/docs';
import type { LayoutTab } from '@/layouts/shared';

import { DocsLayout } from '@/layouts/docs';

export function ClientDocsLayout({ tree, children, ...props }: DocsLayoutProps) {
    const pathname = usePathname();

    // Determine the language from the pathname (e.g., /en/docs/api -> en)
    const segments = pathname.split('/').filter(Boolean);
    const lang = segments[0] === 'ja' ? 'ja' : 'en';

    // Check if we are inside the API Reference section
    const isApiRoute = pathname.includes('/docs/api');

    // Define the custom DockRail tabs specifically for API Reference
    const apiTabs: LayoutTab[] = [
        {
            title: 'API Commands',
            url: `/${lang}/docs/api/api-commands`,
            icon: <Code2 size={16} />,
            description: 'PSJ Command Reference',
        },
        {
            title: 'Data Types',
            url: `/${lang}/docs/api/data-type`,
            icon: <Database size={16} />,
            description: 'Core Data Structures',
        },
    ];

    return (
        <DocsLayout
            tree={tree}
            // Only provide tabs if we are in the API section.
            // When tabs are provided and tabMode is sidebar, Fumadocs renders a DockRail
            // and scopes the sidebar to the active tab's URL.
            tabs={isApiRoute ? apiTabs : false}
            tabMode={isApiRoute ? 'sidebar' : undefined}
            nav={{ enabled: true }} // Header slot is still needed for mobile trigger
            {...props}
        >
            {children}
        </DocsLayout>
    );
}
