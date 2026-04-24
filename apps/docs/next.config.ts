import type { NextConfig } from 'next';

import createBundleAnalyzer from '@next/bundle-analyzer';
import { createMDX } from 'fumadocs-mdx/next';

const withAnalyzer = createBundleAnalyzer({
    enabled: process.env.ANALYZE === 'true',
});

const config: NextConfig = {
    reactStrictMode: true,
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
};

const withMDX = createMDX();

export default withAnalyzer(withMDX(config));
