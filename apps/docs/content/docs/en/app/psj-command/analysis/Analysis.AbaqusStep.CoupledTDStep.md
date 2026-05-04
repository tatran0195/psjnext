---
title: 'Analysis.AbaqusStep.CoupledTDStep()'
description: 'Create Abaqus step for Coupled Temperature-Displacement analysis'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > AbaqusStep > CoupledTDStep'
---

## Description

Create Abaqus step for Coupled Temperature-Displacement analysis.

## Syntax

```psj
Analysis.AbaqusStep.CoupledTDStep(...)
```

## Inputs

### `strName` @type(String) @required

- The step name of Coupled Temperature-Displacement analysis.

### `strDesp` @type(String) @default("")

- The step description of Coupled Temperature-Displacement analysis.

### `iEnableAutomatic` @type(Integer) @default(0)

- The increment method.

### `iMaxInc` @type(Integer) @default(100)

- The maximum number of increments.

### `dInitSize` @type(Double) @default(1.0)

- The initial increment size.

### `dMinSize` @type(Double) @default(1.0e-5)

- The minimum increment size.

### `dMaxSize` @type(Double) @default(1.0)

- The maximum increment size.

### `abaqusPair1` @type(ABAQUS_PAIR) @default(ABAQUS_PAIR)

- The maximum value of the allowable temperature change.

### `abaqusPair2` @type(ABAQUS_PAIR) @default(ABAQUS_PAIR)

- The creep/swelling/viscoelastic strain error tolerance value.

### `iCSVIntegration` @type(Integer) @default(0)

- The creep/swelling/viscoelastic integration method.

### `iMethod` @type(Integer) @default(0)

- The equation solver method.

### `iMatrixStorage` @type(Integer) @default(0)

- The equation solver matrix storage setting.

### `iSolutionTech` @type(Integer) @default(0)

- The solution technique.

### `iAllowedIters` @type(Integer) @default(8)

- The number of iterations allowed before the kernel matrix is reformed.

### `dAdjustFactor` @type(Double) @default(1.0)

- The adjustment factor for the number of solutions in any iteration.

### `iMaxContactIter` @type(Integer) @default(30)

- The maximum number of contact iterations.

### `iType` @type(Integer) @default(0)

- The automatic static stabilization.

### `iEnableUseAdaptive` @type(Integer) @default(1)

- Whether or not use adaptive stabilization with max. Ratio of stabilization to strain energy.

### `dDampingFactor` @type(Double) @default(0.0002)

- The damping factor for automatic static stabilization.

### `dMaxRationofStrainEnergy` @type(Double) @default(0.05)

- The maximum ratio of stabilization to strain energy for automatic static stabilization.

### `iEnableNlgeom` @type(Integer) @default(0)

- Whether or not to consider geometric nonlinear (large deformation) analysis.

### `dTimePeriod` @type(Double) @default(1.0)

- The analysis time.

### `iTransient` @type(Integer) @default(1)

- The analysis response type.

### `iConvertDscntIter` @type(Integer) @default(0)

- The conversion of severe discontinuity iterations.

### `iRamp` @type(Integer) @default(1)

- The number of linear change over step.

### `iExtrapolateMethod` @type(Integer) @default(0)

- The Extrapolate previous state at start of each increment.

### `iEnableIncludeCSV` @type(Integer) @default(0)

- The inclusion of creep/swelling/viscoelatic behavior.

### `listAbaqusOutputRequest` @type(ABAQUS_OUTPUT_REQUEST) @default(ABAQUS_OUTPUT_REQUEST)

- List specifying the list of Abaqus output request.

### `crEdit` @type(Cursor) @default(None)

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

creating_status = Analysis.AbaqusStep.CoupledTDStep(strName="Step1",
                                                    strDesp="Test",
                                                    abaqusPair1=ABAQUS_PAIR(dlTList=[0.0]),
                                                    abaqusPair2=ABAQUS_PAIR(dlTList=[0.0]),
                                                    iMatrixStorage=1,
                                                    iType=2,
                                                    iEnableNlgeom=1,
                                                    iTransient=0,
                                                    listAbaqusOutputRequest=[])

JPT.Debugger(creating_status)
```
