# JCALL v2 — Unified Callable Format
# Efficient at scale: param inheritance + delta versioning + shared param groups

---

## The two efficiency problems, stated precisely

**Problem 1 — Sibling duplication.**
Seven Nastran commands (LinearStatic, NormalModes, Transient, …) have exactly the
same 10-parameter signature. Without inheritance, those 70 param definitions are
written 7 times. At 1000 commands this compounds fast.

**Problem 2 — Version explosion.**
A backward-compatible SDK means most items are unchanged across versions.
Storing a full copy per version produces N_items × N_versions files.
Only the *diff* between versions needs to be stored.

Both problems have the same solution: **express only what changes**.
A `param_group` captures a reusable set of param definitions.
A `changes` block inside each version captures only the delta from the prior version.

---

## Format overview

Three file kinds:

```
sdk.jcall.yaml          ← root manifest (one file)
_groups/<id>.yaml       ← reusable param groups (many files, shared library)
<domain>/<id>.yaml      ← callable items (one file per unique callable)
```

The item file is the unit of authorship. It references groups and carries only
its own unique params plus version deltas. The renderer assembles the full picture
at read time.

---
---

## 1. Root manifest  `sdk.jcall.yaml`

```yaml
jcall: "2.0"

sdk:
  name: "Jupiter CAE Desktop Platform SDK"
  vendor: "TechnoStar Co., Ltd."
  vendor_url: "https://www.e-technostar.com/"

versions:
  # Ordered oldest → newest. Each version is a baseline from which items inherit.
  - id: "5.0.0"
  - id: "5.0.1"
    notes: "Removed iEJobType and iHeatConvection from Analysis.ADVC.Structure"
  - id: "5.1.0"
    notes: "Current release"
  # Adding a new version here is all that's needed to unlock the delta system.

current_version: "5.1.0"

domains:
  - id: macro
    title: Macros
    param_style: positional     # ← controls renderer: show Position column
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

## 2. Param group file  `_groups/<id>.yaml`

A param group is a **named, ordered list of param definitions** that any
callable item can include by reference. It has no domain, no syntax, no return —
it is only a reusable block of params.

```yaml
# _groups/nastran-base.yaml
jcall: "2.0"
kind: param_group
id: nastran-base
description: >
  Common parameters shared by all Nastran analysis export commands.

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
    default: "[]"
    description: List of target parts.

  - name: nastranAnalysis
    type: "$ref:data-type/JPT_NASTRAN_ANALYSIS"
    required: false
    default: "JPT_NASTRAN_ANALYSIS()"
    description: Nastran analysis input parameters.

  - name: bDummyPropAutoAssign
    type: Boolean
    required: false
    default: "False"
    description: Auto-create dummy properties for unassigned parts.

  - name: iDummyPropMaterialID
    type: Integer
    required: false
    default: "0"
    description: Material ID used for dummy property assignment.

  - name: crEdit
    type: Cursor
    required: false
    default: "None"
    description: Existing Nastran job to modify. None creates a new job.

  - name: strPath
    type: String
    required: true
    default: ~
    description: Export path for the BDF file.

  - name: iModelCheckAnswer
    type: Integer
    required: false
    default: "0"
    description: Model checking for dummy properties (0=off, 1=on).

  - name: iDeleteSlaveNodesAnswer
    type: Integer
    required: false
    default: "0"
    description: Delete slave nodes checking (0=off, 1=on).
```

```yaml
# _groups/advc-process-base.yaml
jcall: "2.0"
kind: param_group
id: advc-process-base
description: >
  Core parameters shared by all ADVC process commands (Static, Dynamic,
  EigenValue, Transient, Creep, …).

params:
  - name: strName
    type: String
    required: true
    default: ~
    description: Process name.

  - name: crEdit
    type: Cursor
    required: false
    default: "None"
    description: Existing process to modify. None creates a new process.

  - name: listLoadNode
    type: "List[$ref:data-type/JPT_ADVC_LOAD_NODE]"
    required: false
    default: "[]"
    description: Nodes with assigned loads.

  - name: listLoadCaseNode
    type: "List[$ref:data-type/JPT_ADVC_LOAD_NODE]"
    required: false
    default: "[]"
    description: Nodes with assigned load cases.

  - name: listLoadNodeContact
    type: "List[$ref:data-type/JPT_ADVC_LOAD_NODE]"
    required: false
    default: "[]"
    description: Nodes with assigned contacts.

  - name: ilOutputParamList
    type: List[Integer]
    required: false
    default: "[]"
    description: Output request list (Displacement, Stress, Strain, …).

  - name: iRefType
    type: Integer
    required: false
    default: "0"
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
    type: "List[$ref:data-type/JPT_ADVC_REF_STRESS_RESULT]"
    required: false
    default: "[]"
    description: Reference result data list.
```

```yaml
# _groups/advc-process-struct.yaml
# Extends advc-process-base with structural-analysis-specific params
jcall: "2.0"
kind: param_group
id: advc-process-struct
extends: advc-process-base    # ← groups can extend other groups

params:
  - name: iGeomNonlinear
    type: Integer
    required: false
    default: "0"
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
    type: "$ref:data-type/JPT_ADVC_STRUCT_TIME_STEP"
    required: false
    default: "JPT_ADVC_STRUCT_TIME_STEP()"
    description: Time step and output timing settings.

  - name: bConvergence
    type: Boolean
    required: false
    default: "False"
    description: Enable convergence parameter settings.

  - name: advcConvergence
    type: "$ref:data-type/JPT_ADVC_CONVERGENCE"
    required: false
    default: "JPT_ADVC_CONVERGENCE()"
    description: Convergence parameters. Active when bConvergence=True.

  - name: bContact
    type: Boolean
    required: false
    default: "False"
    description: Enable contact iterator parameter settings.

  - name: advcContactIter
    type: "$ref:data-type/JPT_ADVC_CONTACT_ITER"
    required: false
    default: "JPT_ADVC_CONTACT_ITER()"
    description: Contact iterator parameters. Active when bContact=True.

  - name: bAutoIncrement
    type: Boolean
    required: false
    default: "False"
    description: Enable auto increment parameter settings.

  - name: advcAutoIncrement
    type: "$ref:data-type/JPT_ADVC_AUTO_INCREMENT"
    required: false
    default: "JPT_ADVC_AUTO_INCREMENT()"
    description: Auto increment parameters. Active when bAutoIncrement=True.

  - name: dStabilizationFactor
    type: Double
    required: false
    default: "0.0"
    description: Stabilization factor.

  - name: bCrackGrowth
    type: Boolean
    required: false
    default: "False"
    description: Enable crack growth parameter settings.

  - name: CrackGrowthParam
    type: "$ref:data-type/JPT_ADVC_CRACK_GROWTH"
    required: false
    default: "[]"
    description: Crack growth parameters. Active when bCrackGrowth=True.
```

---

## 3. Item file  `<domain>/<id>.yaml`

### 3a. Minimal item — no unique params, pure group reuse

Seven Nastran commands are fully described by their group. Their item file is tiny:

```yaml
# psj-command/Analysis-Nastran-LinearStatic.yaml
jcall: "2.0"
id: Analysis-Nastran-LinearStatic
title: Analysis.Nastran.LinearStatic()
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: Analysis > Nastran > LinearStatic
description: Export the Nastran BDF input file for Structure Linear Static analysis (SOL 101).
version_introduced: "5.0.0"
macro_link: NastranJob

params:
  - $group: nastran-base     # ← the entire 10-param block, by reference

returns:
  kind: typed
  type: Cursor
  description: The created Nastran job.
```

```yaml
# psj-command/Analysis-Nastran-NormalModes.yaml
jcall: "2.0"
id: Analysis-Nastran-NormalModes
title: Analysis.Nastran.NormalModes()
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: Analysis > Nastran > NormalModes
description: Export the Nastran BDF input file for Normal Modes analysis (SOL 103).
version_introduced: "5.0.0"
macro_link: NastranJob

params:
  - $group: nastran-base     # identical to LinearStatic — one line

returns:
  kind: typed
  type: Cursor
  description: The created Nastran job.
```

All 7 identical Nastran commands follow this pattern. The 10 param definitions
live in one place (`nastran-base.yaml`) and are referenced, never repeated.

### 3b. Item that extends a group with unique params

```yaml
# psj-command/Analysis-Nastran-DirectFrequencyResponse.yaml
jcall: "2.0"
id: Analysis-Nastran-DirectFrequencyResponse
title: Analysis.Nastran.DirectFrequencyResponse()
domain: psj-command
group: Nastran
namespace: Analysis.Nastran
ribbon: Analysis > Nastran > DirectFrequencyResponse
description: Export the Nastran BDF for Direct Frequency Response analysis (SOL 108).
version_introduced: "5.0.0"
macro_link: NastranJob

params:
  - $group: nastran-base        # shared 10 params (minus bDummyPropAutoAssign/iDummyPropMaterialID)
    exclude: [bDummyPropAutoAssign, iDummyPropMaterialID]   # ← those 2 are absent here

  # Unique params for this command only:
  - name: bOutputXYPlots
    type: Boolean
    required: false
    default: "False"
    description: Enable XY plot output.

  - name: iOutputValueSet
    type: Integer
    required: false
    default: "0"
    description: Output value set selector.

  - name: iOutputDOFType
    type: Integer
    required: false
    default: "0"
    description: Output degree-of-freedom type.

  - name: iXYPlotDisplacementType
    type: Integer
    required: false
    default: "0"
    description: XY plot displacement type.

  - name: iXYPlotVelocityType
    type: Integer
    required: false
    default: "0"
    description: XY plot velocity type.

  - name: iXYPlotAccelerationType
    type: Integer
    required: false
    default: "0"
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
    default: "False"
    description: Output geometry ID of dummy properties.

  - name: bDummyPropAutoAssign    # ← re-declared after the XY params (different position)
    type: Boolean
    required: false
    default: "False"
    description: Auto-create dummy properties.

  - name: iDummyPropMaterialID
    type: Integer
    required: false
    default: "0"
    description: Material ID for dummy property assignment.

  - name: crEdit
    type: Cursor
    required: false
    default: "None"
    description: Existing job to modify.

returns:
  kind: typed
  type: Cursor
  description: The created Nastran job.
```

### 3c. ADVC process — group composition with process-specific params

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Static.yaml
jcall: "2.0"
id: Analysis-ADVC-MakeProcess-Static
title: Analysis.ADVC.MakeProcess.Static()
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: Analysis > ADVC > Make Process > Static
description: >
  Create an ADVC Structure Static process. Can be created once or multiple times.
version_introduced: "5.0.0"
macro_link: AdvcStaticProcess

params:
  - $group: advc-process-struct   # inherits advc-process-base through it

returns:
  kind: typed
  type: Cursor
  description: The created or modified ADVC Static process.
```

```yaml
# psj-command/Analysis-ADVC-MakeProcess-Dynamic.yaml
jcall: "2.0"
id: Analysis-ADVC-MakeProcess-Dynamic
title: Analysis.ADVC.MakeProcess.Dynamic()
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: Analysis > ADVC > Make Process > Dynamic
description: >
  Create an ADVC Structure Dynamic process. Can be created once or multiple times.
version_introduced: "5.0.0"
macro_link: AdvcDynamicProcess

params:
  - $group: advc-process-struct
    # Dynamic inserts bDynamic/advcDynamic after advcAutoIncrement, before dStabilizationFactor
    insert_after: advcAutoIncrement
    insert:
      - name: bDynamic
        type: Boolean
        required: false
        default: "False"
        description: Enable dynamic parameter settings.
      - name: advcDynamic
        type: "$ref:data-type/JPT_ADVC_DYNAMIC"
        required: false
        default: "JPT_ADVC_DYNAMIC()"
        description: Dynamic parameters. Active when bDynamic=True.

returns:
  kind: typed
  type: Cursor
  description: The created or modified ADVC Dynamic process.
```

```yaml
# psj-command/Analysis-ADVC-MakeProcess-EigenValue.yaml
jcall: "2.0"
id: Analysis-ADVC-MakeProcess-EigenValue
title: Analysis.ADVC.MakeProcess.EigenValue()
domain: psj-command
group: ADVC
namespace: Analysis.ADVC.MakeProcess
ribbon: Analysis > ADVC > Make Process > Eigen Value
description: Create an ADVC EigenValue (Normal Modes) process.
version_introduced: "5.0.0"
macro_link: AdvcEigenProcess

# EigenValue has a completely different subset — it does NOT use the struct group.
# It uses the base group only and adds its own eigen-specific param.
params:
  - $group: advc-process-base

  - name: bEigenValue
    type: Boolean
    required: false
    default: "False"
    description: Enable eigen value parameter settings.

  - name: advcNormalModal
    type: "$ref:data-type/JPT_ADVC_NORMAL_MODAL"
    required: false
    default: "JPT_ADVC_NORMAL_MODAL()"
    description: Normal modal parameters. Active when bEigenValue=True.

returns:
  kind: typed
  type: Cursor
  description: The created or modified ADVC EigenValue process.
```

### 3d. Macro — positional params

```yaml
# macro/AdvcStaticProcess.yaml
jcall: "2.0"
id: AdvcStaticProcess
title: AdvcStaticProcess()
domain: macro
group: analysis
description: Create ADVC static process.
version_introduced: "5.0.0"
command_link: Analysis-ADVC-MakeProcess-Static

syntax: >
  AdvcStaticProcess(string m_strName, int m_iGeomNonlinear, int fixed_or_auto,
    int num_of_inc, double max_time, double max_dt, double min_dt, int load_type,
    ...)

# Macros use positional params — position is required, name is the C-style identifier
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
        label: "(blank)"
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

  # … positions 9–63 follow same pattern …

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
    description: Reference result type (0=Temperature Load, 1=Stress).

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
    code: >
      JPT.Exec('AdvcStaticProcess("ADVC_DEFAULT_PROCESS", 0, 0, 1, 1, 1, 1e-05,
        -1, -1, 2147483647, -1, 2147483647, 1.79769e+308, 1.79769e+308, ...)')
```

### 3e. Utility — no params except required ones

```yaml
# psj-utility/JPT-BeginDatabaseTransaction.yaml
jcall: "2.0"
id: JPT-BeginDatabaseTransaction
title: JPT.BeginDatabaseTransaction()
domain: psj-utility
group: performance
namespace: JPT
description: >
  Disable screen animation, screen update, and status bar updates to improve
  Jupiter's performance during batch operations.
version_introduced: "5.0.0"

syntax: 'JPT.BeginDatabaseTransaction("transactionName")'

callouts:
  - level: warn
    text: >
      JPT.EndDatabaseTransaction() must be called at the end of the process
      to return Jupiter to the normal state.

params:
  - name: transactionName
    type: String
    required: true
    description: >
      Transaction name displayed in the Undo/Redo menu.

returns:
  kind: void

see_also:
  - $ref: psj-utility/JPT-EndDatabaseTransaction
```

---

## 4. Delta versioning

Version changes are stored as a `changes` block in the item file — not as a
separate file and not as a full copy.

The `changes` block is a list of version entries. Each entry describes only what
is *different* from the previous version. The renderer reconstructs any version
by applying deltas forward from `version_introduced`.

```yaml
# psj-command/Analysis-ADVC-Structure.yaml  (excerpt showing delta versioning)
jcall: "2.0"
id: Analysis-ADVC-Structure
title: Analysis.ADVC.Structure()
domain: psj-command
version_introduced: "5.0.0"

params:
  - $group: advc-structure-base

  # Params present in 5.0.0 that were removed in 5.0.1:
  - name: iEJobType
    type: Integer
    required: false
    default: "0"
    description: Job type (0=Structure).
    enum_values:
      - id: 0
        label: Structure

  - name: iHeatConvection
    type: Integer
    required: false
    default: "1"
    description: Heat convection mode.

  # … remaining params …

returns:
  kind: typed
  type: Cursor
  description: The created ADVC analysis job.

# ── VERSION DELTAS ────────────────────────────────────────────────────────────
# Each entry describes what changed relative to the previous version.
# Items with no `changes` block are identical across all versions since introduced.

changes:
  - version: "5.0.1"
    params:
      remove:
        - iEJobType
        - iHeatConvection
    notes: "Removed iEJobType and iHeatConvection; both are no longer available."

  # If 5.1.0 added a new param:
  # - version: "5.1.0"
  #   params:
  #     add:
  #       - name: bNewFeature
  #         type: Boolean
  #         required: false
  #         default: "False"
  #         description: New feature added in 5.1.0.
  #         after: strPath   # ← insertion point
  #     modify:
  #       - name: strName
  #         changes:
  #           description: "Updated description for 5.1.0."
  #           default: '"Job_1"'   # ← default changed
```

### Delta operation vocabulary

```yaml
changes:
  - version: "X.Y.Z"
    item:
      # Top-level item fields that changed:
      description: "New description text."
      ribbon: "New > Ribbon > Path"
      deprecated: true                   # marks the whole item deprecated

    params:
      add:
        # Full param definitions inserted at a named position
        - name: bNewParam
          type: Boolean
          default: "False"
          description: "Added in X.Y.Z."
          after: existingParamName       # omit = append at end
          inferred: true                 # if the converter inferred this, not stated

      remove:
        # Just the names of params being removed
        - paramName

      modify:
        # Only the fields that changed on an existing param
        - name: existingParam
          changes:
            description: "Revised description."
            default: "new_default"
            enum_values:
              add:
                - id: 5
                  label: "New option"
              remove:
                - id: 2
```

Rules:
- A param with no entry in `changes` is identical to the prior version.
- `add` inserts a new param. `after` names the param it follows; omit to append.
- `remove` deletes a param. The removed definition is still present in the file
  (above the `changes` block) so older-version docs can still render it.
- `modify` patches specific fields of an existing param.
- The renderer reconstructs any version by walking `changes` entries up to the
  requested version.

---

## 5. How the renderer assembles a full item at version V

```
function resolve(item, version):

  1. Start with item.params as the "base" param list.
     (This is the definition as of version_introduced.)

  2. For each entry in item.changes where entry.version <= version:
       apply entry.params.remove  → delete params from list
       apply entry.params.add     → insert params at specified position
       apply entry.params.modify  → patch fields on existing params

  3. Expand each { $group: id } reference:
       a. Load the group file.
       b. If the group has `extends`, recursively expand it first.
       c. Apply any `exclude` or `insert_after` / `insert` overrides
          from the $group reference.
       d. Splice the resulting param list into the item's param list
          at the position of the $group entry.

  4. The result is the complete, ordered, version-specific param list.
```

---

## 6. File count comparison

### Without this format (one full file per item per version):

```
1000 items × 5 versions = 5000 files
~80 params avg × 5 versions = 400 param definitions per item
= 400,000 total param definitions stored
```

### With JCALL v2:

```
1000 item files  (params written once, in the base version)
~30 param group files  (shared definitions)
~50 delta blocks  (most items never change; only changed items have a changes block)
= ~1030 files total
= significantly fewer total param definitions
```

The Nastran example alone: 7 commands × 10 params = 70 definitions → 10 (in group) + 7 × 1 line ($group reference) = 17 total. **75% reduction on that family alone.**

---

## 7. Complete field reference

### Item file

```yaml
jcall: "2.0"                 # required, format version
id: string                   # required, slug unique within SDK
title: string                # required, display call signature
domain: macro | psj-command | psj-utility | psj-gui   # required
group: string?               # nav grouping
namespace: string?           # dotted call prefix (psj-command/utility/gui only)
ribbon: string?              # UI ribbon path (psj-command only)
author: string?
author_url: string?
description: string          # required
version_introduced: string   # required, e.g. "5.0.0"
macro_link: string?          # id of macro this wraps (psj-command only)
command_link: string?        # id of command that wraps this (macro only)
syntax: string?              # verbatim signature; auto-generated if absent
callouts: [Callout]?
params: [Param | GroupRef]   # ordered list; see schemas below
returns: Returns              # required
examples: [Example]?
see_also: [Ref]?
changes: [VersionDelta]?
```

### Param

```yaml
position: integer?    # 1-based; present for macro positional args, absent otherwise
name: string?         # source identifier; required for named params; optional for macro
display_name: string? # clean label for UI when name is cryptic; inferred: true if added by converter
type: string          # primitive or "$ref:data-type/<id>" or "List[$ref:...]"
required: boolean     # true = "This is a required input" in source
default: string?      # exact default value as string; null if undocumented
description: string
enum_values: [EnumValue]?
deprecated: boolean?
deprecated_in: string?
removed_in: string?
inferred: boolean?    # true if this field was inferred, not stated in source
```

### GroupRef

```yaml
$group: string        # id of a _groups/<id>.yaml file
exclude: [string]?    # param names to drop from the group
insert_after: string? # param name after which to insert the following params
insert: [Param]?      # params to insert at the insert_after position
```

### Returns

```yaml
kind: typed | macro_code | void
type: string?         # present when kind=typed
description: string?
codes: [Code]?        # present when kind=macro_code
```

### Code

```yaml
value: string         # e.g. '"1"'
meaning: string
```

### Callout

```yaml
level: warn | info | danger
text: string
```

### VersionDelta

```yaml
version: string
item:                 # top-level field changes
  description: string?
  ribbon: string?
  deprecated: boolean?
  notes: string?
params:
  add: [Param]?       # each may have `after: paramName`
  remove: [string]?   # param names
  modify: [ParamPatch]?
```

### ParamPatch

```yaml
name: string          # identifies the param to patch
changes:              # only the fields that changed
  description: string?
  default: string?
  required: boolean?
  enum_values:
    add: [EnumValue]?
    remove: [integer]?   # enum value ids to remove
```

### EnumValue

```yaml
id: integer | string
label: string
description: string?
```

### Ref

```yaml
$ref: string          # "<domain>/<id>"
label: string?
inferred: boolean?
```

### Example

```yaml
title: string?
language: psj | python
code: string
```

### ParamGroup file

```yaml
jcall: "2.0"
kind: param_group
id: string
description: string?
extends: string?      # id of another param group
params: [Param]
```
