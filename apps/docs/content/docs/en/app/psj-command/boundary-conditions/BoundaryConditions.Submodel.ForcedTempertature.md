---
title: "BoundaryConditions.Submodel.ForcedTempertature()"
description: "Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Submodel > ForcedTempertature"
---

## Description

Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest.

## Syntax

```psj
BoundaryConditions.Submodel.ForcedTempertature(...)
```

## Inputs

### `strName` @type(String) @default("SubmodelForcedTemperature1")

- The submodel forced temperature name.

### `iSolver` @type(Integer) @default(0)

- The solver type. Currently, there is only ADVC solver is available.
  - 0: ADVC solver.

### `strFilePathName` @type(String) @default("/home/")

- The file path name.

### `iProcessNo` @type(Integer)

- The process number of ADVC solver. The value must be greater than 0.
- This is the required input.

### `iReferType` @type(Integer) @default(0)

- The refer type.
  - 0: Blank.
  - 1: Result.
  - 2: Restart.

### `dExtensionRange` @type(Double) @default(DFLT\_DBL)

- The extension range value.

### `dExtensionTol` @type(Double) @default(DFLT\_DBL)

- The extension tolerance.

### `dExtensionLimitTol` @type(Double) @default(DFLT\_DBL)

- The extension limit tolerance.

### `strGlobalElementSet` @type(String) @default("")

- The global element set.

### `iUseBucket` @type(Integer) @default(-1)

- The use bucket.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iNumBucketMaxX` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum X.

### `iNumBucketMaxY` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum Y.

### `iNumBucketMaxZ` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum Z.

### `iPrevBc` @type(Integer) @default(-1)

- The maintaining of the specified boundary conditions.
  - 0: Blank.
  - 1: Default hold.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target entities. The target entities could be Face or Nodes.

### `crEdit` @type(Cursor) @default(None)

- The cursor of boundary condition Forced Temperature need editing.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2-4}
Geometry.Part.Cube()
created_lbc = BoundaryConditions.Submodel.ForcedTempertature(strName="SubmodelForcedTemperature1",
                                                             iReferType=-1,
                                                             crlTargets=[Face(26)])
JPT.Debugger(created_lbc)
```
