'use client';
import { type Dispatch, type SetStateAction, createContext, PropsWithChildren, use, useMemo, useState } from 'react';

export interface VersionItem {
    value: string;
    releasedAt: string | null;
}

export interface VersionProviderProps {
    versions: VersionItem[];
}

interface VersionContextType {
    versions: VersionItem[];
    /** The currently selected API version value, or undefined when "All" is selected. */
    currentVersion: string | undefined;
    setCurrentVersion: Dispatch<SetStateAction<string | undefined>>;
}

const VersionContext = createContext<VersionContextType>({
    versions: [],
    currentVersion: undefined,
    setCurrentVersion: () => {},
});

export function useVersionContext(): VersionContextType {
    return use(VersionContext);
}

export function VersionProvider({ versions, children }: PropsWithChildren<VersionProviderProps>) {
    // Default to the first (latest) version when there are API versions available.
    const [currentVersion, setCurrentVersion] = useState<string | undefined>(versions[0]?.value);

    const ctx = useMemo<VersionContextType>(
        () => ({ versions, currentVersion, setCurrentVersion }),
        [versions, currentVersion],
    );

    return <VersionContext value={ctx}>{children}</VersionContext>;
}
