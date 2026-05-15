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

<!-- @since:5.0.1 @required -->
### strName

- Specify the Transient step name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the step description of the Transient analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEnableAutomatic

- Specify the automatic increment method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMaxInc

- Specify the maximum number of increment.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dInitSize

- Specify the initial increment value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMinSize

- Specify the minimum increment value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMaxSize

- Specify the maximum increment value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMaxAllowTChange

- Specify the maximum allowable change.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iEndsteptBchecked

- Specify whether or not using End the step when the change is less than the_[dlEndsteptTlist](#dlendstepttlist)_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlEndsteptTlist

- Specify the end step value list.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMaxAllowEmissivityChange

- Specify the maximum allowable emissivity change per increment.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the solver.
  - 0: Direct
  - 1: Iterative
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatrixStorage

- Specify the matrix storage setting.
  - 0: Default
  - 1: Unsymmetric
  - 2: Symmetric
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSolutionTech

- Specify the solution technique.
  - 0: Full Newton
  - 1: Quasi-Newton
  - 2: Contact iterations
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAllowedIters

- Specify the number of iterations allowed before the kernel matrix is reformed.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustFactor

- Specify the adjustment factor for the number of solutions in each iteration.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iMaxContactIter

- Specify the maximum number of contact iterations.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableNlgeom

- Specify whether or not to consider geometric nonlinear (large deformation) analysis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTimePeriod

- Specify the analysis time.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iConvertDscntIter

- Specify the conversion of severe discontinuity iterations.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRamp

- Specify the number of linear change over step.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iExtrapolateMethod

- Specify the Extrapolate previous state at start of each increment.
- The default value is 0.

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

A _Cursor_ specifying the newly created or the modified Abaqus Transient step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.TransientStep(strName="Step1", iMaxInc=100, dInitSize=1.0,
  dMinSize=1e-05, dMaxSize=1.0, dMaxAllowEmissivityChange=0.1, iAllowedIters=8,
  dAdjustFactor=1.0, iMaxContactIter=30, dTimePeriod=1.0, iRamp=1, listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
