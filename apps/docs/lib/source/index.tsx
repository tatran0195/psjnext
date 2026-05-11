import { changelog as changelogPosts, docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';
import { toFumadocsSource } from 'fumadocs-mdx/runtime/server';

import { i18n } from '../i18n';
import { customIconsPlugin } from './plugins/custom-icons-plugin';
import { pageTreeCodeTitlesPlugin } from './plugins/page-tree-code-titles-plugin';
import { versionPlugin } from './plugins/version-plugin';

export const APP_VERSIONS = ['5.0.1', '5.1.0'];

export const source = loader({
    source: docs.toFumadocsSource(),
    i18n,
    baseUrl: '/',
    plugins: [
        versionPlugin(),
        lucideIconsPlugin(),
        customIconsPlugin(),
        pageTreeCodeTitlesPlugin(),
        // pageTreeFoldersPlugin(),
    ],
});

export type Page = InferPageType<typeof source>;
export type Meta = InferMetaType<typeof source>;

export const changelog = loader({
    source: toFumadocsSource(changelogPosts, []),
    baseUrl: '/changelog',
    i18n,
});
