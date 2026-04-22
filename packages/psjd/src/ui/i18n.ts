// psjd/src/ui/i18n.ts
// Locale dictionaries for psjd UI strings.
// No external dependency — just a plain object lookup.
//
// Usage:
//   import { ja } from 'psjd/ui';
//   <CallablePage item={item} locale={ja} />

// ─── Type ─────────────────────────────────────────────────────────────────────

export interface PsjdLocale {
    // ── Section headings ───────────────────────────────────────────────────────
    syntax: string;
    parameters: string;
    returns: string;
    seeAlso: string;

    // ── Parameter table headers ────────────────────────────────────────────────
    thName: string;
    thType: string;
    thRequired: string;
    thDefault: string;
    thDescription: string;
    /** Positional column header (#) */
    thPosition: string;

    // ── Parameter badges ───────────────────────────────────────────────────────
    badgeRequired: string;
    badgeDeprecated: string;
    /** Tooltip on the ~ inferred marker */
    badgeInferred: string;
    /** aria-label / title for the required dot when true */
    dotRequired: string;
    /** aria-label / title for the required dot when false */
    dotOptional: string;
    /** aria-label for the em dash "—" (no default) */
    noneAriaLabel: string;

    // ── Empty states ───────────────────────────────────────────────────────────
    noParams: string;
    noParamsFiltered: string;
    returnsVoid: string;

    // ── Deprecated / version metadata ─────────────────────────────────────────
    /** "Deprecated" standalone badge text */
    deprecated: string;
    /** "Deprecated in X.Y.Z" — receives version as interpolation: use {v} */
    deprecatedIn: (version: string) => string;
    /** "Introduced in SDK X.Y.Z" — receives version */
    introducedIn: (version: string) => string;
    /** "removed in X.Y.Z" clause (appended after introducedIn) */
    removedIn: (version: string) => string;

    // ── Version picker ─────────────────────────────────────────────────────────
    sdkVersion: string;

    // ── Ribbon label ───────────────────────────────────────────────────────────
    ribbon: string;

    // ── Param search ───────────────────────────────────────────────────────────
    filterPlaceholder: string;
    filterAriaLabel: string;
    clearFilter: string;
    noMatchingParams: string;
    /** "{n} of {total} parameters" */
    matchCount: (n: number, total: number) => string;

    // ── Code sample panel ──────────────────────────────────────────────────────
    returnsLabel: string;
    copyCode: string;
    copied: string;
    copyToClipboard: string;
    /** Comment line in the Python sample */
    pythonCommentLine: string;
}

// ─── English (default) ────────────────────────────────────────────────────────

export const en: PsjdLocale = {
    syntax: 'Syntax',
    parameters: 'Parameters',
    returns: 'Returns',
    seeAlso: 'See Also',

    thName: 'Name',
    thType: 'Type',
    thRequired: 'Required',
    thDefault: 'Default',
    thDescription: 'Description',
    thPosition: '#',

    badgeRequired: 'required',
    badgeDeprecated: 'deprecated',
    badgeInferred: 'Inferred',
    dotRequired: 'Required',
    dotOptional: 'Optional',
    noneAriaLabel: 'none',

    noParams: 'This callable takes no parameters.',
    noParamsFiltered: 'No parameters match your filter.',
    returnsVoid: 'This callable returns nothing.',

    deprecated: 'Deprecated',
    deprecatedIn: (v) => `Deprecated in ${v}`,
    introducedIn: (v) => `Introduced in SDK ${v}`,
    removedIn: (v) => `, removed in ${v}`,

    sdkVersion: 'SDK Version',
    ribbon: 'Ribbon',

    filterPlaceholder: 'Filter parameters…',
    filterAriaLabel: 'Filter parameters',
    clearFilter: 'Clear filter',
    noMatchingParams: 'No matching parameters',
    matchCount: (n, total) => `${n} of ${total} parameters`,

    returnsLabel: 'Returns',
    copyCode: 'Copy code',
    copied: 'Copied!',
    copyToClipboard: 'Copy to clipboard',
    pythonCommentLine: '# Python scripting via Jupiter PSJ',
};

// ─── Japanese ─────────────────────────────────────────────────────────────────

export const ja: PsjdLocale = {
    syntax: '構文',
    parameters: 'パラメータ',
    returns: '戻り値',
    seeAlso: '関連項目',

    thName: '名前',
    thType: '型',
    thRequired: '必須',
    thDefault: 'デフォルト',
    thDescription: '説明',
    thPosition: '番号',

    badgeRequired: '必須',
    badgeDeprecated: '非推奨',
    badgeInferred: '推定値',
    dotRequired: '必須',
    dotOptional: '任意',
    noneAriaLabel: 'なし',

    noParams: 'このコマンドにパラメータはありません。',
    noParamsFiltered: '条件に一致するパラメータがありません。',
    returnsVoid: 'このコマンドは値を返しません。',

    deprecated: '非推奨',
    deprecatedIn: (v) => `バージョン ${v} より非推奨`,
    introducedIn: (v) => `SDK ${v} で追加`,
    removedIn: (v) => `、バージョン ${v} で削除`,

    sdkVersion: 'SDKバージョン',
    ribbon: 'リボン',

    filterPlaceholder: 'パラメータを絞り込む…',
    filterAriaLabel: 'パラメータを絞り込む',
    clearFilter: '絞り込みをクリア',
    noMatchingParams: '一致するパラメータがありません',
    matchCount: (n, total) => `${total}件中${n}件`,

    returnsLabel: '戻り値',
    copyCode: 'コードをコピー',
    copied: 'コピーしました！',
    copyToClipboard: 'クリップボードにコピー',
    pythonCommentLine: '# Jupiter PSJ を使った Python スクリプト',
};

// ─── Convenience re-export ────────────────────────────────────────────────────

export const locales = { en, ja } as const;
export type LocaleKey = keyof typeof locales;
