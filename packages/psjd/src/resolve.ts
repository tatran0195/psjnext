// psjd/src/resolve.ts
// Implements Section 5 of the psjd v2 spec exactly.
// All outputs are plain serializable objects — no Map/Set leakage.

import type {
    GroupRef,
    ItemFile,
    Param,
    ParamOrGroupRef,
    ParamsDelta,
    ParsedSDK,
    ResolvedItem,
    ResolvedParam,
} from './types.js';

// ─── Semver utilities ─────────────────────────────────────────────────────────

/**
 * Compare two X.Y.Z version strings numerically.
 * Returns negative if a < b, 0 if equal, positive if a > b.
 * Exported so UI components can use it without re-implementing.
 */
export function semverCompare(a: string, b: string): number {
    const pa = a.split('.').map(Number);
    const pb = b.split('.').map(Number);
    for (let i = 0; i < 3; i++) {
        const diff = (pa[i] ?? 0) - (pb[i] ?? 0);
        if (diff !== 0) return diff;
    }
    return 0;
}

export function semverLte(a: string, b: string): boolean {
    return semverCompare(a, b) <= 0;
}

export function semverGte(a: string, b: string): boolean {
    return semverCompare(a, b) >= 0;
}

// ─── Type guard ───────────────────────────────────────────────────────────────

function isGroupRef(p: ParamOrGroupRef): p is GroupRef {
    return '$group' in p;
}

// ─── Group expansion ──────────────────────────────────────────────────────────

/**
 * Recursively expand all { $group } references in a param list.
 *
 * Handles:
 *   - group.extends          (recursive inheritance, circular detection)
 *   - exclude                (drop named params after expansion)
 *   - insert_after + insert  (splice params at a named position)
 */
export function expandGroups(
    sdk: ParsedSDK,
    params: ParamOrGroupRef[],
    _seen: Set<string> = new Set(),
): ResolvedParam[] {
    const out: ResolvedParam[] = [];

    for (const p of params) {
        if (!isGroupRef(p)) {
            // Plain param — copy to avoid mutating source
            out.push({ ...p } as ResolvedParam);
            continue;
        }

        const groupId = p.$group;

        // Circular reference guard
        if (_seen.has(groupId)) {
            throw new Error(
                `Circular group extends detected at "${groupId}". Chain: ${[..._seen, groupId].join(' → ')}`,
            );
        }

        const group = sdk.groups.get(groupId);
        if (!group) {
            throw new Error(`Unknown param group: "${groupId}"`);
        }

        // Build the group's param list, prepending the parent group if extends is set
        const groupParams: ParamOrGroupRef[] = group.extends
            ? [{ $group: group.extends } satisfies GroupRef, ...group.params]
            : [...group.params];

        // Recursively expand
        let resolved = expandGroups(sdk, groupParams, new Set([..._seen, groupId]));

        // Apply exclude
        if (p.exclude && p.exclude.length > 0) {
            const excSet = new Set(p.exclude);
            resolved = resolved.filter((rp) => !excSet.has(rp.name));
        }

        // Apply insert_after + insert
        if (p.insert_after != null && p.insert && p.insert.length > 0) {
            const idx = resolved.findIndex((rp) => rp.name === p.insert_after);
            if (idx === -1) {
                throw new Error(
                    `insert_after: param "${p.insert_after}" not found in expanded group "${groupId}". ` +
                        `Available params: ${resolved.map((r) => r.name).join(', ')}`,
                );
            }
            // Expand any nested group refs inside insert
            const inserted = expandGroups(sdk, p.insert as ParamOrGroupRef[], _seen);
            resolved = [...resolved.slice(0, idx + 1), ...inserted, ...resolved.slice(idx + 1)];
        }

        out.push(...resolved);
    }

    return out;
}

// ─── Delta application ────────────────────────────────────────────────────────

function applyParamsDelta(params: ResolvedParam[], delta: ParamsDelta): ResolvedParam[] {
    // Work on a shallow copy — never mutate the input
    let result = [...params];

    // 1. remove
    if (delta.remove && delta.remove.length > 0) {
        const removeSet = new Set(delta.remove);
        result = result.filter((p) => !removeSet.has(p.name));
    }

    // 2. add — insert at named position or append
    if (delta.add && delta.add.length > 0) {
        for (const addition of delta.add) {
            // Destructure the `after` key (not part of Param spec)
            const { after, ...paramDef } = addition as Param & { after?: string };
            const newParam: ResolvedParam = { ...paramDef, name: paramDef.name ?? '' };
            if (after) {
                const idx = result.findIndex((p) => p.name === after);
                if (idx !== -1) {
                    result = [...result.slice(0, idx + 1), newParam, ...result.slice(idx + 1)];
                } else {
                    result = [...result, newParam];
                }
            } else {
                result = [...result, newParam];
            }
        }
    }

    // 3. modify — patch individual fields on existing params
    if (delta.modify && delta.modify.length > 0) {
        result = result.map((p) => {
            const patch = delta.modify!.find((m) => m.name === p.name);
            if (!patch) return p;

            const updated: ResolvedParam = { ...p };

            if (patch.changes.description !== undefined) {
                updated.description = patch.changes.description;
            }
            if (patch.changes.default !== undefined) {
                updated.default = patch.changes.default;
            }
            if (patch.changes.required !== undefined) {
                updated.required = patch.changes.required;
            }

            if (patch.changes.enum_values) {
                let evs = [...(updated.enum_values ?? [])];
                if (patch.changes.enum_values.remove) {
                    const removeIds = new Set(patch.changes.enum_values.remove.map(String));
                    evs = evs.filter((e) => !removeIds.has(String(e.id)));
                }
                if (patch.changes.enum_values.add) {
                    evs = [...evs, ...patch.changes.enum_values.add];
                }
                updated.enum_values = evs;
            }

            return updated;
        });
    }

    return result;
}

// ─── Item-level delta ─────────────────────────────────────────────────────────

/**
 * Apply item-level field overrides from a VersionDelta.
 * Returns new fields to merge into the resolved item.
 */
function collectItemOverrides(
    item: ItemFile,
    version: string,
): { description: string; ribbon?: string; deprecated?: boolean; versionNotes?: string } {
    let description = item.description;
    let ribbon = item.ribbon;
    let deprecated = item.deprecated;

    const result: {
        description: string;
        ribbon?: string;
        deprecated?: boolean;
        versionNotes?: string;
    } = { description };

    if (ribbon !== undefined) result.ribbon = ribbon;
    if (deprecated !== undefined) result.deprecated = deprecated;

    if (!item.changes) return result;

    const sorted = [...item.changes].sort((a, b) => semverCompare(a.version, b.version));

    for (const delta of sorted) {
        if (!semverLte(delta.version, version)) break;
        if (delta.item) {
            if (delta.item.description !== undefined) result.description = delta.item.description;
            if (delta.item.ribbon !== undefined) result.ribbon = delta.item.ribbon;
            if (delta.item.deprecated !== undefined) result.deprecated = delta.item.deprecated;
        }
        if (delta.notes) result.versionNotes = delta.notes;
    }

    return result;
}

// ─── Public API ───────────────────────────────────────────────────────────────

/**
 * Fully resolve a callable item at a given SDK version.
 *
 * Implements spec Section 5:
 *   1. Start with item.params as the base (state at version_introduced)
 *   2. Expand all { $group } references (groups may also have extends)
 *   3. Walk item.changes in semver order; apply each delta ≤ requested version
 *
 * Returns a plain serializable `ResolvedItem` — no Map/Set, safe across
 * the RSC/client boundary.
 */
export function resolveItem(sdk: ParsedSDK, itemId: string, version: string): ResolvedItem {
    const item = sdk.items.get(itemId);
    if (!item) throw new Error(`Unknown item id: "${itemId}"`);

    if (semverCompare(version, item.version_introduced) < 0) {
        throw new Error(
            `Item "${itemId}" was introduced in ${item.version_introduced}; ` +
                `cannot resolve at ${version}.`,
        );
    }

    // Step 1 + 2: expand groups on the base param list
    let params = expandGroups(sdk, item.params);

    // Step 3: apply version deltas in order
    if (item.changes && item.changes.length > 0) {
        const sorted = [...item.changes].sort((a, b) => semverCompare(a.version, b.version));
        for (const delta of sorted) {
            if (!semverLte(delta.version, version)) break;
            if (delta.params) {
                params = applyParamsDelta(params, delta.params);
            }
        }
    }

    // Collect item-level field overrides
    const overrides = collectItemOverrides(item, version);

    // Determine param_style from the item's domain definition
    const domain = sdk.manifest.domains.find((d) => d.id === item.domain);
    const paramStyle = domain?.param_style ?? 'named';

    // Build a plain serializable object — explicitly pick fields, no spread of
    // ItemFile (which contains params: ParamOrGroupRef[] and changes arrays)
    const resolved: ResolvedItem = {
        id: item.id,
        title: item.title,
        domain: item.domain,
        description: overrides.description,
        version_introduced: item.version_introduced,
        returns: item.returns,
        resolvedParams: params,
        resolvedVersion: version,
        paramStyle,
    };

    // Optional fields — only set if present to keep the object clean
    if (overrides.ribbon !== undefined) resolved.ribbon = overrides.ribbon;
    if (item.group !== undefined) resolved.group = item.group;
    if (item.namespace !== undefined) resolved.namespace = item.namespace;
    if (item.author !== undefined) resolved.author = item.author;
    if (item.author_url !== undefined) resolved.author_url = item.author_url;
    if (item.macro_link !== undefined) resolved.macro_link = item.macro_link;
    if (item.command_link !== undefined) resolved.command_link = item.command_link;
    if (item.syntax !== undefined) resolved.syntax = item.syntax;
    if (item.callouts !== undefined) resolved.callouts = item.callouts;
    if (item.examples !== undefined) resolved.examples = item.examples;
    if (item.see_also !== undefined) resolved.see_also = item.see_also;
    if (item.deprecated_in !== undefined) resolved.deprecated_in = item.deprecated_in;
    if (item.removed_in !== undefined) resolved.removed_in = item.removed_in;
    if (overrides.deprecated !== undefined) resolved.deprecated = overrides.deprecated;
    if (overrides.versionNotes !== undefined) resolved.versionNotes = overrides.versionNotes;

    return resolved;
}

/**
 * Resolve every item in the SDK at a given version.
 * Items introduced after `version` are silently excluded.
 */
export function resolveAll(sdk: ParsedSDK, version: string): ResolvedItem[] {
    const results: ResolvedItem[] = [];
    for (const [, item] of sdk.items) {
        if (semverCompare(version, item.version_introduced) < 0) continue;
        results.push(resolveItem(sdk, item.id, version));
    }
    return results;
}
