'use client';

import dynamic from 'next/dynamic';
import { type ReactNode } from 'react';

import { ThemeProvider, type ThemeProviderProps } from '@teispace/next-themes';
import { DefaultSearchDialogProps } from 'fumadocs-ui/components/dialog/search-default';
import { I18nProvider, I18nProviderProps } from 'fumadocs-ui/contexts/i18n';
import { SearchProvider, SearchProviderProps } from 'fumadocs-ui/contexts/search';

interface SearchOptions extends Omit<SearchProviderProps, 'options' | 'children'> {
    options?: Partial<DefaultSearchDialogProps>;
    enabled?: boolean;
    versions?: { version: string; date: string }[];
}

interface ThemeOptions extends ThemeProviderProps {
    enabled?: boolean;
}

export interface RootProviderProps {
    search?: Partial<SearchOptions>;
    theme?: ThemeOptions;
    i18n?: Omit<I18nProviderProps, 'children'>;
    children?: ReactNode;
}

const SearchDialogComponent = dynamic(() => import('@/components/layouts/search'), {
    ssr: false,
});

export function BaseProvider({ children, theme = {}, search, i18n }: RootProviderProps) {
    let body = children;

    if (search?.enabled !== false) {
        const SearchDialog = (props: DefaultSearchDialogProps) => {
            return <SearchDialogComponent {...props} versions={search?.versions ?? []} />;
        };

        body = (
            <SearchProvider SearchDialog={SearchDialog} {...search}>
                {body}
            </SearchProvider>
        );
    }

    if (theme?.enabled !== false)
        body = (
            <ThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange {...theme}>
                {body}
            </ThemeProvider>
        );

    if (i18n) {
        body = <I18nProvider {...i18n}>{body}</I18nProvider>;
    }

    return <>{body}</>;
}
