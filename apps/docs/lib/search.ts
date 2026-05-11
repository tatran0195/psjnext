import { SortedResult } from 'fumadocs-core/search';

export function compareSemver(a: string, b: string) {
    const pa = a.split('.').map(Number);
    const pb = b.split('.').map(Number);

    for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
        const diff = (pa[i] ?? 0) - (pb[i] ?? 0);
        if (diff !== 0) return diff;
    }
    return 0;
}

export function matchesSearch(item: SortedResult<string> | undefined, searchString: string, exactMatch?: boolean) {
    if (!item || !searchString) {
        return true;
    }

    if (exactMatch) {
        return item.content.toLowerCase().includes(searchString.toLowerCase());
    }

    const searchTerms = searchString
        .split(/\s+/)
        .filter((term) => term.length > 0)
        .map((term) => term.toLowerCase());

    if (searchTerms.length === 0) {
        return true;
    }

    return searchTerms.some((term) => item.content.toLowerCase().includes(term));
}
