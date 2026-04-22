// psjd/src/sidecar.ts
//
// Sidecar translation file support for psjd v2.
//
// A sidecar mirrors the structure of a base item/group file but contains
// ONLY translatable string fields. Everything structural is absent:
//   id, domain, type, default, required, position, $group, macro_link,
//   version_introduced, changes.params.{add,remove}, syntax, code, kind,
//   psjd, inferred, deprecated, deprecated_in, removed_in, version
//
// File naming:  <base-name>.<locale>.yaml
//   e.g.  Analysis-Nastran-LinearStatic.ja.yaml
//         nastran-base.ja.yaml
//
// The sidecar loader is called inside createSDK when a `locale` option is
// supplied. Merged items are stored in sdk.items exactly like unlocalized
// items — resolveItem requires zero changes.

import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

import type {
    Callout,
    EnumValue,
    Example,
    ItemFile,
    Param,
    ParamGroupFile,
    ParamOrGroupRef,
    ParamPatch,
    ParamsDelta,
    Ref,
    ReturnCode,
    Returns,
    VersionDelta,
} from './types.js';

// ─── Sidecar schema types ─────────────────────────────────────────────────────
//
// Every field is optional — a translator only fills what they have.
// Structural fields (id, type, required, position, $group, …) never appear.

export interface SidecarEnumValue {
    /** Must match the base enum's numeric/string id exactly (used for lookup) */
    id: number | string;
    label?: string;
    description?: string;
}

export interface SidecarParam {
    /**
     * For named params: matches Param.name.
     * For positional macro params: also matches Param.name (the C identifier).
     * Used as the lookup key — never translated itself.
     */
    name: string;
    display_name?: string;
    description?: string;
    enum_values?: SidecarEnumValue[];
}

export interface SidecarReturnCode {
    /** Matches ReturnCode.value exactly */
    value: string;
    meaning?: string;
}

export interface SidecarReturns {
    description?: string;
    codes?: SidecarReturnCode[];
}

export interface SidecarCallout {
    /** 0-based index into item.callouts[] */
    index: number;
    text?: string;
}

export interface SidecarExample {
    /** 0-based index into item.examples[] */
    index: number;
    title?: string;
    // `code` and `language` are structural — absent from sidecar
}

export interface SidecarRef {
    /** Matches Ref.$ref exactly */
    $ref: string;
    label?: string;
}

export interface SidecarVersionDeltaItem {
    description?: string;
    ribbon?: string;
    notes?: string;
}

export interface SidecarVersionDeltaParamsAdd {
    /** Matches the added Param.name */
    name: string;
    display_name?: string;
    description?: string;
    enum_values?: SidecarEnumValue[];
}

export interface SidecarVersionDeltaParamsModify {
    /** Matches ParamPatch.name */
    name: string;
    changes?: {
        description?: string;
        enum_values?: {
            add?: SidecarEnumValue[];
        };
    };
}

export interface SidecarVersionDelta {
    /** Matches VersionDelta.version — structural key used for lookup */
    version: string;
    notes?: string;
    item?: SidecarVersionDeltaItem;
    params?: {
        add?: SidecarVersionDeltaParamsAdd[];
        modify?: SidecarVersionDeltaParamsModify[];
    };
}

/** Sidecar for an item file (<domain>/<id>.<locale>.yaml) */
export interface SidecarItemFile {
    /** Must be "2.0" — used to detect accidentally-named base files */
    psjd: '2.0';
    kind: 'sidecar';
    /** Must match the base item's id */
    id: string;
    locale: string;
    // Translatable top-level fields
    title?: string;
    description?: string;
    ribbon?: string;
    // Structured translatable content
    callouts?: SidecarCallout[];
    params?: SidecarParam[];
    returns?: SidecarReturns;
    examples?: SidecarExample[];
    see_also?: SidecarRef[];
    changes?: SidecarVersionDelta[];
}

/** Sidecar for a param group file (_groups/<id>.<locale>.yaml) */
export interface SidecarParamGroupFile {
    psjd: '2.0';
    kind: 'sidecar';
    /** Must match the base group's id */
    id: string;
    locale: string;
    description?: string;
    params?: SidecarParam[];
}

// ─── Validation ───────────────────────────────────────────────────────────────

export interface SidecarValidationError {
    file: string;
    message: string;
}

/**
 * Validate a sidecar against its base item.
 * Returns an array of errors (empty = valid).
 * Does not throw — callers decide whether to warn or fail hard.
 */
export function validateItemSidecar(
    sidecar: SidecarItemFile,
    base: ItemFile,
    sidecarPath: string,
): SidecarValidationError[] {
    const errors: SidecarValidationError[] = [];
    const file = sidecarPath;

    if (sidecar.id !== base.id) {
        errors.push({
            file,
            message: `sidecar id "${sidecar.id}" does not match base id "${base.id}"`,
        });
    }

    // Collect all concrete param names from the base (skip GroupRef entries)
    const baseParamNames = new Set<string>(
        base.params
            .filter((p): p is Param => !('$group' in p))
            .map((p) => p.name)
            .filter((n): n is string => n !== undefined),
    );

    for (const sp of sidecar.params ?? []) {
        if (!baseParamNames.has(sp.name)) {
            errors.push({
                file,
                message: `sidecar param "${sp.name}" not found in base item "${base.id}" (only concrete params can be translated here; group params go in the group sidecar)`,
            });
        }
        // Validate enum value ids
        const baseParam = base.params
            .filter((p): p is Param => !('$group' in p))
            .find((p) => p.name === sp.name);
        if (baseParam && sp.enum_values) {
            const baseEnumIds = new Set((baseParam.enum_values ?? []).map((e) => String(e.id)));
            for (const se of sp.enum_values) {
                if (!baseEnumIds.has(String(se.id))) {
                    errors.push({
                        file,
                        message: `sidecar enum id "${se.id}" on param "${sp.name}" not found in base`,
                    });
                }
            }
        }
    }

    // Validate callout indices
    for (const sc of sidecar.callouts ?? []) {
        if (sc.index < 0 || sc.index >= (base.callouts ?? []).length) {
            errors.push({
                file,
                message: `sidecar callout index ${sc.index} out of range (base has ${(base.callouts ?? []).length} callouts)`,
            });
        }
    }

    // Validate example indices
    for (const se of sidecar.examples ?? []) {
        if (se.index < 0 || se.index >= (base.examples ?? []).length) {
            errors.push({
                file,
                message: `sidecar example index ${se.index} out of range (base has ${(base.examples ?? []).length} examples)`,
            });
        }
    }

    // Validate see_also $ref keys
    const baseSeeAlsoRefs = new Set((base.see_also ?? []).map((r) => r.$ref));
    for (const sr of sidecar.see_also ?? []) {
        if (!baseSeeAlsoRefs.has(sr.$ref)) {
            errors.push({
                file,
                message: `sidecar see_also $ref "${sr.$ref}" not found in base`,
            });
        }
    }

    // Validate version delta keys
    const baseVersions = new Set((base.changes ?? []).map((c) => c.version));
    for (const sd of sidecar.changes ?? []) {
        if (!baseVersions.has(sd.version)) {
            errors.push({
                file,
                message: `sidecar change version "${sd.version}" not found in base changes`,
            });
        }
    }

    return errors;
}

export function validateGroupSidecar(
    sidecar: SidecarParamGroupFile,
    base: ParamGroupFile,
    sidecarPath: string,
): SidecarValidationError[] {
    const errors: SidecarValidationError[] = [];
    const file = sidecarPath;

    if (sidecar.id !== base.id) {
        errors.push({
            file,
            message: `sidecar id "${sidecar.id}" does not match base group id "${base.id}"`,
        });
    }

    const baseParamNames = new Set(
        base.params.map((p) => p.name).filter((n): n is string => n !== undefined),
    );

    for (const sp of sidecar.params ?? []) {
        if (!baseParamNames.has(sp.name)) {
            errors.push({
                file,
                message: `sidecar param "${sp.name}" not found in base group "${base.id}"`,
            });
        }
        const baseParam = base.params.find((p) => p.name === sp.name);
        if (baseParam && sp.enum_values) {
            const baseEnumIds = new Set((baseParam.enum_values ?? []).map((e) => String(e.id)));
            for (const se of sp.enum_values) {
                if (!baseEnumIds.has(String(se.id))) {
                    errors.push({
                        file,
                        message: `sidecar enum id "${se.id}" on param "${sp.name}" not found in base group`,
                    });
                }
            }
        }
    }

    return errors;
}

// ─── Merge helpers ────────────────────────────────────────────────────────────

function mergeEnumValues(
    base: EnumValue[],
    sidecarEnums: SidecarEnumValue[] | undefined,
): EnumValue[] {
    if (!sidecarEnums || sidecarEnums.length === 0) return base;
    const byId = new Map(sidecarEnums.map((e) => [String(e.id), e]));
    return base.map((ev) => {
        const t = byId.get(String(ev.id));
        if (!t) return ev;
        return {
            ...ev,
            ...(t.label !== undefined ? { label: t.label } : {}),
            ...(t.description !== undefined ? { description: t.description } : {}),
        };
    });
}

function mergeParam(base: Param, sidecarParam: SidecarParam | undefined): Param {
    if (!sidecarParam) return base;
    return {
        ...base,
        ...(sidecarParam.display_name !== undefined
            ? { display_name: sidecarParam.display_name }
            : {}),
        ...(sidecarParam.description !== undefined
            ? { description: sidecarParam.description }
            : {}),
        ...(sidecarParam.enum_values && base.enum_values
            ? { enum_values: mergeEnumValues(base.enum_values, sidecarParam.enum_values) }
            : {}),
    };
}

function mergeParamList(
    base: ParamOrGroupRef[],
    sidecarParams: SidecarParam[] | undefined,
): ParamOrGroupRef[] {
    if (!sidecarParams || sidecarParams.length === 0) return base;
    const byName = new Map(sidecarParams.map((p) => [p.name, p]));
    return base.map((p) => {
        if ('$group' in p) return p; // GroupRef — not translated here
        if (!p.name) return p;
        const sp = byName.get(p.name);
        return sp ? mergeParam(p, sp) : p;
    });
}

function mergeReturns(base: Returns, sidecarReturns: SidecarReturns | undefined): Returns {
    if (!sidecarReturns) return base;
    const merged: Returns = {
        ...base,
        ...(sidecarReturns.description !== undefined
            ? { description: sidecarReturns.description }
            : {}),
    };
    if (sidecarReturns.codes && base.codes) {
        const byValue = new Map(sidecarReturns.codes.map((c) => [c.value, c]));
        merged.codes = base.codes.map((rc): ReturnCode => {
            const t = byValue.get(rc.value);
            return t?.meaning !== undefined ? { ...rc, meaning: t.meaning } : rc;
        });
    }
    return merged;
}

function mergeCallouts(
    base: Callout[] | undefined,
    sidecarCallouts: SidecarCallout[] | undefined,
): Callout[] | undefined {
    if (!base || !sidecarCallouts || sidecarCallouts.length === 0) return base;
    const byIndex = new Map(sidecarCallouts.map((c) => [c.index, c]));
    return base.map((callout, i) => {
        const t = byIndex.get(i);
        return t?.text !== undefined ? { ...callout, text: t.text } : callout;
    });
}

function mergeExamples(
    base: Example[] | undefined,
    sidecarExamples: SidecarExample[] | undefined,
): Example[] | undefined {
    if (!base || !sidecarExamples || sidecarExamples.length === 0) return base;
    const byIndex = new Map(sidecarExamples.map((e) => [e.index, e]));
    return base.map((ex, i) => {
        const t = byIndex.get(i);
        return t?.title !== undefined ? { ...ex, title: t.title } : ex;
    });
}

function mergeSeeAlso(
    base: Ref[] | undefined,
    sidecarRefs: SidecarRef[] | undefined,
): Ref[] | undefined {
    if (!base || !sidecarRefs || sidecarRefs.length === 0) return base;
    const byRef = new Map(sidecarRefs.map((r) => [r.$ref, r]));
    return base.map((ref) => {
        const t = byRef.get(ref.$ref);
        return t?.label !== undefined ? { ...ref, label: t.label } : ref;
    });
}

function mergeParamsDeltaAdd(
    base: Array<Param & { after?: string }> | undefined,
    sidecarAdd: SidecarVersionDeltaParamsAdd[] | undefined,
): Array<Param & { after?: string }> | undefined {
    if (!base || !sidecarAdd || sidecarAdd.length === 0) return base;
    const byName = new Map(sidecarAdd.map((p) => [p.name, p]));
    return base.map((p) => {
        const sp = p.name ? byName.get(p.name) : undefined;
        if (!sp) return p;
        return {
            ...p,
            ...(sp.display_name !== undefined ? { display_name: sp.display_name } : {}),
            ...(sp.description !== undefined ? { description: sp.description } : {}),
            ...(sp.enum_values && p.enum_values
                ? { enum_values: mergeEnumValues(p.enum_values, sp.enum_values) }
                : {}),
        };
    });
}

function mergeParamsDeltaModify(
    base: ParamPatch[] | undefined,
    sidecarModify: SidecarVersionDeltaParamsModify[] | undefined,
): ParamPatch[] | undefined {
    if (!base || !sidecarModify || sidecarModify.length === 0) return base;
    const byName = new Map(sidecarModify.map((m) => [m.name, m]));
    return base.map((patch): ParamPatch => {
        const sm = byName.get(patch.name);
        if (!sm?.changes) return patch;
        return {
            ...patch,
            changes: {
                ...patch.changes,
                ...(sm.changes.description !== undefined
                    ? { description: sm.changes.description }
                    : {}),
                ...(sm.changes.enum_values?.add && patch.changes.enum_values?.add
                    ? {
                          enum_values: {
                              ...patch.changes.enum_values,
                              add: mergeEnumValues(
                                  patch.changes.enum_values.add,
                                  sm.changes.enum_values.add,
                              ),
                          },
                      }
                    : {}),
            },
        };
    });
}

function mergeVersionDeltas(
    base: VersionDelta[] | undefined,
    sidecarDeltas: SidecarVersionDelta[] | undefined,
): VersionDelta[] | undefined {
    if (!base || !sidecarDeltas || sidecarDeltas.length === 0) return base;
    const byVersion = new Map(sidecarDeltas.map((d) => [d.version, d]));
    return base.map((delta): VersionDelta => {
        const sd = byVersion.get(delta.version);
        if (!sd) return delta;
        const merged: VersionDelta = { ...delta };
        if (sd.notes !== undefined) merged.notes = sd.notes;
        if (sd.item) {
            merged.item = {
                ...delta.item,
                ...(sd.item.description !== undefined ? { description: sd.item.description } : {}),
                ...(sd.item.ribbon !== undefined ? { ribbon: sd.item.ribbon } : {}),
                ...(sd.item.notes !== undefined ? { notes: sd.item.notes } : {}),
            };
        }
        if (sd.params && delta.params) {
            const mergedParams: ParamsDelta = { ...delta.params };
            const addedParams = mergeParamsDeltaAdd(delta.params.add, sd.params.add);
            if (addedParams !== undefined) mergedParams.add = addedParams;
            const modifiedParams = mergeParamsDeltaModify(delta.params.modify, sd.params.modify);
            if (modifiedParams !== undefined) mergedParams.modify = modifiedParams;
            merged.params = mergedParams;
        }
        return merged;
    });
}

// ─── Public merge functions ───────────────────────────────────────────────────

/**
 * Merge a sidecar translation into a base ItemFile.
 * Returns a new ItemFile — never mutates the base.
 */
export function mergeItemSidecar(base: ItemFile, sidecar: SidecarItemFile): ItemFile {
    const merged: ItemFile = { ...base };

    if (sidecar.title !== undefined) merged.title = sidecar.title;
    if (sidecar.description !== undefined) merged.description = sidecar.description;
    if (sidecar.ribbon !== undefined) merged.ribbon = sidecar.ribbon;

    const callouts = mergeCallouts(base.callouts, sidecar.callouts);
    if (callouts !== undefined) merged.callouts = callouts;

    merged.params = mergeParamList(base.params, sidecar.params);

    const returns = mergeReturns(base.returns, sidecar.returns);
    merged.returns = returns;

    const examples = mergeExamples(base.examples, sidecar.examples);
    if (examples !== undefined) merged.examples = examples;

    const seeAlso = mergeSeeAlso(base.see_also, sidecar.see_also);
    if (seeAlso !== undefined) merged.see_also = seeAlso;

    const changes = mergeVersionDeltas(base.changes, sidecar.changes);
    if (changes !== undefined) merged.changes = changes;

    return merged;
}

/**
 * Merge a sidecar translation into a base ParamGroupFile.
 * Returns a new ParamGroupFile — never mutates the base.
 */
export function mergeGroupSidecar(
    base: ParamGroupFile,
    sidecar: SidecarParamGroupFile,
): ParamGroupFile {
    const merged: ParamGroupFile = { ...base };

    if (sidecar.description !== undefined) merged.description = sidecar.description;

    if (sidecar.params && sidecar.params.length > 0) {
        const byName = new Map(sidecar.params.map((p) => [p.name, p]));
        merged.params = base.params.map((p) => {
            const sp = p.name ? byName.get(p.name) : undefined;
            return sp ? mergeParam(p, sp) : p;
        });
    }

    return merged;
}

// ─── File discovery and loading ───────────────────────────────────────────────

/**
 * Derive the sidecar file path from a base file path and locale.
 * e.g. /content/psj-command/Analysis-Nastran-LinearStatic.yaml + "ja"
 *   → /content/psj-command/Analysis-Nastran-LinearStatic.ja.yaml
 */
export function sidecarPath(baseFilePath: string, locale: string): string {
    const ext = path.extname(baseFilePath); // ".yaml"
    const base = baseFilePath.slice(0, -ext.length); // strip extension
    return `${base}.${locale}${ext}`;
}

/**
 * Try to load and parse a sidecar file.
 * Returns null if the file does not exist (not an error — translation is optional).
 * Throws on parse errors or wrong `kind`.
 */
export function tryLoadSidecar(filePath: string): SidecarItemFile | SidecarParamGroupFile | null {
    if (!fs.existsSync(filePath)) return null;
    const raw = fs.readFileSync(filePath, 'utf8');
    const parsed = parseYaml(raw);
    if (parsed.kind !== 'sidecar') {
        throw new Error(
            `Sidecar file "${filePath}" must have kind: sidecar (got kind: "${parsed.kind}")`,
        );
    }
    return parsed as SidecarItemFile | SidecarParamGroupFile;
}

/**
 * Apply sidecar translations to an entire ParsedSDK in-place.
 * Called by createSDK when a locale is specified.
 *
 * @param items     Mutable items map from the just-loaded ParsedSDK
 * @param groups    Mutable groups map from the just-loaded ParsedSDK
 * @param rootDir   The SDK root directory (contains _groups/ + domain folders)
 * @param domainIds All domain ids from the manifest
 * @param locale    e.g. "ja"
 * @param strict    If true, throw on validation errors. If false, log warnings.
 */
export function applySidecars(opts: {
    items: Map<string, import('./types.js').ItemFile>;
    groups: Map<string, ParamGroupFile>;
    rootDir: string;
    domainIds: string[];
    locale: string;
    strict?: boolean;
}): void {
    const { items, groups, rootDir, domainIds, locale, strict = false } = opts;

    const report = (errors: SidecarValidationError[]) => {
        for (const e of errors) {
            const msg = `[psjd] sidecar validation: ${e.message} (${e.file})`;
            if (strict) throw new Error(msg);
            console.warn(msg);
        }
    };

    // ── Groups ─────────────────────────────────────────────────────────────────
    const groupsDir = path.join(rootDir, '_groups');
    if (fs.existsSync(groupsDir)) {
        for (const [groupId, baseGroup] of groups) {
            // Find the base file to derive the sidecar path
            const candidates = [`${groupId}.yaml`, `${groupId}.yml`];
            for (const fname of candidates) {
                const basePath = path.join(groupsDir, fname);
                if (!fs.existsSync(basePath)) continue;
                const scPath = sidecarPath(basePath, locale);
                const sc = tryLoadSidecar(scPath);
                if (!sc) break;
                const groupSC = sc as SidecarParamGroupFile;
                report(validateGroupSidecar(groupSC, baseGroup, scPath));
                groups.set(groupId, mergeGroupSidecar(baseGroup, groupSC));
                break;
            }
        }
    }

    // ── Items ──────────────────────────────────────────────────────────────────
    for (const domainId of domainIds) {
        const domainDir = path.join(rootDir, domainId);
        if (!fs.existsSync(domainDir)) continue;
        for (const [itemId, baseItem] of items) {
            if (baseItem.domain !== domainId) continue;
            const candidates = [`${itemId}.yaml`, `${itemId}.yml`];
            for (const fname of candidates) {
                const basePath = path.join(domainDir, fname);
                if (!fs.existsSync(basePath)) continue;
                const scPath = sidecarPath(basePath, locale);
                const sc = tryLoadSidecar(scPath);
                if (!sc) break;
                const itemSC = sc as SidecarItemFile;
                report(validateItemSidecar(itemSC, baseItem, scPath));
                items.set(itemId, mergeItemSidecar(baseItem, itemSC));
                break;
            }
        }
    }
}
