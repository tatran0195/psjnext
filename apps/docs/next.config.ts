import type { NextConfig } from 'next';

import createBundleAnalyzer from '@next/bundle-analyzer';
import { createMDX } from 'fumadocs-mdx/next';

const withAnalyzer = createBundleAnalyzer({
    enabled: process.env.ANALYZE === 'true',
});

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
        return [
            {
                source: '/:lang/docs',
                destination: '/:lang',
                permanent: true,
            },

            {
                source: '/:lang/docs/:path*',
                destination: '/:lang/:path*',
                permanent: true,
            },
        ];
    },
};

const withMDX = createMDX();

export default withAnalyzer(withMDX(config));
