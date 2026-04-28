'use client';

import dynamic from 'next/dynamic';
import type { ReactNode } from 'react';

import { RootProvider } from '@/components/provider/next';
import { TooltipProvider } from '@radix-ui/react-tooltip';

import { i18nUI } from '@/lib/i18n';

const SearchDialog = dynamic(() => import('@/components/layouts/search'), {
    ssr: false,
});

export function Provider({ children, lang }: { children: ReactNode; lang: string }) {
    return (
        <RootProvider
            search={{ SearchDialog }}
            i18n={i18nUI.provider(lang)}
            theme={{ enabled: true, defaultTheme: 'system', enableSystem: true }}
        >
            <TooltipProvider>{children}</TooltipProvider>
        </RootProvider>
    );
}
