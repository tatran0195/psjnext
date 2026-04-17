import { defineI18n } from 'fumadocs-core/i18n';

export const i18n = defineI18n({
    languages: ['en', 'ja'],
    defaultLanguage: 'en',
    parser: 'dir',
    hideLocale: 'never',
    fallbackLanguage: 'en',
});

export const localeItems = [
    { name: 'English', locale: 'en' },
    { name: 'Japanese', locale: 'ja' },
];
