import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, test } from 'vitest';

import { loadSDK } from '@/loader';
import { buildEntries } from '@/pages/builder';
import { toText } from '@/pages/to-text';
import { resolveAllItems, resolveItem } from '@/resolver';
import { compareVersions } from '@/version';

const fixtureDir = path.join(fileURLToPath(import.meta.url), '..', 'fixtures');

// ─── Version util ─────────────────────────────────────────────────────────────

describe('compareVersions', () => {
    test('less than', () => expect(compareVersions('5.0.0', '5.0.1')).toBeLessThan(0));
    test('equal', () => expect(compareVersions('5.1.0', '5.1.0')).toBe(0));
    test('greater', () => expect(compareVersions('5.1.0', '5.0.9')).toBeGreaterThan(0));
});

// ─── Loader ───────────────────────────────────────────────────────────────────

describe('loadSDK', () => {
    test('loads manifest, groups and items', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));

        expect(sdk.manifest.jcall).toBe('2.0');
        expect(sdk.manifest.current_version).toBe('5.1.0');
        expect(sdk.manifest.domains).toHaveLength(3);

        expect(sdk.groups.has('nastran-base')).toBe(true);
        expect([...sdk.items.keys()]).toContain('Analysis-Nastran-LinearStatic');
        expect([...sdk.items.keys()]).toContain('Analysis-ADVC-Structure');
    });
});

// ─── Resolver ─────────────────────────────────────────────────────────────────

describe('resolveItem — group expansion', () => {
    test('expands $group reference into flat param list', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const item = sdk.items.get('Analysis-Nastran-LinearStatic')!;
        const domainDef = sdk.manifest.domains.find((d) => d.id === 'psj-command')!;

        const resolved = resolveItem(item, sdk.groups, domainDef, '5.1.0');
        const names = resolved.params.map((p) => p.name);

        expect(names).toContain('strName');
        expect(names).toContain('strPath');
        expect(names).toContain('crEdit');
    });

    test('param_style is taken from domain definition', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const item = sdk.items.get('Analysis-Nastran-LinearStatic')!;
        const domainDef = sdk.manifest.domains.find((d) => d.id === 'psj-command')!;
        const resolved = resolveItem(item, sdk.groups, domainDef, '5.1.0');

        expect(resolved.param_style).toBe('named');
    });
});

describe('resolveItem — version deltas', () => {
    test('param removed in 5.0.1 is absent when resolved at 5.0.1', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        const domainDef = sdk.manifest.domains.find((d) => d.id === 'psj-command')!;

        const resolved = resolveItem(item, sdk.groups, domainDef, '5.0.1');
        const names = resolved.params.map((p) => p.name);
        expect(names).not.toContain('iEJobType');
    });

    test('param is present when resolved at 5.0.0 (before removal)', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const item = sdk.items.get('Analysis-ADVC-Structure')!;
        const domainDef = sdk.manifest.domains.find((d) => d.id === 'psj-command')!;

        const resolved = resolveItem(item, sdk.groups, domainDef, '5.0.0');
        const names = resolved.params.map((p) => p.name);
        expect(names).toContain('iEJobType');
    });
});

// ─── Builder ──────────────────────────────────────────────────────────────────

describe('buildEntries', () => {
    test('creates domain-level groups', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const resolved = resolveAllItems(sdk);
        const entries = buildEntries(resolved);

        const domainGroup = entries.find(
            (e) => e.type === 'group' && e.info.title === 'psj-command',
        );
        expect(domainGroup).toBeDefined();
    });

    test('creates nested group for item.group', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const resolved = resolveAllItems(sdk);
        const entries = buildEntries(resolved);

        const domainGroup = entries.find(
            (e) => e.type === 'group' && e.info.title === 'psj-command',
        );
        expect(domainGroup?.type).toBe('group');
        if (domainGroup?.type !== 'group') return;

        const nastranGroup = domainGroup.entries.find(
            (e) => e.type === 'group' && e.info.title === 'Nastran',
        );
        expect(nastranGroup).toBeDefined();
    });
});

// ─── MDX text generation ──────────────────────────────────────────────────────

describe('toText', () => {
    test('produces valid MDX with frontmatter and JCallPage component', async () => {
        const sdk = await loadSDK(path.join(fixtureDir, 'sdk.jcall.yaml'));
        const resolved = resolveAllItems(sdk);
        const item = [...resolved.values()][0];

        const text = toText({
            type: 'page',
            path: 'test/page.mdx',
            item,
            info: { title: item.title, description: item.description },
        });

        expect(text).toContain('---');
        expect(text).toContain(`title: ${item.title}`);
        expect(text).toContain(`<JCallPage id="${item.id}" />`);
        expect(text).toContain('_jcall:');
    });
});
