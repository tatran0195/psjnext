# psj — Jupiter CAE Desktop SDK Documentation Format

**Specification version:** `2.0`
**Format identifier:** `psj`
**File extension:** `.yaml`

---

## Overview

psj is the authoritative documentation format for the Jupiter CAE Desktop Platform SDK. It describes every callable item — macros, psj-commands, psj-utilities, and psj-gui methods — in a unified schema built for authoring at scale: thousands of items, multiple SDK versions, and multiple human languages.

### Design goals

| Goal                                          | Mechanism                                                                   |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| One format for all four callable domains      | `domain` field drives all renderer decisions                                |
| No repeated param definitions across siblings | Param groups (`_groups/`) referenced by `$group`                            |
| No full-file copies across SDK versions       | Delta blocks (`changes`) record only what changed                           |
| Translations without polluting structure      | Sidecar locale files (`<id>.<locale>.yaml`)                                 |
| Examples always co-located with their item    | Inline `examples` block, never file links                                   |
| Partial translations are valid                | Silent fallback to `en` when a locale key is absent                         |
| Unambiguous schema validation                 | Every field has an explicit type, constraints, and required/optional status |
| Safe cross-file references                    | `$ref` and `$group` resolve at load time; broken refs are build errors      |

---

## Repository layout

```text
sdk.psj.yaml                  ← root manifest
_groups/
  <group-id>.yaml                ← reusable param group definition
  <group-id>.<locale>.yaml       ← locale translations for that group
macro/
  <id>.yaml
  <id>.<locale>.yaml
psj-command/
  <id>.yaml
  <id>.<locale>.yaml
psj-utility/
  <id>.yaml
  <id>.<locale>.yaml
psj-gui/
  <id>.yaml
  <id>.<locale>.yaml
data-type/
  <id>.yaml                      ← structured data-type definitions (NEW in v2)
```

The base file (`.yaml`) is always English and is the source of truth for both structure and English text. A locale sidecar contains only the natural-language fields for that locale. Structural fields (`id`, `type`, `default`, `syntax`, `code`, …) never appear in sidecars.

---

## Table of Contents

- [psj — Jupiter CAE Desktop SDK Documentation Format](#psj--jupiter-cae-desktop-sdk-documentation-format)
    - [Overview](#overview)
        - [Design goals](#design-goals)
    - [Repository layout](#repository-layout)
    - [Table of Contents](#table-of-contents)
    - [1. Root manifest — `sdk.psj.yaml`](#1-root-manifest--sdkpsjyaml)
    - [2. Data-type files — `data-type/<id>.yaml`](#2-data-type-files--data-typeidyaml)
    - [3. Param group files — `_groups/<id>.yaml`](#3-param-group-files--_groupsidyaml)
        - [Group locale sidecar — `_groups/<id>.<locale>.yaml`](#group-locale-sidecar--_groupsidlocaleyaml)
    - [4. Item files — `<domain>/<id>.yaml`](#4-item-files--domainidyaml)
        - [4a. Minimal item — pure group reference](#4a-minimal-item--pure-group-reference)
        - [4b. Group reference with exclusions, overrides, and inline additions](#4b-group-reference-with-exclusions-overrides-and-inline-additions)
        - [4c. Group with mid-list insertion](#4c-group-with-mid-list-insertion)
        - [4d. Macro — positional params](#4d-macro--positional-params)
        - [4e. Utility — with callout](#4e-utility--with-callout)
        - [4f. PSJ-GUI method](#4f-psj-gui-method)
    - [5. Delta versioning](#5-delta-versioning)
        - [5a. Removing params across a version](#5a-removing-params-across-a-version)
        - [5b. Full delta operation vocabulary](#5b-full-delta-operation-vocabulary)
    - [6. Locale sidecar files](#6-locale-sidecar-files)
        - [6a. Localizable vs. structural fields](#6a-localizable-vs-structural-fields)
        - [6b. Item locale sidecar](#6b-item-locale-sidecar)
        - [6c. Macro locale sidecar — positional params keyed by position](#6c-macro-locale-sidecar--positional-params-keyed-by-position)
    - [7. Locale resolution algorithm](#7-locale-resolution-algorithm)
    - [8. Renderer decisions driven by `domain`](#8-renderer-decisions-driven-by-domain)
    - [9. Complete field reference](#9-complete-field-reference)
        - [Item file](#item-file)
        - [Param](#param)
        - [GroupRef](#groupref)
        - [Returns](#returns)
        - [Code](#code)
        - [Callout](#callout)
        - [Example](#example)
        - [VersionDelta](#versiondelta)
        - [ParamPatch](#parampatch)
        - [EnumValue](#enumvalue)
        - [Ref](#ref)
        - [ParamGroup file](#paramgroup-file)
        - [Locale sidecar (item or group)](#locale-sidecar-item-or-group)
    - [10. Type system](#10-type-system)
    - [11. Validation rules (summary)](#11-validation-rules-summary)
    - [12. Tooling \& Integration](#12-tooling--integration)
        - [Fumadocs \& `meta.json` Generation](#fumadocs--metajson-generation)

---

## 1. Root manifest — `sdk.psj.yaml`

```yaml
psj: '2.0' # required; must match spec version being used

# Ordered oldest → newest. Adding an entry here is all that is needed to unlock
# the delta system for items that changed in that release.
versions: # required; at least one entry
    - id: '5.0.0' # required; semver string
      notes: ~ # optional; string; release notes summary
    - id: '5.0.1'
      notes: 'Removed iEJobType and iHeatConvection from Analysis.ADVC.Structure'
    - id: '5.1.0'
      notes: 'Current release'

current_version: '5.1.0' # required; must match one of versions[].id

locales: # required; at least one entry with default: true
    - id: en # BCP-47 language tag
      label: English
      default: true # exactly one locale must be default: true
    - id: ja
      label: 日本語

# Domain declarations control renderer behaviour. The four built-in domains
# are listed below. Custom domains may be added but require a renderer plugin.
domains: # required
    - id: macro # required; must be a valid identifier
      title: Macros # required; display label
      param_style: positional # required; positional | named
    - id: psj-command
      title: PSJ Commands
      param_style: named
    - id: psj-utility
      title: PSJ Utilities
      param_style: named
    - id: psj-gui
      title: PSJ GUI
      param_style: named

# Optional list of maintainers. Replaces per-item author / author_url.
maintainers:
    - name: 'SDK Documentation Team'
      email: 'sdk-docs@example.com' # optional
      url: 'https://example.com' # optional
```

**Validation rules**:

- `current_version` MUST equal one of the `versions[].id` values.
- `versions` MUST be ordered oldest → newest (strict semver ascending).
- Exactly one locale MUST carry `default: true`.
- Each `domain.id` MUST be unique within the list.

---

## 2. Data-type files — `data-type/<id>.yaml`

Data-type files document the structured types referenced via `$ref:data-type/<id>` in param and return declarations. They are documentation artifacts, not code-generation schemas.

```yaml
# data-type/JPT_NASTRAN_ANALYSIS.yaml
psj: '2.0'
kind: data_type # required; must be data_type
id: JPT_NASTRAN_ANALYSIS # required; unique across all data-type files
title: 'JPT_NASTRAN_ANALYSIS' # required; display title (often same as id)
description: >
    Input parameter block for Nastran analysis configuration.
version_introduced: '5.0.0' # required
fields: # ordered list of fields on this type
    - name: iSolverType
      type: Integer
      required: false
      default: '0'
      description: Nastran solver variant.
      enum_values:
          - id: 0
            label: Default
          - id: 1
            label: SMP
```

Data-type locale sidecars (`data-type/<id>.<locale>.yaml`) follow the same sidecar rules as item sidecars.

---

## 3. Param group files — `_groups/<id>.yaml`

A param group is a named, ordered list of param definitions with no domain, syntax, or return value of its own. Any item file includes it by reference. Groups can extend other groups.

It is purely a mechanism to reduce repeated parameter definitions across multiple files; it has no semantic meaning in the final rendered documentation.

```yaml
# _groups/nastran-base.yaml
psj: '2.0'
kind: param_group # required; must be param_group
id: nastran-base # required; unique across all group files
description: >
    Parameters shared by all Nastran analysis export commands.
extends: ~ # optional; id of parent group (single inheritance)
params:
    - name: strName
      type: String
      required: false
      default: '"Job_1"'
      description: Job name for the Nastran analysis.

    - name: strDescription
      type: String
      required: false
      default: '""'
      description: Description of the Nastran analysis job.

    - name: crlTargets
      type: 'List[Cursor]'
      required: false
      default: '[]'
      description: List of target parts.

    - name: nastranAnalysis
      type: '$ref:data-type/JPT_NASTRAN_ANALYSIS'
      required: false
      default: 'JPT_NASTRAN_ANALYSIS()'
      description: Nastran analysis input parameters.

    - name: bDummyPropAutoAssign
      type: Boolean
      required: false
      default: 'False'
      description: Auto-create dummy properties for unassigned parts.

    - name: iDummyPropMaterialID
      type: Integer
      required: false
      default: '0'
      description: Material ID for dummy property assignment.

    - name: crEdit
      type: Cursor
      required: false
      default: 'None'
      description: Existing Nastran job to modify. `None` creates a new job.

    - name: strPath
      type: String
      required: true
      description: Export path for the BDF file.

    - name: iModelCheckAnswer
      type: Integer
      required: false
      default: '0'
      description: Model checking for dummy properties.
      enum_values:
          - id: 0
            label: 'Off'
          - id: 1
            label: 'On'

    - name: iDeleteSlaveNodesAnswer
      type: Integer
      required: false
      default: '0'
      description: Delete slave nodes checking.
      enum_values:
          - id: 0
            label: 'Off'
          - id: 1
            label: 'On'
```

### Group locale sidecar — `_groups/<id>.<locale>.yaml`

The group sidecar translates params that belong to the group. Items referencing the group pick up these translations automatically — they are never duplicated into item-level sidecars.

```yaml
# _groups/nastran-base.ja.yaml
psj: '2.0'
kind: param_group # required; must match base file kind
locale: ja # required; BCP-47 tag matching a manifest locale id
id: nastran-base # required; must match base file id

description: >
    すべてのNastran解析エクスポートコマンドで共有されるパラメータ。

params:
    strName:
        display_name: ジョブ名
        description: Nastran解析のジョブ名。
    strDescription:
        description: Nastran解析ジョブの説明。
    crlTargets:
        description: 対象パーツのリスト。
    nastranAnalysis:
        description: Nastran解析入力パラメータ。
    bDummyPropAutoAssign:
        description: 未割り当てパーツへのダミープロパティの自動生成。
    iDummyPropMaterialID:
        description: ダミープロパティ割り当てに使用する材料ID。
    crEdit:
        description: 変更対象の既存Nastranジョブ。Noneの場合は新規作成。
    strPath:
        display_name: エクスポートパス
        description: BDFファイルのエクスポート先パス。
    iModelCheckAnswer:
        description: ダミープロパティのモデルチェック。
        enum_values:
            0: '無効'
            1: '有効'
    iDeleteSlaveNodesAnswer:
        description: スレーブノード削除チェック。
        enum_values:
            0: '無効'
            1: '有効'
```

---

## 4. Item files — `<domain>/<id>.yaml`

### 4a. Minimal item — pure group reference

```yaml
# psj-command/Analysis-Nastran-LinearStatic.yaml
psj: '2.0'
id: Analysis-Nastran-LinearStatic # required; slug unique within domain
title: 'Analysis.Nastran.LinearStatic()' # required; verbatim call signature
domain: psj-command # required; must match a manifest domain id
group: Nastran # optional; nav grouping label
namespace: Analysis.Nastran # optional (omit for macros); dotted call prefix
ribbon: 'Analysis > Nastran > LinearStatic' # optional; psj-command only
description: >
    Export the Nastran BDF input file for Structure Linear Static analysis (SOL 101).
version_introduced: '5.0.0' # required; must match a manifest version id
stability: stable # optional; stable | experimental | deprecated
macro_link: NastranJob # optional; id of the macro this command wraps (psj-command only)

params:
    - $group: nastran-base # inline all params from the group

returns:
    kind: typed # required; typed | macro_code | void
    type: Cursor # required when kind=typed
    description: The created Nastran job.
```

### 4b. Group reference with exclusions, overrides, and inline additions

```yaml
# psj-command/Analysis-Nastran-DirectFrequencyResponse.yaml
psj: '2.0'
id: Analysis-Nastran-DirectFrequencyResponse
title: 'Analysis.Nastran.DirectFrequencyResponse()'
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: 'Analysis > Nastran > DirectFrequencyResponse'
description: Export the Nastran BDF for Direct Frequency Response analysis (SOL 108).
version_introduced: '5.0.0'
stability: stable
macro_link: NastranJob

params:
    - $group: nastran-base
      exclude: # drop named params from the inlined group
          - bDummyPropAutoAssign
          - iDummyPropMaterialID
          - crEdit
      override: # NEW in v2: patch individual group params
          strPath:
              description: Export path for the frequency response BDF file.

    - name: bOutputXYPlots
      type: Boolean
      required: false
      default: 'False'
      description: Enable XY plot output.

    - name: iOutputValueSet
      type: Integer
      required: false
      default: '0'
      description: Output value set selector.

    - name: iOutputDOFType
      type: Integer
      required: false
      default: '0'
      description: Output degree-of-freedom type.

    - name: iXYPlotDisplacementType
      type: Integer
      required: false
      default: '0'
      description: XY plot displacement type.

    - name: iXYPlotVelocityType
      type: Integer
      required: false
      default: '0'
      description: XY plot velocity type.

    - name: iXYPlotAccelerationType
      type: Integer
      required: false
      default: '0'
      description: XY plot acceleration type.

    - name: strXTitle
      type: String
      required: false
      default: '""'
      description: X-axis title for XY plots.

    - name: strYTitle
      type: String
      required: false
      default: '""'
      description: Y-axis title for XY plots.

    - name: bOutputGeomIDofDummyProp
      type: Boolean
      required: false
      default: 'False'
      description: Output geometry ID of dummy properties.

    - name: bDummyPropAutoAssign
      type: Boolean
      required: false
      default: 'False'
      description: Auto-create dummy properties.

    - name: iDummyPropMaterialID
      type: Integer
      required: false
      default: '0'
      description: Material ID for dummy property assignment.

    - name: crEdit
      type: Cursor
      required: false
      default: 'None'
      description: Existing job to modify.

returns:
    kind: typed
    type: Cursor
    description: The created Nastran job.
```

### 4c. Group with mid-list insertion

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Dynamic.yaml
psj: '2.0'
id: Analysis-ADVC-MakeProcess-Dynamic
title: 'Analysis.ADVC.MakeProcess.Dynamic()'
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: 'Analysis > ADVC > Make Process > Dynamic'
description: Create an ADVC Structure Dynamic process.
version_introduced: '5.0.0'
stability: stable
macro_link: AdvcDynamicProcess

params:
    - $group: advc-process-struct
      insert_after: advcAutoIncrement # splice `insert` params after this param name
      insert:
          - name: bDynamic
            type: Boolean
            required: false
            default: 'False'
            description: Enable dynamic parameter settings.
          - name: advcDynamic
            type: '$ref:data-type/JPT_ADVC_DYNAMIC'
            required: false
            default: 'JPT_ADVC_DYNAMIC()'
            description: Dynamic parameters. Active when bDynamic=True.

returns:
    kind: typed
    type: Cursor
    description: The created or modified ADVC Dynamic process.
```

### 4d. Macro — positional params

```yaml
# macro/AdvcStaticProcess.yaml
psj: '2.0'
id: AdvcStaticProcess
title: 'AdvcStaticProcess()'
domain: macro
group: analysis
description: Create ADVC static process.
version_introduced: '5.0.0'
stability: stable
command_link: Analysis-ADVC-MakeProcess-Static # id of the command wrapping this macro

syntax: >
    AdvcStaticProcess(string m_strName, int m_iGeomNonlinear, int fixed_or_auto,
      int num_of_inc, double max_time, double max_dt, double min_dt, int load_type, ...)

params:
    - position: 1
      name: m_strName
      type: String
      required: true
      description: Name of ADVC static process.

    - position: 2
      name: m_iGeomNonlinear
      type: Integer
      required: true
      description: Geometry nonlinearity mode.
      enum_values:
          - id: 0
            label: '(blank)'
          - id: 1
            label: Total Lagrange
          - id: 2
            label: Updated Lagrange

    - position: 3
      name: fixed_or_auto
      type: Integer
      required: true
      description: Time step control.
      enum_values:
          - id: 0
            label: Auto
          - id: 1
            label: Fixed

    - position: 8
      name: load_type
      type: Integer
      required: true
      description: Load type.
      enum_values:
          - id: -1
            label: Default
          - id: 0
            label: Step
          - id: 1
            label: Ramp

    - position: 15
      name: m_bConvergence
      type: Boolean
      required: true
      description: Whether convergence parameters are defined.

    - position: 64
      name: m_crEdit
      type: Cursor
      required: false
      description: Edit cursor for existing process. Omit to create new.

returns:
    kind: macro_code
    codes:
        - value: '"1"'
          meaning: The function can be executed.
        - value: '"0"'
          meaning: The function cannot be executed.

examples:
    - id: default-process # NEW in v2: stable id for sidecar matching
      title: Create process with default settings
      language: psj
      code: |
          JPT.Exec('AdvcStaticProcess("ADVC_DEFAULT_PROCESS", 0, 0, 1, 1, 1, 1e-05, -1, ...)')
```

### 4e. Utility — with callout

```yaml
# psj-utility/JPT-BeginDatabaseTransaction.yaml
psj: '2.0'
id: JPT-BeginDatabaseTransaction
title: 'JPT.BeginDatabaseTransaction()'
domain: psj-utility
group: performance
namespace: JPT
description: >
    Disable screen animation, screen update, and status bar updates to improve
    Jupiter's performance during batch operations.
version_introduced: '5.0.0'
stability: stable
syntax: 'JPT.BeginDatabaseTransaction("transactionName")'

callouts:
    - id: must-end-transaction # NEW in v2: stable id replaces positional index
      level: warn # warn | info | danger
      text: >
          JPT.EndDatabaseTransaction() must be called at the end of the process
          to return Jupiter to the normal state.

params:
    - name: transactionName
      type: String
      required: true
      description: Transaction name displayed in the Undo/Redo menu.

returns:
    kind: void

see_also:
    - $ref: 'psj-utility/JPT-EndDatabaseTransaction'
      label: JPT.EndDatabaseTransaction() # now localizable via sidecar
```

### 4f. PSJ-GUI method

```yaml
# psj-gui/dlg-add_1delement_selector.yaml
psj: '2.0'
id: dlg-add_1delement_selector
title: 'dlg.add_1delement_selector()'
domain: psj-gui
group: dlg-methods
namespace: dlg
description: >
    Add a 1D element selector to the dialog, enabling the user to select
    1D elements and store the selection.
version_introduced: '5.0.0'
stability: stable
syntax: 'dlg.add_1delement_selector(...)'

params:
    - name: text
      type: String
      required: false
      default: '"1D element"'
      description: Title label for the selector widget.

returns:
    kind: void
```

---

## 5. Delta versioning

Item files carry a `changes` block describing only what differs between versions. Items with no `changes` block are identical across all versions since `version_introduced`. Most items in a backward-compatible SDK will have no `changes` block at all.

### 5a. Removing params across a version

```yaml
# psj-command/Analysis-ADVC-Structure.yaml  (versioning excerpt)
psj: '2.0'
id: Analysis-ADVC-Structure
title: 'Analysis.ADVC.Structure()'
domain: psj-command
version_introduced: '5.0.0'
macro_link: ADVC_Structure

params:
    - $group: advc-structure-base

    # These params existed in 5.0.0 but were removed in 5.0.1.
    # They remain in the file so the 5.0.0 documentation can still render them.
    - name: iEJobType
      type: Integer
      required: false
      default: '0'
      description: Job type.
      enum_values:
          - id: 0
            label: Structure

    - name: iHeatConvection
      type: Integer
      required: false
      default: '1'
      description: Heat convection mode.

returns:
    kind: typed
    type: Cursor
    description: The created ADVC analysis job.

changes:
    - version: '5.0.1'
      notes: iEJobType and iHeatConvection are no longer available in v5.0.1 or higher.
      params:
          remove:
              - iEJobType
              - iHeatConvection
```

### 5b. Full delta operation vocabulary

```yaml
changes:
    - version: 'X.Y.Z' # required; must match a manifest version id

      notes: 'Human-readable summary of what changed in this version.' # optional

      # Optional: top-level item fields that changed in this version.
      item:
          description: 'Revised item description.'
          ribbon: 'New > Ribbon > Path'
          stability: deprecated # NEW in v2: replaces boolean `deprecated` flag

      params:
          # Add new params. `after` names the existing param they follow.
          # Omit `after` to append at the end.
          add:
              - name: bNewFeature
                type: Boolean
                required: false
                default: 'False'
                description: New capability added in X.Y.Z.
                after: strPath
                inferred: true # set when the converter inferred this, not from source

          # Remove params by name.
          remove:
              - iRemovedParam

          # Patch specific fields on existing params.
          modify:
              - name: strName
                changes:
                    description: 'Revised description for X.Y.Z.'
                    default: '"NewDefault"'
                    required: true
                    deprecated: true
                    deprecated_reason: 'Use strJobName instead.' # NEW in v2
                    enum_values:
                        add:
                            - id: 5
                              label: New option
                        remove:
                            - 2 # enum value id to remove
```

**Resolution rules**:

- The base `params` list represents the item as of `version_introduced`.
- `changes` entries are applied in version order up to the requested version.
- `remove` deletes a param from the resolved list. The definition stays in the file above `changes` so older-version renders still have it.
- `add` inserts at the named position; omit `after` to append.
- `modify` patches only the named fields; all other fields are unchanged.
- `item` patches top-level fields. Any field not listed is unchanged.

---

## 6. Locale sidecar files

### 6a. Localizable vs. structural fields

Sidecars contain **only natural-language fields**. Structural fields are never translated and never appear in sidecars.

| Field                                    | Localizable?      |
| ---------------------------------------- | ----------------- |
| `description` (item or group)            | ✅                |
| `params[].description`                   | ✅                |
| `params[].display_name`                  | ✅                |
| `enum_values[].label`                    | ✅                |
| `enum_values[].description`              | ✅                |
| `returns.description`                    | ✅                |
| `returns.codes[].meaning`                | ✅                |
| `callouts[].text`                        | ✅                |
| `examples[].title`                       | ✅                |
| `see_also[].label`                       | ✅                |
| `id`, `title`, `syntax`, `code`          | ❌ — code symbols |
| `type`, `default`, `required`            | ❌ — structural   |
| `namespace`, `ribbon`, `domain`, `group` | ❌ — structural   |
| `version_introduced`, `macro_link`       | ❌ — structural   |
| `stability`                              | ❌ — structural   |

### 6b. Item locale sidecar

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Dynamic.ja.yaml
psj: '2.0'
kind: locale_sidecar # required; must be locale_sidecar
locale: ja # required; BCP-47 tag
id: Analysis-ADVC-MakeProcess-Dynamic # required; must match base file id

description: >
    ADVC構造ダイナミックプロセスを作成します。

# Only params that are NOT from a group are translated here.
# Group params are translated in the respective group sidecar.
params:
    bDynamic:
        description: ダイナミックパラメータ設定の有効/無効。
    advcDynamic:
        description: ダイナミックパラメータの設定。bDynamic=Trueの場合に有効。

returns:
    description: 作成または変更されたADVCダイナミックプロセスのカーソル。

# Callouts matched by id (v2), not by position index.
callouts:
    must-end-transaction:
        text: >
            処理の終了時にJPT.EndDatabaseTransaction()を呼び出して
            Jupiterを通常の状態に戻す必要があります。

# Examples matched by id (v2), not by position index.
examples:
    default-process:
        title: デフォルト設定でのプロセス作成

see_also:
    psj-utility/JPT-EndDatabaseTransaction:
        label: JPT.EndDatabaseTransaction()
```

### 6c. Macro locale sidecar — positional params keyed by position

```yaml
# macro/AdvcStaticProcess.ja.yaml
psj: '2.0'
kind: locale_sidecar
locale: ja
id: AdvcStaticProcess

description: ADVCスタティックプロセスを作成します。

# Positional params are keyed by position integer.
params:
    1:
        description: ADVCスタティックプロセスの名前。
    2:
        description: 幾何非線形オプション。
        enum_values:
            0: (空白)
            1: トータルラグランジュ法
            2: 更新ラグランジュ法
    3:
        description: タイムステップ制御。
        enum_values:
            0: 自動
            1: 固定
    8:
        description: 荷重タイプ。
        enum_values:
            -1: デフォルト
            0: ステップ
            1: ランプ

returns:
    codes:
        '"1"': 関数を実行できます。
        '"0"': 関数を実行できません。

examples:
    default-process:
        title: デフォルト設定でのプロセス作成
```

---

## 7. Locale resolution algorithm

```python
function resolve(item_id, field_path, locale):

  1. If locale == default_locale (en):
       return base_file[field_path]

  2. Load item sidecar: <domain>/<item_id>.<locale>.yaml
     If sidecar exists AND sidecar[field_path] exists:
       return sidecar[field_path]

  3. If field_path is on a param that originated from a $group reference:
       Load group sidecar: _groups/<group_id>.<locale>.yaml
       If group_sidecar[field_path] exists:
         return group_sidecar[field_path]
       If group has `extends`:
         recurse into parent group sidecar (depth-first, parent last)

  4. Fallback: return base_file[field_path]   # en text, no error logged
```

Fallback is silent. Partial translations are valid and expected — an item where only some params are translated shows the translated text for those params and English for the rest. No build failure, no missing-key warnings.

---

## 8. Renderer decisions driven by `domain`

| Behaviour                           | `macro`           | `psj-command`   | `psj-utility` | `psj-gui`   |
| ----------------------------------- | ----------------- | --------------- | ------------- | ----------- |
| Show Position column in param table | ✅                | —               | —             | —           |
| Show namespace prefix in title      | —                 | ✅              | ✅            | ✅          |
| Show Ribbon path                    | —                 | ✅ if present   | —             | —           |
| Show macro linkage card             | ✅ `command_link` | ✅ `macro_link` | —             | —           |
| Syntax highlight style              | `psj-macro`       | Python          | Python        | Python      |
| Return renders as                   | Code table        | Type link       | "No output"   | "No output" |
| Stability badge                     | ✅                | ✅              | ✅            | ✅          |

---

## 9. Complete field reference

### Item file

```yaml
psj: '2.0'              # required; string; must match spec version
id: string                 # required; unique within domain; slug format recommended
title: string              # required; verbatim call signature e.g. "Analysis.Nastran.LinearStatic()"
domain: string             # required; must match a manifest domain id
group: string?             # optional; nav grouping label; localizable
namespace: string?         # optional; dotted call prefix; omit for macros
ribbon: string?            # optional; UI ribbon path; psj-command only
description: string        # required; localizable
version_introduced: string # required; must match a manifest version id
stability: string?         # optional; stable | experimental | deprecated; default: stable
macro_link: string?        # optional; id of the macro this command wraps; psj-command only
command_link: string?      # optional; id of the command that wraps this macro; macro only
syntax: string?            # optional; verbatim signature (auto-generated from id and params if omitted); NOT localizable
callouts: [Callout]?       # optional; warning/info boxes; text IS localizable
params: [Param | GroupRef] # required; ordered list; defines params as of version_introduced
returns: Returns           # required
examples: [Example]?       # optional; always inline; never file links
see_also: [Ref]?           # optional
changes: [VersionDelta]?   # optional; absent = item unchanged across all versions
```

### Param

```yaml
position: integer?         # optional; 1-based; macro positional args only
name: string?              # required for named params; source identifier
display_name: string?      # optional; clean UI label when name is cryptic; localizable
type: string               # required; see Type system below
required: boolean          # required
default: string?           # optional; exact default as string; null if undocumented
description: string        # required; localizable
enum_values: [EnumValue]?  # optional
deprecated: boolean?       # optional; true = deprecated (version tracking is handled via delta blocks)
deprecated_reason: string? # optional; human-readable reason; localizable
inferred: boolean?         # optional; true = added by converter, not stated in source
```

### GroupRef

```yaml
$group: string             # required; id of a _groups/<id>.yaml file
exclude: [string]?         # optional; param names to drop from the inlined group
insert_after: string?      # optional; param name after which to splice `insert`
insert: [Param]?           # optional; params spliced at insert_after position
override:                  # optional; map of param name → Param fields to patch
  <param_name>:
    description: string?
    default: string?
    required: boolean?
```

### Returns

```yaml
kind: string               # required; typed | macro_code | void
type: string?              # required when kind=typed; see Type system
description: string?       # optional; localizable
codes: [Code]?             # required when kind=macro_code
```

### Code

```yaml
value: string # required; e.g. '"1"'; NOT localizable
meaning: string # required; localizable
```

### Callout

```yaml
id: string # required; stable identifier for sidecar matching
level: string # required; warn | info | danger
text: string # required; localizable
```

### Example

```yaml
id: string # required; stable identifier for sidecar matching
title: string? # optional; localizable
language: string # required; psj | python
code: string # required; NOT localizable; always inline, never a file path
```

### VersionDelta

```yaml
version: string            # required; must match a manifest version id
notes: string?             # optional; human-readable summary
item:                      # optional; top-level fields to patch
  description: string?
  ribbon: string?
  stability: string?       # stable | experimental | deprecated
params:                    # optional
  add: [Param]?            # each may carry `after: paramName`
  remove: [string]?        # param names to drop
  modify: [ParamPatch]?    # field-level patches on existing params
```

### ParamPatch

```yaml
name: string               # required; name of the param to patch
changes:                   # required; at least one field must be present
  description: string?
  default: string?
  required: boolean?
  deprecated: boolean?
  deprecated_reason: string?
  enum_values:
    add: [EnumValue]?
    remove: [integer | string]? # enum value ids to remove
```

### EnumValue

```yaml
id: integer | string # required; NOT localizable; stable across versions
label: string # required; localizable
description: string? # optional; localizable
```

### Ref

```yaml
$ref: string # required; "<domain>/<id>"
label: string? # optional; localizable (NEW in v2); display text for the link
inferred: boolean? # optional; true = added by converter, not from source
```

### ParamGroup file

```yaml
psj: '2.0' # required
kind: param_group # required; must be param_group
id: string # required; unique across all group files
description: string? # optional; localizable
extends: string? # optional; id of parent group (single inheritance)
params: [Param] # required; ordered list
```

### Locale sidecar (item or group)

```yaml
psj: '2.0' # required
kind: locale_sidecar # required; must be locale_sidecar
locale: string # required; BCP-47 tag matching a manifest locale id
id: string # required; ties to base file id

description: string?

callouts: # keyed by callout id
    <callout_id>:
        text: string

params:
    # For named params (psj-command / psj-utility / psj-gui / group):
    <param_name>:
        display_name: string?
        description: string?
        deprecated_reason: string?
        enum_values:
            <id>: string # just the label; use enum value id as key

    # For positional params (macro):
    <position_integer>:
        description: string?
        enum_values:
            <id>: string

returns:
    description: string?
    codes:
        <value>: string # meaning; use the value string as key e.g. '"1"': ...

examples: # keyed by example id (NEW in v2)
    <example_id>:
        title: string?

see_also: # keyed by $ref value (NEW in v2)
    <domain/id>:
        label: string?
```

---

## 10. Type system

The `type` field on `Param` and `Returns` accepts the following forms:

| Form          | Example                                   | Notes                                                       |
| ------------- | ----------------------------------------- | ----------------------------------------------------------- |
| Primitive     | `String`, `Integer`, `Boolean`, `Double`  | Case-sensitive                                              |
| SDK cursor    | `Cursor`                                  | Points to any SDK object                                    |
| Generic list  | `List[Cursor]`, `List[Integer]`           | Single type argument                                        |
| Data-type ref | `$ref:data-type/JPT_NASTRAN_ANALYSIS`     | Must resolve to a `data-type/` file                         |
| List of ref   | `List[$ref:data-type/JPT_ADVC_LOAD_NODE]` | Combines list and ref forms                                 |
| Untyped list  | `List`                                    | Use only for macro params with undocumented element type    |
| Vector        | `Vector`                                  | Fixed-length numeric tuple; size not encoded in type string |

---

## 11. Validation rules (summary)

Tooling SHOULD enforce these rules at build time and report them as errors (not warnings):

1. `psj` version in every file MUST match the manifest `psj` version.
2. Every `$group` reference MUST resolve to an existing `_groups/<id>.yaml`.
3. Every `$ref:data-type/<id>` MUST resolve to an existing `data-type/<id>.yaml`.
4. Every `$ref: <domain>/<id>` in `see_also` MUST resolve to an existing item file.
5. Every `version_introduced` and `changes[].version` MUST match a manifest `versions[].id`.
6. `current_version` MUST match a manifest `versions[].id`.
7. `macro_link` and `command_link` targets MUST resolve to existing item files.
8. `GroupRef.insert_after` MUST name a param that exists in the resolved group (after `exclude`).
9. `GroupRef.exclude` names MUST all exist in the referenced group.
10. `GroupRef.override` keys MUST all exist in the referenced group (after `exclude`).
11. `VersionDelta.params.remove` names MUST exist in the item's effective param list at that version.
12. `VersionDelta.params.modify[].name` MUST exist in the item's effective param list at that version.
13. Within a sidecar, `callouts` keys MUST match `id` values in the base file.
14. Within a sidecar, `examples` keys MUST match `id` values in the base file.
15. Positional param `position` values MUST be unique within an item.
16. Named param `name` values MUST be unique within the resolved param list of an item.
17. Each `EnumValue.id` MUST be unique within its `enum_values` list.
18. `stability` MUST be one of `stable`, `experimental`, `deprecated`.
19. `Callout.level` MUST be one of `warn`, `info`, `danger`.
20. `Returns.kind` MUST be one of `typed`, `macro_code`, `void`.
21. `kind: typed` MUST include a `type` field; `kind: void` MUST NOT.
22. `kind: macro_code` MUST include a non-empty `codes` list.

---

## 12. Tooling & Integration

### Fumadocs & `meta.json` Generation

The `psj` format is designed to integrate cleanly with documentation frameworks like Fumadocs. When building the documentation output, the `psjapi/server` converter can automatically emit `meta.json` files alongside the page endpoints, controlling sidebar folder grouping and internal ordering.

This behaviour is driven by the `group` field in each item declaration, which determines the logical folder. The `folderStyle` configuration within the converter determines the shape of the `meta.json` pages list:

- **`folder`**: Emits actual nested sub-directories (`[ "group-slug" ]`).
- **`separator`**: Emits flattened logical groups within a single sidebar using Fumadocs text separators (`[ "---Group Name---", "...group-slug" ]`).
