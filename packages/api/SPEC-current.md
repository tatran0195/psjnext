# psjapi — Jupiter CAE Desktop SDK Documentation Format

**Format identifier:** `psjapi` **File extension:** `.yaml` (identified by `psjapi:` version key) **Current version:**
`1.0`

psjapi is the documentation format for the Jupiter CAE Desktop Platform SDK. It describes every callable item in the SDK
— macros, psj-commands, psj-utilities, and psj-gui methods — in a unified schema designed for authoring at scale:
thousands of items, multiple SDK versions, and multiple human languages.

---

## Design goals

| Goal                                          | Mechanism                                           |
| --------------------------------------------- | --------------------------------------------------- |
| One format for all four callable domains      | `domain:` field drives all renderer decisions       |
| No repeated param definitions across siblings | Param groups (`_groups/`) referenced by `$group:`   |
| No full-file copies across SDK versions       | Delta blocks (`changes:`) record only what changed  |
| Translations without polluting structure      | Sidecar locale files (`<id>.ja.yaml`)               |
| Examples always co-located with their item    | Inline `examples:` block, never file links          |
| Partial translations are valid                | Silent fallback to `en` when a locale key is absent |

---

## Repository layout

```
sdk.psjapi.yaml                  ← root manifest
_groups/
  <group-id>.yaml                ← reusable param group definition
  <group-id>.ja.yaml             ← Japanese translations for that group
  <group-id>.zh.yaml             ← (future) Chinese translations
macro/
  <id>.yaml
  <id>.ja.yaml
psj-command/
  <id>.yaml
  <id>.ja.yaml
psj-utility/
  <id>.yaml
  <id>.ja.yaml
psj-gui/
  <id>.yaml
  <id>.ja.yaml
```

The base file (`.yaml`) is always English — the source of truth for both structure and English text. A locale sidecar
contains only the natural-language fields for that locale. Structural fields (`id`, `type`, `default`, `syntax`, `code`,
…) never appear in sidecars.

---

## 1. Root manifest — `sdk.psjapi.yaml`

```yaml
psjapi: '1.0'

sdk:
    name: 'Jupiter CAE Desktop Platform SDK'
    vendor: 'TechnoStar Co., Ltd.'
    vendor_url: 'https://www.e-technostar.com/'

versions:
    # Ordered oldest → newest.
    # Adding an entry here is all that's needed to unlock the delta system for
    # items that changed in that release.
    - id: '5.0.0'
    - id: '5.0.1'
      notes: 'Removed iEJobType and iHeatConvection from Analysis.ADVC.Structure'
    - id: '5.1.0'
      notes: 'Current release'

current_version: '5.1.0'

locales:
    - id: en
      label: English
      default: true # base files are the EN source; no sidecar needed for EN
    - id: ja
      label: 日本語
    # - id: zh
    #   label: 中文

domains:
    - id: macro
      title: Macros
      param_style: positional # renderer shows Position column; hides Name column
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

---

## 2. Param group files — `_groups/<id>.yaml`

A param group is a named, ordered list of param definitions with no domain, syntax, or return value of its own. Any item
file includes it by reference. Groups can extend other groups.

### 2a. Group definition

```yaml
# _groups/nastran-base.yaml
psjapi: '1.0'
kind: param_group
id: nastran-base
description: >
    Parameters shared by all Nastran analysis export commands.

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
      type: List[Cursor]
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
      description: Existing Nastran job to modify. None creates a new job.

    - name: strPath
      type: String
      required: true
      description: Export path for the BDF file.

    - name: iModelCheckAnswer
      type: Integer
      required: false
      default: '0'
      description: Model checking for dummy properties (0=off, 1=on).

    - name: iDeleteSlaveNodesAnswer
      type: Integer
      required: false
      default: '0'
      description: Delete slave nodes checking (0=off, 1=on).
```

```yaml
# _groups/advc-process-base.yaml
psjapi: '1.0'
kind: param_group
id: advc-process-base
description: >
    Core parameters shared by all ADVC process commands.

params:
    - name: strName
      type: String
      required: true
      description: Process name.

    - name: crEdit
      type: Cursor
      required: false
      default: 'None'
      description: Existing process to modify. None creates a new process.

    - name: listLoadNode
      type: 'List[$ref:data-type/JPT_ADVC_LOAD_NODE]'
      required: false
      default: '[]'
      description: Nodes with assigned loads.

    - name: listLoadCaseNode
      type: 'List[$ref:data-type/JPT_ADVC_LOAD_NODE]'
      required: false
      default: '[]'
      description: Nodes with assigned load cases.

    - name: listLoadNodeContact
      type: 'List[$ref:data-type/JPT_ADVC_LOAD_NODE]'
      required: false
      default: '[]'
      description: Nodes with assigned contacts.

    - name: ilOutputParamList
      type: List[Integer]
      required: false
      default: '[]'
      description: Output request list (Displacement, Stress, Strain, …).

    - name: iRefType
      type: Integer
      required: false
      default: '0'
      description: Reference result type.
      enum_values:
          - id: 0
            label: Temperature Load
          - id: 1
            label: Stress

    - name: strRefPath
      type: String
      required: false
      default: '""'
      description: Path of reference result.

    - name: listAdvcRefStressResult
      type: 'List[$ref:data-type/JPT_ADVC_REF_STRESS_RESULT]'
      required: false
      default: '[]'
      description: Reference result data list.
```

```yaml
# _groups/advc-process-struct.yaml
psjapi: '1.0'
kind: param_group
id: advc-process-struct
extends: advc-process-base # inherits all params from base first

params:
    - name: iGeomNonlinear
      type: Integer
      required: false
      default: '0'
      description: Geometry nonlinearity mode.
      enum_values:
          - id: 0
            label: None
          - id: 1
            label: Total Lagrange
          - id: 2
            label: Updated Lagrange
          - id: 3
            label: Linear
          - id: 4
            label: NonLinear

    - name: advcStructTimeStep
      type: '$ref:data-type/JPT_ADVC_STRUCT_TIME_STEP'
      required: false
      default: 'JPT_ADVC_STRUCT_TIME_STEP()'
      description: Time step and output timing settings.

    - name: bConvergence
      type: Boolean
      required: false
      default: 'False'
      description: Enable convergence parameter settings.

    - name: advcConvergence
      type: '$ref:data-type/JPT_ADVC_CONVERGENCE'
      required: false
      default: 'JPT_ADVC_CONVERGENCE()'
      description: Convergence parameters. Active when bConvergence=True.

    - name: bContact
      type: Boolean
      required: false
      default: 'False'
      description: Enable contact iterator parameter settings.

    - name: advcContactIter
      type: '$ref:data-type/JPT_ADVC_CONTACT_ITER'
      required: false
      default: 'JPT_ADVC_CONTACT_ITER()'
      description: Contact iterator parameters. Active when bContact=True.

    - name: bAutoIncrement
      type: Boolean
      required: false
      default: 'False'
      description: Enable auto increment parameter settings.

    - name: advcAutoIncrement
      type: '$ref:data-type/JPT_ADVC_AUTO_INCREMENT'
      required: false
      default: 'JPT_ADVC_AUTO_INCREMENT()'
      description: Auto increment parameters. Active when bAutoIncrement=True.

    - name: dStabilizationFactor
      type: Double
      required: false
      default: '0.0'
      description: Stabilization factor.

    - name: bCrackGrowth
      type: Boolean
      required: false
      default: 'False'
      description: Enable crack growth parameter settings.

    - name: CrackGrowthParam
      type: '$ref:data-type/JPT_ADVC_CRACK_GROWTH'
      required: false
      default: '[]'
      description: Crack growth parameters. Active when bCrackGrowth=True.
```

### 2b. Group locale sidecar

The group sidecar translates params that belong to the group. Items referencing the group pick up these translations
automatically — they are never duplicated into item-level sidecars.

```yaml
# _groups/advc-process-base.ja.yaml
psjapi: '1.0'
locale: ja
id: advc-process-base

params:
    strName:
        display_name: プロセス名
        description: プロセス名。

    crEdit:
        description: 変更対象の既存プロセスのカーソル。Noneの場合は新規作成。

    listLoadNode:
        description: モデル内で荷重が割り当てられたノードのリスト。

    listLoadCaseNode:
        description: モデル内でロードケースが割り当てられたノードのリスト。

    listLoadNodeContact:
        description: モデル内でコンタクトが割り当てられたノードのリスト。

    ilOutputParamList:
        description: 変位・応力・ひずみなどの出力要求リスト。

    iRefType:
        description: 参照結果のタイプ。
        enum_values:
            0: 温度荷重
            1: 応力

    strRefPath:
        description: 参照結果のファイルパス。

    listAdvcRefStressResult:
        description: 参照結果データのリスト。
```

```yaml
# _groups/advc-process-struct.ja.yaml
psjapi: '1.0'
locale: ja
id: advc-process-struct

params:
    iGeomNonlinear:
        description: 幾何非線形オプション。
        enum_values:
            0: なし
            1: トータルラグランジュ法
            2: 更新ラグランジュ法
            3: 線形
            4: 非線形

    advcStructTimeStep:
        description: タイムステップおよび出力タイミング定義の設定。

    bConvergence:
        description: 収束パラメータ設定の有効/無効。

    advcConvergence:
        description: 収束パラメータの設定。bConvergence=Trueの場合に有効。

    bContact:
        description: コンタクトイテレータパラメータ設定の有効/無効。

    advcContactIter:
        description: コンタクトイテレータパラメータの設定。bContact=Trueの場合に有効。

    bAutoIncrement:
        description: 自動インクリメントパラメータ設定の有効/無効。

    advcAutoIncrement:
        description: 自動インクリメントパラメータの設定。bAutoIncrement=Trueの場合に有効。

    dStabilizationFactor:
        description: 安定化係数。

    bCrackGrowth:
        description: き裂進展パラメータ設定の有効/無効。

    CrackGrowthParam:
        description: き裂進展パラメータの設定。bCrackGrowth=Trueの場合に有効。
```

```yaml
# _groups/nastran-base.ja.yaml
psjapi: '1.0'
locale: ja
id: nastran-base

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
        description: ダミープロパティのモデルチェック（0=無効、1=有効）。

    iDeleteSlaveNodesAnswer:
        description: スレーブノード削除チェック（0=無効、1=有効）。
```

---

## 3. Item files — `<domain>/<id>.yaml`

### 3a. Minimal item — pure group reference

Seven Nastran commands share identical params. Each item file is four lines of identity plus one `$group` reference.

```yaml
# psj-command/Analysis-Nastran-LinearStatic.yaml
psjapi: '1.0'
id: Analysis-Nastran-LinearStatic
title: Analysis.Nastran.LinearStatic()
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: Analysis > Nastran > LinearStatic
description: Export the Nastran BDF input file for Structure Linear Static analysis (SOL 101).
version_introduced: '5.0.0'
macro_link: NastranJob

params:
    - $group: nastran-base

returns:
    kind: typed
    type: Cursor
    description: The created Nastran job.
```

The six other identical Nastran commands (`NormalModes`, `LinearBuckling`, `ModalFrequencyResponse`,
`ModalTransientResponse`, `SteadyState`, `Transient`) follow exactly this pattern, differing only in `id`, `title`,
`ribbon`, `description`, and their SOL number.

### 3b. Item that extends a group with excluded and reordered params

```yaml
# psj-command/Analysis-Nastran-DirectFrequencyResponse.yaml
psjapi: '1.0'
id: Analysis-Nastran-DirectFrequencyResponse
title: Analysis.Nastran.DirectFrequencyResponse()
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: Analysis > Nastran > DirectFrequencyResponse
description: Export the Nastran BDF for Direct Frequency Response analysis (SOL 108).
version_introduced: '5.0.0'
macro_link: NastranJob

params:
    - $group: nastran-base
      exclude: [bDummyPropAutoAssign, iDummyPropMaterialID, crEdit]

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

### 3c. Item with group insertion — ADVC Dynamic process

`Dynamic` is identical to `Static` except two params are inserted mid-list. The `insert_after` + `insert` mechanism
handles this without forking a new group.

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Dynamic.yaml
psjapi: '1.0'
id: Analysis-ADVC-MakeProcess-Dynamic
title: Analysis.ADVC.MakeProcess.Dynamic()
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: Analysis > ADVC > Make Process > Dynamic
description: Create an ADVC Structure Dynamic process.
version_introduced: '5.0.0'
macro_link: AdvcDynamicProcess

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
            type: '$ref:data-type/JPT_ADVC_DYNAMIC'
            required: false
            default: 'JPT_ADVC_DYNAMIC()'
            description: Dynamic parameters. Active when bDynamic=True.

returns:
    kind: typed
    type: Cursor
    description: The created or modified ADVC Dynamic process.
```

### 3d. Item using base group only — ADVC EigenValue

EigenValue doesn't use the structural group at all, only the base.

```yaml
# psj-command/Analysis-ADVC-MakeProcess-EigenValue.yaml
psjapi: '1.0'
id: Analysis-ADVC-MakeProcess-EigenValue
title: Analysis.ADVC.MakeProcess.EigenValue()
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: Analysis > ADVC > Make Process > Eigen Value
description: Create an ADVC EigenValue (Normal Modes) process.
version_introduced: '5.0.0'
macro_link: AdvcEigenProcess

params:
    - $group: advc-process-base

    - name: bEigenValue
      type: Boolean
      required: false
      default: 'False'
      description: Enable eigen value parameter settings.

    - name: advcNormalModal
      type: '$ref:data-type/JPT_ADVC_NORMAL_MODAL'
      required: false
      default: 'JPT_ADVC_NORMAL_MODAL()'
      description: Normal modal parameters. Active when bEigenValue=True.

returns:
    kind: typed
    type: Cursor
    description: The created or modified ADVC EigenValue process.
```

### 3e. Macro — positional params

Macros carry `position` instead of (or alongside) `name`. The C-style identifier is preserved exactly as written in the
source.

```yaml
# macro/AdvcStaticProcess.yaml
psjapi: '1.0'
id: AdvcStaticProcess
title: AdvcStaticProcess()
domain: macro
group: analysis
description: Create ADVC static process.
version_introduced: '5.0.0'
command_link: Analysis-ADVC-MakeProcess-Static

syntax: >
    AdvcStaticProcess(string m_strName, int m_iGeomNonlinear, int fixed_or_auto,
      int num_of_inc, double max_time, double max_dt, double min_dt, int load_type,
      int output_last, int output_interval, int restart_last, int restart_interval,
      double output_time_interval, double restart_time_interval,
      bool m_bConvergence, ...)

params:
    - position: 1
      name: m_strName
      type: String
      description: Name of ADVC static process.

    - position: 2
      name: m_iGeomNonlinear
      type: Integer
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
      description: Time step control.
      enum_values:
          - id: 0
            label: Auto
          - id: 1
            label: Fixed

    - position: 4
      name: num_of_inc
      type: Integer
      description: Number of increments.

    - position: 5
      name: max_time
      type: Double
      description: Maximum time.

    - position: 6
      name: max_dt
      type: Double
      description: Maximum time step size.

    - position: 7
      name: min_dt
      type: Double
      description: Minimum time step size.

    - position: 8
      name: load_type
      type: Integer
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
      description: Whether convergence parameters are defined.

    - position: 30
      name: m_bContact
      type: Boolean
      description: Whether contact iterator parameters are defined.

    - position: 43
      name: m_bAutoIncrement
      type: Boolean
      description: Whether auto increment parameters are defined.

    - position: 64
      name: m_crEdit
      type: Cursor
      description: Edit cursor for existing process.

    - position: 65
      name: m_LoadNodeList
      type: List
      description: Status of loads.

    - position: 66
      name: m_LoadCaseNodeList
      type: List
      description: Status of load cases.

    - position: 67
      name: m_LoadNodeContactList
      type: List
      description: Status and data of contacts.

    - position: 68
      name: m_OutputParamList
      type: List
      description: Output parameters.

    - position: 69
      name: m_iRefType
      type: Integer
      description: Reference result type.
      enum_values:
          - id: 0
            label: Temperature Load
          - id: 1
            label: Stress

    - position: 70
      name: m_strRefPath
      type: String
      description: Path of reference result.

    - position: 71
      name: m_ReferenceResultList
      type: List
      description: Reference result data.

returns:
    kind: macro_code
    codes:
        - value: '"1"'
          meaning: The function can be executed.
        - value: '"0"'
          meaning: The function cannot be executed.

examples:
    - language: psj
      code: |
          JPT.Exec('AdvcStaticProcess("ADVC_DEFAULT_PROCESS", 0, 0, 1, 1, 1, 1e-05,
            -1, -1, 2147483647, -1, 2147483647, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 1.79769e+308, 2147483647, 2147483647, 1.79769e+308,
            2147483647, 0, -1, 2147483647, 2147483647, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 1.79769e+308, 2147483647, 0, 1.79769e+308, 1.79769e+308,
            0, 0, 2147483647, 2147483647, 2147483647, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 2147483647, 2147483647, 1.79769e+308, 1.79769e+308,
            1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 1.79769e+308,
            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0:0,
            [(29:1, 0:0, 1), (29:2, 0:0, 1), (37:1, 0:0, 1)],
            [], [], [], -1, "", [], "", 2147483647)')
```

### 3f. Utility — with callout warning

```yaml
# psj-utility/JPT-BeginDatabaseTransaction.yaml
psjapi: '1.0'
id: JPT-BeginDatabaseTransaction
title: JPT.BeginDatabaseTransaction()
domain: psj-utility
group: performance
namespace: JPT
description: >
    Disable screen animation, screen update, and status bar updates to improve Jupiter's performance during batch
    operations.
version_introduced: '5.0.0'
syntax: 'JPT.BeginDatabaseTransaction("transactionName")'

callouts:
    - level: warn
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
    - $ref: psj-utility/JPT-EndDatabaseTransaction
```

### 3g. PSJ-GUI method

```yaml
# psj-gui/dlg-add_1delement_selector.yaml
psjapi: '1.0'
id: dlg-add_1delement_selector
title: dlg.add_1delement_selector()
domain: psj-gui
group: dlg-methods
namespace: dlg
description: >
    Add a 1D element selector to the dialog, enabling the user to select 1D elements and store the selection.
version_introduced: '5.0.0'
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

## 4. Delta versioning

Item files carry a `changes` block describing only what differs between versions. Items with no `changes` block are
identical across all versions since `version_introduced`. Most items in a backward-compatible SDK will have no `changes`
block at all.

### 4a. Removing params across a version

```yaml
# psj-command/Analysis-ADVC-Structure.yaml  (versioning excerpt)
psjapi: '1.0'
id: Analysis-ADVC-Structure
title: Analysis.ADVC.Structure()
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
      description: Job type. Structure=0.
      enum_values:
          - id: 0
            label: Structure

    - name: iHeatConvection
      type: Integer
      required: false
      default: '1'
      description: Heat convection mode.

    # … all other params …

returns:
    kind: typed
    type: Cursor
    description: The created ADVC analysis job.

changes:
    - version: '5.0.1'
      params:
          remove:
              - iEJobType
              - iHeatConvection
      notes: >
          iEJobType and iHeatConvection are no longer available in v5.0.1 or higher.
```

### 4b. Full delta operation vocabulary

```yaml
changes:
    - version: 'X.Y.Z'

      # Optional: top-level item fields that changed in this version.
      item:
          description: 'Revised item description.'
          ribbon: 'New > Ribbon > Path'
          deprecated: true # marks the whole item deprecated from this version

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

          # Remove params by name only.
          remove:
              - iRemovedParam

          # Patch specific fields on existing params.
          modify:
              - name: strName
                changes:
                    description: 'Revised description for X.Y.Z.'
                    default: '"NewDefault"'
                    required: true
                    enum_values:
                        add:
                            - id: 5
                              label: New option
                        remove:
                            - id: 2 # remove enum value by id
```

**Resolution rules:**

- The base `params` list represents the item as of `version_introduced`.
- `changes` entries are applied in version order up to the requested version.
- `remove` deletes a param from the resolved list. The definition stays in the file above `changes` so older-version
  renders still have it.
- `add` inserts at the named position; omit `after` to append.
- `modify` patches only the named fields; all other fields are unchanged.

---

## 5. Locale sidecar files

### 5a. What belongs in a sidecar

Sidecars contain **only natural-language fields**. Structural fields are never translated and never appear in sidecars.

| Field                                    | Localizable?      |
| ---------------------------------------- | ----------------- |
| `description` (item)                     | ✅                |
| `params[].description`                   | ✅                |
| `params[].display_name`                  | ✅                |
| `enum_values[].label`                    | ✅                |
| `enum_values[].description`              | ✅                |
| `returns.description`                    | ✅                |
| `returns.codes[].meaning`                | ✅                |
| `callouts[].text`                        | ✅                |
| `examples[].title`                       | ✅                |
| `id`, `title`, `syntax`, `code`          | ❌ — code symbols |
| `type`, `default`, `required`            | ❌ — structural   |
| `namespace`, `ribbon`, `domain`, `group` | ❌ — structural   |
| `version_introduced`, `macro_link`       | ❌ — structural   |

### 5b. Item locale sidecar

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Static.ja.yaml
psjapi: '1.0'
locale: ja
id: Analysis-ADVC-MakeProcess-Static

description: >
    ADVC構造スタティックプロセスを作成します。 このプロセスは1回または複数回作成できます。

# Only params that are NOT from a group are translated here.
# Group params are translated in _groups/advc-process-struct.ja.yaml
# and _groups/advc-process-base.ja.yaml.
params:
    # (In this case, all params come from advc-process-struct, so this section
    # is empty. It is shown here for illustration.)

returns:
    description: 作成または変更されたADVCスタティックプロセスのカーソル。
```

A more typical example — item with its own unique params:

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Dynamic.ja.yaml
psjapi: '1.0'
locale: ja
id: Analysis-ADVC-MakeProcess-Dynamic

description: >
    ADVC構造ダイナミックプロセスを作成します。

# bDynamic and advcDynamic are unique to this item (inserted via $group insert).
# They are translated here, not in any group sidecar.
params:
    bDynamic:
        description: ダイナミックパラメータ設定の有効/無効。
    advcDynamic:
        description: ダイナミックパラメータの設定。bDynamic=Trueの場合に有効。

returns:
    description: 作成または変更されたADVCダイナミックプロセスのカーソル。
```

### 5c. Macro locale sidecar — positional params keyed by position

```yaml
# macro/AdvcStaticProcess.ja.yaml
psjapi: '1.0'
locale: ja
id: AdvcStaticProcess

description: ADVCスタティックプロセスを作成します。

# Positional params are keyed by position number.
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
    65:
        description: 荷重のステータス。
    66:
        description: ロードケースのステータス。
    67:
        description: コンタクトのステータスとデータ。
    68:
        description: 出力パラメータ。
    69:
        description: 参照結果のタイプ。
        enum_values:
            0: 温度荷重
            1: 応力

returns:
    codes:
        '"1"': 関数を実行できます。
        '"0"': 関数を実行できません。

examples:
    - title: デフォルト設定でのプロセス作成
```

### 5d. Utility locale sidecar

```yaml
# psj-utility/JPT-BeginDatabaseTransaction.ja.yaml
psjapi: '1.0'
locale: ja
id: JPT-BeginDatabaseTransaction

description: >
    スクリーンアニメーション、画面更新、ステータスバーの更新を無効にして Jupiterのパフォーマンスを向上させます。

callouts:
    - level: warn
      text: >
          処理の終了時にJPT.EndDatabaseTransaction()を呼び出して Jupiterを通常の状態に戻す必要があります。

params:
    transactionName:
        description: Undo/Redoメニューに表示されるトランザクション名。

returns:
    description: ~ # void — no return description needed
```

---

## 6. Locale resolution algorithm

```
function get_text(item_id, field_path, locale):

  1. If locale == "en":
       return base_file[field_path]

  2. Load sidecar: <domain>/<item_id>.<locale>.yaml
     If sidecar[field_path] exists:
       return sidecar[field_path]

  3. If field_path is on a param that came from a $group reference:
       Load group sidecar: _groups/<group_id>.<locale>.yaml
       If group_sidecar[field_path] exists:
         return group_sidecar[field_path]
       If group has `extends`:
         recurse into parent group sidecar

  4. Fallback: return base_file[field_path]   # EN text, no error
```

Fallback is silent. Partial translations are valid and expected — an item where only some params are translated shows
the translated text for those params and English for the rest. No build failure, no missing-key warnings.

---

## 7. Renderer decisions driven by `domain`

All four domains share the same schema. The `domain` field tells the renderer which display choices to apply:

| Behaviour                           | `macro`           | `psj-command`   | `psj-utility` | `psj-gui`   |
| ----------------------------------- | ----------------- | --------------- | ------------- | ----------- |
| Show Position column in param table | ✅                | —               | —             | —           |
| Show namespace prefix in title      | —                 | ✅              | ✅            | ✅          |
| Show Ribbon path                    | —                 | ✅ if present   | —             | —           |
| Show macro linkage card             | ✅ `command_link` | ✅ `macro_link` | —             | —           |
| Syntax highlight style              | `psj-macro`       | Python          | Python        | Python      |
| Return renders as                   | Code table        | Type link       | "No output"   | "No output" |

---

## 8. Complete field reference

### Item file

```yaml
psjapi: "1.0"              # required
id: string                 # required; slug unique within domain
title: string              # required; verbatim call signature e.g. "Analysis.Nastran.LinearStatic()"
domain: macro              # required; macro | psj-command | psj-utility | psj-gui
                           # ↑ single field drives all renderer decisions
group: string?             # nav grouping label
namespace: string?         # dotted call prefix; omit for macros
ribbon: string?            # UI ribbon path; psj-command only
author: string?
author_url: string?
description: string        # required; localizable
version_introduced: string # required; e.g. "5.0.0"
macro_link: string?        # id of the macro this command wraps; psj-command only
command_link: string?      # id of the command that wraps this macro; macro only
syntax: string?            # verbatim signature; NOT localizable
callouts: [Callout]?       # warning/info boxes; text IS localizable
params: [Param | GroupRef] # ordered list; defines params as of version_introduced
returns: Returns            # required
examples: [Example]?       # always inline; never file links
see_also: [Ref]?
changes: [VersionDelta]?   # absent = item unchanged across all versions
```

### Param

```yaml
position: integer?      # 1-based; macro positional args only
name: string?           # source identifier; required for named params
display_name: string?   # clean UI label when name is cryptic; localizable
type: string            # String | Integer | Boolean | Double | Cursor | List | Vector |
                        # "$ref:data-type/<id>" | "List[$ref:data-type/<id>]"
required: boolean
default: string?        # exact default as string; null if undocumented
description: string     # localizable
enum_values: [EnumValue]?
deprecated: boolean?
deprecated_in: string?
removed_in: string?
inferred: boolean?      # true = added by converter, not stated in source
```

### GroupRef

```yaml
$group: string          # id of a _groups/<id>.yaml file
exclude: [string]?      # param names to drop from the group
insert_after: string?   # existing param name after which to splice `insert`
insert: [Param]?        # params spliced in at insert_after position
```

### Returns

```yaml
kind: typed | macro_code | void
type: string?           # present when kind=typed; "$ref:data-type/<id>" or primitive
description: string?    # localizable
codes: [Code]?          # present when kind=macro_code
```

### Code

```yaml
value: string # e.g. '"1"'; NOT localizable
meaning: string # localizable
```

### Callout

```yaml
level: warn | info | danger
text: string # localizable
```

### Example

```yaml
title: string? # localizable
language: psj | python
code: string # NOT localizable; always inline, never a file path
```

### VersionDelta

```yaml
version: string
notes: string?
item:
  description: string?
  ribbon: string?
  deprecated: boolean?
params:
  add: [Param]?         # each may carry `after: paramName`
  remove: [string]?     # param names only
  modify: [ParamPatch]?
```

### ParamPatch

```yaml
name: string
changes:
  description: string?
  default: string?
  required: boolean?
  deprecated: boolean?
  enum_values:
    add: [EnumValue]?
    remove: [integer | string]?   # enum value ids to remove
```

### EnumValue

```yaml
id: integer | string # NOT localizable
label: string # localizable
description: string? # localizable
```

### Ref

```yaml
$ref: string # "<domain>/<id>"
label: string?
inferred: boolean?
```

### ParamGroup file

```yaml
psjapi: '1.0'
kind: param_group
id: string
description: string? # localizable
extends: string? # id of parent group
params: [Param]
```

### Locale sidecar (item or group)

```yaml
psjapi: '1.0'
locale: string # e.g. "ja"
id: string # ties to base file

description: string?

callouts:
    - level: warn | info | danger # must match base file entry order
      text: string

params:
    # For named params (psj-command / psj-utility / psj-gui / group):
    <param_name>:
        display_name: string?
        description: string?
        enum_values:
            <id>: string # just the label; use id (integer or string) as key

    # For positional params (macro):
    <position_integer>:
        description: string?
        enum_values:
            <id>: string

returns:
    description: string?
    codes:
        <value>: string # meaning; use the value string as key e.g. '"1"': ...

examples:
    - title: string? # matches by index; omit entries where title is unchanged
```

---

## 9. Efficiency summary

### File count at scale

```
1000 items × 1 base file          = 1000 .yaml files
~30 param groups                   =   30 .yaml files
~30 group × 2 locales              =   60 .ja.yaml files  (groups)
~1000 items × 2 locales            = 2000 .ja.yaml files  (items)
─────────────────────────────────────────
Total                              = 3090 files
vs. naive 1000 items × 5 versions × 2 locales = 10,000 files

Delta blocks (most items unchanged) ≈ 50 changes blocks across 1000 items
```

### Param definition count — Nastran family example

```
Naive:   7 commands × 10 params = 70 param definitions
psjapi:  10 (in nastran-base.yaml) + 7 × 1 line ($group reference) = 17 total
Reduction: 76%

For nastran-base.ja.yaml:
  10 translated descriptions written once
  All 7 commands pick them up automatically
```
