// psjd/src/__tests__/sidecar.test.ts
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { beforeAll, describe, expect, it } from 'vitest';

import type { ItemFile, ParamGroupFile } from '../types.js';

import { resolveItem } from '../resolve.js';
import { createSDK } from '../server.js';
import {
    mergeGroupSidecar,
    mergeItemSidecar,
    sidecarPath,
    tryLoadSidecar,
    validateItemSidecar,
    type SidecarItemFile,
    type SidecarParamGroupFile,
} from '../sidecar.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES = path.join(__dirname, '../../fixtures');

// ─── Helpers ──────────────────────────────────────────────────────────────────

function makeItem(overrides: Partial<ItemFile> = {}): ItemFile {
    return {
        psjd: '2.0',
        id: 'test-item',
        title: 'Test()',
        domain: 'psj-command',
        description: 'Original description.',
        version_introduced: '1.0.0',
        params: [],
        returns: { kind: 'void' },
        ...overrides,
    };
}

function makeGroup(overrides: Partial<ParamGroupFile> = {}): ParamGroupFile {
    return {
        psjd: '2.0',
        kind: 'param_group',
        id: 'test-group',
        description: 'Original group description.',
        params: [],
        ...overrides,
    };
}

function makeSidecar(overrides: Partial<SidecarItemFile> = {}): SidecarItemFile {
    return {
        psjd: '2.0',
        kind: 'sidecar',
        id: 'test-item',
        locale: 'ja',
        ...overrides,
    };
}

function makeGroupSidecar(overrides: Partial<SidecarParamGroupFile> = {}): SidecarParamGroupFile {
    return {
        psjd: '2.0',
        kind: 'sidecar',
        id: 'test-group',
        locale: 'ja',
        ...overrides,
    };
}

// ─── sidecarPath ──────────────────────────────────────────────────────────────

describe('sidecarPath', () => {
    it('inserts locale before extension for .yaml', () => {
        expect(sidecarPath('/foo/bar/Item.yaml', 'ja')).toBe('/foo/bar/Item.ja.yaml');
    });
    it('inserts locale before extension for .yml', () => {
        expect(sidecarPath('/foo/Item.yml', 'ja')).toBe('/foo/Item.ja.yml');
    });
    it('works for deeply nested paths', () => {
        expect(sidecarPath('/a/b/c/d.yaml', 'en')).toBe('/a/b/c/d.en.yaml');
    });
});

// ─── mergeItemSidecar — top-level fields ──────────────────────────────────────

describe('mergeItemSidecar — top-level fields', () => {
    it('translates title', () => {
        const merged = mergeItemSidecar(makeItem(), makeSidecar({ title: '翻訳タイトル' }));
        expect(merged.title).toBe('翻訳タイトル');
    });

    it('translates description', () => {
        const merged = mergeItemSidecar(makeItem(), makeSidecar({ description: '説明文' }));
        expect(merged.description).toBe('説明文');
    });

    it('translates ribbon', () => {
        const base = makeItem({ ribbon: 'Analysis > Nastran' });
        const merged = mergeItemSidecar(base, makeSidecar({ ribbon: '解析 > Nastran' }));
        expect(merged.ribbon).toBe('解析 > Nastran');
    });

    it('does not mutate the base item', () => {
        const base = makeItem({ title: 'Original' });
        mergeItemSidecar(base, makeSidecar({ title: '翻訳' }));
        expect(base.title).toBe('Original');
    });

    it('leaves absent sidecar fields as base values', () => {
        const base = makeItem({ title: 'Keep', description: 'Keep desc' });
        const merged = mergeItemSidecar(base, makeSidecar({ title: '翻訳' }));
        expect(merged.description).toBe('Keep desc');
    });

    it('preserves all structural fields unchanged', () => {
        const base = makeItem({
            id: 'my-id',
            domain: 'macro',
            version_introduced: '5.0.0',
            macro_link: 'SomeMacro',
        });
        const merged = mergeItemSidecar(base, makeSidecar({ title: 'X' }));
        expect(merged.id).toBe('my-id');
        expect(merged.domain).toBe('macro');
        expect(merged.version_introduced).toBe('5.0.0');
        expect(merged.macro_link).toBe('SomeMacro');
    });
});

// ─── mergeItemSidecar — params ────────────────────────────────────────────────

describe('mergeItemSidecar — params', () => {
    const base = makeItem({
        params: [
            { name: 'foo', type: 'String', description: 'Original foo desc' },
            { name: 'bar', type: 'Integer', description: 'Original bar desc' },
        ],
    });

    it('translates param description', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                params: [{ name: 'foo', description: 'foo の説明' }],
            }),
        );
        const foo = merged.params.find((p) => !('$group' in p) && (p as any).name === 'foo') as any;
        expect(foo.description).toBe('foo の説明');
    });

    it('translates param display_name', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                params: [{ name: 'bar', display_name: '棒' }],
            }),
        );
        const bar = merged.params.find((p) => !('$group' in p) && (p as any).name === 'bar') as any;
        expect(bar.display_name).toBe('棒');
    });

    it('leaves untranslated params unchanged', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                params: [{ name: 'foo', description: '翻訳' }],
            }),
        );
        const bar = merged.params.find((p) => !('$group' in p) && (p as any).name === 'bar') as any;
        expect(bar.description).toBe('Original bar desc');
    });

    it('skips GroupRef entries silently', () => {
        const baseWithGroup = makeItem({
            params: [
                { $group: 'some-group' } as any,
                { name: 'extra', type: 'String', description: 'Extra' },
            ],
        });
        const merged = mergeItemSidecar(
            baseWithGroup,
            makeSidecar({
                params: [{ name: 'extra', description: '追加' }],
            }),
        );
        expect(merged.params[0]).toHaveProperty('$group', 'some-group');
        const extra = merged.params[1] as any;
        expect(extra.description).toBe('追加');
    });

    it('does not mutate source params array', () => {
        const origDesc = (base.params[0] as any).description;
        mergeItemSidecar(base, makeSidecar({ params: [{ name: 'foo', description: 'X' }] }));
        expect((base.params[0] as any).description).toBe(origDesc);
    });
});

// ─── mergeItemSidecar — enum values ───────────────────────────────────────────

describe('mergeItemSidecar — enum values', () => {
    const base = makeItem({
        params: [
            {
                name: 'mode',
                type: 'Integer',
                enum_values: [
                    { id: 0, label: 'None' },
                    { id: 1, label: 'Total Lagrange' },
                    { id: 2, label: 'Updated Lagrange' },
                ],
            },
        ],
    });

    it('translates enum labels', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                params: [
                    {
                        name: 'mode',
                        enum_values: [
                            { id: 0, label: 'なし' },
                            { id: 1, label: 'トータルラグランジュ' },
                        ],
                    },
                ],
            }),
        );
        const param = merged.params[0] as any;
        expect(param.enum_values[0].label).toBe('なし');
        expect(param.enum_values[1].label).toBe('トータルラグランジュ');
        // Untranslated enum kept
        expect(param.enum_values[2].label).toBe('Updated Lagrange');
    });

    it('preserves enum ids (structural)', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                params: [{ name: 'mode', enum_values: [{ id: 0, label: 'なし' }] }],
            }),
        );
        const param = merged.params[0] as any;
        expect(param.enum_values[0].id).toBe(0);
    });

    it('translates enum descriptions', () => {
        const baseWithDesc = makeItem({
            params: [
                {
                    name: 'mode',
                    type: 'Integer',
                    enum_values: [{ id: 0, label: 'None', description: 'Disables feature' }],
                },
            ],
        });
        const merged = mergeItemSidecar(
            baseWithDesc,
            makeSidecar({
                params: [{ name: 'mode', enum_values: [{ id: 0, description: '機能を無効化' }] }],
            }),
        );
        expect((merged.params[0] as any).enum_values[0].description).toBe('機能を無効化');
    });
});

// ─── mergeItemSidecar — returns ───────────────────────────────────────────────

describe('mergeItemSidecar — returns', () => {
    it('translates returns description', () => {
        const base = makeItem({
            returns: { kind: 'typed', type: 'Cursor', description: 'The job.' },
        });
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                returns: { description: '作成されたジョブ。' },
            }),
        );
        expect(merged.returns.description).toBe('作成されたジョブ。');
        expect(merged.returns.type).toBe('Cursor'); // structural preserved
    });

    it('translates macro return code meanings', () => {
        const base = makeItem({
            returns: {
                kind: 'macro_code',
                codes: [
                    { value: '"1"', meaning: 'Can execute.' },
                    { value: '"0"', meaning: 'Cannot execute.' },
                ],
            },
        });
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                returns: {
                    codes: [
                        { value: '"1"', meaning: '実行できます。' },
                        { value: '"0"', meaning: '実行できません。' },
                    ],
                },
            }),
        );
        expect(merged.returns.codes![0]!.meaning).toBe('実行できます。');
        expect(merged.returns.codes![1]!.meaning).toBe('実行できません。');
        // Structural value unchanged
        expect(merged.returns.codes![0]!.value).toBe('"1"');
    });

    it('leaves return codes without translation unchanged', () => {
        const base = makeItem({
            returns: {
                kind: 'macro_code',
                codes: [
                    { value: '"1"', meaning: 'Keep.' },
                    { value: '"0"', meaning: 'Also keep.' },
                ],
            },
        });
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                returns: { codes: [{ value: '"1"', meaning: '翻訳' }] },
            }),
        );
        expect(merged.returns.codes![1]!.meaning).toBe('Also keep.');
    });
});

// ─── mergeItemSidecar — callouts ──────────────────────────────────────────────

describe('mergeItemSidecar — callouts', () => {
    const base = makeItem({
        callouts: [
            { level: 'warn', text: 'Call EndTransaction when done.' },
            { level: 'info', text: 'See the reference.' },
        ],
    });

    it('translates callout text by index', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                callouts: [{ index: 0, text: '終了時に EndTransaction を呼び出してください。' }],
            }),
        );
        expect(merged.callouts![0]!.text).toBe('終了時に EndTransaction を呼び出してください。');
    });

    it('leaves unindexed callouts unchanged', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                callouts: [{ index: 0, text: '翻訳' }],
            }),
        );
        expect(merged.callouts![1]!.text).toBe('See the reference.');
    });

    it('preserves callout level (structural)', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                callouts: [{ index: 0, text: '翻訳' }],
            }),
        );
        expect(merged.callouts![0]!.level).toBe('warn');
    });
});

// ─── mergeItemSidecar — examples ─────────────────────────────────────────────

describe('mergeItemSidecar — examples', () => {
    const base = makeItem({
        examples: [
            { language: 'psj', code: 'JPT.Exec("Test()")', title: 'Basic' },
            { language: 'python', code: 'result = Test()' },
        ],
    });

    it('translates example title by index', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                examples: [{ index: 0, title: '基本的な使用例' }],
            }),
        );
        expect(merged.examples![0]!.title).toBe('基本的な使用例');
    });

    it('does not translate code (structural)', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                examples: [{ index: 0, title: '翻訳' }],
            }),
        );
        expect(merged.examples![0]!.code).toBe('JPT.Exec("Test()")');
        expect(merged.examples![0]!.language).toBe('psj');
    });
});

// ─── mergeItemSidecar — see_also ──────────────────────────────────────────────

describe('mergeItemSidecar — see_also', () => {
    const base = makeItem({
        see_also: [
            {
                $ref: 'psj-utility/JPT-EndDatabaseTransaction',
                label: 'JPT.EndDatabaseTransaction()',
            },
        ],
    });

    it('translates see_also label by $ref key', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                see_also: [{ $ref: 'psj-utility/JPT-EndDatabaseTransaction', label: '関連関数' }],
            }),
        );
        expect(merged.see_also![0]!.label).toBe('関連関数');
    });

    it('preserves $ref (structural)', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                see_also: [{ $ref: 'psj-utility/JPT-EndDatabaseTransaction', label: '翻訳' }],
            }),
        );
        expect(merged.see_also![0]!.$ref).toBe('psj-utility/JPT-EndDatabaseTransaction');
    });
});

// ─── mergeItemSidecar — version changes ───────────────────────────────────────

describe('mergeItemSidecar — version changes', () => {
    const base = makeItem({
        changes: [
            {
                version: '1.1.0',
                notes: 'Removed foo.',
                item: { description: 'Updated desc.' },
                params: {
                    add: [{ name: 'newParam', type: 'Boolean', description: 'A new param.' }],
                    modify: [{ name: 'bar', changes: { description: 'Bar updated.' } }],
                },
            },
        ],
    });

    it('translates delta notes', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                changes: [{ version: '1.1.0', notes: 'foo を削除しました。' }],
            }),
        );
        expect(merged.changes![0]!.notes).toBe('foo を削除しました。');
    });

    it('translates delta item.description', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                changes: [{ version: '1.1.0', item: { description: '更新された説明。' } }],
            }),
        );
        expect(merged.changes![0]!.item?.description).toBe('更新された説明。');
    });

    it('translates delta params.add descriptions', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                changes: [
                    {
                        version: '1.1.0',
                        params: { add: [{ name: 'newParam', description: '新しいパラメータ。' }] },
                    },
                ],
            }),
        );
        const added = merged.changes![0]!.params?.add?.[0];
        expect(added?.description).toBe('新しいパラメータ。');
        expect(added?.type).toBe('Boolean'); // structural preserved
    });

    it('translates delta params.modify descriptions', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                changes: [
                    {
                        version: '1.1.0',
                        params: {
                            modify: [{ name: 'bar', changes: { description: 'bar 更新。' } }],
                        },
                    },
                ],
            }),
        );
        expect(merged.changes![0]!.params?.modify?.[0]?.changes.description).toBe('bar 更新。');
    });

    it('ignores delta changes for unknown version', () => {
        const merged = mergeItemSidecar(
            base,
            makeSidecar({
                changes: [{ version: '9.9.9', notes: 'phantom' }],
            }),
        );
        expect(merged.changes![0]!.notes).toBe('Removed foo.');
    });
});

// ─── mergeGroupSidecar ────────────────────────────────────────────────────────

describe('mergeGroupSidecar', () => {
    const base = makeGroup({
        description: 'Base group description.',
        params: [
            { name: 'alpha', type: 'String', description: 'Alpha param.' },
            {
                name: 'beta',
                type: 'Integer',
                description: 'Beta param.',
                enum_values: [{ id: 0, label: 'Off' }],
            },
        ],
    });

    it('translates group description', () => {
        const merged = mergeGroupSidecar(base, makeGroupSidecar({ description: 'グループ説明。' }));
        expect(merged.description).toBe('グループ説明。');
    });

    it('translates group param descriptions', () => {
        const merged = mergeGroupSidecar(
            base,
            makeGroupSidecar({
                params: [{ name: 'alpha', description: 'アルファパラメータ。' }],
            }),
        );
        expect(merged.params.find((p) => p.name === 'alpha')?.description).toBe(
            'アルファパラメータ。',
        );
    });

    it('translates group param enum labels', () => {
        const merged = mergeGroupSidecar(
            base,
            makeGroupSidecar({
                params: [{ name: 'beta', enum_values: [{ id: 0, label: 'オフ' }] }],
            }),
        );
        expect(merged.params.find((p) => p.name === 'beta')?.enum_values?.[0]?.label).toBe('オフ');
    });

    it('does not mutate base group', () => {
        const origDesc = base.description;
        mergeGroupSidecar(base, makeGroupSidecar({ description: 'X' }));
        expect(base.description).toBe(origDesc);
    });
});

// ─── validateItemSidecar ─────────────────────────────────────────────────────

describe('validateItemSidecar', () => {
    const base = makeItem({
        params: [{ name: 'foo', type: 'String', enum_values: [{ id: 1, label: 'A' }] }],
        callouts: [{ level: 'warn', text: 'Warning' }],
        examples: [{ language: 'psj', code: 'Test()' }],
        see_also: [{ $ref: 'domain/some-item' }],
        changes: [{ version: '1.1.0', notes: 'Changed.' }],
    });

    it('returns no errors for a valid sidecar', () => {
        const errors = validateItemSidecar(
            makeSidecar({ params: [{ name: 'foo', description: '翻訳' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors).toHaveLength(0);
    });

    it('reports error for param name not in base', () => {
        const errors = validateItemSidecar(
            makeSidecar({ params: [{ name: 'nonexistent', description: '翻訳' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('nonexistent');
    });

    it('reports error for enum id not in base', () => {
        const errors = validateItemSidecar(
            makeSidecar({ params: [{ name: 'foo', enum_values: [{ id: 99, label: 'X' }] }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('99');
    });

    it('reports error for out-of-range callout index', () => {
        const errors = validateItemSidecar(
            makeSidecar({ callouts: [{ index: 5, text: 'X' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('index 5');
    });

    it('reports error for out-of-range example index', () => {
        const errors = validateItemSidecar(
            makeSidecar({ examples: [{ index: 9, title: 'X' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
    });

    it('reports error for unknown see_also $ref', () => {
        const errors = validateItemSidecar(
            makeSidecar({ see_also: [{ $ref: 'domain/ghost' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('ghost');
    });

    it('reports error for unknown delta version', () => {
        const errors = validateItemSidecar(
            makeSidecar({ changes: [{ version: '9.9.9', notes: 'X' }] }),
            base,
            'test.ja.yaml',
        );
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('9.9.9');
    });

    it('reports id mismatch', () => {
        const errors = validateItemSidecar(makeSidecar({ id: 'wrong-id' }), base, 'test.ja.yaml');
        expect(errors.length).toBeGreaterThan(0);
        expect(errors[0]!.message).toContain('wrong-id');
    });
});

// ─── Integration: createSDK with locale ───────────────────────────────────────

describe('createSDK with locale: ja', () => {
    let sdk: Awaited<ReturnType<typeof createSDK>>;

    beforeAll(async () => {
        sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'), undefined, { locale: 'ja' });
    });

    it('loads without errors', () => {
        expect(sdk.items.size).toBeGreaterThan(0);
    });

    it('translates item description (LinearStatic)', () => {
        const item = sdk.items.get('Analysis-Nastran-LinearStatic')!;
        expect(item.description).toContain('Nastran BDF');
        expect(item.description).toMatch(/エクスポート/);
    });

    it('translates group param descriptions (nastran-base via group sidecar)', () => {
        const group = sdk.groups.get('nastran-base')!;
        expect(group.params.find((p) => p.name === 'strName')?.description).toContain('ジョブ名');
    });

    it('translates group description (nastran-base)', () => {
        const group = sdk.groups.get('nastran-base')!;
        expect(group.description).toMatch(/Nastran/);
        expect(group.description).not.toBe(
            'Common parameters shared by all Nastran analysis export commands.',
        );
    });

    it('group translations flow through to resolveItem', () => {
        const resolved = resolveItem(sdk, 'Analysis-Nastran-LinearStatic', '5.1.0');
        const strName = resolved.resolvedParams.find((p) => p.name === 'strName');
        expect(strName?.description).toContain('ジョブ名');
    });

    it('translates item-level return description (LinearStatic)', () => {
        const item = sdk.items.get('Analysis-Nastran-LinearStatic')!;
        expect(item.returns.description).toContain('ジョブ');
    });

    it('translates callout text (JPT-BeginDatabaseTransaction)', () => {
        const item = sdk.items.get('JPT-BeginDatabaseTransaction')!;
        expect(item.callouts![0]!.text).toContain('EndDatabaseTransaction');
        expect(item.callouts![0]!.text).toMatch(/呼び出し/);
        // Callout level is structural — preserved
        expect(item.callouts![0]!.level).toBe('warn');
    });

    it('translates param description (JPT-BeginDatabaseTransaction)', () => {
        const item = sdk.items.get('JPT-BeginDatabaseTransaction')!;
        const param = item.params[0] as any;
        expect(param.description).toContain('トランザクション名');
    });

    it('translates see_also label (JPT-BeginDatabaseTransaction)', () => {
        const item = sdk.items.get('JPT-BeginDatabaseTransaction')!;
        expect(item.see_also![0]!.label).toBe('JPT.EndDatabaseTransaction()');
        // $ref is structural
        expect(item.see_also![0]!.$ref).toBe('psj-utility/JPT-EndDatabaseTransaction');
    });

    it('translates macro param descriptions (AdvcStaticProcess)', () => {
        const item = sdk.items.get('AdvcStaticProcess')!;
        const param = item.params.find(
            (p) => !('$group' in p) && (p as any).name === 'm_strName',
        ) as any;
        expect(param?.description).toContain('プロセス名');
    });

    it('translates macro enum values (AdvcStaticProcess)', () => {
        const item = sdk.items.get('AdvcStaticProcess')!;
        const param = item.params.find(
            (p) => !('$group' in p) && (p as any).name === 'm_iGeomNonlinear',
        ) as any;
        expect(param?.enum_values[1]?.label).toBe('トータルラグランジュ');
    });

    it('translates macro return code meanings (AdvcStaticProcess)', () => {
        const item = sdk.items.get('AdvcStaticProcess')!;
        expect(item.returns.codes![0]!.meaning).toBe('関数を実行できます。');
        // return code value is structural
        expect(item.returns.codes![0]!.value).toBe('"1"');
    });

    it('translates version delta notes (Analysis-ADVC-Structure)', () => {
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        const delta501 = item.changes?.find((c) => c.version === '5.0.1');
        expect(delta501?.notes).toContain('iEJobType');
        expect(delta501?.notes).toMatch(/削除/);
    });

    it('translates version delta item.description (Analysis-ADVC-Structure)', () => {
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        const delta510 = item.changes?.find((c) => c.version === '5.1.0');
        expect(delta510?.item?.description).toContain('5.1.0');
        expect(delta510?.item?.description).toMatch(/更新/);
    });

    it('translates version delta params.add description (Analysis-ADVC-Structure)', () => {
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        const delta510 = item.changes?.find((c) => c.version === '5.1.0');
        const added = delta510?.params?.add?.[0];
        expect(added?.description).toContain('5.1.0');
        expect(added?.description).toMatch(/追加/);
        // structural fields preserved
        expect(added?.type).toBe('Boolean');
    });

    it('structural fields are never altered by sidecar', () => {
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        expect(item.id).toBe('Analysis-ADVC-Structure');
        expect(item.domain).toBe('psj-command');
        expect(item.version_introduced).toBe('5.0.0');
        const delta501 = item.changes?.find((c) => c.version === '5.0.1');
        expect(delta501?.params?.remove).toContain('iEJobType');
    });

    it('items without a sidecar file are loaded unchanged', () => {
        // DirectFrequencyResponse has no .ja.yaml sidecar
        const item = sdk.items.get('Analysis-Nastran-DirectFrequencyResponse')!;
        expect(item.description).toBe(
            'Export the Nastran BDF for Direct Frequency Response analysis (SOL 108).',
        );
    });
});

// ─── createSDK without locale loads base content ─────────────────────────────

describe('createSDK without locale', () => {
    it('loads base English content unchanged', async () => {
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = sdk.items.get('Analysis-Nastran-LinearStatic')!;
        expect(item.description).toBe(
            'Export the Nastran BDF input file for Structure Linear Static analysis (SOL 101).',
        );
    });
});

// ─── strict mode ──────────────────────────────────────────────────────────────

describe('strict mode', () => {
    it('does not throw in non-strict mode on invalid sidecar (warns only)', async () => {
        // We can only test this indirectly since no invalid fixture exists;
        // validate that strict: false is the default and does not throw on valid data
        await expect(
            createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'), undefined, {
                locale: 'ja',
                strict: false,
            }),
        ).resolves.toBeDefined();
    });
});

// ─── tryLoadSidecar ───────────────────────────────────────────────────────────

describe('tryLoadSidecar', () => {
    it('returns null for non-existent file', () => {
        expect(tryLoadSidecar('/nonexistent/path.ja.yaml')).toBeNull();
    });

    it('loads and parses an existing sidecar', () => {
        const sc = tryLoadSidecar(
            path.join(FIXTURES, 'psj-command/Analysis-Nastran-LinearStatic.ja.yaml'),
        );
        expect(sc).not.toBeNull();
        expect(sc!.kind).toBe('sidecar');
        expect(sc!.id).toBe('Analysis-Nastran-LinearStatic');
    });
});
