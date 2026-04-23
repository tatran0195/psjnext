import { i18n } from '@/lib/i18n';
import { docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';

import * as apiV5_1_0 from 'collections/5.1.0/server';
import * as apiV5_2_0 from 'collections/5.2.0/server';
import { customIconsPlugin } from './plugins/custom-icons-plugin';
import { pageTreeCodeTitlesPlugin } from './plugins/page-tree-code-titles-plugin';
import { pageTreeFoldersPlugin } from './plugins/page-tree-folders-plugin';

const sharedConfig = {
    i18n,
    plugins: [
        lucideIconsPlugin(),
        customIconsPlugin(),
        pageTreeCodeTitlesPlugin(),
        pageTreeFoldersPlugin(),
    ],
}

export const docsSource = loader({
    docs: docs.toFumadocsSource(),
    'api/5.2.0': apiV5_2_0.docs.toFumadocsSource(),
    'api/5.1.0': apiV5_1_0.docs.toFumadocsSource(),
}, {
    ...sharedConfig,
    baseUrl: '/',
});

export type Page = InferPageType<typeof docsSource>;
export type Meta = InferMetaType<typeof docsSource>;
