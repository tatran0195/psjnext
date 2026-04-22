// psjd/src/__tests__/resolve.test.ts
import { describe, expect, it } from 'vitest';

import type { ItemFile, ParamGroupFile, ParsedSDK } from '../types.js';

import {
    expandGroups,
    resolveAll,
    resolveItem,
    semverCompare,
    semverGte,
    semverLte,
} from '../resolve.js';

// ─── Helpers ──────────────────────────────────────────────────────────────────

function makeSDK(
    overrides: Partial<ParsedSDK> = {},
    items: [string, ItemFile][] = [],
    groups: [string, ParamGroupFile][] = [],
): ParsedSDK {
    return {
        manifest: {
            psjd: '2.0',
            sdk: { name: 'Test SDK', vendor: 'Test' },
            versions: [{ id: '1.0.0' }, { id: '1.1.0' }, { id: '2.0.0' }],
            current_version: '2.0.0',
            domains: [
                { id: 'psj-command', title: 'PSJ', param_style: 'named' },
                { id: 'macro', title: 'Macros', param_style: 'positional' },
            ],
        },
        items: new Map(items),
        groups: new Map(groups),
        currentVersion: '2.0.0',
        versionIds: ['1.0.0', '1.1.0', '2.0.0'],
        ...overrides,
    };
}

function makeItem(overrides: Partial<ItemFile> = {}): ItemFile {
    return {
        psjd: '2.0',
        id: 'test-item',
        title: 'Test()',
        domain: 'psj-command',
        description: 'A test item.',
        version_introduced: '1.0.0',
        params: [],
        returns: { kind: 'void' },
        ...overrides,
    };
}

// ─── semverCompare ────────────────────────────────────────────────────────────

describe('semverCompare', () => {
    it('returns 0 for equal versions', () => {
        expect(semverCompare('1.0.0', '1.0.0')).toBe(0);
        expect(semverCompare('5.1.0', '5.1.0')).toBe(0);
    });

    it('correctly orders major versions', () => {
        expect(semverCompare('2.0.0', '1.0.0')).toBeGreaterThan(0);
        expect(semverCompare('1.0.0', '2.0.0')).toBeLessThan(0);
    });

    it('correctly orders minor versions', () => {
        expect(semverCompare('1.1.0', '1.0.0')).toBeGreaterThan(0);
        expect(semverCompare('5.1.0', '5.0.1')).toBeGreaterThan(0);
    });

    it('correctly orders patch versions', () => {
        expect(semverCompare('1.0.1', '1.0.0')).toBeGreaterThan(0);
    });

    it('handles double-digit minor/patch (lexicographic would fail)', () => {
        // String comparison: '5.10.0' < '5.9.0' — our numeric compare must not do that
        expect(semverCompare('5.10.0', '5.9.0')).toBeGreaterThan(0);
        expect(semverCompare('1.0.10', '1.0.9')).toBeGreaterThan(0);
    });

    it('semverLte works', () => {
        expect(semverLte('1.0.0', '1.0.0')).toBe(true);
        expect(semverLte('1.0.0', '2.0.0')).toBe(true);
        expect(semverLte('2.0.0', '1.0.0')).toBe(false);
    });

    it('semverGte works', () => {
        expect(semverGte('2.0.0', '1.0.0')).toBe(true);
        expect(semverGte('1.0.0', '1.0.0')).toBe(true);
        expect(semverGte('1.0.0', '2.0.0')).toBe(false);
    });
});

// ─── expandGroups ─────────────────────────────────────────────────────────────

describe('expandGroups', () => {
    it('passes through plain params unchanged', () => {
        const sdk = makeSDK();
        const result = expandGroups(sdk, [
            { name: 'foo', type: 'String' },
            { name: 'bar', type: 'Integer' },
        ]);
        expect(result).toHaveLength(2);
        expect(result[0]?.name).toBe('foo');
        expect(result[1]?.name).toBe('bar');
    });

    it('expands a simple group reference', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'base-group',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'base-group',
                        params: [
                            { name: 'alpha', type: 'String' },
                            { name: 'beta', type: 'Integer' },
                        ],
                    },
                ],
            ],
        );
        const result = expandGroups(sdk, [{ $group: 'base-group' }]);
        expect(result).toHaveLength(2);
        expect(result[0]?.name).toBe('alpha');
        expect(result[1]?.name).toBe('beta');
    });

    it('applies exclude to drop params from a group', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'my-group',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'my-group',
                        params: [
                            { name: 'keep', type: 'String' },
                            { name: 'drop1', type: 'Integer' },
                            { name: 'drop2', type: 'Boolean' },
                        ],
                    },
                ],
            ],
        );
        const result = expandGroups(sdk, [{ $group: 'my-group', exclude: ['drop1', 'drop2'] }]);
        expect(result).toHaveLength(1);
        expect(result[0]?.name).toBe('keep');
    });

    it('applies insert_after to splice params', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'g',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'g',
                        params: [
                            { name: 'a', type: 'String' },
                            { name: 'b', type: 'String' },
                        ],
                    },
                ],
            ],
        );
        const result = expandGroups(sdk, [
            {
                $group: 'g',
                insert_after: 'a',
                insert: [{ name: 'mid', type: 'Integer' }],
            },
        ]);
        expect(result.map((p) => p.name)).toEqual(['a', 'mid', 'b']);
    });

    it('expands group extends recursively', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'parent',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'parent',
                        params: [{ name: 'from-parent', type: 'String' }],
                    },
                ],
                [
                    'child',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'child',
                        extends: 'parent',
                        params: [{ name: 'from-child', type: 'Integer' }],
                    },
                ],
            ],
        );
        const result = expandGroups(sdk, [{ $group: 'child' }]);
        expect(result.map((p) => p.name)).toEqual(['from-parent', 'from-child']);
    });

    it('throws on circular extends', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                ['a', { psjd: '2.0', kind: 'param_group', id: 'a', extends: 'b', params: [] }],
                ['b', { psjd: '2.0', kind: 'param_group', id: 'b', extends: 'a', params: [] }],
            ],
        );
        expect(() => expandGroups(sdk, [{ $group: 'a' }])).toThrow(/Circular/);
    });

    it('throws on missing group', () => {
        const sdk = makeSDK();
        expect(() => expandGroups(sdk, [{ $group: 'nonexistent' }])).toThrow(/Unknown param group/);
    });

    it('throws on insert_after referencing missing param', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'g',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'g',
                        params: [{ name: 'x', type: 'String' }],
                    },
                ],
            ],
        );
        expect(() =>
            expandGroups(sdk, [
                {
                    $group: 'g',
                    insert_after: 'does-not-exist',
                    insert: [{ name: 'y', type: 'String' }],
                },
            ]),
        ).toThrow(/insert_after/);
    });

    it('does not mutate source params array', () => {
        const sdk = makeSDK(
            {},
            [],
            [
                [
                    'g',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'g',
                        params: [{ name: 'x', type: 'String' }],
                    },
                ],
            ],
        );
        const source = [{ $group: 'g' }] as const;
        expandGroups(sdk, [...source]);
        // source array unchanged
        expect(source).toHaveLength(1);
    });
});

// ─── resolveItem ──────────────────────────────────────────────────────────────

describe('resolveItem', () => {
    it('resolves a simple item with no groups and no deltas', () => {
        const sdk = makeSDK({}, [
            [
                'simple',
                makeItem({
                    id: 'simple',
                    params: [{ name: 'foo', type: 'String', required: true, default: '""' }],
                }),
            ],
        ]);
        const resolved = resolveItem(sdk, 'simple', '1.0.0');
        expect(resolved.id).toBe('simple');
        expect(resolved.resolvedParams).toHaveLength(1);
        expect(resolved.resolvedParams[0]?.name).toBe('foo');
        expect(resolved.resolvedVersion).toBe('1.0.0');
    });

    it('applies paramStyle from the domain', () => {
        const sdk = makeSDK({}, [
            ['macro-item', makeItem({ id: 'macro-item', domain: 'macro', params: [] })],
        ]);
        const resolved = resolveItem(sdk, 'macro-item', '1.0.0');
        expect(resolved.paramStyle).toBe('positional');
    });

    it('throws for unknown item id', () => {
        const sdk = makeSDK();
        expect(() => resolveItem(sdk, 'ghost', '1.0.0')).toThrow(/Unknown item/);
    });

    it('throws when requested version is before version_introduced', () => {
        const sdk = makeSDK({}, [
            ['late', makeItem({ id: 'late', version_introduced: '2.0.0', params: [] })],
        ]);
        expect(() => resolveItem(sdk, 'late', '1.0.0')).toThrow(/introduced in 2\.0\.0/);
    });

    it('applies delta removes correctly', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [
                        { name: 'keep', type: 'String' },
                        { name: 'gone', type: 'Integer' },
                    ],
                    changes: [
                        {
                            version: '1.1.0',
                            params: { remove: ['gone'] },
                        },
                    ],
                }),
            ],
        ]);
        const at100 = resolveItem(sdk, 'item', '1.0.0');
        expect(at100.resolvedParams.map((p) => p.name)).toEqual(['keep', 'gone']);

        const at110 = resolveItem(sdk, 'item', '1.1.0');
        expect(at110.resolvedParams.map((p) => p.name)).toEqual(['keep']);
    });

    it('applies delta adds at end when no after', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [{ name: 'a', type: 'String' }],
                    changes: [
                        {
                            version: '1.1.0',
                            params: {
                                add: [
                                    {
                                        name: 'b',
                                        type: 'Boolean',
                                        required: false,
                                        default: 'False',
                                    },
                                ],
                            },
                        },
                    ],
                }),
            ],
        ]);
        const resolved = resolveItem(sdk, 'item', '1.1.0');
        expect(resolved.resolvedParams.map((p) => p.name)).toEqual(['a', 'b']);
    });

    it('applies delta adds at named position', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [
                        { name: 'a', type: 'String' },
                        { name: 'c', type: 'String' },
                    ],
                    changes: [
                        {
                            version: '1.1.0',
                            params: {
                                add: [{ name: 'b', type: 'Integer', after: 'a' } as any],
                            },
                        },
                    ],
                }),
            ],
        ]);
        const resolved = resolveItem(sdk, 'item', '1.1.0');
        expect(resolved.resolvedParams.map((p) => p.name)).toEqual(['a', 'b', 'c']);
    });

    it('applies delta modifies (description, default, required)', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [
                        { name: 'x', type: 'String', default: '"old"', description: 'Old desc' },
                    ],
                    changes: [
                        {
                            version: '1.1.0',
                            params: {
                                modify: [
                                    {
                                        name: 'x',
                                        changes: { description: 'New desc', default: '"new"' },
                                    },
                                ],
                            },
                        },
                    ],
                }),
            ],
        ]);
        const resolved = resolveItem(sdk, 'item', '1.1.0');
        expect(resolved.resolvedParams[0]?.description).toBe('New desc');
        expect(resolved.resolvedParams[0]?.default).toBe('"new"');
    });

    it('applies multiple deltas in version order (not file order)', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [{ name: 'a', type: 'String' }],
                    // intentionally out of order in the array
                    changes: [
                        { version: '2.0.0', params: { add: [{ name: 'c', type: 'String' }] } },
                        { version: '1.1.0', params: { add: [{ name: 'b', type: 'String' }] } },
                    ],
                }),
            ],
        ]);
        const at110 = resolveItem(sdk, 'item', '1.1.0');
        expect(at110.resolvedParams.map((p) => p.name)).toEqual(['a', 'b']);

        const at200 = resolveItem(sdk, 'item', '2.0.0');
        expect(at200.resolvedParams.map((p) => p.name)).toEqual(['a', 'b', 'c']);
    });

    it('applies item-level description override from delta', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    description: 'Original.',
                    params: [],
                    changes: [
                        {
                            version: '1.1.0',
                            item: { description: 'Updated.' },
                        },
                    ],
                }),
            ],
        ]);
        const at100 = resolveItem(sdk, 'item', '1.0.0');
        expect(at100.description).toBe('Original.');

        const at110 = resolveItem(sdk, 'item', '1.1.0');
        expect(at110.description).toBe('Updated.');
    });

    it('carries versionNotes from delta.notes', () => {
        const sdk = makeSDK({}, [
            [
                'item',
                makeItem({
                    id: 'item',
                    params: [],
                    changes: [{ version: '1.1.0', notes: 'Behaviour changed.' }],
                }),
            ],
        ]);
        const resolved = resolveItem(sdk, 'item', '1.1.0');
        expect(resolved.versionNotes).toBe('Behaviour changed.');
    });

    it('result is a plain serializable object (no Maps)', () => {
        const sdk = makeSDK({}, [['item', makeItem({ id: 'item', params: [] })]]);
        const resolved = resolveItem(sdk, 'item', '1.0.0');
        // JSON.stringify must not throw
        expect(() => JSON.stringify(resolved)).not.toThrow();
    });

    it('expands groups + applies deltas correctly together', () => {
        const sdk = makeSDK(
            {},
            [
                [
                    'item',
                    makeItem({
                        id: 'item',
                        params: [{ $group: 'g' } as any],
                        changes: [{ version: '1.1.0', params: { remove: ['from-group'] } }],
                    }),
                ],
            ],
            [
                [
                    'g',
                    {
                        psjd: '2.0',
                        kind: 'param_group',
                        id: 'g',
                        params: [
                            { name: 'from-group', type: 'String' },
                            { name: 'other', type: 'Integer' },
                        ],
                    },
                ],
            ],
        );
        const at100 = resolveItem(sdk, 'item', '1.0.0');
        expect(at100.resolvedParams.map((p) => p.name)).toEqual(['from-group', 'other']);

        const at110 = resolveItem(sdk, 'item', '1.1.0');
        expect(at110.resolvedParams.map((p) => p.name)).toEqual(['other']);
    });
});

// ─── resolveAll ───────────────────────────────────────────────────────────────

describe('resolveAll', () => {
    it('excludes items introduced after the requested version', () => {
        const sdk = makeSDK({}, [
            ['old', makeItem({ id: 'old', version_introduced: '1.0.0', params: [] })],
            ['new', makeItem({ id: 'new', version_introduced: '2.0.0', params: [] })],
        ]);
        const at100 = resolveAll(sdk, '1.0.0');
        expect(at100.map((i) => i.id)).toEqual(['old']);

        const at200 = resolveAll(sdk, '2.0.0');
        expect(at200.map((i) => i.id)).toContain('old');
        expect(at200.map((i) => i.id)).toContain('new');
    });

    it('returns empty array when no items qualify', () => {
        const sdk = makeSDK({}, [
            ['future', makeItem({ id: 'future', version_introduced: '2.0.0', params: [] })],
        ]);
        const result = resolveAll(sdk, '1.0.0');
        expect(result).toHaveLength(0);
    });
});
