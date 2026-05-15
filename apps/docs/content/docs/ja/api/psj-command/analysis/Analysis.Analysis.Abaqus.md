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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### bRBE2toMPC

- Specify the RBE2 to MPC.

<!-- @since:5.0.1 @required -->
### bRenameProcess

- Specify the rename process.

<!-- @since:5.0.1 @required -->
### iCodeType

- Specify the code type.

<!-- @since:5.0.1 @required -->
### iSurfDefType

- Specify the surface definition type.

<!-- @since:5.0.1 @required -->
### iUnit

- Specify the unit.

<!-- @since:5.0.1 @required -->
### iWriteType

- Specify the write type.

<!-- @since:5.0.1 @required -->
### strDescription

- Specify the description.

<!-- @since:5.0.1 @required -->
### crlStepSequence

- Specify the step sequence.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the edit.

<!-- @since:5.0.1 @required -->
### strlUserText

- Specify the user text.

<!-- @since:5.0.1 @required -->
### bExptNdEleGroups

- Specify the exeption nd element groups.

<!-- @since:5.0.1 @required -->
### bDeleteFloatingNodes

- Specify the delete floating nodes.

<!-- @since:5.0.1 @required -->
### bExptFaceElemGroups2Surface

- Specify the exeption face element groups2 surface.

<!-- @since:5.0.1 @required -->
### bLoadCase

- Specify the load case.

<!-- @since:5.0.1 @required -->
### bAutoAssignDummyProperty

- Specify the auto assign dummy property.

<!-- @since:5.0.1 @required -->
### crDummyMat

- Specify the dummy material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.Analysis.Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
```
