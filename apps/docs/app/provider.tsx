'use client';

import dynamic from 'next/dynamic';
import type { ReactNode } from 'react';
import { TooltipProvider } from '@radix-ui/react-tooltip';
import { localeItems } from '@/lib/i18n';
import { SearchProvider } from '@/contexts/search';
import { I18nProvider } from '@/contexts/i18n';
import { ThemeProvider } from 'next-themes';

const SearchDialog = dynamic(() => import('@/components/layouts/search'), {
    ssr: false,
});

export function Provider({ children, locale }: { children: ReactNode; locale: string }) {
    return (
        <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
        >
            <I18nProvider locale={locale} locales={localeItems}>
                <SearchProvider SearchDialog={SearchDialog} preload>
                    <TooltipProvider>{children}</TooltipProvider>
                </SearchProvider>
            </I18nProvider>
        </ThemeProvider>
    );
}
