---
title: "Analysis.AbaqusStep.DynamicExplicitStep()"
description: "Create Abaqus Step - Dynamic Explicit Type"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Abaqus"
---

## Description

Create Abaqus Step - Dynamic Explicit Type.

## Syntax

```psj
Analysis.AbaqusStep.DynamicExplicitStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the Dynamic Explicit step name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the step description of Dynamic Explicit analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEnableAutomatic

- Specify the increment method.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iIncrmtEstimator

- Specify the use of the stable increment estimator.
  - 0: Global
  - 1: Element by element
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### abaqusPair1

- Specify the maximum time increment value.
- The default value is _[ABAQUS\_PAIR](./../../data-type/psj-command/parameter-types/ABAQUS _PAIR)_.

<!-- @since:5.0.1 @optional -->
### dTimeScalfactor

- Specify the time scaling factor.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### abaqusPair2

- Specify the user-defined time increment.
- The default value is _[ABAQUS\_PAIR](./../../data-type/psj-command/parameter-types/ABAQUS _PAIR)_.

<!-- @since:5.0.1 @optional -->
### iEnableNlgeom

- Specify whether or not to consider geometric nonlinear (large deformation) analysis.
  - 0: Not consider
  - 1: Consider
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dTimePeriod

- Specify the analysis time.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iEnableIncludeHeatEffect

- Specify whether or not include adiabatic heating effects.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dLinearBlkVisco

- Specify the linear bulk viscosity parameter.
- The default value is 0.06.

<!-- @since:5.0.1 @optional -->
### dQuadrBlkVisco

- Specify the quadratic bulk viscosity parameter.
- The default value is 1.2.

<!-- @since:5.0.1 @optional -->
### listAbaqusOutputRequest

- Specify the list of Abaqus output request.
- The default value is _[ABAQUS\_OUTPUT\_REQUEST](./../../data-type/psj-command/parameter-types/ABAQUS _OUTPUT _REQUEST)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Dynamic Explicit step.

## Sample Code

```psj {1-2}
process = Analysis.AbaqusStep.DynamicExplicitStep(strName="Step1",
  abaqusPair1=ABAQUS _PAIR(dlTList=[0.0]), listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
