# PSJ SDK Documentation Format — Specification v3.3

**Specification version:** `3.3` **Format identifier:** `psj` **File extension:** `.yaml`

---

## Overview

psj is the authoritative documentation format for the Jupiter CAE Desktop Platform SDK. It describes every callable item
— macros, psj-commands, psj-utilities, and psj-gui methods — in a unified schema built for authoring at scale: thousands
of items, multiple SDK versions, and multiple human languages.

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
| Navigable at scale                            | Folder hierarchy replaces flat `group` field; `meta.yaml` per folder        |
| Group metadata is localizable                 | `meta.<locale>.yaml` sidecars carry translated folder titles                |
| Data-types organised by semantic scope        | `built-in/`, `pre/`, `post/`, `gui/` — not by domain name                   |
| Data-types renderable in Fumadocs             | Data-type pages are first-class Fumadocs pages under `psjapi/data-type/`    |

---

## Repository layout

```text
sdk.psj.yaml

_groups/
  <group-id>.yaml
  <group-id>.<locale>.yaml

data-type/
  built-in/                         ← scalar types shared by all domains
    meta.yaml
    python-built-in-types.yaml
    jupiter-built-in-types.yaml
    <id>.<locale>.yaml

  pre/                              ← types used in pre-processing
    meta.yaml
    built-in/
      meta.yaml
      BodyVector.yaml
      ConnectVector.yaml
      VersionInfo.yaml
      <id>.<locale>.yaml
    enum/
      meta.yaml
      DItemType.yaml
      ElemType.yaml
      ElemKind.yaml
      MaterialPropertyType.yaml
      MaterialUnitType.yaml         ← index; see_also to per-unit files
      LengthUnit.yaml
      TimeUnit.yaml
      MassUnit.yaml
      ForceUnit.yaml
      PressureUnit.yaml
      AssociateType.yaml
      PathType.yaml
      DTableType.yaml
      BoolType.yaml
      MessageBoxType.yaml
      SelectMethodType.yaml
      <id>.<locale>.yaml
    class/
      meta.yaml
      JPT_NASTRAN_ANALYSIS.yaml
      JPT_ABAQUS_LBC_STEP_INFO.yaml
      JPT_ABAQUS_OUTPUT_REQUEST.yaml
      JPT_ADVC_DYNAMIC.yaml
      <id>.<locale>.yaml

  post/                             ← types used in post-processing
    meta.yaml
    built-in/
      meta.yaml
      DPostAnalysis.yaml
      DPostElem.yaml
      DPostTimeStep.yaml
      <id>.<locale>.yaml
    enum/
      meta.yaml
      PostJobType.yaml
      PostAnalysisType.yaml
      PostDataRangeType.yaml
      PostDataLocationType.yaml
      PostDataConversionType.yaml
      PostDataContinuousType.yaml
      PostDataCoordinateType.yaml
      PostData1DType.yaml
      PostData2DType.yaml
      PostResultDataAmtType.yaml
      <id>.<locale>.yaml

  gui/                              ← types used in GUI
    meta.yaml
    built-in/
      meta.yaml
      PSJFont.yaml
      TableCellID.yaml
      TableCellRange.yaml
      <id>.<locale>.yaml
    class/
      meta.yaml
      PSJMessageBox.yaml
      <id>.<locale>.yaml

macro/
  meta.yaml
  <SubFolder>/
    meta.yaml
    meta.<locale>.yaml
    <id>.yaml
    <id>.<locale>.yaml

psj-command/
  meta.yaml
  <SubFolder>/
    meta.yaml
    meta.<locale>.yaml
    <id>.yaml
    <id>.<locale>.yaml

psj-utility/
  meta.yaml
  <SubFolder>/
    meta.yaml
    meta.<locale>.yaml
    <id>.yaml
    <id>.<locale>.yaml

psj-gui/
  meta.yaml
  msgbox/
    meta.yaml
    add_button.yaml
    show.yaml
    set_caption.yaml
    set_header.yaml
    set_icon.yaml
    set_message.yaml
    enable_checkbox.yaml
    set_buttons.yaml
    <id>.<locale>.yaml
  <SubFolder>/
    meta.yaml
    meta.<locale>.yaml
    <id>.yaml
    <id>.<locale>.yaml
```

**Key layout rules:**

- The base file (`.yaml`) is always English and is the source of truth for both structure and English text.
- A locale sidecar contains only natural-language fields. Structural fields never appear in sidecars.
- Each subfolder MUST contain a `meta.yaml`. The domain root MAY contain a `meta.yaml`.
- An item `id` MUST equal its path relative to the domain root using `/` separators without file extension.
- A data-type `id` MUST equal its path relative to `data-type/` using `/` separators without file extension (e.g.
  `pre/enum/DItemType`).
- `$ref:data-type/<id>` MUST use the full semantic-scope path (e.g. `$ref:data-type/pre/class/JPT_NASTRAN_ANALYSIS`).
- `data-type` is a **reference library**, not a domain. It has no manifest entry, no `param_style`, and no renderer
  domain row.

---

## Table of Contents

- [1. Root manifest](#1-root-manifest--sdkpsjyaml)
- [2. Group meta files](#2-group-meta-files--metayaml)
- [3. Data-type files](#3-data-type-files--data-typescopecategoryidyaml)
- [4. Param group files](#4-param-group-files--_groupsidyaml)
- [5. Item files](#5-item-files--domainsubfolderidyaml)
- [6. Delta versioning](#6-delta-versioning)
- [7. Locale sidecar files](#7-locale-sidecar-files)
- [8. Locale resolution algorithm](#8-locale-resolution-algorithm)
- [9. Renderer decisions driven by `domain`](#9-renderer-decisions-driven-by-domain)
- [10. Data-type renderer](#10-data-type-renderer)
- [11. Complete field reference](#11-complete-field-reference)
- [12. Type system](#12-type-system)
- [13. Validation rules](#13-validation-rules)
- [14. Tooling & Integration](#14-tooling--integration)

---

## 1. Root manifest — `sdk.psj.yaml`

```yaml
psj: '3.3'

versions:
    - id: '5.0.0'
    - id: '5.0.1'
    - id: '5.1.0'

current_version: '5.1.0'

locales:
    - id: en
      label: English
      default: true
    - id: ja
      label: 日本語

# The four callable domains. data-type is NOT listed here.
domains:
    - id: macro
      title: Macros
      param_style: positional
    - id: psj-command
      title: PSJ Commands
      param_style: named
    - id: psj-utility
      title: PSJ Utilities
      param_style: named
    - id: psj-gui
      title: PSJ GUI
      param_style: named
```

**Validation rules:**

- `current_version` MUST equal one of the `versions[].id` values.
- `versions` MUST be ordered oldest → newest (strict semver ascending).
- Exactly one locale MUST carry `default: true`.
- Each `domain.id` MUST be unique within the list.
- `data-type` MUST NOT appear as a `domain.id`.

---

## 2. Group meta files — `meta.yaml`

Every subfolder within a domain and within `data-type/` MUST contain a `meta.yaml`.

```yaml
# data-type/pre/enum/meta.yaml
psj: '3.3'
kind: group_meta
title: 'Pre-Processing Enumeration Types'
description: >
    Enumeration types used in pre-processing commands and utilities.
order:
    - DItemType
    - ElemType
    - ElemKind
    - MaterialPropertyType
    - MaterialUnitType
    - AssociateType
    - PathType
    - DTableType
    - BoolType
    - MessageBoxType
    - SelectMethodType
icon: enum
```

### Group meta locale sidecar — `meta.<locale>.yaml`

```yaml
# data-type/pre/enum/meta.ja.yaml
psj: '3.3'
kind: group_meta
locale: ja
title: '前処理 列挙型'
description: >
    前処理コマンドおよびユーティリティで使用される列挙型。
```

**Validation rules:**

- `meta.yaml` MUST exist in every subfolder under a domain root and under `data-type/`.
- `kind` MUST be `group_meta`.
- If `order` is present, ALL direct children MUST be listed — partial ordering is not allowed.
- `order` entries MUST each resolve to an existing child file stem or subfolder name.
- `meta.<locale>.yaml` locale tag MUST match a locale declared in the manifest.

---

## 3. Data-type files — `data-type/<scope>/<category>/<id>.yaml`

Data-type files document all types referenced via `$ref:data-type/<id>` in param and return declarations. They are
**first-class documentation pages** rendered under `psjapi/data-type/` in Fumadocs, not hidden reference artifacts.

### Scope folders

| Scope            | Path                  | Contains                                                           |
| ---------------- | --------------------- | ------------------------------------------------------------------ |
| Global built-ins | `data-type/built-in/` | Scalar primitives and Jupiter core types shared by all domains     |
| Pre-processing   | `data-type/pre/`      | Types used by `psj-command` and pre-processing `psj-utility` items |
| Post-processing  | `data-type/post/`     | Types used by post-processing `psj-utility` items                  |
| GUI              | `data-type/gui/`      | Types used by `psj-gui` items                                      |

### Category subfolders

| Folder      | `category` value | Rule                                              |
| ----------- | ---------------- | ------------------------------------------------- |
| `built-in/` | `built-in`       | Primitive scalars and advanced Jupiter core types |
| `enum/`     | `enumeration`    | Integer or string enumeration tables              |
| `class/`    | `class`          | Constructor + fields types                        |

Data-type files placed at the scope root (e.g. `data-type/pre/`) are index or overview pages with no category subfolder
requirement.

### 3a. Built-in types

```yaml
# data-type/built-in/python-built-in-types.yaml
psj: '3.3'
kind: data_type
id: built-in/python-built-in-types
title: 'Python Built-in Types'
category: built-in
description: >
    Standard Python scalar types available as parameter and return types across all PSJ domains.
since: '5.0.0'
values:
    - id: String
      label: String
      description: UTF-8 text value. Written as str in Python.
    - id: Integer
      label: Integer
      description: 32-bit signed integer. Written as int in Python.
    - id: Boolean
      label: Boolean
      description: True or False. Written as bool in Python.
    - id: Double
      label: Double
      description: 64-bit floating point. Written as float in Python.
```

```yaml
# data-type/built-in/jupiter-built-in-types.yaml
psj: '3.3'
kind: data_type
id: built-in/jupiter-built-in-types
title: 'Jupiter Built-in Types'
category: built-in
description: >
    Advanced built-in types specific to the Jupiter CAE platform.
since: '5.0.0'
values:
    - id: Cursor
      label: Cursor
      description: >
          Points to any SDK object in the Jupiter database. Passed by reference; resolved at call time.
    - id: List
      label: List
      description: Ordered collection. Element type specified as List[T].
    - id: Vector
      label: Vector
      description: Fixed-length numeric tuple. Size is not encoded in the type string.
```

### 3b. Enumeration types

```yaml
# data-type/pre/enum/DItemType.yaml
psj: '3.3'
kind: data_type
id: pre/enum/DItemType
title: 'DItemType'
category: enumeration
namespace: 'JPT.DItemType'
description: >
    Enumeration representing the type of a DItem in Jupiter. Use JPT.DItemType.<NAME> in code, or the integer ID where
    noted.
since: '5.0.0'
values:
    - id: 2
      name: INST
      label: Sub Assembly
      description: Sub assembly node for tree display.
    - id: 3
      name: BODY
      label: Parts
    - id: 10
      name: NODE
      label: Node
```

```yaml
# data-type/pre/enum/MaterialUnitType.yaml  ← index file
psj: '3.3'
kind: data_type
id: pre/enum/MaterialUnitType
title: 'Material Unit Types'
category: enumeration
description: >
    Index of all physical unit enumerations available via JPT.UnitType. Each unit group is documented in its own file.
since: '5.0.0'
see_also:
    - $ref: 'data-type/pre/enum/LengthUnit'
    - $ref: 'data-type/pre/enum/TimeUnit'
    - $ref: 'data-type/pre/enum/MassUnit'
    - $ref: 'data-type/pre/enum/ForceUnit'
    - $ref: 'data-type/pre/enum/PressureUnit'
```

```yaml
# data-type/pre/enum/LengthUnit.yaml  ← one file per unit group
psj: '3.3'
kind: data_type
id: pre/enum/LengthUnit
title: 'LengthUnit'
category: enumeration
namespace: 'JPT.UnitType'
description: Enumeration of length unit variants.
since: '5.0.0'

values:
    - id: 0
      name: Length_mm
      label: Millimetre (mm)
    - id: 1
      name: Length_m
      label: Metre (m)
    - id: 2
      name: Length_in
      label: Inch (in)
```

### 3c. Class types — constructor + fields

```yaml
# data-type/pre/class/JPT_NASTRAN_ANALYSIS.yaml
psj: '3.3'
kind: data_type
id: pre/class/JPT_NASTRAN_ANALYSIS
title: 'JPT_NASTRAN_ANALYSIS'
category: class
description: >
    Input parameter block for Nastran analysis configuration.
since: '5.0.0'
constructor_syntax: 'JPT_NASTRAN_ANALYSIS(iSolverType=0)'

fields:
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

### 3d. Composite class with methods

```yaml
# data-type/gui/class/PSJMessageBox.yaml
psj: '3.3'
kind: data_type
id: gui/class/PSJMessageBox
title: 'PSJMessageBox'
category: class
description: >
    Message box dialog class. Construct and configure the dialog, then call show() to display it and retrieve the user's
    response.
since: '5.0.0'
constructor_syntax: 'PSJMessageBox()'

# Methods are full item files in the psj-gui domain.
# $ref paths include the domain prefix and resolve across any domain.
methods:
    - $ref: 'psj-gui/msgbox/set_caption'
    - $ref: 'psj-gui/msgbox/set_header'
    - $ref: 'psj-gui/msgbox/set_icon'
    - $ref: 'psj-gui/msgbox/set_message'
    - $ref: 'psj-gui/msgbox/enable_checkbox'
    - $ref: 'psj-gui/msgbox/set_buttons'
    - $ref: 'psj-gui/msgbox/add_button'
    - $ref: 'psj-gui/msgbox/show'

examples:
    - id: basic-usage
      title: Create and show a message box
      language: python
      code: |
          msgbox = PSJMessageBox()
          msgbox.set_caption(text="PSJ Message Box")
          msgbox.set_message(text="This is an error message box")
          msgbox.set_buttons(button_type=msgbox_buttons.yes_no_cancel)
          print("clicked:" + msgbox.show())
```

### 3e. Data-type locale sidecar — enumeration

```yaml
# data-type/pre/enum/DItemType.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: pre/enum/DItemType

description: >
    Jupiter の DItem の種類を表す列挙型。

values:
    2:
        label: サブアセンブリ
        description: ツリー表示用サブアセンブリノード。
    3:
        label: パーツ
    10:
        label: ノード
```

### 3f. Data-type locale sidecar — class

```yaml
# data-type/pre/class/JPT_NASTRAN_ANALYSIS.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: pre/class/JPT_NASTRAN_ANALYSIS

description: >
    Nastran解析設定の入力パラメータブロック。

fields:
    iSolverType:
        description: Nastranソルバーのバリアント。
        enum_values:
            0: デフォルト
            1: SMP
```

---

## 4. Param group files — `_groups/<id>.yaml`

```yaml
# _groups/nastran-base.yaml
psj: '3.3'
kind: param_group
id: nastran-base
description: >
    Parameters shared by all Nastran analysis export commands.
extends: ~
params:
    - name: strName
      type: String
      required: false
      default: '"Job_1"'
      description: Job name for the Nastran analysis.

    - name: nastranAnalysis
      type: '$ref:data-type/pre/class/JPT_NASTRAN_ANALYSIS'
      required: false
      default: 'JPT_NASTRAN_ANALYSIS()'
      description: Nastran analysis input parameters.

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
```

### Group locale sidecar

```yaml
# _groups/nastran-base.ja.yaml
psj: '3.3'
kind: param_group
locale: ja
id: nastran-base

description: >
    すべてのNastran解析エクスポートコマンドで共有されるパラメータ。

params:
    strName:
        display_name: ジョブ名
        description: Nastran解析のジョブ名。
    nastranAnalysis:
        description: Nastran解析入力パラメータ。
    strPath:
        display_name: エクスポートパス
        description: BDFファイルのエクスポート先パス。
    iModelCheckAnswer:
        description: ダミープロパティのモデルチェック。
        enum_values:
            0: '無効'
            1: '有効'
```

---

## 5. Item files — `<domain>/<SubFolder>/<id>.yaml`

### 5a. PSJ Command — pure group reference

```yaml
# psj-command/Nastran/LinearStatic.yaml
psj: '3.3'
id: Nastran/LinearStatic
title: 'Analysis.Nastran.LinearStatic()'
domain: psj-command
namespace: Analysis.Nastran
ribbon: 'Analysis > Nastran > LinearStatic'
description: >
    Export the Nastran BDF input file for Structure Linear Static analysis (SOL 101).
since: '5.0.0'
stability: stable
macro_link: Analysis/NastranJob
syntax: 'Analysis.Nastran.LinearStatic(...)'

params:
    - $group: nastran-base

returns:
    kind: typed
    type: Cursor
    description: The created Nastran job.
```

### 5b. PSJ Command — group with exclusions, overrides, and additions

```yaml
# psj-command/Nastran/DirectFrequencyResponse.yaml
psj: '3.3'
id: Nastran/DirectFrequencyResponse
title: 'Analysis.Nastran.DirectFrequencyResponse()'
domain: psj-command
namespace: Analysis.Nastran
ribbon: 'Analysis > Nastran > DirectFrequencyResponse'
description: >
    Export the Nastran BDF for Direct Frequency Response analysis (SOL 108).
since: '5.0.0'
stability: stable
macro_link: Analysis/NastranJob
syntax: 'Analysis.Nastran.DirectFrequencyResponse(...)'

params:
    - $group: nastran-base
      exclude:
          - bDummyPropAutoAssign
          - iDummyPropMaterialID
      override:
          strPath:
              description: Export path for the frequency response BDF file.

    - name: bOutputXYPlots
      type: Boolean
      required: false
      default: 'False'
      description: Enable XY plot output.

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

### 5c. PSJ Command — group with mid-list insertion

```yaml
# psj-command/ADVC/MakeProcess/Dynamic.yaml
psj: '3.3'
id: ADVC/MakeProcess/Dynamic
title: 'Analysis.ADVC.MakeProcess.Dynamic()'
domain: psj-command
namespace: Analysis.ADVC.MakeProcess
ribbon: 'Analysis > ADVC > Make Process > Dynamic'
description: Create an ADVC Structure Dynamic process.
since: '5.0.0'
stability: stable
macro_link: Analysis/AdvcDynamicProcess
syntax: 'Analysis.ADVC.MakeProcess.Dynamic(...)'

params:
    - $group: advc-process-struct
      insert_after: advcAutoIncrement
      insert:
          - name: bDynamic
            type: Boolean
            required: false
            default: 'False'
            description: Enable dynamic parameter settings.
          - name: advcDynamic
            type: '$ref:data-type/pre/class/JPT_ADVC_DYNAMIC'
            required: false
            default: 'JPT_ADVC_DYNAMIC()'
            description: Dynamic parameters. Active when bDynamic=True.

returns:
    kind: typed
    type: Cursor
    description: The created or modified ADVC Dynamic process.
```

### 5d. Macro — positional params

```yaml
# macro/Analysis/AdvcStaticProcess.yaml
psj: '3.3'
id: Analysis/AdvcStaticProcess
title: 'AdvcStaticProcess()'
domain: macro
description: Create ADVC static process.
since: '5.0.0'
stability: stable
command_link: ADVC/MakeProcess/Static
syntax: >
    AdvcStaticProcess(string m_strName, int m_iGeomNonlinear,
      int fixed_or_auto, int num_of_inc, double max_time,
      double max_dt, double min_dt, int load_type, ...)

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
    - id: default-process
      title: Create process with default settings
      language: psj
      code: |
          JPT.Exec('AdvcStaticProcess("ADVC_DEFAULT_PROCESS", 0, 0, 1, 1, 1, 1e-05, -1, ...)')
```

### 5e. PSJ Utility — with callout

```yaml
# psj-utility/JPT/BeginDatabaseTransaction.yaml
psj: '3.3'
id: JPT/BeginDatabaseTransaction
title: 'JPT.BeginDatabaseTransaction()'
domain: psj-utility
namespace: JPT
description: >
    Disable screen animation, screen update, and status bar updates to improve Jupiter's performance during batch
    operations.
since: '5.0.0'
stability: stable
syntax: 'JPT.BeginDatabaseTransaction("transactionName")'

callouts:
    - id: must-end-transaction
      level: warn
      text: >
          JPT.EndDatabaseTransaction() must be called at the end of the process to return Jupiter to the normal state.

params:
    - name: transactionName
      type: String
      required: true
      description: Transaction name displayed in the Undo/Redo menu.

returns:
    kind: void

see_also:
    - $ref: 'psj-utility/JPT/EndDatabaseTransaction'
```

### 5f. PSJ-GUI — class method

Methods on composite class types live as full item files in the `psj-gui` domain. `class_ref` points back to the owning
data-type and MUST NOT appear outside `psj-gui`.

```yaml
# psj-gui/msgbox/add_button.yaml
psj: '3.3'
id: msgbox/add_button
title: 'PSJMessageBox.add_button()'
domain: psj-gui
namespace: PSJMessageBox
description: Add a custom button to the message box.
since: '5.0.0'
stability: stable
syntax: 'msgbox.add_button(text, id)'
class_ref: 'data-type/gui/class/PSJMessageBox'

params:
    - name: text
      type: String
      required: true
      description: Label displayed on the button.

    - name: id
      type: String
      required: true
      description: Identifier returned by show() when this button is clicked.

returns:
    kind: void

see_also:
    - $ref: 'psj-gui/msgbox/show'
```

### 5g. PSJ-GUI — standard dialog method

```yaml
# psj-gui/dlg/add_1delement_selector.yaml
psj: '3.3'
id: dlg/add_1delement_selector
title: 'dlg.add_1delement_selector()'
domain: psj-gui
namespace: dlg
description: >
    Add a 1D element selector to the dialog, enabling the user to select 1D elements and store the selection.
since: '5.0.0'
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

## 6. Delta versioning

### 6a. Item delta — removing params

```yaml
# psj-command/ADVC/Structure.yaml
psj: '3.3'
id: ADVC/Structure
title: 'Analysis.ADVC.Structure()'
domain: psj-command
since: '5.0.0'
macro_link: Analysis/ADVC_Structure
syntax: 'Analysis.ADVC.Structure(...)'

params:
    - $group: advc-structure-base

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
      notes: iEJobType and iHeatConvection removed.
      params:
          remove:
              - iEJobType
              - iHeatConvection
```

### 6b. Full delta operation vocabulary

```yaml
changes:
    - version: 'X.Y.Z'
      notes: 'Summary.'

      # Patch top-level fields.
      item:
          description: 'Revised.'
          ribbon: 'New > Path'
          stability: deprecated

      # Item files — param-level changes.
      params:
          add:
              - name: bNewFeature
                type: Boolean
                required: false
                default: 'False'
                description: New capability.
                after: strPath
          remove:
              - iRemovedParam
          modify:
              - name: strName
                changes:
                    description: 'Revised.'
                    default: '"NewDefault"'
                    required: true
                    deprecated: 'Use strJobName instead.'
                    enum_values:
                        add:
                            - id: 5
                              label: New option
                        remove:
                            - 2

      # built-in / enumeration data-type files — value-level changes.
      values:
          add:
              - id: 99
                name: NEW_VARIANT
                label: New Variant
                after: 10
          remove:
              - 3
          modify:
              - id: 2
                changes:
                    label: 'Updated Label'
                    deprecated: true

      # class data-type files — field-level changes.
      fields:
          add:
              - name: bNewField
                type: Boolean
                required: false
                default: 'False'
                description: New field.
          remove:
              - crObsoleteField
          modify:
              - name: iCurflag
                changes:
                    description: 'Revised.'
                    default: '1'
```

**Resolution rules:**

- The base `params` / `values` / `fields` list represents the file as of `introduced `.
- `changes` entries are applied in version order up to the requested version.
- `remove` deletes an entry from the resolved list; the definition stays in the file for older-version renders.
- `add` inserts at the named position; omit `after` to append.
- `modify` patches only the named fields; all other fields are unchanged.
- `item` patches top-level fields; any field not listed is unchanged.
- `params` delta MUST NOT appear on data-type files.
- `values` delta MUST NOT appear on item files or `category: class` data-type files.
- `fields` delta MUST NOT appear on item files or `category: built-in` / `category: enumeration` data-type files.

---

## 7. Locale sidecar files

### 7a. Localizable vs. structural fields

| Field                            | Localizable?                |
| -------------------------------- | --------------------------- |
| `description` (any file)         | ✅                          |
| `params[].description`           | ✅                          |
| `params[].display_name`          | ✅                          |
| `params[].deprecated`            | ✅ reason string            |
| `enum_values[].label`            | ✅                          |
| `enum_values[].description`      | ✅                          |
| `fields[].description`           | ✅                          |
| `fields[].remarks`               | ✅                          |
| `fields[].enum_values[].label`   | ✅                          |
| `values[].label`                 | ✅                          |
| `values[].description`           | ✅                          |
| `returns.description`            | ✅                          |
| `returns.codes[].meaning`        | ✅                          |
| `callouts[].text`                | ✅                          |
| `examples[].title`               | ✅                          |
| `meta.yaml` → `title`            | ✅ via `meta.<locale>.yaml` |
| `meta.yaml` → `description`      | ✅ via `meta.<locale>.yaml` |
| `id`, `title`, `syntax`, `code`  | ❌ code symbols             |
| `type`, `default`, `required`    | ❌ structural               |
| `namespace`, `ribbon`, `domain`  | ❌ structural               |
| `introduced `, `macro_link`      | ❌ structural               |
| `stability`, `category`          | ❌ structural               |
| `constructor_syntax`             | ❌ code symbol              |
| `values[].id`, `values[].name`   | ❌ structural               |
| `fields[].name`, `fields[].type` | ❌ structural               |

### 7b. Item locale sidecar

```yaml
# psj-command/ADVC/MakeProcess/Dynamic.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: ADVC/MakeProcess/Dynamic

description: >
    ADVC構造ダイナミックプロセスを作成します。

params:
    bDynamic:
        description: ダイナミックパラメータ設定の有効/無効。
    advcDynamic:
        description: ダイナミックパラメータの設定。bDynamic=Trueの場合に有効。

returns:
    description: 作成または変更されたADVCダイナミックプロセスのカーソル。

callouts:
    must-end-transaction:
        text: >
            処理の終了時にJPT.EndDatabaseTransaction()を呼び出して Jupiterを通常の状態に戻す必要があります。

examples:
    default-process:
        title: デフォルト設定でのプロセス作成
```

### 7c. Macro locale sidecar

```yaml
# macro/Analysis/AdvcStaticProcess.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: Analysis/AdvcStaticProcess

description: ADVCスタティックプロセスを作成します。

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

returns:
    codes:
        '"1"': 関数を実行できます。
        '"0"': 関数を実行できません。

examples:
    default-process:
        title: デフォルト設定でのプロセス作成
```

### 7d. Data-type locale sidecar — enumeration

```yaml
# data-type/pre/enum/DItemType.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: pre/enum/DItemType

description: >
    Jupiter の DItem の種類を表す列挙型。

values:
    2:
        label: サブアセンブリ
        description: ツリー表示用サブアセンブリノード。
    3:
        label: パーツ
    10:
        label: ノード
```

### 7e. Data-type locale sidecar — class

```yaml
# data-type/pre/class/JPT_NASTRAN_ANALYSIS.ja.yaml
psj: '3.3'
kind: locale_sidecar
locale: ja
id: pre/class/JPT_NASTRAN_ANALYSIS

description: >
    Nastran解析設定の入力パラメータブロック。

fields:
    iSolverType:
        description: Nastranソルバーのバリアント。
        enum_values:
            0: デフォルト
            1: SMP
```

---

## 8. Locale resolution algorithm

```python
function resolve(file_id, field_path, locale):

  1. If locale == default_locale (en):
       return base_file[field_path]

  2. Load sidecar: <file_path>.<locale>.yaml
     If sidecar exists AND sidecar[field_path] exists:
       return sidecar[field_path]

  3. If field_path is on a param that originated from a $group reference:
       Load group sidecar: _groups/<group_id>.<locale>.yaml
       If group_sidecar[field_path] exists:
         return group_sidecar[field_path]
       If group has `extends`:
         recurse into parent group sidecar (depth-first, parent last)

  4. Fallback: return base_file[field_path]   # en text; no error logged
```

Fallback is silent. Partial translations are valid and expected.

---

## 9. Renderer decisions driven by `domain`

Applies to the four callable item domains only. `data-type` is not a domain and has its own renderer (Section 10).

| Behaviour                           | `macro`           | `psj-command`   | `psj-utility` | `psj-gui`         |
| ----------------------------------- | ----------------- | --------------- | ------------- | ----------------- |
| Show Position column in param table | ✅                | —               | —             | —                 |
| Show namespace prefix in title      | —                 | ✅              | ✅            | ✅                |
| Show Ribbon path                    | —                 | ✅ if present   | —             | —                 |
| Show macro linkage card             | ✅ `command_link` | ✅ `macro_link` | —             | —                 |
| Show class back-reference card      | —                 | —               | —             | ✅ if `class_ref` |
| Syntax highlight style              | `psj-macro`       | Python          | Python        | Python            |
| Return renders as                   | Code table        | Type link       | "No output"   | "No output"       |
| Stability badge                     | ✅                | ✅              | ✅            | ✅                |

---

## 10. Data-type renderer

Data-type pages are rendered as first-class pages under `psjapi/data-type/` in Fumadocs. They are navigable, linkable,
and expandable by users checking type definitions while reading item documentation.

### 10a. Output URL structure

```text
psjapi/
  data-type/
    built-in/
      python-built-in-types
      jupiter-built-in-types
    pre/
      built-in/
        BodyVector
        ConnectVector
        VersionInfo
      enum/
        DItemType
        ElemType
        ElemKind
        MaterialPropertyType
        MaterialUnitType
        LengthUnit
        TimeUnit
        ...
      class/
        JPT_NASTRAN_ANALYSIS
        JPT_ABAQUS_LBC_STEP_INFO
        ...
    post/
      built-in/
        DPostAnalysis
        DPostElem
        DPostTimeStep
      enum/
        PostAnalysisType
        ...
    gui/
      built-in/
        PSJFont
        TableCellID
        TableCellRange
      class/
        PSJMessageBox
```

### 10b. Renderer behaviour by category

| Behaviour                       | `built-in`    | `enumeration`        | `class`                 |
| ------------------------------- | ------------- | -------------------- | ----------------------- |
| Show `namespace` accessor badge | ✅ if present | ✅ if present        | —                       |
| Show `constructor_syntax` block | —             | —                    | ✅ if present           |
| Show values table               | ✅            | ✅                   | —                       |
| Values table has Name column    | —             | ✅ if any `name` set | —                       |
| Show fields table               | —             | —                    | ✅ if `fields` present  |
| Show methods list               | —             | —                    | ✅ if `methods` present |
| Methods link to item pages      | —             | —                    | ✅                      |
| Show examples block             | ✅ if present | ✅ if present        | ✅ if present           |
| Show see_also block             | ✅ if present | ✅ if present        | ✅ if present           |
| Show version badge              | ✅            | ✅                   | ✅                      |
| Show stability badge            | ✅            | ✅                   | ✅                      |
| Show `deprecated` warning       | ✅ per value  | ✅ per value         | ✅ per field            |

### 10c. Inline type links in item pages

When a param or return `type` contains a `$ref:data-type/<id>`, the renderer MUST emit an inline hyperlink to the
corresponding data-type page. The link text is the type's `title`.

```text
# Rendered param row example:
nastranAnalysis  |  JPT_NASTRAN_ANALYSIS ↗  |  No  |  JPT_NASTRAN_ANALYSIS()
                        ↑ links to psjapi/data-type/pre/class/JPT_NASTRAN_ANALYSIS
```

### 10d. Fumadocs sidebar integration

The `data-type/` tree is included in the Fumadocs sidebar under a top-level `Data Types` section, separate from the four
domain sections. Each scope folder (`built-in/`, `pre/`, `post/`, `gui/`) becomes a collapsible sidebar group driven by
its `meta.yaml`.

```text
Sidebar:
  ├── Macros
  ├── PSJ Commands
  ├── PSJ Utilities
  ├── PSJ GUI
  └── Data Types              ← top-level collapsible
        ├── Built-in Types
        ├── Pre-Processing
        │     ├── Built-in
        │     ├── Enumerations
        │     └── Classes
        ├── Post-Processing
        │     ├── Built-in
        │     └── Enumerations
        └── GUI
              ├── Built-in
              └── Classes
```

---

## 11. Complete field reference

### Item file

```yaml
psj: '3.3'
id: string                  # required; path relative to domain root
title: string               # required; verbatim call signature
domain: string              # required; must match a manifest domain id
namespace: string?          # optional; dotted call prefix; omit for macros
ribbon: string?             # optional; psj-command only
description: string         # required; localizable
since: string  # required; must match a manifest version id
stability: string?          # optional; stable | experimental | deprecated; default: stable
macro_link: string?         # optional; path-based id; psj-command only
command_link: string?       # optional; path-based id; macro only
class_ref: string?          # optional; data-type path-based id; psj-gui only
syntax: string              # required
callouts: [Callout]?        # optional
params: [Param | GroupRef]  # required
returns: Returns            # required
examples: [Example]?        # optional; always inline
see_also: [Ref]?            # optional
changes: [VersionDelta]?    # optional
```

### Data-type file

```yaml
psj: '3.3'
kind: data_type             # required; must be data_type
id: string                  # required; path relative to data-type/
                            # e.g. pre/enum/DItemType, gui/class/PSJMessageBox
title: string               # required; display title
category: string            # required; built-in | enumeration | class
namespace: string?          # optional; Python accessor prefix e.g. JPT.DItemType
description: string         # required; localizable
since: string  # required; must match a manifest version id
stability: string?          # optional; stable | experimental | deprecated; default: stable

# category: built-in or enumeration
values: [DataTypeValue]?    # required for built-in and enumeration

# category: class
constructor_syntax: string? # optional; NOT localizable
fields: [Field]?            # optional
methods: [Ref]?             # optional; $ref to item files; any domain allowed

# shared
examples: [Example]?
see_also: [Ref]?
changes: [VersionDelta]?
```

### DataTypeValue

```yaml
id: integer | string # required; NOT localizable; stable across versions
name: string? # optional; constant accessor e.g. JPT.DItemType.BODY
label: string # required; localizable
description: string? # optional; localizable
deprecated: boolean? # optional
```

### Field (class data-types)

```yaml
name: string                # required; NOT localizable
type: string                # required; see Type system
required: boolean           # required
default: string?            # optional
description: string         # required; localizable
enum_values: [EnumValue]?   # optional
remarks: string?            # optional; localizable
deprecated: string?         # optional; presence implies deprecated; value is reason
```

### Param

```yaml
position: integer?          # optional; 1-based; macro only
name: string                # required for named params
display_name: string?       # optional; localizable
type: string                # required; see Type system
required: boolean           # required
default: string?            # optional
description: string         # required; localizable
enum_values: [EnumValue]?   # optional
deprecated: string?         # optional; presence implies deprecated; value is reason
```

### GroupRef

```yaml
$group: string              # required; id of a _groups/<id>.yaml
exclude: [string]?          # optional; param names to drop
insert_after: string?       # optional; param name after which to splice insert
insert: [Param]?            # optional
override:                   # optional; param name → fields to patch
  <param_name>:
    description: string?
    default: string?
    required: boolean?
```

### Returns

```yaml
kind: string                # required; typed | macro_code | void
type: string?               # required when kind=typed; MUST NOT appear otherwise
description: string?        # optional; localizable; MUST NOT appear when kind=void
codes: [Code]?              # required when kind=macro_code
```

### Code

```yaml
value: string # required; NOT localizable
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
code: string # required; NOT localizable; always inline
```

### VersionDelta

```yaml
version: string             # required; must match a manifest version id
notes: string?              # optional

item:                       # optional; top-level fields to patch
  description: string?
  ribbon: string?
  stability: string?

params:                     # optional; item files only
  add: [Param]?
  remove: [string]?
  modify: [ParamPatch]?

values:                     # optional; built-in and enumeration data-type files only
  add: [DataTypeValue]?     # each may carry `after: <value_id>`
  remove: [integer|string]?
  modify: [ValuePatch]?

fields:                     # optional; class data-type files only
  add: [Field]?             # each may carry `after: <field_name>`
  remove: [string]?
  modify: [FieldPatch]?
```

### ParamPatch

```yaml
name: string
changes:
  description: string?
  default: string?
  required: boolean?
  deprecated: string?
  enum_values:
    add: [EnumValue]?
    remove: [integer | string]?
```

### ValuePatch

```yaml
id: integer | string
changes:
    label: string?
    description: string?
    deprecated: boolean?
```

### FieldPatch

```yaml
name: string
changes:
  description: string?
  default: string?
  required: boolean?
  remarks: string?
  deprecated: string?
  enum_values:
    add: [EnumValue]?
    remove: [integer | string]?
```

### EnumValue

```yaml
id: integer | string # required; NOT localizable; stable across versions
label: string # required; localizable
description: string? # optional; localizable
```

### Ref

```yaml
$ref: string # required; "<domain>/<id>" or "data-type/<id>"
```

### Group meta file

```yaml
psj: '3.3'
kind: group_meta            # required
title: string               # required; display label
description: string?        # optional; localizable
order: [string]?            # optional; if present ALL children must be listed
icon: string?               # optional; icon hint for renderer
```

### ParamGroup file

```yaml
psj: '3.3'
kind: param_group # required
id: string # required; unique across all group files
description: string? # optional; localizable
extends: string? # optional; id of parent group
params: [Param] # required
```

### Locale sidecar (item or param group)

```yaml
psj: '3.3'
kind: locale_sidecar
locale: string
id: string

description: string?

callouts:
    <callout_id>:
        text: string

params:
    # Named params:
    <param_name>:
        display_name: string?
        description: string?
        deprecated: string?
        enum_values:
            <id>: string

    # Positional params (macro):
    <position_integer>:
        description: string?
        enum_values:
            <id>: string

returns:
    description: string?
    codes:
        <value>: string

examples:
    <example_id>:
        title: string?
```

### Locale sidecar (data-type)

```yaml
psj: '3.3'
kind: locale_sidecar
locale: string
id: string # path-based data-type id e.g. pre/enum/DItemType

description: string?

# built-in or enumeration data-types — keyed by value id:
values:
    <value_id>:
        label: string?
        description: string?

# class data-types — keyed by field name:
fields:
    <field_name>:
        description: string?
        remarks: string?
        deprecated: string?
        enum_values:
            <id>: string

examples:
    <example_id>:
        title: string?
```

---

## 12. Type system

| Form          | Example                                             | Notes                                  |
| ------------- | --------------------------------------------------- | -------------------------------------- |
| Primitive     | `String`, `Integer`, `Boolean`, `Double`            | Case-sensitive                         |
| SDK cursor    | `Cursor`                                            | Points to any SDK object               |
| Generic list  | `List[Cursor]`, `List[Integer]`                     | Single type argument                   |
| Data-type ref | `$ref:data-type/pre/class/JPT_NASTRAN_ANALYSIS`     | Full semantic-scope path required      |
| List of ref   | `List[$ref:data-type/pre/class/JPT_ADVC_LOAD_NODE]` | Combines list and ref                  |
| Untyped list  | `List`                                              | Only when element type is undocumented |
| Vector        | `Vector`                                            | Fixed-length numeric tuple             |

Renderer MUST emit an inline hyperlink to `psjapi/data-type/<id>` for every `$ref:data-type/<id>` occurrence in a param
or return `type` field.

---

## 13. Validation rules

Tooling MUST enforce these rules at build time and report them as errors.

**Manifest**:

1. `psj` version in every file MUST match the manifest `psj` version.
2. `current_version` MUST equal one of the `versions[].id` values.
3. `versions` MUST be ordered oldest → newest (strict semver ascending).
4. Exactly one locale MUST carry `default: true`.
5. Each `domain.id` MUST be unique within the manifest domains list.
6. `data-type` MUST NOT appear as a `domain.id`.

**Identity & references** 7. Each item `id` MUST equal its path relative to the domain root using `/` separators without
file extension. 8. Each data-type `id` MUST equal its path relative to `data-type/` using `/` separators without file
extension. 9. The first path segment of a data-type `id` MUST be one of `built-in`, `pre`, `post`, `gui`. 10. Every
`$group` reference MUST resolve to an existing `_groups/<id>.yaml`. 11. Every `$ref:data-type/<id>` MUST resolve to an
existing data-type file whose `category` is consistent with the usage context. 12. Every `$ref: <domain>/<id>` in
`see_also` or `methods` MUST resolve to an existing item file. 13. `macro_link` and `command_link` targets MUST resolve
to existing item files. 14. `class_ref` MUST resolve to a data-type file with `category: class`. 15. Every `introduced `
and `changes[].version` MUST match a manifest `versions[].id`.

**Folder & meta** 16. Every subfolder within a domain root and within `data-type/` MUST contain a `meta.yaml` with
`kind: group_meta`. 17. If `order` is present in `meta.yaml`, ALL direct children MUST be listed — partial ordering is
not allowed. 18. `order` entries MUST each resolve to an existing child file stem or subfolder name. 19.
`meta.<locale>.yaml` locale tag MUST match a locale declared in the manifest. 20. The `group` field MUST NOT appear in
any item or data-type file.

**Data-type category placement** 21. `category: built-in` files MUST reside in a `built-in/` subfolder. 22.
`category: enumeration` files MUST reside in an `enum/` subfolder. 23. `category: class` files MUST reside in a `class/`
subfolder.

**Data-type field constraints** 24. `category: built-in` or `category: enumeration` MUST include `values` and MUST NOT
include `fields`, `constructor_syntax`, or `methods`. 25. `category: class` MUST NOT include `values`. MAY include
`fields`, `constructor_syntax`, and `methods`. 26. `domain_scope` MUST NOT appear in any data-type file.

**Item field constraints** 27. `class_ref` MUST NOT appear on items whose `domain` is not `psj-gui`. 28. `macro_link`
MUST NOT appear on items whose `domain` is not `psj-command`. 29. `command_link` MUST NOT appear on items whose `domain`
is not `macro`. 30. `ribbon` MUST NOT appear on items whose `domain` is not `psj-command`.

**Group references** 31. `GroupRef.insert_after` MUST name a param that exists in the resolved group after `exclude` is
applied. 32. `GroupRef.exclude` names MUST all exist in the referenced group. 33. `GroupRef.override` keys MUST all
exist in the referenced group after `exclude` is applied.

**Delta versioning** 34. `VersionDelta.params` MUST NOT appear on data-type files. 35. `VersionDelta.values` MUST NOT
appear on item files or `category: class` data-type files. 36. `VersionDelta.fields` MUST NOT appear on item files,
`category: built-in`, or `category: enumeration` data-type files. 37. `VersionDelta.params.remove` names MUST exist in
the effective param list at that version. 38. `VersionDelta.params.modify[].name` MUST exist in the effective param list
at that version. 39. `VersionDelta.values.remove` ids MUST exist in the effective values list at that version. 40.
`VersionDelta.values.modify[].id` MUST exist in the effective values list at that version. 41.
`VersionDelta.fields.remove` names MUST exist in the effective fields list at that version. 42.
`VersionDelta.fields.modify[].name` MUST exist in the effective fields list at that version.

**Sidecars** 43. Within a sidecar, `callouts` keys MUST match `id` values in the base file. 44. Within a sidecar,
`examples` keys MUST match `id` values in the base file. 45. Within a sidecar, `values` keys MUST match `id` values in
the base file `values` list. 46. Within a sidecar, `fields` keys MUST match `name` values in the base file `fields`
list. 47. Sidecar `locale` MUST match a locale declared in the manifest.

**Params and values** 48. Positional param `position` values MUST be unique within an item. 49. Named param `name`
values MUST be unique within the resolved param list of an item. 50. Each `EnumValue.id` MUST be unique within its
`enum_values` list. 51. Each `DataTypeValue.id` MUST be unique within its `values` list. 52. Each `Field.name` MUST be
unique within its `fields` list.

**Field values** 53. `stability` MUST be one of `stable`, `experimental`, `deprecated`. If absent, treat as
`stable`. 54. `Callout.level` MUST be one of `warn`, `info`, `danger`. 55. `Returns.kind` MUST be one of `typed`,
`macro_code`, `void`. 56. `kind: typed` MUST include `type`. `kind: void` MUST NOT include `type` or `description`.
`kind: macro_code` MUST NOT include `type` and MUST include a non-empty `codes` list. 57. `category` MUST be one of
`built-in`, `enumeration`, `class`. 58. `methods` entries MUST use full `$ref` paths including domain prefix.

---

## 14. Tooling & Integration

### Fumadocs & `meta.json` Generation

- Each `meta.yaml` maps to a Fumadocs `meta.json` in the corresponding output folder.
- The `order` field drives the `pages` array in the emitted `meta.json`.
- The `title` field resolved via `meta.<locale>.yaml` drives the folder display label.
- The `folderStyle` configuration determines output shape:
    - **`folder`**: Emits actual nested sub-directories.
    - **`separator`**: Emits flattened logical groups using Fumadocs text separators.

### Data-type page generation

The `psjapi/server` converter generates a Fumadocs page for every data-type file. Pages are placed under
`psjapi/data-type/<scope>/` mirroring the source tree. The converter:

1. Reads each `data-type/<scope>/<category>/<id>.yaml`.
2. Resolves locale via the sidecar algorithm.
3. Emits an MDX page at `psjapi/data-type/<scope>/<category>/<id>.mdx`.
4. Emits a `meta.json` for each folder driven by the corresponding `meta.yaml`.
5. Registers each data-type page in the top-level sidebar under **Data Types**.

### Inline type link resolution

For every param or return `type` containing `$ref:data-type/<id>`, the converter emits a hyperlink component pointing to
`psjapi/data-type/<id>`. Broken `$ref` paths are build errors (Rule 11).
