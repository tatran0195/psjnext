import { createPSJAPIPage } from 'psjapi/ui';

import { psjServer } from '@/lib/psj-server';

export const APIPage = createPSJAPIPage(psjServer, {
    resolveRef: (ref, locale) => `/${locale}/sdk/${ref.toLowerCase().replace(/\./g, '-')}`,
});
