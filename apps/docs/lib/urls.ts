/**
 * Normalize a URL or path by removing trailing slashes
 */
export function normalize(urlOrPath: string) {
    if (urlOrPath.length > 1 && urlOrPath.endsWith('/')) return urlOrPath.slice(0, -1);
    return urlOrPath;
}

/**
 * Check if a URL or path is active
 * @param href - The URL or path to check
 * @param pathname - The current pathname
 * @param nested - Whether to check for nested paths
 * @returns True if the URL or path is active, false otherwise
 */
export function isActive(href: string, pathname: string, nested = false): boolean {
    href = normalize(href);
    pathname = normalize(pathname);

    return href === pathname || (nested && pathname.startsWith(`${href}/`));
}
