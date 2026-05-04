---
title: 'Analysis.AbaqusStep.DynamicStep()'
description: 'Create Abaqus step for Dynamic analysis'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > AbaqusStep > DynamicStep'
---

## Description

Create Abaqus step for Dynamic analysis.

## Syntax

```psj
Analysis.AbaqusStep.DyanmicStep(...)
```

## Inputs

### `strName` @type(String) @required

- The Dynamic step name.

### `strDesp` @type(String) @default("")

- The Dynamic step description.

### `iAutomatic` @type(Integer) @default(0)

- The increment method.

### `iMaxInc` @type(Integer) @default(100)

- The maximum number of increments.

### `dInitSize` @type(Double) @default(1.0)

- The initial increment size.

### `dMinSize` @type(Double) @default(1.0e-5)

- The minimum increment size.

### `dMaxSize` @type(Double) @default(1.0)

- The maximum increment size.

### `iSuppressHalfResCal` @type(Integer) @default(0)

- Whether or not suppress the calculation of the half-increment residual tolerance.

### `dHalfStepResTol` @type(Double) @default(DFLT_DBL)

- The half-increment residual tolerance value.

### `iMethod` @type(Integer) @default(0)

- The equation solver method.

### `iMatrixStorage` @type(Integer) @default(0)

- The equation solver matrix storage setting.

### `iSolutionTech` @type(Integer) @default(0)

- The solution technique.

### `iAllowedIters` @type(Integer) @default(8)

- The number of iterations allowed before the kernel matrix is reformed.

### `dAdjustFactor` @type(Double) @default(1.0)

- The adjustment factor for the number of solutions in each iteration.

### `iMaxContactIter` @type(Integer) @default(30)

- The maximum number of contact iterations.

### `dDampingControl` @type(Double) @default(-0.05)

- The numerical damping control parameter.

### `iByPassCalInitAcceleration` @type(Integer) @default(1)

- Whether or not to bypass calculations of initial accelerations at beginning of step.

### `iNlGeom` @type(Integer) @default(0)

- Whether or not to consider geometric nonlinear (large deformation) analysis.

### `dTimePeriod` @type(Double) @default(1.0)

- The analysis time.

### `iIncldHeatEffect` @type(Integer) @default(1)

- Whether or not to consider adiabatic heating effects.

### `iConvertDscntIter` @type(Integer) @default(0)

- The conversion of severe discontinuity iterations.

### `iRamp` @type(Integer) @default(1)

- The number of linear change over step.

### `iExtrapolateMethod` @type(Integer) @default(0)

- The Extrapolate previous state at start of each increment.

### `iAcceptByMaxIters` @type(Integer) @default(0)

- Whether or not to accept the solution after reaching maximum number of iterations.

### `listAbaqusOutputRequest` @type(ABAQUS_OUTPUT_REQUEST) @default(ABAQUS_OUTPUT_REQUEST)

- List specifying the list of Abaqus output request.

### `crEdit` @type(Cursor) @default(None)

- An existing Abaqus step.
    - If this parameter is used, the specified step will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new step will be created.

## Return Code

A _Cursor_ specifying the created/modified Abaqus Dynamic step.

## Sample Code

```psj {31,32,33}
from os import environ
import re

Geometry.Part.Cube(iPartColor=5619133)
Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Properties.Material.Add("Concrete",
                        [Density([(DENSITY, 2.3e-09)]),
                        Elastic([(YOUNGS_MODULUS, 30000.0),
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=12275404,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

creating_status = Analysis.AbaqusStep.DynamicStep("Step1",
                                                  iAutomatic=1,
                                                  listOutput=[])

JPT.Debugger(creating_status)
```
