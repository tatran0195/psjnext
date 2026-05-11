export interface BreadcrumbItem {
    name: string;
    url?: string;
}

export const SPECIAL_PAGES_BREADCRUMBS: Record<string, BreadcrumbItem[]> = {
    '/landing': [{ name: 'Home', url: '/' }, { name: 'PSJ — Python Scripting for Jupiter' }],
    '/showcase': [{ name: 'Home', url: '/' }, { name: 'Showcase Catalog' }],
    '/changelog': [{ name: 'Home', url: '/' }, { name: 'Changelog' }],
};

/**
 * Resolves breadcrumbs for pages that are not part of the standard Fumadocs tree.
 */
export function getSpecialPageBreadcrumbs(pathname: string): BreadcrumbItem[] | null {
    // Remove trailing slash and find matching key
    const cleanPath = pathname.replace(/\/$/, '');

    for (const [route, items] of Object.entries(SPECIAL_PAGES_BREADCRUMBS)) {
        if (cleanPath.includes(route)) {
            return items;
        }
    }

    return null;
}
