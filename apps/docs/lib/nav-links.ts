import type { LinkItemType } from '@/layouts/shared';

export const navLinks: LinkItemType[] = [
    { type: 'main', text: 'Home', url: '/', active: 'nested-url' },
    { type: 'main', text: 'Showcase', url: '/showcase', active: 'nested-url' },
    { type: 'main', text: 'Changelog', url: '/changelog', active: 'nested-url' },
];
