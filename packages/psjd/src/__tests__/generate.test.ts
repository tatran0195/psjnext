// psjd/src/__tests__/generate.test.ts
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';

import { generateFiles } from '../index.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES = path.join(__dirname, '../../fixtures');

let tmpDir: string;

beforeEach(() => {
    tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'psjd-test-'));
});

afterEach(() => {
    fs.rmSync(tmpDir, { recursive: true, force: true });
});

describe('generateFiles', () => {
    it('generates MDX files for every item at current version', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'item',
        });
        const allFiles: string[] = [];
        function walk(dir: string) {
            for (const f of fs.readdirSync(dir)) {
                const full = path.join(dir, f);
                if (fs.statSync(full).isDirectory()) walk(full);
                else allFiles.push(full);
            }
        }
        walk(tmpDir);
        const mdxFiles = allFiles.filter((f) => f.endsWith('.mdx'));
        expect(mdxFiles.length).toBeGreaterThanOrEqual(5);
    });

    it('generated MDX contains frontmatter with correct fields', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'item',
            includeDescription: true,
        });
        // Find the LinearStatic file
        let found: string | undefined;
        function walk(dir: string) {
            for (const f of fs.readdirSync(dir)) {
                const full = path.join(dir, f);
                if (fs.statSync(full).isDirectory()) walk(full);
                else if (f.includes('linearstatic')) found = full;
            }
        }
        walk(tmpDir);
        expect(found).toBeDefined();
        const content = fs.readFileSync(found!, 'utf8');
        expect(content).toContain('psjdId:');
        expect(content).toContain('psjdVersion:');
        expect(content).toContain('Analysis-Nastran-LinearStatic');
        expect(content).toContain('<CallablePage');
    });

    it('generated MDX imports CallablePage', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'item',
        });
        let anyFile: string | undefined;
        function walk(dir: string) {
            for (const f of fs.readdirSync(dir)) {
                const full = path.join(dir, f);
                if (fs.statSync(full).isDirectory()) walk(full);
                else if (f.endsWith('.mdx') && !anyFile) anyFile = full;
            }
        }
        walk(tmpDir);
        const content = fs.readFileSync(anyFile!, 'utf8');
        expect(content).toContain("from 'psjd/ui'");
    });

    it('injects custom imports', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'item',
            imports: [{ names: ['MY_CONST'], from: '@/constants' }],
        });
        let anyFile: string | undefined;
        function walk(dir: string) {
            for (const f of fs.readdirSync(dir)) {
                const full = path.join(dir, f);
                if (fs.statSync(full).isDirectory()) walk(full);
                else if (f.endsWith('.mdx') && !anyFile) anyFile = full;
            }
        }
        walk(tmpDir);
        const content = fs.readFileSync(anyFile!, 'utf8');
        expect(content).toContain("from '@/constants'");
    });

    it('per=namespace generates one file per namespace', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'namespace',
        });
        const files = fs.readdirSync(tmpDir).filter((f) => f.endsWith('.mdx'));
        expect(files.length).toBeGreaterThanOrEqual(2);
    });

    it('respects custom name resolver', async () => {
        await generateFiles({
            input: path.join(FIXTURES, 'sdk.psjd.yaml'),
            output: tmpDir,
            per: 'item',
            name: (item) => `custom/${item.id.toLowerCase()}`,
        });
        const customDir = path.join(tmpDir, 'custom');
        expect(fs.existsSync(customDir)).toBe(true);
        const files = fs.readdirSync(customDir).filter((f) => f.endsWith('.mdx'));
        expect(files.length).toBeGreaterThanOrEqual(5);
    });

    it('accepts a pre-parsed ParsedSDK object', async () => {
        const { createSDK } = await import('../server.js');
        const sdk = await createSDK(path.join(FIXTURES, 'sdk.psjd.yaml'));
        await expect(generateFiles({ input: sdk, output: tmpDir })).resolves.not.toThrow();
        const files = fs.readdirSync(tmpDir, { recursive: true });
        expect(files.length).toBeGreaterThan(0);
    });
});
