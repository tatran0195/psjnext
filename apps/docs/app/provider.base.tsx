'use client';

import { lazy, type ReactNode } from 'react';

import { ThemeProvider, type ThemeProviderProps } from '@teispace/next-themes';
import { DefaultSearchDialogProps } from 'fumadocs-ui/components/dialog/search-default';
import { I18nProvider, I18nProviderProps } from 'fumadocs-ui/contexts/i18n';
import { SearchProvider, SearchProviderProps } from 'fumadocs-ui/contexts/search';

interface SearchOptions extends Omit<SearchProviderProps, 'options' | 'children'> {
    options?: Partial<DefaultSearchDialogProps>;

    /**
     * Enable search functionality
     *
     * @defaultValue `true`
     */
    enabled?: boolean;
}

interface ThemeOptions extends ThemeProviderProps {
    /**
     * Enable `next-themes`
     *
     * @defaultValue true
     */
    enabled?: boolean;
}

export interface RootProviderProps {
    /**
     * @remarks `SearchProviderProps`
     */
    search?: Partial<SearchOptions>;

    /**
     * Customize options for `next-themes`
     */
    theme?: ThemeOptions;

    i18n?: Omit<I18nProviderProps, 'children'>;

    children?: ReactNode;
}

const DefaultSearchDialog = lazy(() => import('fumadocs-ui/components/dialog/search-default'));

export function BaseProvider({ children, theme = {}, search, i18n }: RootProviderProps) {
    let body = children;

    if (search?.enabled !== false)
        body = (
            <SearchProvider SearchDialog={DefaultSearchDialog} {...search}>
                {body}
            </SearchProvider>
        );

    if (theme?.enabled !== false)
        body = (
            <ThemeProvider
                attribute="class"
                defaultTheme="system"
                enableSystem
                disableTransitionOnChange
                {...theme}
            >
                {body}
            </ThemeProvider>
        );

    if (i18n) {
        body = <I18nProvider {...i18n}>{body}</I18nProvider>;
    }

    return <>{body}</>;
}
