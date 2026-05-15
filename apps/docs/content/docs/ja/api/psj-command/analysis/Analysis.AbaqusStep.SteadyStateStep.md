---
title: "Analysis.AbaqusStep.SteadyStateStep()"
description: "Create Abaqus step for Steady State analysis"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > AbaqusStep > SteadyStateStep"
---

## Description

Create Abaqus step for Steady State analysis.

## Syntax

```psj
Analysis.AbaqusStep.SteadyStateStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the Steady State step name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the Steady State step description.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iAutomatic

- Specify the increment method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMaxInc

- Specify the maximum number of increments.
- The default value is 100.

<!-- @since:5.0.1 @optional -->
### iInitSize

- Specify the initial increment size.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dMinSize

- Specify the minimum increment size.
- The default value is 1.0e-5.

<!-- @since:5.0.1 @optional -->
### dMaxSize

- Specify the maximum increment size.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMaxAllowTChange

- Specify the maximum value of the allowable temperature change.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### endStepTemp

- Specify the end step temperature information.
- The default value is _[ABAQUS\_PAIR](./../../data-type/psj-command/parameter-types/ABAQUS _PAIR)_.

<!-- @since:5.0.1 @optional -->
### dMaxAllowEmissivityChange

- Specify the maximum allowable emissivity change per increment.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the equation solver method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatrixStorage

- Specify the equation solver matrix storage setting.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSolutionTech

- Specify the solution technique.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAllowedIters

- Specify the number of iterations allowed before the kernel matrix is reformed.
- The default value is 8.

<!-- @since:5.0.1 @optional -->
### iAdjustFactor

- Specify the adjustment factor for the number of solutions in each iteration.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iMaxContactIter

- Specify the maximum number of contact iterations.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### iNlGeom

- Specify whether or not to consider geometric nonlinear (large deformation) analysis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTimePeriod

- Specify the analysis time.
- The default value is 1.0.

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

A _Cursor_ specifying the created/modified Abaqus Steady State step.

## Sample Code

```psj {31,32,33,34}
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
                        Elastic([(YOUNGS _MODULUS, 30000.0), 
                                 (POISSONS _RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)], 
                 strName="Solid Property 1", 
                 iPropertyColor=12275404, 
                 crMaterial=Material(1), 
                 iCordM=-2, 
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL, 
                 dDispHG=DFLT _DBL, 
                 iFLG=-1)

creating _status = Analysis.AbaqusStep.SteadyStateStep("Step1", 
                                                      iAutomatic=1, 
                                                      iRamp=1, 
                                                      listAbaqusOutputRequest=[])

JPT.Debugger(creating _status)
```
