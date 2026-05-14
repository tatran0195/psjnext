---
title: "Analysis.Analysis.Abaqus()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Analysis > Abaqus"
macro _link: "[CreateAbaqusJob](../../macro/analysis/CreateAbaqusJob)"
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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bRBE2toMPC`

- The RBE2 to MPC.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bRenameProcess`

- The rename process.

<!-- @since:5.0.1 @type:Integer @required -->
### `iCodeType`

- The code type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iSurfDefType`

- The surface definition type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iUnit`

- The unit.

<!-- @since:5.0.1 @type:Integer @required -->
### `iWriteType`

- The write type.

<!-- @since:5.0.1 @type:String @required -->
### `strDescription`

- The description.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlStepSequence`

- The step sequence.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlUserText`

- The user text.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bExptNdEleGroups`

- The exeption nd element groups.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bDeleteFloatingNodes`

- The delete floating nodes.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bExptFaceElemGroups2Surface`

- The exeption face element groups2 surface.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bLoadCase`

- The load case.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bAutoAssignDummyProperty`

- The auto assign dummy property.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crDummyMat`

- The dummy material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```
