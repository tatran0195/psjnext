import Link from 'next/link';

import { ApiVersion } from '@/lib/api-versions';

interface VersionMeta {
    version: string;
    status: string;
}

interface Props {
    title: string;
    version: ApiVersion;
    removedIn: string;
    versionMeta: VersionMeta[];
}

export function TombstonePage({ title, version, removedIn, versionMeta }: Props) {
    const lastAvailable = [...versionMeta].filter((v) => v.status !== 'removed').at(-1);

    return (
        <div style={{ padding: '40px 0' }}>
            <div
                style={{
                    border: '1px solid var(--color-border-danger)',
                    borderRadius: 8,
                    padding: '24px 28px',
                    background: 'var(--color-background-danger)',
                    marginBottom: 24,
                }}
            >
                <p
                    style={{
                        margin: 0,
                        fontSize: 13,
                        color: 'var(--color-text-danger)',
                        fontWeight: 500,
                    }}
                >
                    Removed in {removedIn}
                </p>
                <h2 style={{ margin: '8px 0 4px', color: 'var(--color-text-primary)' }}>{title}</h2>
                <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: 14 }}>
                    This API was removed in version {removedIn} and is no longer available in{' '}
                    {version}.
                </p>
            </div>

            {lastAvailable && (
                <p style={{ fontSize: 14, color: 'var(--color-text-secondary)' }}>
                    Last available in{' '}
                    <Link
                        href={`/docs/api/${lastAvailable.version}`}
                        style={{ color: 'var(--color-text-info)' }}
                    >
                        v{lastAvailable.version}
                    </Link>
                    .
                </p>
            )}
        </div>
    );
}
