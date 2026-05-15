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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @required -->
### iPos

- Specify the position.

<!-- @since:5.0.1 @required -->
### iViewCp

- Specify the view component.

<!-- @since:5.0.1 @required -->
### iCp

- Specify the component.

<!-- @since:5.0.1 @required -->
### iSrcType

- Specify the source type.

<!-- @since:5.0.1 @required -->
### iMappedCpIndexArr0

- Specify the mapped component index arr0.

<!-- @since:5.0.1 @required -->
### dScaleR

- Specify the scale r.

<!-- @since:5.0.1 @required -->
### vecOffset

- Specify the offset.

<!-- @since:5.0.1 @required -->
### vecRotate

- Specify the rotate.

<!-- @since:5.0.1 @required -->
### dScaleT

- Specify the scale t.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the path.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the edit.

<!-- @since:5.0.1 @required -->
### iMappingMethod

- Specify the mapping method.

<!-- @since:5.0.1 @required -->
### iSubmodelBCMappingType

- Specify the submodel c mapping type.

<!-- @since:5.0.1 @required -->
### iMappingFromStepNo

- Specify the mapping from step no.

<!-- @since:5.0.1 @required -->
### bSetADVCFile

- Specify the set ADVC file.

<!-- @since:5.0.1 @required -->
### strADVCResultFile

- Specify the ADVC result file.

<!-- @since:5.0.1 @required -->
### bSetDetATol

- Specify the set det a tolerance.

<!-- @since:5.0.1 @required -->
### dDetATol

- Specify the det a tolerance.

<!-- @since:5.0.1 @required -->
### bSetElementSet

- Specify the set element set.

<!-- @since:5.0.1 @required -->
### strElementSet

- Specify the element set.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
EngReliability.SubModelBC(strName, crlTargets, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```
