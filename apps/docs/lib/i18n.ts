import { defineI18n } from 'fumadocs-core/i18n';
import { defineI18nUI } from 'fumadocs-ui/i18n';

export const i18n = defineI18n({
    languages: ['en', 'ja'],
    defaultLanguage: 'en',
    parser: 'dir',
    hideLocale: 'never',
    fallbackLanguage: 'en',
});

export const i18nUI = defineI18nUI(i18n, {
    en: {
        displayName: 'English',
    },
    ja: {
        displayName: '日本語',
        search: '検索',
    },
});
