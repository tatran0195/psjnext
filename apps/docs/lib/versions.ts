// lib/versions.ts
// Version registry. Sửa file này khi thêm/xóa/đổi alias versions.
// source.config.ts và lib/source.ts cần được update theo.

export type VersionMeta = {
    label: string;
    frozen: boolean;
    // 'local'  → content committed trong repo (content/api/latest)
    // 'github' → pre-fetched bởi CI vào content/api/X.Y.Z
    sourceType: 'local' | 'github';
};

export const VERSION_META = {
    latest: { label: 'latest', frozen: false, sourceType: 'local' },
    '5.1.0': { label: '5.1.0', frozen: true, sourceType: 'github' },
    '5.0.1': { label: '5.0.1', frozen: true, sourceType: 'github' },
} satisfies Record<string, VersionMeta>;

export type CanonicalVersion = keyof typeof VERSION_META;

// Alias → canonical. Update khi release version mới.
export const VERSION_ALIASES: Record<string, CanonicalVersion> = {
    stable: '5.1.0',
};

// Chỉ các keys này mới được serve — cả canonical lẫn alias.
export const ACTIVE_VERSIONS = ['latest', 'stable', '5.1.0', '5.0.1'] as const;
export type ActiveVersion = (typeof ACTIVE_VERSIONS)[number];

// ─── Helpers ──────────────────────────────────────────────────────────────────

export function resolveVersion(key: string): CanonicalVersion | null {
    if (key in VERSION_META) return key as CanonicalVersion;
    if (key in VERSION_ALIASES) return VERSION_ALIASES[key]!;
    return null;
}

export function isVersionActive(key: string): boolean {
    return (ACTIVE_VERSIONS as readonly string[]).includes(key);
}

export function getVersionMeta(key: string): VersionMeta | null {
    const canonical = resolveVersion(key);
    return canonical ? VERSION_META[canonical] : null;
}

/** Canonical versions không duplicate (loại bỏ alias trùng canonical). */
export function getActiveCanonicalVersions(): CanonicalVersion[] {
    const seen = new Set<CanonicalVersion>();
    for (const key of ACTIVE_VERSIONS) {
        const canonical = resolveVersion(key);
        if (canonical) seen.add(canonical);
    }
    return [...seen];
}
