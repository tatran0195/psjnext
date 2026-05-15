---
title: "Analysis.ADVC.MakeProcess.Static()"
description: "Create ADVC Structure Static process for analysis work. This process could be created in one time or multiple times"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Make Process > Static"
macro _link: "[AdvcStaticProcess](../../macro/analysis/AdvcStaticProcess)"
---

## Description

Create ADVC Structure Static process for analysis work. This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Static(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the process name of ADVC - Static process.

<!-- @since:5.0.1 @optional -->
### iGeomNonlinear

- Specify the Geometry nonlinear option:
  - If _iGeomNonlinear=0_: None
  - If _iGeomNonlinear=1_: Total Lagrange - Consider the geometric nonlinearity due to total Lagrange method
  - If _iGeomNonlinear=2_: Updated Lagrange - Consider the geometric nonlinearity due to updated Lagrange method
  - If _iGeomNonlinear=3_: Linear
  - If _iGeomNonlinear=4_: NonLinear
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### advcStructTimeStep

- Specify the setting of Structure Static parameters such as Time Step, Output Timing Definition.
- The default value is [ADVC\_STRUCT\_TIME\_STEP](./../../data-type/psj-command/parameter-types/ADVC _STRUCT _TIME _STEP).

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify to be enable/disable the Convergence parameters setting option.
- If _True_: Enable setting option to modify the Convergence parameters
- If _False_: Disable setting option to modify the Convergence parameters
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcConvergence

- Specify the Convergence parameters setting.
- The default value is [ADVC\_CONVERGENCE](./../../data-type/psj-command/parameter-types/ADVC _CONVERGENCE).

<!-- @since:5.0.1 @optional -->
### bContact

- Specify to modify the Contact iterator parameters setting option.
  - If _True_: Enable setting option to modify the Contact iterator parameters
  - If _False_: Disable setting option to modify the Contact iterator parameters
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcContactIter

- Specify the Contact iterator parameters setting.
- The default value is [ADVC\_CONTACT\_ITER](./../../data-type/psj-command/parameter-types/ADVC _CONTACT _ITER).

<!-- @since:5.0.1 @optional -->
### bAutoIncrement

- Specify to modify the Auto Increment parameters setting option.
  - If _True_: Enable setting option to modify the Auto Increment parameters
  - If _False_: Disable setting option to modify the Auto Increment parameters
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcAutoIncrement

- Specify the Auto Increment parameters setting.
- The default value is [ADVC\_AUTO\_INCREMENT](./../../data-type/psj-command/parameter-types/ADVC _AUTO _INCREMENT).

<!-- @since:5.0.1 @optional -->
### dStabilizationFactor

- Specify the Stabilization factor.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the ADVC Static process in Assembly Tree to modify it. This option uses only for editing process purpose.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listLoadNode

- Specify the list of nodes that assigned loads in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadCaseNode

- Specify the list of nodes that assigned load cases in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadNodeContact

- Specify the list of nodes that assigned contacts in the model.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilOutputParamList

- Specify the list of output request for the result type such as Displacement, Stress, Strain,...
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iRefType

- Specify the result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strRefPath

- Specify the path of reference result.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listAdvcRefStressResult

- Specify the list of data of Reference Result.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bCrackGrowth

- Specify whether set crack growth parameters.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### CrackGrowthParam

- Specify the list of data of Reference Result.
- The default value is \[].

## Return Code

A _Cursor_ specifying the created or the modified ADVC Static process.

## Sample Code

```psj {31,32,33,34,35,36,37}
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

creating _status = Analysis.ADVC.MakeProcess.Static(strName="Process _0", 
                                                   advcStructTimeStep=ADVC _STRUCT _TIME _STEP(iNumOfInc=10), 
                                                   dStabilizationFactor=DFLT _DBL, 
                                                   listLoadNode=[], 
                                                   listLoadCaseNode=[], 
                                                   listLoadNodeContact=[], 
                                                   listAdvcRefStressResult=[])

JPT.Debugger(creating _status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx", 
                        strName="Job _1", 
                        crlProcessSequence=[ADVCProcessStatic(1)], 
                        crlTargets=[Part(1)], 
                        bAutoAssignDummyProp=True, 
                        listLoadNodeContact=[], 
                        iUiPrecision=6, 
                        bExportGeometryID=True)
```
