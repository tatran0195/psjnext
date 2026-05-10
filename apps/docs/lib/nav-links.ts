import type { LinkItemType } from '@/layouts/shared';

export const navLinks: LinkItemType[] = [
    { type: 'main', text: 'Home', url: '/landing', active: 'nested-url' },
    { type: 'main', text: 'Fundamentals', url: '/docs', active: 'nested-url' },
    { type: 'main', text: 'Tutorials', url: '/docs/tutorials', active: 'nested-url' },
    { type: 'main', text: 'API Reference', url: '/docs/api', active: 'nested-url' },
    { type: 'main', text: 'Showcase', url: '/showcase', active: 'nested-url' },
];
