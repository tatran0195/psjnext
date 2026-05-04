---
title: 'Analysis.AbaqusStep.TransientStep()'
description: 'Create Abaqus Step - Transient Type'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > Abaqus'
---

<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create Abaqus step for Transient analysis.

## Syntax

```psj
Analysis.AbaqusStep.TransientStep(...)
```

## Inputs

### `strName` @type(String) @required

- The Transient step name.

### `strDesp` @type(String) @default("")

- The step description of the Transient analysis.

### `iEnableAutomatic` @type(Integer) @default(0)

- The automatic increment method.

### `iMaxInc` @type(Integer) @default(0)

- The maximum number of increment.

### `dInitSize` @type(Double) @default(DFLT_DBL)

- The initial increment value.

### `dMinSize` @type(Double) @default(DFLT_DBL)

- The minimum increment value.

### `dMaxSize` @type(Double) @default(DFLT_DBL)

- The maximum increment value.

### `dMaxAllowTChange` @type(Double) @default(DFLT_DBL)

- The maximum allowable change.

### `iEndsteptBchecked` @type(Integer) @default(0)

- Whether or not using End the step when the change is less than th&#x65;_[dlEndsteptTlist](#dlendstepttlist)_.

### `dlEndsteptTlist` @type(Double List) @default(\[])

- The end step value list.

### `dMaxAllowEmissivityChange` @type(Double) @default(DFLT_DBL)

- The maximum allowable emissivity change per increment.

### `iMethod` @type(Integer) @default(0)

- The solver.
    - 0: Direct
    - 1: Iterative

### `iMatrixStorage` @type(Integer) @default(0)

- The matrix storage setting.
    - 0: Default
    - 1: Unsymmetric
    - 2: Symmetric

### `iSolutionTech` @type(Integer) @default(0)

- The solution technique.
    - 0: Full Newton
    - 1: Quasi-Newton
    - 2: Contact iterations

### `iAllowedIters` @type(Integer) @default(0)

- The number of iterations allowed before the kernel matrix is reformed.

### `dAdjustFactor` @type(Integer) @default(DFLT_DBL)

- The adjustment factor for the number of solutions in each iteration.

### `iMaxContactIter` @type(Integer) @default(0)

- The maximum number of contact iterations.

### `iEnableNlgeom` @type(Integer) @default(0)

- Whether or not to consider geometric nonlinear (large deformation) analysis.

### `dTimePeriod` @type(Double) @default(DFLT_DBL)

- The analysis time.

### `iConvertDscntIter` @type(Integer) @default(0)

- The conversion of severe discontinuity iterations.

### `iRamp` @type(Integer) @default(0)

- The number of linear change over step.

### `iExtrapolateMethod` @type(Integer) @default(0)

- The Extrapolate previous state at start of each increment.

### `listAbaqusOutputRequest` @type(ABAQUS_OUTPUT_REQUEST) @default(ABAQUS_OUTPUT_REQUEST)

- List specifying the list of Abaqus output request.

### `crEdit` @type(Cursor) @default(None)

- An existing Abaqus step.
    - If this parameter is used, the specified step will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new step will be created.

## Return Code

A _Cursor_ specifying the newly created or the modified Abaqus Transient step.

## Sample Code

```psj {1-3}
process = Analysis.AbaqusStep.TransientStep(strName="Step1", iMaxInc=100, dInitSize=1.0,
  dMinSize=1e-05, dMaxSize=1.0, dMaxAllowEmissivityChange=0.1, iAllowedIters=8,
  dAdjustFactor=1.0, iMaxContactIter=30, dTimePeriod=1.0, iRamp=1, listAbaqusOutputRequest=[])

print("Result Dynamic Process has ID: " + str(process)) #for checking return value
```
