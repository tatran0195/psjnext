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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ForceVector1".

<!-- @since:5.0.1 @optional -->
### dFTotalForce

- Specify the total force.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dX

- Specify the x.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dY

- Specify the y.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iEnDirection

- Specify the en direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAngleRange

- Specify the angle range.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify the arrow direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bDistributeInAxis

- Specify the distribute in axis.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT _DBL, dA=DFLT _DBL, dX=DFLT _DBL, dY=DFLT _DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
