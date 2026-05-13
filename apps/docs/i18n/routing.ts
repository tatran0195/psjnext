import { I18nConfig } from 'fumadocs-core/i18n';
import { defineRouting } from 'next-intl/routing';

export const routing = defineRouting({
    locales: ['en', 'ja'],
    defaultLocale: 'en',
    localePrefix: 'always',
});

export const i18nDocsConfig: I18nConfig = {
    languages: routing.locales as unknown as string[],
    defaultLanguage: routing.defaultLocale,
    hideLocale: 'never',
    parser: 'dir',
    fallbackLanguage: 'en',
};
