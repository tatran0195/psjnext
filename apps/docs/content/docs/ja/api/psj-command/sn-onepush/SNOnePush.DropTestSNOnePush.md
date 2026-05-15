---
title: "SNOnePush.DropTestSNOnePush()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SNOnePush > DropTestSNOnePush"
---

## Description

Unknown Description

## Syntax

```psj
SNOnePush.DropTestSNOnePush(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iDir

- Specify the direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRopHeight

- Specify the drop height.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dSolutionTime

- Specify the solution time.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iNumOutput

- Specify the number output.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### dContactFriction

- Specify the contact friction.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### iRotAxis

- Specify the rotation axis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRotAngle

- Specify the rotation angle.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dRelevantElemRate

- Specify the relevant element rate.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dChangeMassRate

- Specify the change mass rate.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMinTimeStep

- Specify the minimum time step.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### strSolverFile

- Specify the solver file.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### dFloorSize

- Specify the floor size.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bRename

- Specify the rename.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crMat

- Specify the material.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.DropTestSNOnePush(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```
