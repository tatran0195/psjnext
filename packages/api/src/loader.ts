import { readdir, readFile, stat } from 'node:fs/promises';
import * as path from 'node:path';
import { parse as parseYaml } from 'yaml';

import type {
    Callout,
    CalloutTranslation,
    DataTypeFile,
    DataTypeLocaleSidecar,
    Domain,
    EnumValue,
    EnumValuePatch,
    EnumValueTranslations,
    Example,
    ExampleTranslation,
    Field,
    GroupLocaleSidecar,
    GroupMetaFile,
    GroupRef,
    ItemFile,
    ItemLocaleSidecar,
    Param,
    ParamGroupFile,
    ParamOrGroupRef,
    ParamTranslation,
    ProcessedSdk,
    PSJAPIOptions,
    PSJAPIServer,
    ResolvedDataType,
    ResolvedField,
    ResolvedItem,
    ResolvedParam,
    Returns,
    SdkManifest,
    VersionDelta,
} from './types';

import { buildSdkVersions } from './versions';

type ParamWithGroup = Param & { _fromGroup?: string };

// ─── Internal cache ───────────────────────────────────────────────────────────

interface LoadedSdk extends ProcessedSdk {
    /** Locale sidecars keyed by "<domain>/<id>.<locale>" */
    itemSidecars: Map<string, ItemLocaleSidecar>;
    /** Group sidecars keyed by "<group-id>.<locale>" */
    groupSidecars: Map<string, GroupLocaleSidecar>;
    /** DataType locale sidecars keyed by "<id>.<locale>" */
    dataTypeSidecars: Map<string, DataTypeLocaleSidecar>;
    /** Group meta locale sidecars keyed by "<path>.<locale>" */
    groupMetaSidecars: Map<string, GroupMetaSidecar>;
}

/** Locale sidecar for group meta files (only localizable fields) */
interface GroupMetaSidecar {
    psj?: '3.3';
    kind?: 'group_meta';
    locale?: string;
    title?: string;
    description?: string;
}

async function walk(dir: string): Promise<string[]> {
    let results: string[] = [];
    try {
        const list = await readdir(dir);
        for (const file of list) {
            const filePath = path.join(dir, file);
            const statResult = await stat(filePath);
            if (statResult.isDirectory()) {
                results = results.concat(await walk(filePath));
            } else {
                results.push(filePath);
            }
        }
    } catch {
        // ignore
    }
    return results;
}

// ─── Guard helpers ────────────────────────────────────────────────────────────

function isGroupRef(p: ParamOrGroupRef): p is GroupRef {
    return '$group' in p;
}

// ─── Loader ──────────────────────────────────────────────────────────────────

async function safeReadYaml<T>(filePath: string): Promise<T | undefined> {
    try {
        const text = await readFile(filePath, 'utf-8');
        return parseYaml(text) as T;
    } catch {
        return undefined;
    }
}

async function loadSdk(rootDir: string): Promise<LoadedSdk> {
    const manifestPath = path.join(rootDir, 'sdk.psj.yaml');
    const manifest = (await safeReadYaml<SdkManifest>(manifestPath)) as SdkManifest;
    if (!manifest) {
        throw new Error(`[@psj/api] Could not read manifest at: ${manifestPath}`);
    }

    const items = new Map<string, ItemFile>();
    const groups = new Map<string, ParamGroupFile>();
    const dataTypes = new Map<string, DataTypeFile>();
    const groupMetas = new Map<string, GroupMetaFile>();
    const itemSidecars = new Map<string, ItemLocaleSidecar>();
    const groupSidecars = new Map<string, GroupLocaleSidecar>();
    const dataTypeSidecars = new Map<string, DataTypeLocaleSidecar>();
    const groupMetaSidecars = new Map<string, GroupMetaSidecar>();

    const DOMAIN_DIRS: Domain[] = ['macro', 'psj-command', 'psj-utility', 'psj-gui'];

    // Load param groups
    const groupsDir = path.join(rootDir, '_groups');
    let groupFiles: string[] = [];
    try {
        groupFiles = await readdir(groupsDir);
    } catch {
        // _groups/ is optional
    }

    for (const file of groupFiles) {
        if (!file.endsWith('.yaml')) continue;
        const filePath = path.join(groupsDir, file);
        const basename = file.slice(0, -5); // strip .yaml

        const localeMatch = basename.match(/^(.+)\.([a-z]{2})$/);
        if (localeMatch) {
            // locale sidecar
            const [, groupId, locale] = localeMatch;
            const sidecar = await safeReadYaml<GroupLocaleSidecar>(filePath);
            if (sidecar) {
                groupSidecars.set(`${groupId}.${locale}`, sidecar);
            }
        } else {
            // base group file
            const group = await safeReadYaml<ParamGroupFile>(filePath);
            if (group && group.kind === 'param_group') {
                groups.set(group.id, group);
            }
        }
    }

    // Load data-types
    const dataTypeDir = path.join(rootDir, 'data-type');
    const dtFiles = await walk(dataTypeDir);
    for (const filePath of dtFiles) {
        if (!filePath.endsWith('.yaml')) continue;
        const relativePath = path.relative(dataTypeDir, filePath).replace(/\\/g, '/');
        const dirName = path.dirname(relativePath);
        const basename = path.basename(relativePath, '.yaml');

        if (basename === 'meta') {
            const meta = await safeReadYaml<GroupMetaFile>(filePath);
            if (meta && meta.kind === 'group_meta') {
                groupMetas.set(`data-type/${dirName === '.' ? '' : dirName}`, meta);
            }
        } else if (basename.startsWith('meta.')) {
            const locale = basename.slice(5); // remove meta.
            const sidecar = await safeReadYaml<GroupMetaSidecar>(filePath);
            if (sidecar) groupMetaSidecars.set(`data-type/${dirName === '.' ? '' : dirName}.${locale}`, sidecar);
        } else {
            const localeMatch = basename.match(/^(.+)\.([a-z]{2})$/);
            if (localeMatch) {
                const [, , locale] = localeMatch;
                const itemId = relativePath.slice(0, -(locale.length + 6));
                const sidecar = await safeReadYaml<DataTypeLocaleSidecar>(filePath);
                if (sidecar) dataTypeSidecars.set(`${itemId}.${locale}`, sidecar);
            } else {
                const dt = await safeReadYaml<DataTypeFile>(filePath);
                if (dt && dt.kind === 'data_type') {
                    const itemId = relativePath.slice(0, -5);
                    dataTypes.set(itemId, dt);
                }
            }
        }
    }

    // Load items from domain directories
    for (const domain of DOMAIN_DIRS) {
        const domainDir = path.join(rootDir, domain);
        const domainFiles = await walk(domainDir);

        for (const filePath of domainFiles) {
            if (!filePath.endsWith('.yaml')) continue;
            const relativePath = path.relative(domainDir, filePath).replace(/\\/g, '/');
            const dirName = path.dirname(relativePath);
            const basename = path.basename(relativePath, '.yaml');

            if (basename === 'meta') {
                const meta = await safeReadYaml<GroupMetaFile>(filePath);
                if (meta && meta.kind === 'group_meta') {
                    // key includes domain to avoid collision, e.g. macro/SubFolder
                    groupMetas.set(`${domain}/${dirName === '.' ? '' : dirName}`.replace(/\/$/, ''), meta);
                }
            } else if (basename.startsWith('meta.')) {
                const locale = basename.slice(5); // remove meta.
                const sidecar = await safeReadYaml<GroupMetaSidecar>(filePath);
                if (sidecar)
                    groupMetaSidecars.set(
                        `${domain}/${dirName === '.' ? '' : dirName}`.replace(/\/$/, '') + `.${locale}`,
                        sidecar,
                    );
            } else {
                const localeMatch = basename.match(/^(.+)\.([a-z]{2})$/);
                if (localeMatch) {
                    const [, , locale] = localeMatch;
                    const itemId = relativePath.slice(0, -(locale.length + 6));
                    const sidecar = await safeReadYaml<ItemLocaleSidecar>(filePath);
                    if (sidecar) {
                        itemSidecars.set(`${domain}/${itemId}.${locale}`, sidecar);
                    }
                } else {
                    const item = await safeReadYaml<ItemFile>(filePath);
                    if (item && item.psj) {
                        const itemId = relativePath.slice(0, -5);
                        items.set(`${domain}/${itemId}`, item);
                    }
                }
            }
        }
    }

    return {
        manifest,
        items,
        groups,
        dataTypes,
        groupMetas,
        itemSidecars,
        groupSidecars,
        dataTypeSidecars,
        groupMetaSidecars,
    };
}

// ─── Group expansion ──────────────────────────────────────────────────────────

/** Recursively expand a group, respecting `extends`, returning flat Param list */
function expandGroup(groupId: string, groups: Map<string, ParamGroupFile>): ParamWithGroup[] {
    const group = groups.get(groupId);
    if (!group) {
        console.warn(`[@psj/api] Unknown group: ${groupId}`);
        return [];
    }

    let base: Param[] = [];
    if (group.extends) {
        base = expandGroup(group.extends, groups);
    }

    // Deduplicate — group's own params override base if same name
    const names = new Set(group.params.map((p) => p.name));
    const filtered = base.filter((p) => !names.has(p.name));
    return [...filtered, ...group.params];
}

/** Expand param list (which may contain GroupRef entries) into a flat Param list */
function expandParams(raw: ParamOrGroupRef[], groups: Map<string, ParamGroupFile>): ParamWithGroup[] {
    const result: Param[] = [];

    for (const entry of raw) {
        if (!isGroupRef(entry)) {
            result.push(entry);
            continue;
        }

        let groupParams: ParamWithGroup[] = expandGroup(entry.$group, groups).map((p) => ({
            ...p,
            _fromGroup: entry.$group,
        }));

        // exclude
        if (entry.exclude && entry.exclude.length > 0) {
            const excluded = new Set(entry.exclude);
            groupParams = groupParams.filter((p) => !excluded.has(p.name ?? ''));
        }

        // insert_after + insert
        if (entry.insert_after && entry.insert && entry.insert.length > 0) {
            const idx = groupParams.findIndex((p) => p.name === entry.insert_after);
            const inserted = entry.insert.map((p) => ({
                ...p,
                _fromGroup: entry.$group,
            }));
            if (idx !== -1) {
                groupParams.splice(idx + 1, 0, ...inserted);
            } else {
                groupParams.push(...inserted);
            }
        }

        // override — patch specific param fields without excluding
        if (entry.override) {
            groupParams = groupParams.map((p) => {
                const patch = entry.override![p.name ?? ''];
                if (!patch) return p;
                return {
                    ...p,
                    ...(patch.description !== undefined && { description: patch.description }),
                    ...(patch.default !== undefined && { default: patch.default }),
                    ...(patch.required !== undefined && { required: patch.required }),
                };
            });
        }

        result.push(...groupParams);
    }

    return result;
}

// ─── Version delta application ────────────────────────────────────────────────

/** Return the list of version ids up to and including `targetVersion`, in order */
function versionsUpTo(manifest: SdkManifest, targetVersion: string): string[] {
    const ids = manifest.versions.map((v) => v.id);
    const idx = ids.indexOf(targetVersion);
    return idx === -1 ? ids : ids.slice(0, idx + 1);
}

function applyEnumPatch(current: EnumValue[] | undefined, patch: EnumValuePatch): EnumValue[] {
    let result = [...(current ?? [])];
    if (patch.add) {
        result.push(...patch.add);
    }
    if (patch.remove) {
        const removeSet = new Set(patch.remove.map(String));
        result = result.filter((ev) => !removeSet.has(String(ev.id)));
    }
    return result;
}

function applyDeltasToParams(
    params: ParamWithGroup[],
    deltas: VersionDelta[],
    targetVersions: string[],
): ParamWithGroup[] {
    let result: ParamWithGroup[] = [...params];

    for (const delta of deltas) {
        if (!targetVersions.includes(delta.version)) continue;

        const { params: paramDelta } = delta;
        if (!paramDelta) continue;

        // remove
        if (paramDelta.remove) {
            const removeSet = new Set(paramDelta.remove);
            result = result.filter((p) => !removeSet.has(p.name ?? ''));
        }

        // add
        if (paramDelta.add) {
            for (const newParam of paramDelta.add) {
                const { after, ...param } = newParam as Param & { after?: string };
                if (after) {
                    const idx = result.findIndex((p) => p.name === after);
                    if (idx !== -1) {
                        result.splice(idx + 1, 0, param);
                    } else {
                        result.push(param);
                    }
                } else {
                    result.push(param);
                }
            }
        }

        // modify
        if (paramDelta.modify) {
            for (const patch of paramDelta.modify) {
                const idx = result.findIndex((p) => p.name === patch.name);
                if (idx === -1) continue;
                const existing = { ...result[idx] };
                const { changes } = patch;
                if (changes.description !== undefined) existing.description = changes.description;
                if (changes.default !== undefined) existing.default = changes.default;
                if (changes.required !== undefined) existing.required = changes.required;
                if (changes.deprecated !== undefined) existing.deprecated = changes.deprecated;
                if (changes.enum_values) {
                    existing.enum_values = applyEnumPatch(existing.enum_values, changes.enum_values);
                }
                result[idx] = existing;
            }
        }
    }

    return result;
}

function applyDeltasToFields(fields: Field[], deltas: VersionDelta[], targetVersions: string[]): Field[] {
    let result: Field[] = [...fields];

    for (const delta of deltas) {
        if (!targetVersions.includes(delta.version)) continue;
        const { fields: fieldDelta } = delta;
        if (!fieldDelta) continue;

        if (fieldDelta.remove) {
            const removeSet = new Set(fieldDelta.remove);
            result = result.filter((f) => !removeSet.has(f.name));
        }

        if (fieldDelta.add) {
            for (const newField of fieldDelta.add) {
                const { after, ...field } = newField as Field & { after?: string };
                if (after) {
                    const idx = result.findIndex((f) => f.name === after);
                    if (idx !== -1) result.splice(idx + 1, 0, field as Field);
                    else result.push(field as Field);
                } else {
                    result.push(field as Field);
                }
            }
        }

        if (fieldDelta.modify) {
            for (const patch of fieldDelta.modify) {
                const idx = result.findIndex((f) => f.name === patch.name);
                if (idx === -1) continue;
                const existing = { ...result[idx] };
                const { changes } = patch;
                if (changes.description !== undefined) existing.description = changes.description;
                if (changes.default !== undefined) existing.default = changes.default;
                if (changes.required !== undefined) existing.required = changes.required;
                if (changes.remarks !== undefined) existing.remarks = changes.remarks;
                if (changes.deprecated !== undefined) existing.deprecated = changes.deprecated;
                if (changes.enum_values) {
                    existing.enum_values = applyEnumPatch(existing.enum_values, changes.enum_values);
                }
                result[idx] = existing;
            }
        }
    }
    return result;
}

function applyDeltasToValues(values: EnumValue[], deltas: VersionDelta[], targetVersions: string[]): EnumValue[] {
    let result: EnumValue[] = [...values];
    for (const delta of deltas) {
        if (!targetVersions.includes(delta.version)) continue;
        const { values: valueDelta } = delta;
        if (!valueDelta) continue;

        if (valueDelta.remove) {
            const removeSet = new Set(valueDelta.remove.map(String));
            result = result.filter((v) => !removeSet.has(String(v.id)));
        }

        if (valueDelta.add) {
            for (const newVal of valueDelta.add) {
                const { after, ...val } = newVal as EnumValue & { after?: number | string };
                if (after !== undefined) {
                    const idx = result.findIndex((v) => String(v.id) === String(after));
                    if (idx !== -1) result.splice(idx + 1, 0, val as EnumValue);
                    else result.push(val as EnumValue);
                } else {
                    result.push(val as EnumValue);
                }
            }
        }

        if (valueDelta.modify) {
            for (const patch of valueDelta.modify) {
                const idx = result.findIndex((v) => String(v.id) === String(patch.id));
                if (idx === -1) continue;
                const existing = { ...result[idx] };
                const { changes } = patch;
                if (changes.label !== undefined) existing.label = changes.label;
                if (changes.description !== undefined) existing.description = changes.description;
                if (changes.deprecated !== undefined) existing.deprecated = changes.deprecated;
                result[idx] = existing;
            }
        }
    }
    return result;
}

// ─── Locale resolution ────────────────────────────────────────────────────────

function translateParam<T extends Param>(param: T, key: string, translation: ParamTranslation | undefined): T {
    if (!translation) return param;
    const result = { ...param };
    if (translation.display_name) result.display_name = translation.display_name;
    if (translation.description) result.description = translation.description;
    if (translation.enum_values && result.enum_values) {
        result.enum_values = result.enum_values.map((ev) => {
            const label = (translation.enum_values as EnumValueTranslations)?.[ev.id];
            return label ? { ...ev, label } : ev;
        });
    }
    return result;
}

function translateCallouts(
    callouts: Callout[],
    translations: Record<string, CalloutTranslation> | undefined,
): Callout[] {
    if (!translations) return callouts;
    return callouts.map((c) => {
        const t = translations[c.id];
        return t ? { ...c, text: t.text } : c;
    });
}

function translateReturns(returns: Returns, translation: ItemLocaleSidecar['returns']): Returns {
    if (!translation) return returns;
    const result = { ...returns };
    if (translation.description) result.description = translation.description;
    if (translation.codes && result.codes) {
        result.codes = result.codes.map((code) => {
            const meaning = (translation.codes as Record<string, string>)?.[code.value];
            return meaning ? { ...code, meaning } : code;
        });
    }
    return result;
}

function translateExamples(
    examples: Example[],
    translations: Record<string, ExampleTranslation> | undefined,
): Example[] {
    if (!translations) return examples;
    return examples.map((ex) => {
        const t = translations[ex.id];
        return t?.title ? { ...ex, title: t.title } : ex;
    });
}

// ─── Item resolution ──────────────────────────────────────────────────────────

export function resolveItem(item: ItemFile, sdk: LoadedSdk, version: string, locale: string): ResolvedItem {
    const { manifest, groups, itemSidecars, groupSidecars } = sdk;

    // 1. Expand group refs → flat params (as of introduced )
    let params: ParamWithGroup[] = expandParams(item.params, groups);

    // 2. Apply deltas up to requested version
    if (item.changes && item.changes.length > 0) {
        const targetVersions = versionsUpTo(manifest, version);
        params = applyDeltasToParams(params as Param[], item.changes, targetVersions) as ParamWithGroup[];
    }

    // 3. Determine top-level item fields including delta item patches
    let description = item.description;
    let ribbon = item.ribbon;
    let stability: import('./types').Stability = item.stability ?? 'stable';

    if (item.changes) {
        const targetVersions = versionsUpTo(manifest, version);
        for (const delta of item.changes) {
            if (!targetVersions.includes(delta.version)) continue;
            if (delta.item?.description) description = delta.item.description;
            if (delta.item?.ribbon) ribbon = delta.item.ribbon;
            if (delta.item?.stability) stability = delta.item.stability;
        }
    }
    const deprecated = stability === 'deprecated';

    // 4. Merge locale translations (en = no sidecar needed)
    let callouts = item.callouts ?? [];
    let returns = item.returns;
    let examples = item.examples ?? [];

    if (locale !== 'en') {
        const itemSidecarKey = `${item.domain}/${item.id}.${locale}`;
        const itemSidecar = itemSidecars.get(itemSidecarKey);

        if (itemSidecar) {
            if (itemSidecar.description) description = itemSidecar.description;
            callouts = translateCallouts(callouts, itemSidecar.callouts);
            returns = translateReturns(returns, itemSidecar.returns);
            examples = translateExamples(examples, itemSidecar.examples);

            // Translate item-specific params (not from a group)
            if (itemSidecar.params) {
                params = params.map((p) => {
                    if ((p as ParamWithGroup)._fromGroup) return p; // handled by group sidecar below
                    const key = p.position !== undefined ? String(p.position) : (p.name ?? '');
                    const t = (itemSidecar.params as Record<string, ParamTranslation>)?.[key];
                    return translateParam(p, key, t);
                });
            }
        }

        // Translate params that came from groups
        const groupIds = new Set(params.map((p) => (p as ParamWithGroup)._fromGroup).filter((p) => p !== undefined));
        for (const groupId of groupIds) {
            const groupSidecarKey = `${groupId}.${locale}`;
            const groupSidecar = groupSidecars.get(groupSidecarKey);
            if (!groupSidecar?.params) continue;

            params = params.map((p) => {
                if ((p as ParamWithGroup)._fromGroup !== groupId) return p;
                const key = p.position !== undefined ? String(p.position) : (p.name ?? '');
                const t = (groupSidecar.params as Record<string, ParamTranslation>)?.[key];
                return translateParam(p, key, t);
            });

            // If group has extends, walk up the chain
            const group = groups.get(groupId);
            if (group?.extends) {
                const parentSidecarKey = `${group.extends}.${locale}`;
                const parentSidecar = groupSidecars.get(parentSidecarKey);
                if (parentSidecar?.params) {
                    params = params.map((p) => {
                        if ((p as ParamWithGroup)._fromGroup !== groupId) return p;
                        // Only translate if not already translated by child group sidecar
                        const key = p.position !== undefined ? String(p.position) : (p.name ?? '');
                        const childTranslation = (groupSidecar.params as Record<string, ParamTranslation>)?.[key];
                        if (childTranslation) return p; // already handled
                        const t = (parentSidecar.params as Record<string, ParamTranslation>)?.[key];
                        return translateParam(p, key, t);
                    });
                }
            }
        }
    }

    // 5. Build resolved params (clean up internal _fromGroup marker)
    const resolvedParams: ResolvedParam[] = params.map((p) => {
        const { _fromGroup, ...rest } = p as ParamWithGroup;
        return {
            ...rest,
            name: rest.name ?? String(rest.position ?? ''),
            _fromGroup,
        } as ResolvedParam;
    });

    // 6. Apply version-aware deprecated_in / removed_in
    //    Build a version-order index: lower index = older version.
    const versionOrder = new Map<string, number>(manifest.versions.map((v, i) => [v.id, i] as [string, number]));
    const targetIdx = versionOrder.get(version) ?? manifest.versions.length - 1;

    const versionedParams = resolvedParams.map((p) => {
        let result = { ...p };
        // deprecated_in overrides the static deprecated flag:
        // mark as deprecated ONLY at or past deprecated_in version, clear it before.
        if (result.deprecated_in) {
            const depIdx = versionOrder.get(result.deprecated_in) ?? Infinity;
            if (depIdx <= targetIdx && !result.deprecated) {
                result.deprecated = true;
            } else if (depIdx > targetIdx) {
                delete result.deprecated;
            }
        }
        // Similarly for removed_in
        if (result.removed_in) {
            const remIdx = versionOrder.get(result.removed_in) ?? Infinity;
            result = { ...result, removed: remIdx <= targetIdx };
        }
        return result;
    });

    return {
        id: item.id,
        title: item.title,
        domain: item.domain,
        namespace: item.namespace,
        ribbon,
        stability,
        description,
        since: item.introduced,
        macro_link: item.macro_link,
        command_link: item.command_link,
        class_ref: item.class_ref,
        syntax: item.syntax,
        callouts,
        params: versionedParams,
        returns,
        examples,
        see_also: item.see_also ?? [],
        deprecated,
    };
}

export function resolveDataType(dt: DataTypeFile, sdk: LoadedSdk, version: string, locale: string): ResolvedDataType {
    const { manifest, dataTypeSidecars } = sdk;

    let values = dt.values ? [...dt.values] : undefined;
    let fields = dt.fields ? [...dt.fields] : undefined;

    if (dt.changes && dt.changes.length > 0) {
        const targetVersions = versionsUpTo(manifest, version);
        if (values) values = applyDeltasToValues(values, dt.changes, targetVersions);
        if (fields) fields = applyDeltasToFields(fields, dt.changes, targetVersions);
    }

    let description = dt.description;
    let stability = dt.stability ?? 'stable';

    if (dt.changes) {
        const targetVersions = versionsUpTo(manifest, version);
        for (const delta of dt.changes) {
            if (!targetVersions.includes(delta.version)) continue;
            if (delta.item?.description) description = delta.item.description;
            if (delta.item?.stability) stability = delta.item.stability;
        }
    }
    const deprecated = stability === 'deprecated';

    let examples = dt.examples ?? [];

    if (locale !== 'en') {
        const sidecarKey = `${dt.id}.${locale}`;
        const sidecar = dataTypeSidecars.get(sidecarKey);

        if (sidecar) {
            if (sidecar.description) description = sidecar.description;
            examples = translateExamples(examples, sidecar.examples);

            if (values && sidecar.values) {
                values = values.map((v) => {
                    const t = sidecar.values![v.id];
                    if (!t) return v;
                    return {
                        ...v,
                        ...(t.label && { label: t.label }),
                        ...(t.description && { description: t.description }),
                    };
                });
            }

            if (fields && sidecar.fields) {
                fields = fields.map((f) => {
                    const t = sidecar.fields![f.name];
                    if (!t) return f;
                    const res = { ...f };
                    if (t.description) res.description = t.description;
                    if (t.remarks) res.remarks = t.remarks;
                    if (t.enum_values && res.enum_values) {
                        res.enum_values = res.enum_values.map((ev) => {
                            const lbl = t.enum_values![ev.id];
                            return lbl ? { ...ev, label: lbl } : ev;
                        });
                    }
                    return res;
                });
            }
        }
    }

    const versionOrder = new Map<string, number>(manifest.versions.map((v, i) => [v.id, i] as [string, number]));
    const targetIdx = versionOrder.get(version) ?? manifest.versions.length - 1;

    let resolvedFields: ResolvedField[] | undefined;
    if (fields) {
        resolvedFields = fields.map((f) => {
            const res: ResolvedField = { ...f };
            if (res.deprecated_in) {
                const depIdx = versionOrder.get(res.deprecated_in) ?? Infinity;
                if (depIdx <= targetIdx && !res.deprecated) {
                    res.deprecated = true;
                } else if (depIdx > targetIdx) {
                    delete res.deprecated;
                }
            }
            if (res.removed_in) {
                const remIdx = versionOrder.get(res.removed_in) ?? Infinity;
                res.removed = remIdx <= targetIdx;
            }
            return res as ResolvedField;
        });
    }

    return {
        id: dt.id,
        title: dt.title,
        category: dt.category,
        namespace: dt.namespace,
        description,
        since: dt.introduced,
        stability,
        values,
        constructor_syntax: dt.constructor_syntax,
        fields: resolvedFields,
        methods: dt.methods,
        examples,
        see_also: dt.see_also ?? [],
        deprecated,
    };
}

// ─── createPSJAPI ─────────────────────────────────────────────────────────────

export function createPSJAPI(options: PSJAPIOptions): PSJAPIServer {
    const { root, disableCache = false, defaultLocale = 'en' } = options;

    // Resolve root to directory
    const rootDir = root.endsWith('.yaml') ? path.dirname(root) : root;

    let cachedLoad: Promise<LoadedSdk> | undefined;

    async function getLoadedSdk(): Promise<LoadedSdk> {
        if (!disableCache && cachedLoad) return cachedLoad;
        cachedLoad = loadSdk(rootDir);
        return cachedLoad;
    }

    return {
        options,

        async getProcessedSdk(): Promise<ProcessedSdk> {
            const sdk = await getLoadedSdk();
            return {
                manifest: sdk.manifest,
                items: sdk.items,
                groups: sdk.groups,
                dataTypes: sdk.dataTypes,
                groupMetas: sdk.groupMetas,
            };
        },

        async resolveItem(id: string, version?: string, locale?: string): Promise<ResolvedItem | undefined> {
            const sdk = await getLoadedSdk();
            const item = sdk.items.get(id);
            if (!item) return undefined;

            const resolvedVersion = version ?? sdk.manifest.current_version ?? sdk.manifest.versions.at(-1)?.id ?? '0';
            const resolvedLocale = locale ?? defaultLocale;

            return resolveItem(item, sdk, resolvedVersion, resolvedLocale);
        },

        async resolveDataType(id: string, version?: string, locale?: string): Promise<ResolvedDataType | undefined> {
            const sdk = await getLoadedSdk();
            const dt = sdk.dataTypes.get(id);
            if (!dt) return undefined;

            const resolvedVersion = version ?? sdk.manifest.current_version ?? sdk.manifest.versions.at(-1)?.id ?? '0';
            const resolvedLocale = locale ?? defaultLocale;

            return resolveDataType(dt, sdk, resolvedVersion, resolvedLocale);
        },

        async getVersions() {
            const sdk = await getLoadedSdk();
            return buildSdkVersions(sdk.manifest);
        },
    };
}
