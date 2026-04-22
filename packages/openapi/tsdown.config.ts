import { defineConfig } from 'tsdown';

export default defineConfig({
    format: 'esm',
    target: 'es2023',
    entry: ['./src/index.ts', './src/ui/index.tsx'],
    fixedExtension: false,
    unbundle: true,
    dts: {
        sourcemap: false,
    },
    sourcemap: false,
    platform: 'neutral',
    deps: {
        neverBundle: [/^node:/],
    },
    exports: {
        enabled: true,
        legacy: true,
    },
});
