import type { I18nUIConfig } from 'fumadocs-ui/i18n';

// ─── Default translations (English) ──────────────────────────────────────────

export const defaultTranslations = {
    // Section headings
    syntax: 'Syntax',
    parameters: 'Parameters',
    returns: 'Returns',
    seeAlso: 'See Also',
    examples: 'Examples',

    // Parameter table labels
    paramPosition: 'Pos',
    paramName: 'Parameter',
    paramType: 'Type',
    paramRequired: 'required',
    paramDeprecated: 'deprecated',
    paramDefault: 'Default',

    // Returns
    returnVoid: 'No return value.',

    // Callout levels
    calloutWarn: 'Warning',
    calloutInfo: 'Info',
    calloutDanger: 'Danger',

    // Domain labels
    domainMacro: 'Macro',
    domainCommand: 'PSJ Command',
    domainUtility: 'PSJ Utility',
    domainGui: 'PSJ GUI',

    // Domain sidebar badges
    badgeMacro: 'macro',
    badgeCommand: 'cmd',
    badgeUtility: 'util',
    badgeGui: 'gui',

    // Meta labels
    metaNamespace: 'Namespace',
    metaRibbon: 'Ribbon',
    metaDeprecated: 'Deprecated',
    metaVersionIntroduced: 'Since',

    // Cross-reference card
    linkCardMacro: 'Macro implementation',
    linkCardCommand: 'High-level command',

    // Misc
    noExamples: 'No examples available.',
    exampleLabel: 'Example',
    itemNotFound: 'Item not found',
};

export type PsjAPITranslations = typeof defaultTranslations;

// ─── Built-in locale translations ─────────────────────────────────────────────

export const translations: Partial<Record<string, Partial<PsjAPITranslations>>> = {
    ja: {
        syntax: '構文',
        parameters: 'パラメータ',
        returns: '戻り値',
        seeAlso: '関連項目',
        examples: '例',

        paramPosition: '位置',
        paramName: 'パラメータ名',
        paramType: '型',
        paramRequired: '必須',
        paramDeprecated: '非推奨',
        paramDefault: 'デフォルト',

        returnVoid: '戻り値はありません。',

        calloutWarn: '警告',
        calloutInfo: '情報',
        calloutDanger: '危険',

        domainMacro: 'マクロ',
        domainCommand: 'PSJコマンド',
        domainUtility: 'PSJユーティリティ',
        domainGui: 'PSJ GUI',

        metaNamespace: '名前空間',
        metaRibbon: 'リボン',
        metaDeprecated: '非推奨',
        metaVersionIntroduced: '追加バージョン',

        linkCardMacro: 'マクロ実装',
        linkCardCommand: '高レベルコマンド',

        noExamples: '例はありません。',
        exampleLabel: '例',
        itemNotFound: '項目が見つかりません',
    },
};

// ─── defineI18nPsjAPI ─────────────────────────────────────────────────────────

type DeepMerge<A, B> = Omit<A, keyof B> & B;

function deepmerge<A extends object, B extends Partial<A>>(base: A, override: B): DeepMerge<A, B> {
    return { ...base, ...override } as DeepMerge<A, B>;
}

/**
 * Wraps a fumadocs-ui I18nUIConfig and injects psjapi translations into each
 * locale's `translations.psjapi` key.
 *
 * Built-in translations for 'en' and 'ja' are provided; pass `overrides` to
 * customise any key for any language.
 */
export function defineI18nPsjAPI<Languages extends string>(
    config: I18nUIConfig<Languages>,
    overrides: Partial<Record<NoInfer<Languages>, Partial<PsjAPITranslations>>> = {},
): I18nUIConfig<Languages> {
    return {
        ...config,
        provider(locale = config.defaultLanguage) {
            const out = config.provider(locale);

            // Merge: defaults → built-in locale → caller overrides
            const builtIn = translations[locale as string] ?? {};
            const callerOverride = overrides[locale as Languages] ?? {};
            const merged = deepmerge(deepmerge(defaultTranslations, builtIn), callerOverride);

            out.translations ??= {};
            (out.translations as Record<string, unknown>).psjapi = merged;

            return out;
        },
    };
}

// ─── usePsjTranslations hook (client components) ──────────────────────────────

/**
 * Extract psjapi translations from the fumadocs-ui I18n context.
 * Use inside any client component that needs localised labels.
 *
 * ```tsx
 * 'use client';
 * import { usePsjTranslations } from 'fumadocs-psjapi/i18n';
 *
 * export function ParamLabel() {
 *   const t = usePsjTranslations();
 *   return <span>{t.parameters}</span>;
 * }
 * ```
 */
export function usePsjTranslations(): PsjAPITranslations {
    // Dynamic import to avoid bundling the hook in server-only builds
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const { useI18n } = require('fumadocs-ui/contexts/i18n') as {
        useI18n: () => { translations?: Record<string, unknown> };
    };
    const ctx = useI18n();
    const t = (ctx.translations as Record<string, unknown> | undefined)?.psjapi;
    if (t && typeof t === 'object') return t as PsjAPITranslations;
    return defaultTranslations;
}
