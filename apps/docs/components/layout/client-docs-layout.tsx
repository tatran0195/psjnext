'use client';

import { usePathname } from 'next/navigation';

import type { DocsLayoutProps } from '@/layouts/docs';

import { DocsLayout } from '@/layouts/docs';

export function ClientDocsLayout({ tree, children, ...props }: DocsLayoutProps) {
    const pathname = usePathname();

    const isApiRoute = pathname.includes('/docs/api');

    return (
        <DocsLayout tree={tree} tabMode={isApiRoute ? 'sidebar' : undefined} nav={{ enabled: true }} {...props}>
            {children}
        </DocsLayout>
    );
}
