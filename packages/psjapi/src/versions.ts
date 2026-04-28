import type { SdkManifest, SdkVersion, SdkVersions } from './types';

// ─── Private factory ──────────────────────────────────────────────────────────

/** Build a {@link SdkVersions} value object from a raw manifest. */
export function buildSdkVersions(manifest: SdkManifest): SdkVersions {
    const all: SdkVersion[] = manifest.versions.map((v) => {
        const isCurrent = v.id === manifest.current_version;
        return {
            id: v.id,
            label: isCurrent ? `${v.id} (latest)` : v.id,
            isCurrent,
        };
    });

    const current = all.find((v) => v.isCurrent) ?? all[0];
    const ids = all.map((v) => v.id);

    return {
        all,
        current,
        ids,
        find: (id) => all.find((v) => v.id === id),
    };
}
