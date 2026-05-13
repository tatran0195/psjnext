import { changelog as changelogPosts, docs } from 'collections/server';
import { type InferMetaType, type InferPageType, loader } from 'fumadocs-core/source';
import { slugsPlugin } from 'fumadocs-core/source/slugs';
import { statusBadgesPlugin } from 'fumadocs-core/source/status-badges';
import { toFumadocsSource } from 'fumadocs-mdx/runtime/server';

import { env } from '@/env';
// import { i18n } from '../i18n';
import { i18nDocsConfig as i18n } from '@/i18n/routing';

import { codeTitlesPlugin } from './plugins/code-titles-plugin';
import { iconsPlugin } from './plugins/icons-plugin';
import { versionPlugin } from './plugins/version-plugin';

export const APP_VERSIONS = ['5.0.1', '5.1.0'];

export const source = loader({
    source: docs.toFumadocsSource(),
    i18n,
    baseUrl: '/docs',
    plugins: [iconsPlugin(), codeTitlesPlugin(), versionPlugin(), statusBadgesPlugin(), slugsPlugin()],
});

export type Page = InferPageType<typeof source>;
export type Meta = InferMetaType<typeof source>;

export const changelog = loader({
    source: toFumadocsSource(changelogPosts, []),
    baseUrl: '/changelog',
    i18n,
});

export function getApiVersions() {
    const changelogMap = new Map(
        changelog.getPages().map((p) => [p.data.version.startsWith('v') ? p.data.version.slice(1) : p.data.version, p]),
    );

    return env.API_VERSIONS.map((version) => {
        const page = changelogMap.get(version);

        return {
            value: version,
            releasedAt: page?.data.date ?? null,
        };
    });
}
