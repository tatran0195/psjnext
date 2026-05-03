---
title: "EngReliability.SubModelBC()"
description: "create mapping forced displacement"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "EngReliability > SubModelBC"
---

## Description

Create mapping forced displacement

## Syntax

```psj
EngReliability.SubModelBC(strName, crlTargets, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `iPos` @type(Integer) @required

- The position.

### `iViewCp` @type(Integer) @required

- The view component.

### `iCp` @type(Integer) @required

- The component.

### `iSrcType` @type(Integer) @required

- The source type.

### `iMappedCpIndexArr0` @type(Integer) @required

- The mapped component index arr0.

### `dScaleR` @type(Double) @required

- The scale r.

### `vecOffset` @type(Vector) @required

- The offset.

### `vecRotate` @type(Vector) @required

- The rotate.

### `dScaleT` @type(Double) @required

- The scale t.

### `strPath` @type(String) @required

- The path.

### `crEdit` @type(Cursor) @required

- The edit.

### `iMappingMethod` @type(Integer) @required

- The mapping method.

### `iSubmodelBCMappingType` @type(Integer) @required

- The submodel c mapping type.

### `iMappingFromStepNo` @type(Integer) @required

- The mapping from step no.

### `bSetADVCFile` @type(Boolean) @required

- The set ADVC file.

### `strADVCResultFile` @type(String) @required

- The ADVC result file.

### `bSetDetATol` @type(Boolean) @required

- The set det a tolerance.

### `dDetATol` @type(Double) @required

- The det a tolerance.

### `bSetElementSet` @type(Boolean) @required

- The set element set.

### `strElementSet` @type(String) @required

- The element set.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
EngReliability.SubModelBC(strName, crlTargets, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
```
