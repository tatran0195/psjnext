import { createPSJAPIPage } from 'psjapi/ui';

import { psjServer } from '@/lib/psj-server';

export const APIPage = createPSJAPIPage(psjServer, {
    // Resolve $ref and see_also links to versioned URLs
    resolveRef: (ref) => {
        // ref is like "psj-command/Analysis-ADVC-MakeProcess-Static" or "macro/AdvcStaticProcess"
        // We can't know the current lang/version from here, so link to canonical path.
        // The middleware will redirect to the correct locale.
        const normalized = ref
            .replace(/([a-z])([A-Z])/g, '$1-$2') // split camelCase/PascalCase boundaries
            .replace(/_/g, '-')
            .toLowerCase();
        return `/sdk/${normalized}`; // resolved at render in layout or middleware
    },
});
