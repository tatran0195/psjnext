'use client';
import { useRouter } from 'next/navigation';

import type { ApiVersion } from '@/lib/source/plugins/version-plugin';

interface VersionMeta {
    version: string;
    status: 'available' | 'deprecated' | 'removed';
}

interface Props {
    currentVersion: ApiVersion;
    baseSlug: string[];
    versionMeta: VersionMeta[];
    status: 'available' | 'deprecated' | 'removed';
}

const statusLabel: Record<string, string> = {
    available: '',
    deprecated: 'deprecated',
    removed: 'removed',
};

const statusColor: Record<string, string> = {
    available: 'var(--color-text-secondary)',
    deprecated: 'var(--color-text-warning)',
    removed: 'var(--color-text-danger)',
};

export function VersionDropdown({ currentVersion, baseSlug, versionMeta, status }: Props) {
    const router = useRouter();

    return (
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 20 }}>
            <label
                htmlFor="api-version-select"
                style={{ fontSize: 13, color: 'var(--color-text-secondary)' }}
            >
                API version
            </label>
            <select
                id="api-version-select"
                value={currentVersion}
                onChange={(e) => {
                    router.push(`/app/${e.target.value}/${baseSlug.join('/')}`);
                }}
                style={{
                    fontSize: 13,
                    padding: '3px 8px',
                    borderRadius: 6,
                    border: '1px solid var(--color-border-primary)',
                    background: 'var(--color-background-secondary)',
                    color: 'var(--color-text-primary)',
                }}
            >
                {versionMeta.map(({ version, status: vStatus }) => (
                    <option key={version} value={version}>
                        {version}
                        {statusLabel[vStatus] ? ` (${statusLabel[vStatus]})` : ''}
                    </option>
                ))}
            </select>

            {status !== 'available' && (
                <span
                    style={{
                        fontSize: 12,
                        fontWeight: 500,
                        color: statusColor[status],
                        background:
                            status === 'deprecated'
                                ? 'var(--color-background-warning)'
                                : 'var(--color-background-danger)',
                        padding: '2px 8px',
                        borderRadius: 4,
                    }}
                >
                    {status}
                </span>
            )}
        </div>
    );
}
