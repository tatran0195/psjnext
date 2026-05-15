---
title: "BoundaryConditions.Pressure.FunctionLoadToCylinderSine()"
description: "Define a pressure load on the selected face or element surface based on a sine function distribution."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > FunctionLoadToCylinderSine"
---

## Description

Define a pressure load on the selected face or element surface based on a sine function distribution.

## Syntax

```psj
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "PressureSine1".

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
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
### bDistributionAxis

- Specify the distribution axis.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iPressureDirectionMode

- Specify the pressure direction mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bIsTotalForceAdjustment

- Specify the is total force adjustment.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dTotalForce

- Specify the total force.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### vecPressureDirection

- Specify the pressure direction.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### crCoordinateSystemForDirection

- Specify the coordinate system for direction.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bIsCornerNodesDistribution

- Specify the is corner nodes distribution.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### strFormulaForA

- Specify the formula for a.
- The default value is "".

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
BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTargets=[], crEdit=None)
```
