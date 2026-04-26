import { compile } from '@fumadocs/tailwind/compile';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

/**
 * Compile Tailwind utility classes used in psjapi UI components into a single
 * `css/generated/shared.css` file that consumers can import.
 *
 * This runs after every tsdown build via the `onSuccess` hook.
 */
export async function compileInline(): Promise<void> {
    await mkdir('css/generated', { recursive: true });

    await writeFile(
        'css/generated/shared.css',
        compile([
            {
                // Scan all UI component source files for Tailwind classes
                base: path.resolve('src'),
                pattern: 'ui/**/*.{ts,tsx}',
                negated: false,
            },
            {
                // Include server components (source-api plugin JSX)
                base: path.resolve('src'),
                pattern: 'server/**/*.tsx',
                negated: false,
            },
        ]),
    );

    console.log('[psjapi] generated CSS files');
}
