import { defineConfig } from 'tsdown';

import { compileInline } from './scripts/compile-inline.utils.ts';

export default defineConfig({
    format: 'esm',
    target: 'es2023',
    entry: [
        // Root — types, loader, file generator
        './src/index.ts',
        // i18n UI translations
        './src/i18n.ts',
        // UI — server component factory (RSC)
        './src/ui/index.ts',
        // Server — source API + loader plugin
        './src/server/index.ts',
    ],
    fixedExtension: false,
    unbundle: true,
    dts: {
        sourcemap: false,
    },
    sourcemap: false,
    async onSuccess() {
        await compileInline();
    },
    // Components run in browser (RSC output is still browser-targeted)
    platform: 'browser',
    deps: {
        // Bundle these into the dist so consumers don't need them as direct deps
        onlyBundle: ['yaml'],
        neverBundle: [/^node:/],
    },
    exports: {
        enabled: true,
        customExports(v) {
            // Expose css/ directory so consumers can import:
            //   import 'fumadocs-psjapi/css/preset.css'
            v['./css/*'] = './css/*';
            return v;
        },
        legacy: true,
    },
});
