---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic()"
description: "Create Force (Quadratic) y = a*x^2 + b"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Quadratic"
---

## Description

Create Force (Quadratic) y = a\*x^2 + b.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ForceQuadratic1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFTotalForce`

- The total force.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dB`

- The .

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
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTargets=[], crEdit=None)
```
