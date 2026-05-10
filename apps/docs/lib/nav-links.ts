import type { LinkItemType } from '@/layouts/shared';

export const navLinks: LinkItemType[] = [
    { type: 'main', text: 'Home', url: '/en/landing', active: 'nested-url' },
    { type: 'main', text: 'Fundamentals', url: '/en', active: 'nested-url' },
    {
        type: 'main',
        text: 'Guides',
        url: '/en/guides/basic/database/Table_advanced_sample_2',
        active: 'nested-url',
    },
    {
        type: 'main',
        text: 'API Reference',
        url: '/en/api/5.1.0/psj-command/ac-modeling/ACModeling.ACBoundary.FirstMethod',
        active: 'nested-url',
    },
    { type: 'main', text: 'Showcase', url: '/en/showcase', active: 'nested-url' },
    { type: 'main', text: 'Changelog', url: '/en/changelog', active: 'nested-url' },
];
