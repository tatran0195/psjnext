// lib/layout.shared.tsx
//
// v16:
//   - defineI18nUI() từ 'fumadocs-ui/i18n' vẫn còn
//   - i18nUI.provider(lang) truyền vào RootProvider i18n prop
//   - baseOptions() nhận locale để build localized nav

import { defineI18nUI } from 'fumadocs-ui/i18n';

import { i18n } from '@/lib/i18n';

import type { Translations } from 'fumadocs-ui/i18n';
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

const jaTranslations: Partial<Translations> = {
    search: 'ドキュメントを検索',
    toc: '目次',
    lastUpdate: '最終更新',
    nextPage: '次のページ',
    previousPage: '前のページ',
    chooseLanguage: '言語を選択',
};

export const i18nUI = defineI18nUI(i18n, {
    translations: {
        en: { displayName: 'English' },
        ja: { displayName: '日本語', ...jaTranslations },
    },
});

export function baseOptions(locale: string): BaseLayoutProps {
    return {
        i18n, // required — fumadocs dùng để build language switcher
        nav: {
            title: 'My Docs',
        },
        links: [
            {
                text: locale === 'ja' ? 'ドキュメント' : 'Docs',
                url: '/docs',
                active: 'nested-url',
            },
            {
                text: 'API',
                url: '/api/latest',
                active: 'nested-url',
            },
        ],
    };
}
