---
title: "BoundaryConditions.Force.FunctionLoadCylinder.Vector()"
description: "Define the force load on selected entity based on the distribution of the vector function"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Force > FunctionLoadCylinder > Vector"
---

## Description

Define the force load on selected entity based on the distribution of the vector function.

## Syntax

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Vector(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ForceVector1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFTotalForce`

- The total force.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dX`

- The x.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dY`

- The y.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnDirection`

- The en direction.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngleRange`

- The angle range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iArrowDir`

- The arrow direction.

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
BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT _DBL, dA=DFLT _DBL, dX=DFLT _DBL, dY=DFLT _DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
