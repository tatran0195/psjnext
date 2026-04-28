import { createI18nMiddleware } from 'fumadocs-core/i18n/middleware';
import { isMarkdownPreferred, rewritePath } from 'fumadocs-core/negotiation';
import { type NextFetchEvent, type NextRequest, NextResponse } from 'next/server';
import { i18n } from './lib/i18n';

const i18nMiddleware = createI18nMiddleware(i18n);

const { rewrite: rewriteLLM } = rewritePath('/:lang/docs{/*path}', '/llms.mdx/:lang/docs{/*path}');
const { rewrite: rewriteMdx } = rewritePath('/:lang/docs{/*path}.mdx', '/llms.mdx/:lang/docs{/*path}');

export const config = {
    matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};

export default async function proxy(request: NextRequest, event: NextFetchEvent) {
    const response = await i18nMiddleware(request, event);

    if (response?.status && response.status >= 300 && response.status < 400) {
        return response;
    }

    const { pathname } = request.nextUrl;

    const mdxResult = rewriteMdx(pathname);
    if (mdxResult) {
        return NextResponse.rewrite(new URL(mdxResult, request.nextUrl));
    }

    if (isMarkdownPreferred(request)) {
        const llmResult = rewriteLLM(pathname);
        if (llmResult) {
            return NextResponse.rewrite(new URL(llmResult, request.nextUrl));
        }
    }

    return response || NextResponse.next();
}
