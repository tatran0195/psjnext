import { Suggestion } from '@/components/layouts/not-found';
import { env } from '@/env';

interface SearchResult {
    id: string;
    url: string;
    type: 'page' | 'heading' | 'text';
    content: string;
}

const IGNORED_EXTENSIONS = [
    '.png',
    '.jpg',
    '.jpeg',
    '.gif',
    '.svg',
    '.webp',
    '.ico',
    '.css',
    '.js',
    '.map',
    '.txt',
    '.xml',
];

function shouldIgnorePath(pathname: string): boolean {
    const lower = pathname.toLowerCase();

    return (
        IGNORED_EXTENSIONS.some((ext) => lower.endsWith(ext)) ||
        lower.startsWith('/_next') ||
        lower.startsWith('/api') ||
        lower === '/favicon.ico' ||
        lower === '/robots.txt' ||
        lower === '/sitemap.xml'
    );
}

function normalizeQuery(pathname: string): string {
    return decodeURIComponent(pathname)
        .replace(/^\/+/, '')
        .replace(/\.[a-z0-9]+$/i, '')
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .replace(/[\W_]+/g, ' ')
        .toLowerCase()
        .trim();
}

export async function getSuggestions(pathname: string): Promise<Suggestion[]> {
    if (!pathname || shouldIgnorePath(pathname)) {
        return [];
    }

    const query = normalizeQuery(pathname);

    if (!query) return [];

    try {
        const params = new URLSearchParams({ query });

        const baseUrl = typeof window !== 'undefined' ? '' : env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000';

        const res = await fetch(`${baseUrl}/api/search?${params}`, {
            next: {
                revalidate: 60,
            },
        });

        if (!res.ok) {
            return [];
        }

        const results: SearchResult[] = await res.json();

        if (!Array.isArray(results)) {
            return [];
        }

        const seen = new Set<string>();

        const ranked = results
            .filter((result) => result.type === 'page')
            .filter((result) => {
                if (seen.has(result.url)) {
                    return false;
                }

                seen.add(result.url);
                return true;
            })
            .map((result) => ({
                result,
                score: scoreResult(result, query),
            }))
            .filter(({ score }) => score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 5);

        return ranked.map(({ result }) => ({
            id: result.id,
            href: result.url,
            title: result.content,
        }));
    } catch (error) {
        console.error('Failed to get suggestions:', error);

        return [];
    }
}

function scoreResult(result: SearchResult, query: string): number {
    const q = query.toLowerCase().trim();

    const content = result.content.toLowerCase();
    const url = result.url.toLowerCase();

    let score = 0;

    // Exact title match
    if (content === q) score += 100;

    // Exact URL match
    if (url === q || url.endsWith(`/${q}`)) {
        score += 90;
    }

    // Starts with query
    if (content.startsWith(q)) {
        score += 50;
    }

    // URL contains query
    if (url.includes(q)) {
        score += 40;
    }

    // Content contains query
    if (content.includes(q)) {
        score += 30;
    }

    // Token matching
    const tokens = q.split(/\s+/);

    for (const token of tokens) {
        if (content.includes(token)) {
            score += 10;
        }

        if (url.includes(token)) {
            score += 8;
        }
    }

    // Prefer shorter URLs
    score -= url.length * 0.05;

    return score;
}
