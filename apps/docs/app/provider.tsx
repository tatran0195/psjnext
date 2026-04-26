'use client';

import dynamic from 'next/dynamic';
import type { ReactNode } from 'react';

import { TooltipProvider } from '@radix-ui/react-tooltip';
import { RootProvider } from 'fumadocs-ui/provider/next';

import { localeItems } from '@/lib/i18n';

const SearchDialog = dynamic(() => import('@/components/layouts/search'), {
    ssr: false,
});

export function Provider({ children, locale }: { children: ReactNode; locale: string }) {
    return (
        <RootProvider
            search={{ SearchDialog }}
            i18n={{ locale, locales: localeItems }}
            theme={{ enabled: true, defaultTheme: 'system', enableSystem: true }}
        >
            <TooltipProvider>{children}</TooltipProvider>
        </RootProvider>
    );
}
