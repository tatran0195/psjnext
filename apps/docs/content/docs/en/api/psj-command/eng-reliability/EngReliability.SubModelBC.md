---
title: "EngReliability.SubModelBC()"
description: "create mapping forced displacement"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "EngReliability > SubModelBC"
---

## Description

Create mapping forced displacement

## Syntax

```psj
EngReliability.SubModelBC(strName, crlTargets, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @required -->
### `iPos`

- The position.

<!-- @since:5.0.1 @type:Integer @required -->
### `iViewCp`

- The view component.

<!-- @since:5.0.1 @type:Integer @required -->
### `iCp`

- The component.

<!-- @since:5.0.1 @type:Integer @required -->
### `iSrcType`

- The source type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iMappedCpIndexArr0`

- The mapped component index arr0.

<!-- @since:5.0.1 @type:Double @required -->
### `dScaleR`

- The scale r.

<!-- @since:5.0.1 @type:Vector @required -->
### `vecOffset`

- The offset.

<!-- @since:5.0.1 @type:Vector @required -->
### `vecRotate`

- The rotate.

<!-- @since:5.0.1 @type:Double @required -->
### `dScaleT`

- The scale t.

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @required -->
### `iMappingMethod`

- The mapping method.

<!-- @since:5.0.1 @type:Integer @required -->
### `iSubmodelBCMappingType`

- The submodel c mapping type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iMappingFromStepNo`

- The mapping from step no.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bSetADVCFile`

- The set ADVC file.

<!-- @since:5.0.1 @type:String @required -->
### `strADVCResultFile`

- The ADVC result file.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bSetDetATol`

- The set det a tolerance.

<!-- @since:5.0.1 @type:Double @required -->
### `dDetATol`

- The det a tolerance.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bSetElementSet`

- The set element set.

<!-- @since:5.0.1 @type:String @required -->
### `strElementSet`

- The element set.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
EngReliability.SubModelBC(strName, crlTargets, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```
