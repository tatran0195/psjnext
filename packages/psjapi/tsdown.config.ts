import { defineConfig } from 'tsdown';

export default defineConfig({
    format: 'esm',
    target: 'es2023',
    entry: ['./src/ui/*', './src/server/index.ts', './src/index.ts'],
    fixedExtension: false,
    unbundle: true,
    dts: {
        sourcemap: false,
    },
    sourcemap: false,
    platform: 'browser',
    deps: {
        onlyBundle: ['fast-content-type-parse', 'pathe', 'yaml'],
        neverBundle: [/^node:/, /^@types\//, /^mdast-util-/, /^micromark-/, /^remark-/],
    },
    exports: {
        enabled: true,
        customExports(v) {
            v['./css/*'] = './css/*';
            return v;
        },
        legacy: true,
    },
});
