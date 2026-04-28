// scripts/generate-psj-docs.ts
import { psjServer } from '@/lib/psj-server';
import { generateFiles } from 'psjapi';

await generateFiles({
    input: psjServer,
    output: './content/psj-sdk/generated',
    groupBy: 'domain',
    // Re-generate on YAML file changes during `next dev`
    watch: process.env.NODE_ENV === 'development',
});
