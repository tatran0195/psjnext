---
title: "BoundaryConditions.Pressure.Hydrostatic()"
description: "Create hydrostatic pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > Hydrostatic"
---

## Description

Create hydrostatic pressure.

## Syntax

```psj
BoundaryConditions.Pressure.Hydrostatic(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "PressureHydrostatic1".

<!-- @since:5.0.1 @optional -->
### dFHPressure

- Specify the h pressure.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dFDensity

- Specify the density.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iDensityUnit

- Specify the density unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFGravity

- Specify the gravity.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iGravityUnit

- Specify the gravity unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iGravityDir

- Specify the gravity direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFWaterSuface

- Specify the water suface.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iSufaceUnit

- Specify the suface unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDistributionMethod

- Specify the distribution method.
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
BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTargets=[], crEdit=None)
```
