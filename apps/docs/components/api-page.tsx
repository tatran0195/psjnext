import { psjapi } from '@/lib/psjapi';
import { createPSJAPIPage } from 'psjapi/ui';

export const APIPage = createPSJAPIPage(psjapi, {
  shikiOptions: { themes: { light: 'catppuccin-latte', dark: 'catppuccin-mocha' } },
});
