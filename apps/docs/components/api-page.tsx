import { psjServer } from '@/lib/psj-server';
import { createPSJAPIPage } from 'psjapi/ui';

export const APIPage = createPSJAPIPage(psjServer, {
    resolveRef: (ref, locale) => `/${locale}/sdk/${ref.toLowerCase().replace(/\./g, '-')}`,
});
