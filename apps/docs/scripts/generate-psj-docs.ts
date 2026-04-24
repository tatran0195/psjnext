import { generateFiles } from 'psjapi';

// scripts/generate-psj-docs.ts
import { psjapi } from '@/lib/psjapi';

await generateFiles({
    input: psjapi,
    output: './content/ref',
    groupBy: 'domain',
    // Re-generate on YAML file changes during `next dev`
    watch: process.env.NODE_ENV === 'development',
});
