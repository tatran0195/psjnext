import { llms } from 'fumadocs-core/source';

import { docsSource } from '@/lib/source';

export const revalidate = false;

export function GET() {
    return new Response(llms(docsSource).index());
}
