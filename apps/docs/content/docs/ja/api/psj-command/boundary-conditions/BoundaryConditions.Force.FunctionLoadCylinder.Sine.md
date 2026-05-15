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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ForceSine1".

<!-- @since:5.0.1 @optional -->
### dFTotalForce

- Specify the total force.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
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
BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTargets=[], crEdit=None)
```
