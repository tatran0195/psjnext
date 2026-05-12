export type VersionStatus = 'available' | 'deprecated' | 'removed' | 'unavailable';

function parseSemver(v: string): [number, number, number] {
    const [a = 0, b = 0, c = 0] = v.split('.').map(Number);
    return [a, b, c];
}

/** Returns true if `a >= b` */
export function semverGte(a: string, b: string): boolean {
    const pa = parseSemver(a);
    const pb = parseSemver(b);
    for (let i = 0; i < 3; i++) {
        if (pa[i] > pb[i]) return true;
        if (pa[i] < pb[i]) return false;
    }
    return true;
}

export function getVersionStatus(
    version: string,
    introduced?: string,
    deprecated?: string,
    removed?: string,
): VersionStatus {
    if (introduced && !semverGte(version, introduced)) return 'unavailable';
    if (removed && semverGte(version, removed)) return 'removed';
    if (deprecated && semverGte(version, deprecated)) return 'deprecated';
    return 'available';
}

/** All statuses that are visible in the sidebar (not completely hidden) */
export function isVisible(status: VersionStatus): boolean {
    return status !== 'unavailable';
}
