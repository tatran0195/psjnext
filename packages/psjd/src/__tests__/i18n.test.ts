// psjd/src/__tests__/i18n.test.ts
import { describe, expect, it } from 'vitest';

import { en, ja, locales, type PsjdLocale } from '../ui/i18n.js';

// ─── Completeness: every key in `en` must exist in `ja` ──────────────────────

describe('locale completeness', () => {
    const enKeys = Object.keys(en) as Array<keyof PsjdLocale>;

    it('ja has every key that en has', () => {
        for (const key of enKeys) {
            expect(ja, `ja is missing key: "${key}"`).toHaveProperty(key);
        }
    });

    it('en has every key that ja has', () => {
        for (const key of Object.keys(ja) as Array<keyof PsjdLocale>) {
            expect(en, `en is missing key: "${key}"`).toHaveProperty(key);
        }
    });

    it('all string keys are non-empty strings in en', () => {
        for (const key of enKeys) {
            const val = en[key];
            if (typeof val === 'string') {
                expect(val.trim(), `en.${key} must not be empty`).not.toBe('');
            }
        }
    });

    it('all string keys are non-empty strings in ja', () => {
        for (const key of enKeys) {
            const val = ja[key];
            if (typeof val === 'string') {
                expect(val.trim(), `ja.${key} must not be empty`).not.toBe('');
            }
        }
    });

    it('all function keys produce non-empty strings in en', () => {
        for (const key of enKeys) {
            const val = en[key];
            if (typeof val === 'function') {
                // Call with representative sample args
                const result = (val as (...args: string[] | number[]) => string)(
                    '5.1.0' as any,
                    10 as any,
                );
                expect(typeof result, `en.${key}() must return a string`).toBe('string');
                expect(result.trim(), `en.${key}() must return non-empty string`).not.toBe('');
            }
        }
    });

    it('all function keys produce non-empty strings in ja', () => {
        for (const key of enKeys) {
            const val = ja[key];
            if (typeof val === 'function') {
                const result = (val as (...args: string[] | number[]) => string)(
                    '5.1.0' as any,
                    10 as any,
                );
                expect(typeof result, `ja.${key}() must return a string`).toBe('string');
                expect(result.trim(), `ja.${key}() must return non-empty string`).not.toBe('');
            }
        }
    });
});

// ─── en string correctness ────────────────────────────────────────────────────

describe('en locale', () => {
    it('static strings', () => {
        expect(en.syntax).toBe('Syntax');
        expect(en.parameters).toBe('Parameters');
        expect(en.returns).toBe('Returns');
        expect(en.seeAlso).toBe('See Also');
        expect(en.thName).toBe('Name');
        expect(en.thType).toBe('Type');
        expect(en.thRequired).toBe('Required');
        expect(en.thDefault).toBe('Default');
        expect(en.thDescription).toBe('Description');
        expect(en.thPosition).toBe('#');
        expect(en.badgeRequired).toBe('required');
        expect(en.badgeDeprecated).toBe('deprecated');
        expect(en.sdkVersion).toBe('SDK Version');
        expect(en.ribbon).toBe('Ribbon');
        expect(en.returnsLabel).toBe('Returns');
    });

    it('introducedIn interpolates version', () => {
        expect(en.introducedIn('5.1.0')).toBe('Introduced in SDK 5.1.0');
        expect(en.introducedIn('5.0.0')).toContain('5.0.0');
    });

    it('removedIn interpolates version', () => {
        expect(en.removedIn('6.0.0')).toContain('6.0.0');
    });

    it('deprecatedIn interpolates version', () => {
        expect(en.deprecatedIn('5.0.1')).toContain('5.0.1');
        expect(en.deprecatedIn('5.0.1')).toContain('Deprecated');
    });

    it('matchCount interpolates n and total', () => {
        expect(en.matchCount(3, 10)).toBe('3 of 10 parameters');
        expect(en.matchCount(1, 1)).toBe('1 of 1 parameters');
    });

    it('empty state strings', () => {
        expect(en.noParams).toContain('no parameters');
        expect(en.noParamsFiltered).toContain('match');
        expect(en.returnsVoid).toContain('nothing');
    });
});

// ─── ja locale correctness ────────────────────────────────────────────────────

describe('ja locale', () => {
    it('uses Japanese characters for section headings', () => {
        expect(ja.syntax).toBe('構文');
        expect(ja.parameters).toBe('パラメータ');
        expect(ja.returns).toBe('戻り値');
        expect(ja.seeAlso).toBe('関連項目');
    });

    it('table headers are Japanese', () => {
        expect(ja.thName).toBe('名前');
        expect(ja.thType).toBe('型');
        expect(ja.thRequired).toBe('必須');
        expect(ja.thDefault).toBe('デフォルト');
        expect(ja.thDescription).toBe('説明');
    });

    it('introducedIn includes SDK version', () => {
        const result = ja.introducedIn('5.1.0');
        expect(result).toContain('5.1.0');
        expect(result).toContain('SDK');
    });

    it('deprecatedIn includes version', () => {
        const result = ja.deprecatedIn('5.0.1');
        expect(result).toContain('5.0.1');
    });

    it('matchCount produces Japanese format (total before n)', () => {
        const result = ja.matchCount(3, 10);
        // Format: "10件中3件"
        expect(result).toContain('3');
        expect(result).toContain('10');
        // total appears before n in Japanese
        expect(result.indexOf('10')).toBeLessThan(result.indexOf('3'));
    });

    it('filter strings are Japanese', () => {
        expect(ja.filterPlaceholder).toContain('パラメータ');
        expect(ja.clearFilter).toBeTruthy();
        expect(ja.noMatchingParams).toBeTruthy();
    });

    it('copy button strings are Japanese', () => {
        expect(ja.copied).toContain('コピー');
        expect(ja.copyCode).toContain('コピー');
    });

    it('returnsLabel is correct', () => {
        expect(ja.returnsLabel).toBe('戻り値');
    });

    it('pythonCommentLine is Japanese', () => {
        expect(ja.pythonCommentLine).toMatch(/^#/);
        expect(ja.pythonCommentLine).toContain('Jupiter');
    });
});

// ─── locales registry ─────────────────────────────────────────────────────────

describe('locales registry', () => {
    it('contains en and ja', () => {
        expect(locales.en).toBe(en);
        expect(locales.ja).toBe(ja);
    });

    it('can look up by key', () => {
        const key = 'ja' as const;
        expect(locales[key].syntax).toBe('構文');
    });
});

// ─── Custom locale (structural typing check) ──────────────────────────────────

describe('custom locale (structural compatibility)', () => {
    it('accepts a partial override as PsjdLocale when fully implementing the interface', () => {
        // This is a compile-time check expressed as a runtime test:
        // a user can create a fully-typed custom locale.
        const custom: PsjdLocale = {
            ...en,
            syntax: 'Syntaxe', // French override
            parameters: 'Paramètres',
            returns: 'Retour',
            seeAlso: 'Voir aussi',
        };
        expect(custom.syntax).toBe('Syntaxe');
        expect(custom.parameters).toBe('Paramètres');
        // Falls back to en for everything else
        expect(custom.thName).toBe('Name');
    });
});
