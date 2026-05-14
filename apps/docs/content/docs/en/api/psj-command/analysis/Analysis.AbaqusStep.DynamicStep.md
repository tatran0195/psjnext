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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The Dynamic step name.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The Dynamic step description.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAutomatic`

- The increment method.

<!-- @since:5.0.1 @type:Integer @optional @default:100 -->
### `iMaxInc`

- The maximum number of increments.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dInitSize`

- The initial increment size.

<!-- @since:5.0.1 @type:Double @optional @default:1.0e-5 -->
### `dMinSize`

- The minimum increment size.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMaxSize`

- The maximum increment size.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSuppressHalfResCal`

- Whether or not suppress the calculation of the half-increment residual tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dHalfStepResTol`

- The half-increment residual tolerance value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The equation solver method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatrixStorage`

- The equation solver matrix storage setting.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolutionTech`

- The solution technique.

<!-- @since:5.0.1 @type:Integer @optional @default:8 -->
### `iAllowedIters`

- The number of iterations allowed before the kernel matrix is reformed.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dAdjustFactor`

- The adjustment factor for the number of solutions in each iteration.

<!-- @since:5.0.1 @type:Integer @optional @default:30 -->
### `iMaxContactIter`

- The maximum number of contact iterations.

<!-- @since:5.0.1 @type:Double @optional @default:-0.05 -->
### `dDampingControl`

- The numerical damping control parameter.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iByPassCalInitAcceleration`

- Whether or not to bypass calculations of initial accelerations at beginning of step.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNlGeom`

- Whether or not to consider geometric nonlinear (large deformation) analysis.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTimePeriod`

- The analysis time.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iIncldHeatEffect`

- Whether or not to consider adiabatic heating effects.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConvertDscntIter`

- The conversion of severe discontinuity iterations.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iRamp`

- The number of linear change over step.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iExtrapolateMethod`

- The Extrapolate previous state at start of each increment.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAcceptByMaxIters`

- Whether or not to accept the solution after reaching maximum number of iterations.

<!-- @since:5.0.1 @type:ABAQUS _OUTPUT _REQUEST @optional @default:ABAQUS _OUTPUT _REQUEST -->
### `listAbaqusOutputRequest`

- The list specifying the list of Abaqus output request.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Abaqus step.
  - If this parameter is used, the specified step will be modified.
  - If it is left _None_, a new step will be created.

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
