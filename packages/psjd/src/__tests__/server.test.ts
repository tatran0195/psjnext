// psjd/src/__tests__/server.test.ts
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import { createPsjd, createSDK, psjdSource } from '../server.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES = path.join(__dirname, '../../fixtures');

// ─── createSDK ────────────────────────────────────────────────────────────────

describe('createSDK', () => {
    it('loads the fixture SDK without errors', async () => {
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        expect(sdk.manifest.sdk.name).toBe('Jupiter CAE Desktop Platform SDK');
        expect(sdk.currentVersion).toBe('5.1.0');
        expect(sdk.versionIds).toEqual(['5.0.0', '5.0.1', '5.1.0']);
    });

    it('loads all param groups', async () => {
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        expect(sdk.groups.has('nastran-base')).toBe(true);
        expect(sdk.groups.has('advc-process-base')).toBe(true);
        expect(sdk.groups.has('advc-process-struct')).toBe(true);
    });

    it('loads item files from all domain folders', async () => {
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        expect(sdk.items.has('Analysis-Nastran-LinearStatic')).toBe(true);
        expect(sdk.items.has('Analysis-Nastran-DirectFrequencyResponse')).toBe(true);
        expect(sdk.items.has('Analysis-ADVC-Structure')).toBe(true);
        expect(sdk.items.has('AdvcStaticProcess')).toBe(true);
        expect(sdk.items.has('JPT-BeginDatabaseTransaction')).toBe(true);
    });

    it('throws on missing sdk.psjd.yaml', async () => {
        await expect(createSDK('/nonexistent/sdk.psjd.yaml')).rejects.toThrow(/not found/);
    });

    it('nastran-base group has 10 params', async () => {
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const group = sdk.groups.get('nastran-base')!;
        expect(group.params).toHaveLength(10);
    });
});

// ─── Integration: resolveItem with real fixtures ───────────────────────────────

describe('resolveItem with fixtures', () => {
    it('LinearStatic: expands nastran-base to 10 params', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-Nastran-LinearStatic', '5.1.0');
        expect(item.resolvedParams).toHaveLength(10);
        expect(item.paramStyle).toBe('named');
    });

    it('DirectFrequencyResponse: excludes 2 params and adds 3 unique params', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-Nastran-DirectFrequencyResponse', '5.1.0');
        // 10 base - 2 excluded + 3 unique = 11
        expect(item.resolvedParams).toHaveLength(11);
        const names = item.resolvedParams.map((p) => p.name);
        expect(names).not.toContain('bDummyPropAutoAssign');
        expect(names).not.toContain('iDummyPropMaterialID');
        expect(names).toContain('bOutputXYPlots');
    });

    it('ADVC-Structure at 5.0.0 has iEJobType and iHeatConvection', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-ADVC-Structure', '5.0.0');
        const names = item.resolvedParams.map((p) => p.name);
        expect(names).toContain('iEJobType');
        expect(names).toContain('iHeatConvection');
    });

    it('ADVC-Structure at 5.0.1 removes iEJobType and iHeatConvection', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-ADVC-Structure', '5.0.1');
        const names = item.resolvedParams.map((p) => p.name);
        expect(names).not.toContain('iEJobType');
        expect(names).not.toContain('iHeatConvection');
        expect(item.versionNotes).toContain('Removed');
    });

    it('ADVC-Structure at 5.1.0 adds bNewFeature after iGeomNonlinear', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-ADVC-Structure', '5.1.0');
        const names = item.resolvedParams.map((p) => p.name);
        expect(names).toContain('bNewFeature');
        const iGeomIdx = names.indexOf('iGeomNonlinear');
        const bNewIdx = names.indexOf('bNewFeature');
        expect(bNewIdx).toBe(iGeomIdx + 1);
        expect(item.description).toContain('5.1.0');
    });

    it('advc-process-struct expands its parent (advc-process-base) via extends', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-ADVC-Structure', '5.1.0');
        const names = item.resolvedParams.map((p) => p.name);
        // From advc-process-base via advc-process-struct
        expect(names).toContain('strName');
        expect(names).toContain('crEdit');
        // From advc-process-struct itself
        expect(names).toContain('iGeomNonlinear');
        expect(names).toContain('bConvergence');
    });

    it('AdvcStaticProcess (macro) has positional paramStyle', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'AdvcStaticProcess', '5.1.0');
        expect(item.paramStyle).toBe('positional');
        expect(item.resolvedParams).toHaveLength(5);
        expect(item.resolvedParams[0]?.name).toBe('m_strName');
    });

    it('JPT-BeginDatabaseTransaction has void returns and callout', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'JPT-BeginDatabaseTransaction', '5.1.0');
        expect(item.returns.kind).toBe('void');
        expect(item.callouts).toHaveLength(1);
        expect(item.callouts![0]!.level).toBe('warn');
        expect(item.resolvedParams).toHaveLength(1);
        expect(item.resolvedParams[0]?.required).toBe(true);
    });

    it('resolved item is JSON-serializable (no Maps)', async () => {
        const { resolveItem } = await import('../resolve.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        const item = resolveItem(sdk, 'Analysis-Nastran-LinearStatic', '5.1.0');
        expect(() => JSON.stringify(item)).not.toThrow();
    });
});

// ─── createPsjd ─────────────────────────────────────────────────────────────

describe('createPsjd', () => {
    it('returns an instance with _options', () => {
        const psjd = createPsjd({ input: './sdk.psjd.yaml' });
        expect(psjd._options.input).toBe('./sdk.psjd.yaml');
    });

    it('stores locales and strict options', () => {
        const psjd = createPsjd({
            input: './sdk.psjd.yaml',
            locales: ['en', 'ja'],
            strict: true,
        });
        expect(psjd._options.locales).toEqual(['en', 'ja']);
        expect(psjd._options.strict).toBe(true);
    });
});

// ─── psjdSource (async, v16) ─────────────────────────────────────────────────

describe('psjdSource', () => {
    it('generates page and meta files (no locales)', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd, { version: '5.1.0', groupBy: 'namespace' });
        const pages = source.files.filter((f) => f.type === 'page');
        const metas = source.files.filter((f) => f.type === 'meta');
        expect(pages.length).toBeGreaterThanOrEqual(5);
        expect(metas.length).toBeGreaterThanOrEqual(1);
    });

    it('page data has correct discriminator and locale field', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd);
        for (const p of source.files.filter((f) => f.type === 'page')) {
            expect(p.data.type).toBe('psjd');
            expect(typeof p.data.psjdId).toBe('string');
            expect(typeof p.data.version).toBe('string');
            expect(typeof (p.data as any).locale).toBe('string');
        }
    });

    it('page data is JSON-serializable', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd);
        for (const f of source.files) {
            expect(() => JSON.stringify(f.data)).not.toThrow();
        }
    });

    it('groupBy domain produces domain-prefixed paths', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd, { groupBy: 'domain' });
        const paths = source.files.map((f) => f.path);
        expect(paths.some((p) => p.includes('psj-command'))).toBe(true);
    });

    it('does not produce duplicate page paths', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd);
        const pagePaths = source.files.filter((f) => f.type === 'page').map((f) => f.path);
        expect(new Set(pagePaths).size).toBe(pagePaths.length);
    });

    it('defaults to currentVersion', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd);
        for (const p of source.files.filter((f) => f.type === 'page')) {
            expect(p.data.version).toBe('5.1.0');
        }
    });

    it('baseDir option prefixes all virtual paths', async () => {
        const psjd = createPsjd({ input: path.join(FIXTURES, 'sdk.psjd.yaml') });
        const source = await psjdSource(psjd, { baseDir: 'api-ref' });
        for (const f of source.files) {
            expect(f.path.startsWith('api-ref/')).toBe(true);
        }
    });

    it('with locales: emits locale-tagged files for each locale', async () => {
        const psjd = createPsjd({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            locales: ['en', 'ja'],
        });
        const source = await psjdSource(psjd);
        const enPages = source.files.filter((f) => f.type === 'page' && f.locale === 'en');
        const jaPages = source.files.filter((f) => f.type === 'page' && f.locale === 'ja');
        expect(enPages.length).toBeGreaterThanOrEqual(5);
        expect(jaPages.length).toBeGreaterThanOrEqual(5);
        expect(enPages.length).toBe(jaPages.length);
    });

    it('with locales: ja pages have sidecar-translated description', async () => {
        const psjd = createPsjd({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            locales: ['en', 'ja'],
        });
        const source = await psjdSource(psjd);
        const jaPage = source.files.find(
            (f) =>
                f.type === 'page' &&
                f.locale === 'ja' &&
                (f.data as any).psjdId === 'Analysis-Nastran-LinearStatic',
        );
        expect(jaPage).toBeDefined();
        expect((jaPage!.data as any).description).toMatch(/エクスポート/);
    });

    it('with locales: en pages keep English content', async () => {
        const psjd = createPsjd({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            locales: ['en', 'ja'],
        });
        const source = await psjdSource(psjd);
        const enPage = source.files.find(
            (f) =>
                f.type === 'page' &&
                f.locale === 'en' &&
                (f.data as any).psjdId === 'Analysis-Nastran-LinearStatic',
        );
        expect((enPage!.data as any).description).toContain('Linear Static');
    });

    it('with locales: meta files are locale-tagged', async () => {
        const psjd = createPsjd({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            locales: ['en', 'ja'],
        });
        const source = await psjdSource(psjd);
        const enMetas = source.files.filter((f) => f.type === 'meta' && f.locale === 'en');
        const jaMetas = source.files.filter((f) => f.type === 'meta' && f.locale === 'ja');
        expect(enMetas.length).toBeGreaterThan(0);
        expect(jaMetas.length).toBeGreaterThan(0);
    });
});
