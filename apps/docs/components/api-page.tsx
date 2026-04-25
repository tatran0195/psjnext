import { createPSJAPIPage } from 'psjapi/ui';

import { psjapi } from '@/lib/psjapi';

export const APIPage = createPSJAPIPage(psjapi, {
    shikiOptions: { themes: { light: 'catppuccin-latte', dark: 'catppuccin-mocha' } },
});
