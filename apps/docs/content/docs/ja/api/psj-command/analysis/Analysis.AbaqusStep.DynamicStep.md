---
title: "Analysis.AbaqusStep.DynamicStep()"
description: "Create Abaqus step for Dynamic analysis"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > AbaqusStep > DynamicStep"
---

## Description

Create Abaqus step for Dynamic analysis.

## Syntax

```psj
Analysis.AbaqusStep.DyanmicStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the Dynamic step name.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the Dynamic step description.
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
### dInitSize

- Specify the initial increment size.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMinSize

- Specify the minimum increment size.
- The default value is 1.0e-5.

<!-- @since:5.0.1 @optional -->
### dMaxSize

- Specify the maximum increment size.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iSuppressHalfResCal

- Specify whether or not suppress the calculation of the half-increment residual tolerance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dHalfStepResTol

- Specify the half-increment residual tolerance value.
- The default value is _DFLT\_DBL_.

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
### dAdjustFactor

- Specify the adjustment factor for the number of solutions in each iteration.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iMaxContactIter

- Specify the maximum number of contact iterations.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### dDampingControl

- Specify the numerical damping control parameter.
- The default value is -0.05.

<!-- @since:5.0.1 @optional -->
### iByPassCalInitAcceleration

- Specify whether or not to bypass calculations of initial accelerations at beginning of step.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iNlGeom

- Specify whether or not to consider geometric nonlinear (large deformation) analysis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTimePeriod

- Specify the analysis time.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iIncldHeatEffect

- Specify whether or not to consider adiabatic heating effects.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iConvertDscntIter

- Specify the conversion of severe discontinuity iterations.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRamp

- Specify the number of linear change over step.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iExtrapolateMethod

- Specify the Extrapolate previous state at start of each increment.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAcceptByMaxIters

- Specify whether or not to accept the solution after reaching maximum number of iterations.
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

creating _status = Analysis.AbaqusStep.DynamicStep("Step1", 
                                                  iAutomatic=1, 
                                                  listOutput=[])

JPT.Debugger(creating _status)
```
