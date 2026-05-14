---
title: "BoundaryConditions.Submodel.SubmodelForcedFlux()"
description: "Create submodel forced flux"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Submodel > SubmodelForcedFlux"
---

## Description

Create submodel forced flux.

## Syntax

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolver`

- The solver.

<!-- @since:5.0.1 @type:String @optional @default:"/home/" -->
### `strFilePathName`

- The file path name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iProcessNo`

- The process no.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iReferType`

- The refer type.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExtensionRange`

- The extension range.

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

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxX`

- The number bucket maximum x.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxY`

- The number bucket maximum y.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNumBucketMaxZ`

- The number bucket maximum z.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iPrevBc`

- The prev bc.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Submodel.SubmodelForcedFlux(strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT _DBL, dExtensionTol=DFLT _DBL, dExtensionLimitTol=DFLT _DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT _INT, iNumBucketMaxY=DFLT _INT, iNumBucketMaxZ=DFLT _INT, iPrevBc=-1, crlTargets=[], crEdit=None)
```
