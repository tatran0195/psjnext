import { type NextFetchEvent, type NextRequest, NextResponse } from 'next/server';

import { createI18nMiddleware } from 'fumadocs-core/i18n/middleware';
import { isMarkdownPreferred, rewritePath } from 'fumadocs-core/negotiation';

import { i18n } from './lib/i18n';

const i18nMiddleware = createI18nMiddleware(i18n);

const { rewrite: rewriteLLM } = rewritePath('/:lang/docs{/*path}', '/llms.mdx/:lang/docs{/*path}');
const { rewrite: rewriteMdx } = rewritePath('/:lang/docs{/*path}.mdx', '/llms.mdx/:lang/docs{/*path}');

export const config = {
    matcher: ['/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:png|jpg|jpeg|gif|webp|avif|svg|ico)).*)'],
};

export default async function proxy(request: NextRequest, event: NextFetchEvent) {
    const { pathname } = request.nextUrl;

    // ── 1. LLM / MDX rewrites — run BEFORE i18n so paths are matched as-is ──
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

    // ── 2. fumadocs i18n — handles locale detection, prefix redirect, cookie ──
    return i18nMiddleware(request, event);
}
