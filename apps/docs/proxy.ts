import { type NextFetchEvent, type NextRequest, NextResponse } from 'next/server';

import { createI18nMiddleware } from 'fumadocs-core/i18n/middleware';
import { isMarkdownPreferred, rewritePath } from 'fumadocs-core/negotiation';

import { i18n } from './lib/i18n';

const i18nMiddleware = createI18nMiddleware(i18n);

const { rewrite: rewriteLLM } = rewritePath('/docs/*path', '/llms.mdx/*path');
const { rewrite: rewriteMdx } = rewritePath('/docs{/*path}.mdx', '/llms.mdx{/*path}');

export const config = {
    matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};

export default async function proxy(request: NextRequest) {
    const i18nResult = await i18nMiddleware(request, {} as NextFetchEvent);
    if (i18nResult && i18nResult.status !== 200) {
        return i18nResult;
    }

    const result = rewriteMdx(request.nextUrl.pathname);
    if (result) {
        return NextResponse.rewrite(new URL(result, request.nextUrl));
    }

    if (isMarkdownPreferred(request)) {
        const result = rewriteLLM(request.nextUrl.pathname);

        if (result) {
            return NextResponse.rewrite(new URL(result, request.nextUrl));
        }
    }

    return NextResponse.next();
}
