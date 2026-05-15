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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ForceQuadratic1".

<!-- @since:5.0.1 @optional -->
### dFTotalForce

- Specify the total force.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dB

- Specify the .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iAngleBase

- Specify the angle base.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAngleRange

- Specify the angle range.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iEnArrowDir

- Specify the en arrow direction.
- The default value is 0.

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
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTargets=[], crEdit=None)
```
