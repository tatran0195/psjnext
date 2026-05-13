import { defineI18n } from 'fumadocs-core/i18n';
import { defineI18nUI } from 'fumadocs-ui/i18n';

import { translations, type SupportedLanguage, type TranslationDict } from './i18n-translations';
export { translations };
export type { SupportedLanguage, TranslationDict };
export type TranslationScope = keyof TranslationDict;

/**
 * Scoped dictionary helper to reduce prop drilling and noise.
 * Returns only the specified section of the translation dictionary.
 */
export function getDictionary<S extends TranslationScope>(lang: string, scope: S): TranslationDict[S] {
    const dict = getFullDictionary(lang);
    return dict[scope];
}

/**
 * Helper to get the full dictionary for a language.
 */
export function getFullDictionary(lang: string | SupportedLanguage): TranslationDict {
    const dict = translations[lang as SupportedLanguage] || translations.en;
    return dict as TranslationDict;
}

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
