import registry from '../versions.json';

export type VersionMeta = {
    label: string;
    frozen: boolean;
    sourceType: 'local' | 'git';
};

export const VERSION_META = registry.meta as Record<string, VersionMeta>;

export type CanonicalVersion = keyof typeof VERSION_META;

export const ACTIVE_VERSIONS = registry.active as readonly string[];
export type ActiveVersion = (typeof ACTIVE_VERSIONS)[number];

// ─── Helpers ──────────────────────────────────────────────────────────────────

export function isVersionActive(key: string): boolean {
    return (ACTIVE_VERSIONS as readonly string[]).includes(key);
}

export function getVersionMeta(key: string): VersionMeta | null {
    return VERSION_META[key as CanonicalVersion] ?? null;
}
