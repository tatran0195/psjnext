import * as fs from 'node:fs';
import * as path from 'node:path';

import type { ItemFile, JCallManifest, LoadedSDK, ParamGroupFile, ResolvedItem } from './types';

import { loadSDK, loadSDKFromRaw } from './loader';
import { resolveAllItems } from './resolver';

export interface JCallOptions {
    /**
     * Path to `sdk.jcall.yaml`, or a function returning raw SDK data.
     */
    input:
        | string
        | (() =>
              | { manifest: JCallManifest; groups: ParamGroupFile[]; items: ItemFile[] }
              | Promise<{ manifest: JCallManifest; groups: ParamGroupFile[]; items: ItemFile[] }>);

    /**
     * Override the resolved version (defaults to manifest.current_version).
     */
    version?: string;

    /** Disable caching (re-loads SDK on every call) */
    disableCache?: boolean;
}

export interface JCallServer {
    readonly options: JCallOptions;
    /** Load and return the raw SDK (manifest + groups + items). */
    getSDK(): Promise<LoadedSDK>;
    /**
     * Return fully-resolved items for the given (or configured) version.
     * Keys are item ids.
     */
    getResolvedItems(version?: string): Promise<Map<string, ResolvedItem>>;
    /** @private Watch paths for file-change support */
    _getWatchPaths(): string[];
}

export function createJCall(options: JCallOptions): JCallServer {
    const { disableCache = false } = options;
    let cachedSDK: Promise<LoadedSDK> | undefined;

    async function getSDK(): Promise<LoadedSDK> {
        if (typeof options.input === 'string') {
            return loadSDK(options.input);
        }
        const raw = await options.input();
        return loadSDKFromRaw(raw.manifest, raw.groups, raw.items);
    }

    return {
        options,
        getSDK() {
            if (disableCache) return getSDK();
            return (cachedSDK ??= getSDK());
        },
        async getResolvedItems(version?: string) {
            const sdk = await this.getSDK();
            return resolveAllItems(sdk, version ?? options.version);
        },
        _getWatchPaths() {
            if (typeof options.input !== 'string') return [];
            const root = path.dirname(options.input);
            // Return all discovered yaml files that actually exist right now
            const candidates = [options.input];
            for (const sub of ['_groups', ...['macro', 'psj-command', 'psj-utility', 'psj-gui']]) {
                const dir = path.join(root, sub);
                if (fs.existsSync(dir)) {
                    try {
                        const files = fs.readdirSync(dir);
                        candidates.push(
                            ...files
                                .filter((f) => f.endsWith('.yaml') || f.endsWith('.yml'))
                                .map((f) => path.join(dir, f)),
                        );
                    } catch {
                        /* ignore */
                    }
                }
            }
            return candidates;
        },
    };
}
