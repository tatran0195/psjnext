---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Sine()"
description: "Define the force load on selected entity based on the distribution of the sine function"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Sine"
---

## Description

Define the force load on selected entity based on the distribution of the sine function.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Sine(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ForceSine1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFTotalForce`

- The total force.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAngleBase`

- The angle base.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngleRange`

- The angle range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnArrowDir`

- The en arrow direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDistributeInAxis`

- The distribute in axis.

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
BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
