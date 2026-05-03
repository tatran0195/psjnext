---
title: "BoundaryConditions.Submodel.SubmodelForcedFlux()"
description: "Create submodel forced flux"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Submodel > SubmodelForcedFlux"
---

## Description

Create submodel forced flux.

## Syntax

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `iSolver` @type(Integer) @default(0)

- The solver.

### `strFilePathName` @type(String) @default("/home/")

- The file path name.

### `iProcessNo` @type(Integer) @default(0)

- The process no.

### `iReferType` @type(Integer) @default(-1)

- The refer type.

### `dExtensionRange` @type(Double) @default(DFLT\_DBL)

- The extension range.

### `dExtensionTol` @type(Double) @default(DFLT\_DBL)

- The extension tolerance.

### `dExtensionLimitTol` @type(Double) @default(DFLT\_DBL)

- The extension limit tolerance.

### `strGlobalElementSet` @type(String) @default("")

- The global element set.

### `iUseBucket` @type(Integer) @default(-1)

- The use bucket.

### `iNumBucketMaxX` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum x.

### `iNumBucketMaxY` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum y.

### `iNumBucketMaxZ` @type(Integer) @default(DFLT\_INT)

- The number bucket maximum z.

### `iPrevBc` @type(Integer) @default(-1)

- The prev bc.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTargets=[], crEdit=None)
```
