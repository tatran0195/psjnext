---
title: "Analysis.AbaqusStep.TransientStep()"
description: "Create Abaqus Step - Transient Type"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Abaqus"
---

## Description

Create Abaqus step for Transient analysis.

## Syntax

```psj
Analysis.AbaqusStep.TransientStep(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The Transient step name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The step description of the Transient analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableAutomatic`

- The automatic increment method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMaxInc`

- The maximum number of increment.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInitSize`

- The initial increment value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMinSize`

- The minimum increment value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxSize`

- The maximum increment value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxAllowTChange`

- The maximum allowable change.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEndsteptBchecked`

- Whether or not using End the step when the change is less than the_[dlEndsteptTlist](#dlendstepttlist)_.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlEndsteptTlist`

- The end step value list.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxAllowEmissivityChange`

- The maximum allowable emissivity change per increment.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The solver.
  - 0: Direct
  - 1: Iterative

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatrixStorage`

- The matrix storage setting.
  - 0: Default
  - 1: Unsymmetric
  - 2: Symmetric

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolutionTech`

- The solution technique.
  - 0: Full Newton
  - 1: Quasi-Newton
  - 2: Contact iterations

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAllowedIters`

- The number of iterations allowed before the kernel matrix is reformed.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _DBL -->
### `dAdjustFactor`

- The adjustment factor for the number of solutions in each iteration.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMaxContactIter`

- The maximum number of contact iterations.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableNlgeom`

- Whether or not to consider geometric nonlinear (large deformation) analysis.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTimePeriod`

- The analysis time.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConvertDscntIter`

- The conversion of severe discontinuity iterations.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRamp`

- The number of linear change over step.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iExtrapolateMethod`

- The Extrapolate previous state at start of each increment.

<!-- @since:5.0.1 @type:ABAQUS _OUTPUT _REQUEST @optional @default:ABAQUS _OUTPUT _REQUEST -->
### `listAbaqusOutputRequest`

- The list specifying the list of Abaqus output request.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Transient step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.TransientStep(strName="Step1", iMaxInc=100, dInitSize=1.0,
  dMinSize=1e-05, dMaxSize=1.0, dMaxAllowEmissivityChange=0.1, iAllowedIters=8,
  dAdjustFactor=1.0, iMaxContactIter=30, dTimePeriod=1.0, iRamp=1, listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
