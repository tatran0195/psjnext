export type VersionMeta = {
    label: string;
    frozen: boolean;
    sourceType: 'local' | 'git';
};

export const VERSION_META = {
    '5.1.0': { label: '5.1.0', frozen: false, sourceType: 'local' },
    '5.0.1': { label: '5.0.1', frozen: true, sourceType: 'git' },
} satisfies Record<string, VersionMeta>;

export type CanonicalVersion = keyof typeof VERSION_META;

export const ACTIVE_VERSIONS = ['5.1.0', '5.0.1'] as const;
export type ActiveVersion = (typeof ACTIVE_VERSIONS)[number];

// ─── Helpers ──────────────────────────────────────────────────────────────────

export function isVersionActive(key: string): boolean {
    return (ACTIVE_VERSIONS as readonly string[]).includes(key);
}

export function getVersionMeta(key: string): VersionMeta | null {
    return VERSION_META[key as CanonicalVersion] ?? null;
}
