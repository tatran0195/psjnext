---
title: 'Analysis.Analysis.Abaqus()'
description: 'Unknown Description'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > Analysis > Abaqus'
macro_link: '[CreateAbaqusJob](../../macro/analysis/CreateAbaqusJob)'
---

## Description

Unknown Description

## Syntax

```psj
Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType,
    iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence,
    crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes,
    bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `bRBE2toMPC` @type(Boolean) @required

- The RBE2 to MPC.

### `bRenameProcess` @type(Boolean) @required

- The rename process.

### `iCodeType` @type(Integer) @required

- The code type.

### `iSurfDefType` @type(Integer) @required

- The surface definition type.

### `iUnit` @type(Integer) @required

- The unit.

### `iWriteType` @type(Integer) @required

- The write type.

### `strDescription` @type(String) @required

- The description.

### `crlStepSequence` @type(List\[Cursor]) @required

- The step sequence.

### `crEdit` @type(Cursor) @required

- The edit.

### `strlUserText` @type(List\[String]) @required

- The user text.

### `bExptNdEleGroups` @type(Boolean) @required

- The exeption nd element groups.

### `bDeleteFloatingNodes` @type(Boolean) @required

- The delete floating nodes.

### `bExptFaceElemGroups2Surface` @type(Boolean) @required

- The exeption face element groups2 surface.

### `bLoadCase` @type(Boolean) @required

- The load case.

### `bAutoAssignDummyProperty` @type(Boolean) @required

- The auto assign dummy property.

### `crDummyMat` @type(Cursor) @required

- The dummy material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```
