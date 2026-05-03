---
title: "SNOnePush.DropTest.UpdateFloor()"
description: "Assemble cylinder layer"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SNOnePush > DropTest > UpdateFloor"
---

## Description

Assemble cylinder layer

## Syntax

```psj
SNOnePush.DropTest.UpdateFloor(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iDir` @type(Integer) @default(0)

- The direction.

### `dRopHeight` @type(Double) @default(0.0)

- The drop height.

### `dSolutionTime` @type(Double) @default(0.0)

- The solution time.

### `iNumberOutput` @type(Integer) @default(20)

- The number output.

### `dContactFriction` @type(Double) @default(0.1)

- The contact friction.

### `iRotAxis` @type(Integer) @default(0)

- The rotation axis.

### `dRotAngle` @type(Double) @default(0.0)

- The rotation angle.

### `dRelevantElemRate` @type(Double) @default(0.0)

- The relevant element rate.

### `dChangeMassRate` @type(Double) @default(0.0)

- The change mass rate.

### `dMinTimeStep` @type(Double) @default(0.0)

- The minimum time step.

### `strSolverFile` @type(String) @default("")

- The solver file.

### `dFloorSize` @type(Double) @default(0.0)

- The floor size.

### `bRename` @type(Boolean) @default(True)

- The rename.

### `crMat` @type(Cursor) @default(None)

- The material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.DropTest.UpdateFloor(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```
