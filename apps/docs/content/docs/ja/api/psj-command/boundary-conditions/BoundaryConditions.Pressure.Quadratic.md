---
title: "BoundaryConditions.Pressure.Quadratic()"
description: "Create quadratic pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > Quadratic"
---

## Description

Create quadratic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Quadratic(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "PressureQuadratic1".

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dB

- Specify the .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crCoordinate

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dAngleRange

- Specify the angle range.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iPressureDirectionMode

- Specify the pressure direction mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlPressureDirection

- Specify the pressure direction.
- The default value is \[0.0,0.0,0.0].

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
BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTargets=[], crEdit=None)
```
