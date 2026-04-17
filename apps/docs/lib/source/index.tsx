import { docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';

import { i18n } from '@/lib/i18n';

import { customIconsPlugin } from './plugins/custom-icons-plugin';
import { pageTreeCodeTitlesPlugin } from './plugins/page-tree-code-titles-plugin';
import { pageTreeFoldersPlugin } from './plugins/page-tree-folders-plugin';

export const source = loader({
    source: docs.toFumadocsSource(),
    i18n,
    baseUrl: '/',
    plugins: [
        lucideIconsPlugin(),
        customIconsPlugin(),
        pageTreeCodeTitlesPlugin(),
        pageTreeFoldersPlugin(),
    ],
});

export type Page = InferPageType<typeof source>;
export type Meta = InferMetaType<typeof source>;
