import { i18n } from '@/lib/i18n';
import { docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';

import { customIconsPlugin } from './plugins/custom-icons-plugin';
import { pageTreeCodeTitlesPlugin } from './plugins/page-tree-code-titles-plugin';
import { pageTreeFoldersPlugin } from './plugins/page-tree-folders-plugin';
import { pageTreeTagsPlugin } from './plugins/page-tree-tags-plugin';

const TAG_STYLES: Record<string, string> = {
    New: 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300',
    Alpha: 'bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300',
    Beta: 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300',
    Experimental: 'bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300',
    Deprecated: 'bg-rose-100 text-rose-700 dark:bg-rose-900 dark:text-rose-300',
};

export const docsSource = loader({
    source: docs.toFumadocsSource(),
    i18n,
    baseUrl: '/',
    plugins: [
        lucideIconsPlugin(),
        customIconsPlugin(),
        pageTreeCodeTitlesPlugin(),
        pageTreeFoldersPlugin(),
        pageTreeTagsPlugin(TAG_STYLES),
    ],
});

export type Page = InferPageType<typeof docsSource>;
export type Meta = InferMetaType<typeof docsSource>;

// SYNC-VERSIONS:START
import * as apiV5_1_0 from 'collections/5.1.0/server';
import * as apiV5_2_0 from 'collections/5.2.0/server';
type VersionModule = { docs: { toFumadocsSource: () => Parameters<typeof loader>[0]['source'] } };
const versionModules: Record<string, VersionModule> = {
    '5.2.0': apiV5_2_0 as unknown as VersionModule,
    '5.1.0': apiV5_1_0 as unknown as VersionModule,
};
export const apiSources = {
    '5.2.0': loader({ baseUrl: '/api/5.2.0', i18n, source: versionModules['5.2.0'].docs.toFumadocsSource() }),
    '5.1.0': loader({ baseUrl: '/api/5.1.0', i18n, source: versionModules['5.1.0'].docs.toFumadocsSource() }),
} as const;
// SYNC-VERSIONS:END
export type ApiVersion = keyof typeof apiSources;
export type ApiPage = InferPageType<(typeof apiSources)[ApiVersion]>;