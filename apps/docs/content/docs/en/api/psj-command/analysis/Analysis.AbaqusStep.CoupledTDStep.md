---
title: "Analysis.AbaqusStep.CoupledTDStep()"
description: "Create Abaqus step for Coupled Temperature-Displacement analysis"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > AbaqusStep > CoupledTDStep"
---

## Description

Create Abaqus step for Coupled Temperature-Displacement analysis.

## Syntax

```psj
Analysis.AbaqusStep.CoupledTDStep(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the step name of Coupled Temperature-Displacement analysis.

<!-- @since:5.0.1 @optional -->
### strDesp

- Specify the step description of Coupled Temperature-Displacement analysis.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEnableAutomatic

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
### abaqusPair1

- Specify the maximum value of the allowable temperature change.
- The default value is _[ABAQUS\_PAIR](./../../data-type/psj-command/parameter-types/ABAQUS _PAIR)_.

<!-- @since:5.0.1 @optional -->
### abaqusPair2

- Specify the creep/swelling/viscoelastic strain error tolerance value.
- The default value is _[ABAQUS\_PAIR](./../../data-type/psj-command/parameter-types/ABAQUS _PAIR)_.

<!-- @since:5.0.1 @optional -->
### iCSVIntegration

- Specify the creep/swelling/viscoelastic integration method.
- The default value is 0.

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

- Specify the adjustment factor for the number of solutions in any iteration.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iMaxContactIter

- Specify the maximum number of contact iterations.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the automatic static stabilization.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableUseAdaptive

- Specify whether or not use adaptive stabilization with max. Ratio of stabilization to strain energy.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dDampingFactor

- Specify the damping factor for automatic static stabilization.
- The default value is 0.0002.

<!-- @since:5.0.1 @optional -->
### dMaxRationofStrainEnergy

- Specify the maximum ratio of stabilization to strain energy for automatic static stabilization.
- The default value is 0.05.

<!-- @since:5.0.1 @optional -->
### iEnableNlgeom

- Specify whether or not to consider geometric nonlinear (large deformation) analysis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTimePeriod

- Specify the analysis time.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iTransient

- Specify the analysis response type.
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
### iEnableIncludeCSV

- Specify the inclusion of creep/swelling/viscoelatic behavior.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### listAbaqusOutputRequest

- Specify the list of Abaqus output request.
- The default value is _[ABAQUS\_OUTPUT\_REQUEST](./../../data-type/psj-command/parameter-types/ABAQUS _OUTPUT _REQUEST)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the editing Abaqus Coupled Temperature-Displacement step.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created/modified Abaqus Coupled Temperature-Displacement step.

## Sample Code

```psj {31,32,33,34,35,36,37,38,39}
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

creating _status = Analysis.AbaqusStep.CoupledTDStep(strName="Step1", 
                                                    strDesp="Test", 
                                                    abaqusPair1=ABAQUS _PAIR(dlTList=[0.0]), 
                                                    abaqusPair2=ABAQUS _PAIR(dlTList=[0.0]), 
                                                    iMatrixStorage=1, 
                                                    iType=2, 
                                                    iEnableNlgeom=1, 
                                                    iTransient=0, 
                                                    listAbaqusOutputRequest=[])

JPT.Debugger(creating _status)
```
