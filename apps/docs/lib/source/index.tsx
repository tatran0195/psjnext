import { docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';
import { i18n } from '../i18n';
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

export const source = loader({
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

export type Page = InferPageType<typeof source>;
export type Meta = InferMetaType<typeof source>;
