import { defineConfig } from 'tsup';

export default defineConfig([
    // Server-only entries (Node.js, can use 'fs', 'path', 'yaml')
    {
        entry: {
            index: 'src/index.ts',
            server: 'src/server.ts',
        },
        format: ['esm'],
        dts: true,
        sourcemap: true,
        clean: true,
        external: ['react', 'react-dom'],
        platform: 'node',
        target: 'node18',
    },
    // UI entry (browser-safe, no Node builtins)
    {
        entry: {
            'ui/index': 'src/ui/index.ts',
        },
        format: ['esm'],
        dts: true,
        sourcemap: true,
        external: ['react', 'react-dom'],
        platform: 'browser',
        target: 'es2020',
        async onSuccess() {
            const fs = await import('fs');
            if (fs.existsSync('src/ui/styles.css')) {
                fs.mkdirSync('dist/ui', { recursive: true });
                fs.copyFileSync('src/ui/styles.css', 'dist/ui/styles.css');
            }
        },
    },
]);
