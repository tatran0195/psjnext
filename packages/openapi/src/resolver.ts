/**
 * JCALL v2 resolver — implements the algorithm from jcall.spec §5.
 *
 * Given a raw ItemFile and the full groups map, it:
 *   1. Starts from item.params as the base list (definition at version_introduced)
 *   2. Applies VersionDelta entries up to the requested version
 *   3. Expands every { $group } reference (with recursive `extends`, `exclude`, `insert_after`)
 *
 * The output is a ResolvedItem with a flat, ordered ResolvedParam list.
 */
import type {
    ItemFile,
    LoadedSDK,
    ManifestDomain,
    Param,
    ParamGroupFile,
    ParamOrGroupRef,
    ParamPatch,
    ParamWithAfter,
    ResolvedItem,
    ResolvedParam,
} from './types';

import { isGroupRef } from './types';
import { compareVersions } from './version';

// ─── Public API ───────────────────────────────────────────────────────────────

export function resolveItem(
    item: ItemFile,
    groups: Map<string, ParamGroupFile>,
    domainDef: ManifestDomain,
    targetVersion: string,
): ResolvedItem {
    // Step 1: start from the base param list
    let paramList: ParamOrGroupRef[] = [...item.params];

    // Step 2: apply version deltas in order
    const deltas = (item.changes ?? []).filter(
        (d) => compareVersions(d.version, targetVersion) <= 0,
    );
    for (const delta of deltas) {
        if (!delta.params) continue;
        const { add, remove, modify } = delta.params;

        if (remove) {
            paramList = paramList.filter(
                (p) => !isGroupRef(p) && p.name && !remove.includes(p.name),
            );
        }
        if (add) {
            for (const newParam of add) {
                paramList = insertParam(paramList, newParam);
            }
        }
        if (modify) {
            for (const patch of modify) {
                paramList = applyPatch(paramList, patch);
            }
        }
    }

    // Step 3: expand group refs into flat param list
    const resolvedParams = expandParams(paramList, groups);

    // Build top-level item fields, applying any item-level deltas
    let description = item.description;
    let ribbon = item.ribbon;
    let deprecated: boolean | undefined;

    for (const delta of deltas) {
        if (delta.item?.description) description = delta.item.description;
        if (delta.item?.ribbon) ribbon = delta.item.ribbon;
        if (delta.item?.deprecated) deprecated = delta.item.deprecated;
    }

    return {
        id: item.id,
        title: item.title,
        domain: item.domain,
        param_style: domainDef.param_style,
        group: item.group,
        namespace: item.namespace,
        ribbon,
        description,
        version_introduced: item.version_introduced,
        macro_link: item.macro_link,
        command_link: item.command_link,
        syntax: item.syntax,
        callouts: item.callouts,
        params: resolvedParams,
        returns: item.returns,
        examples: item.examples,
        see_also: item.see_also,
        deprecated,
        resolved_version: targetVersion,
    };
}

/**
 * Resolves all items in the SDK for the given version.
 * Defaults to manifest.current_version.
 */
export function resolveAllItems(sdk: LoadedSDK, version?: string): Map<string, ResolvedItem> {
    const targetVersion = version ?? sdk.manifest.current_version;
    const domainMap = new Map(sdk.manifest.domains.map((d) => [d.id, d]));
    const result = new Map<string, ResolvedItem>();

    for (const [id, item] of sdk.items) {
        const domainDef = domainMap.get(item.domain);
        if (!domainDef) {
            console.warn(`[JCALL] Unknown domain "${item.domain}" for item "${id}"`);
            continue;
        }
        // Skip items not yet introduced in this version
        if (compareVersions(item.version_introduced, targetVersion) > 0) continue;

        result.set(id, resolveItem(item, sdk.groups, domainDef, targetVersion));
    }

    return result;
}

// ─── Group expansion ──────────────────────────────────────────────────────────

function expandParams(
    params: ParamOrGroupRef[],
    groups: Map<string, ParamGroupFile>,
): ResolvedParam[] {
    const result: ResolvedParam[] = [];

    for (const p of params) {
        if (!isGroupRef(p)) {
            result.push(p as ResolvedParam);
            continue;
        }

        // Expand group (with recursive extends chain)
        let groupParams = expandGroup(p.$group, groups);

        // Apply exclude
        if (p.exclude?.length) {
            groupParams = groupParams.filter((gp) => !p.exclude!.includes(gp.name));
        }

        // Apply insert_after / insert
        if (p.insert_after && p.insert?.length) {
            const insertIdx = groupParams.findIndex((gp) => gp.name === p.insert_after);
            if (insertIdx !== -1) {
                groupParams.splice(insertIdx + 1, 0, ...(p.insert as ResolvedParam[]));
            } else {
                groupParams.push(...(p.insert as ResolvedParam[]));
            }
        }

        result.push(...groupParams);
    }

    return result;
}

/** Recursively expand a group (following `extends`), return flat param list. */
function expandGroup(groupId: string, groups: Map<string, ParamGroupFile>): ResolvedParam[] {
    const group = groups.get(groupId);
    if (!group) {
        console.warn(`[JCALL] Group "${groupId}" not found`);
        return [];
    }

    let base: ResolvedParam[] = [];
    if (group.extends) {
        base = expandGroup(group.extends, groups);
    }

    return [...base, ...(group.params as ResolvedParam[])];
}

// ─── Delta helpers ────────────────────────────────────────────────────────────

function insertParam(list: ParamOrGroupRef[], newParam: ParamWithAfter): ParamOrGroupRef[] {
    const { after, ...param } = newParam;
    if (!after) return [...list, param as Param];

    const idx = list.findIndex((p) => !isGroupRef(p) && (p as Param).name === after);
    if (idx === -1) return [...list, param as Param];

    const copy = [...list];
    copy.splice(idx + 1, 0, param as Param);
    return copy;
}

function applyPatch(list: ParamOrGroupRef[], patch: ParamPatch): ParamOrGroupRef[] {
    return list.map((p) => {
        if (isGroupRef(p) || (p as Param).name !== patch.name) return p;
        const updated = { ...(p as Param) };
        const { description, default: def, required, type, enum_values } = patch.changes;
        if (description !== undefined) updated.description = description;
        if (def !== undefined) updated.default = def;
        if (required !== undefined) updated.required = required;
        if (type !== undefined) updated.type = type;
        if (enum_values) {
            let evs = [...(updated.enum_values ?? [])];
            if (enum_values.remove) {
                evs = evs.filter((e) => !enum_values.remove!.includes(e.id));
            }
            if (enum_values.add) {
                evs = [...evs, ...enum_values.add];
            }
            updated.enum_values = evs;
        }
        return updated;
    });
}
