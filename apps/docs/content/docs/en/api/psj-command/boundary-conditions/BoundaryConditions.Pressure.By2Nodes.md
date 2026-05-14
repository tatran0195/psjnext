---
title: "BoundaryConditions.Pressure.By2Nodes()"
description: "Create load boundary condition of 2nodes pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > By2Nodes"
---

## Description

Create load boundary condition of 2nodes pressure.

## Syntax

```psj
BoundaryConditions.Pressure.By2Nodes(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"PressureLinear1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeA`

- The node a.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPressureA`

- The pressure a.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNodeAUnit`

- The node a unit.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeB`

- The node .

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPressureB`

- The pressure .

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNodeBUnit`

- The node unit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDirection`

- The direction.

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
BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTargets=[], crEdit=None)
```
