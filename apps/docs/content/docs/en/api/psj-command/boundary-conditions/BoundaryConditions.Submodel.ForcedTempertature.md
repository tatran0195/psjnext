---
title: "BoundaryConditions.Submodel.ForcedTempertature()"
description: "Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Submodel > ForcedTempertature"
---

## Description

Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest.

## Syntax

```psj
BoundaryConditions.Submodel.ForcedTempertature(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"SubmodelForcedTemperature1" -->
### `strName`

- The submodel forced temperature name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolver`

- The solver type. Currently, there is only ADVC solver is available.
  - 0: ADVC solver.

<!-- @since:5.0.1 @type:String @optional @default:"/home/" -->
### `strFilePathName`

- The file path name.

<!-- @since:5.0.1 @type:Integer @optional -->
### `iProcessNo`

- The process number of ADVC solver. The value must be greater than 0.
- This is the required input.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iReferType`

- The refer type.
  - 0: Blank.
  - 1: Result.
  - 2: Restart.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionRange`

- The extension range value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionTol`

- The extension tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionLimitTol`

- The extension limit tolerance.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strGlobalElementSet`

- The global element set.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iUseBucket`

- The use bucket.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxX`

- The number bucket maximum X.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxY`

- The number bucket maximum Y.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxZ`

- The number bucket maximum Z.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iPrevBc`

- The maintaining of the specified boundary conditions.
  - 0: Blank.
  - 1: Default hold.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target entities. The target entities could be Face or Nodes.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The cursor of boundary condition Forced Temperature need editing.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {2-4}
Geometry.Part.Cube()
created _lbc = BoundaryConditions.Submodel.ForcedTempertature(strName="SubmodelForcedTemperature1",
                                                             iReferType=-1,
                                                             crlTargets=[Face(26)])
JPT.Debugger(created _lbc)
```
