import type { NextConfig } from 'next';

import createBundleAnalyzer from '@next/bundle-analyzer';
import { createMDX } from 'fumadocs-mdx/next';
import createNextIntlPlugin from 'next-intl/plugin';

const withAnalyzer = createBundleAnalyzer({
    enabled: process.env.ANALYZE === 'true',
});
const withNextIntl = createNextIntlPlugin('./i18n/request.ts');

const versions = (process.env.API_VERSIONS || '').split(',').filter(Boolean);
const latestVersion = versions[0] || '5.1.0';

const config: NextConfig = {
    env: {
        API_VERSIONS: process.env.API_VERSIONS,
    },
    reactStrictMode: true,
    transpilePackages: ['@mermaid-js/layout-elk'],

    logging: {
        fetches: {
            fullUrl: true,
        },
    },

    serverExternalPackages: [
        'ts-morph',
        'typescript',
        'oxc-transform',
        'twoslash',
        'shiki',
        '@takumi-rs/image-response',
    ],

    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'avatars.githubusercontent.com',
                port: '',
            },
        ],
    },

    async redirects() {
        if (versions.length <= 1) return [];
        return [
            {
                source: '/docs/api/:product(macro|psj-command|psj-gui)',
                destination: `/docs/api/${latestVersion}/:product`,
                permanent: false,
            },
            {
                source: '/docs/data-types',
                destination: `/docs/api/${latestVersion}/data-types`,
                permanent: false,
            },
        ];
    },
};

const withMDX = createMDX();

export default withAnalyzer(withNextIntl(withMDX(config)));
