---
title: "SNOnePush.DropTest.UpdateFloor()"
description: "Assemble cylinder layer"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SNOnePush > DropTest > UpdateFloor"
---

## Description

Assemble cylinder layer

## Syntax

```psj
SNOnePush.DropTest.UpdateFloor(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDir`

- The direction.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRopHeight`

- The drop height.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSolutionTime`

- The solution time.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iNumberOutput`

- The number output.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dContactFriction`

- The contact friction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRotAxis`

- The rotation axis.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRotAngle`

- The rotation angle.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRelevantElemRate`

- The relevant element rate.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dChangeMassRate`

- The change mass rate.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinTimeStep`

- The minimum time step.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strSolverFile`

- The solver file.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFloorSize`

- The floor size.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRename`

- The rename.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMat`

- The material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.DropTest.UpdateFloor(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```
