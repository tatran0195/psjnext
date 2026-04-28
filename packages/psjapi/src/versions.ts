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
        switch: (currentPath, newVersionId) => switchVersion(currentPath, newVersionId),
    };
}

// ─── Standalone URL helper ────────────────────────────────────────────────────

/**
 * Rewrite the version segment inside a path of the shape:
 *   /[lang]/sdk/[version]/[...slug]
 *
 * Also available as `versions.switch(path, newId)` on a {@link SdkVersions}
 * object, which avoids importing this directly.
 *
 * @example
 * switchVersion('/en/sdk/5.0.1/macro/foo', '5.1.0')
 *   // → '/en/sdk/5.1.0/macro/foo'
 */
export function switchVersion(currentPath: string, newVersionId: string): string {
    const parts = currentPath.split('/');
    // ['', lang, 'sdk', version, ...slug]
    if (parts.length >= 4 && parts[2] === 'sdk') {
        parts[3] = newVersionId;
        return parts.join('/');
    }
    return currentPath;
}
