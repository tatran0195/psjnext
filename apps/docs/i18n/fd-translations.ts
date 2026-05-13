import { Translations } from 'fumadocs-ui/i18n';
import { type Locale } from 'next-intl';

const ja: Partial<Translations> = {
    search: '検索',
    searchNoResult: '検索結果がありません',
    toc: '目次',
    tocNoHeadings: '見出しがありません',
    lastUpdate: '最終更新',
    chooseLanguage: '选择语言',
    nextPage: '下一页',
    previousPage: '上一页',
    chooseTheme: '选择主题',
    editOnGithub: '在 GitHub 上编辑',
};

export const fumadocsUiTranslations: Partial<Record<Locale, Partial<Translations>>> = {
    ja,
};
