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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The step name of Coupled Temperature-Displacement analysis.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDesp`

- The step description of Coupled Temperature-Displacement analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableAutomatic`

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

<!-- @since:5.0.1 @type:ABAQUS _PAIR @optional @default:ABAQUS _PAIR -->
### `abaqusPair1`

- The maximum value of the allowable temperature change.

<!-- @since:5.0.1 @type:ABAQUS _PAIR @optional @default:ABAQUS _PAIR -->
### `abaqusPair2`

- The creep/swelling/viscoelastic strain error tolerance value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCSVIntegration`

- The creep/swelling/viscoelastic integration method.

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

- The adjustment factor for the number of solutions in any iteration.

<!-- @since:5.0.1 @type:Integer @optional @default:30 -->
### `iMaxContactIter`

- The maximum number of contact iterations.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The automatic static stabilization.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableUseAdaptive`

- Whether or not use adaptive stabilization with max. Ratio of stabilization to strain energy.

<!-- @since:5.0.1 @type:Double @optional @default:0.0002 -->
### `dDampingFactor`

- The damping factor for automatic static stabilization.

<!-- @since:5.0.1 @type:Double @optional @default:0.05 -->
### `dMaxRationofStrainEnergy`

- The maximum ratio of stabilization to strain energy for automatic static stabilization.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableNlgeom`

- Whether or not to consider geometric nonlinear (large deformation) analysis.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTimePeriod`

- The analysis time.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iTransient`

- The analysis response type.

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
### `iEnableIncludeCSV`

- The inclusion of creep/swelling/viscoelatic behavior.

<!-- @since:5.0.1 @type:ABAQUS _OUTPUT _REQUEST @optional @default:ABAQUS _OUTPUT _REQUEST -->
### `listAbaqusOutputRequest`

- The list specifying the list of Abaqus output request.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The editing Abaqus Coupled Temperature-Displacement step.

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
