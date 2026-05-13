---
title: 'Analysis.AbaqusStep.DynamicExplicitStep()'
description: 'Create Abaqus Step - Dynamic Explicit Type'
since: '5.0.1'
ribbon: 'Analysis > Abaqus'
---

<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create Abaqus Step - Dynamic Explicit Type.

## Syntax

```psj
Analysis.AbaqusStep.DynamicExplicitStep(...)
```

## Inputs

### `strName` @type(String) @required

- The Dynamic Explicit step name.

### `strDesp` @type(String) @default("")

- The step description of Dynamic Explicit analysis.

### `iEnableAutomatic` @type(Integer) @default(1)

- The increment method.

### `iIncrmtEstimator` @type(Integer) @default(0)

- The use of the stable increment estimator.
    - 0: Global
    - 1: Element by element

### `abaqusPair1` @type(ABAQUS_PAIR) @default(ABAQUS_PAIR)

- The maximum time increment value.

### `dTimeScalfactor` @type(Double) @default(1.0)

- The time scaling factor.

### `abaqusPair2` @type(ABAQUS_PAIR) @default(ABAQUS_PAIR)

- The user-defined time increment.

### `iEnableNlgeom` @type(Integer) @default(1)

- Whether or not to consider geometric nonlinear (large deformation) analysis.
    - 0: Not consider
    - 1: Consider

### `dTimePeriod` @type(Double) @default(1.0)

- The analysis time.

### `iEnableIncludeHeatEffect` @type(Integer) @default(0)

- Whether or not include adiabatic heating effects.

### `dLinearBlkVisco` @type(Double) @default(0.06)

- The linear bulk viscosity parameter.

### `dQuadrBlkVisco` @type(Double) @default(1.2)

- The quadratic bulk viscosity parameter.

### `listAbaqusOutputRequest` @type(ABAQUS_OUTPUT_REQUEST) @default(ABAQUS_OUTPUT_REQUEST)

- List specifying the list of Abaqus output request.

### `crEdit` @type(Cursor) @default(None)

- An existing Abaqus step.
    - If this parameter is used, the specified step will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Dynamic Explicit step.

## Sample Code

```psj {1-2}
process = Analysis.AbaqusStep.DynamicExplicitStep(strName="Step1",
  abaqusPair1=ABAQUS_PAIR(dlTList=[0.0]), listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
