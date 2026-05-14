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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The Dynamic Explicit step name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The step description of Dynamic Explicit analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableAutomatic`

- The increment method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iIncrmtEstimator`

- The use of the stable increment estimator.
  - 0: Global
  - 1: Element by element

<!-- @since:5.0.1 @type:ABAQUS _PAIR @optional @default:ABAQUS _PAIR -->
### `abaqusPair1`

- The maximum time increment value.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTimeScalfactor`

- The time scaling factor.

<!-- @since:5.0.1 @type:ABAQUS _PAIR @optional @default:ABAQUS _PAIR -->
### `abaqusPair2`

- The user-defined time increment.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableNlgeom`

- Whether or not to consider geometric nonlinear (large deformation) analysis.
  - 0: Not consider
  - 1: Consider

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTimePeriod`

- The analysis time.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableIncludeHeatEffect`

- Whether or not include adiabatic heating effects.

<!-- @since:5.0.1 @type:Double @optional @default:0.06 -->
### `dLinearBlkVisco`

- The linear bulk viscosity parameter.

<!-- @since:5.0.1 @type:Double @optional @default:1.2 -->
### `dQuadrBlkVisco`

- The quadratic bulk viscosity parameter.

<!-- @since:5.0.1 @type:ABAQUS _OUTPUT _REQUEST @optional @default:ABAQUS _OUTPUT _REQUEST -->
### `listAbaqusOutputRequest`

- The list specifying the list of Abaqus output request.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Dynamic Explicit step.

## Sample Code

```psj {1-2}
process = Analysis.AbaqusStep.DynamicExplicitStep(strName="Step1",
  abaqusPair1=ABAQUS _PAIR(dlTList=[0.0]), listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
