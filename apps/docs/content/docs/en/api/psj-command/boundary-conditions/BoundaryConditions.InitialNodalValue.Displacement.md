---
title: "BoundaryConditions.InitialNodalValue.Displacement()"
description: "Create Initial Dynamic"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Displacement"
---

## Description

Create Initial Dynamic.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Displacement(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InitialDisplacement1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Vector @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `vecInit`

- The initial.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSelNode`

- The selection node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeSet`

- The node set.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

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
BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT _DBL,DFLT _DBL,DFLT _DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTargets=[], crEdit=None)
```
