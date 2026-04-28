import { loader } from 'fumadocs-core/source';
import { psjPlugin, psjSource } from 'psjapi/server';

import { i18n } from './i18n';
import { psjServer } from './psj-server';

export const psjDocs = loader({
    source: await psjSource(psjServer, {
        groupBy: 'domain',
        per: 'item',
        i18nParser: 'dir',
        versionInUrl: true,
    }),
    plugins: [psjPlugin()],
    baseUrl: '/sdk',
    i18n,
});
