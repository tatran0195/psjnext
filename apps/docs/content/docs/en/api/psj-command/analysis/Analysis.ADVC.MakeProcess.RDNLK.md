---
title: "Analysis.ADVC.MakeProcess.RDNLK()"
description: "Create ADVC RDNLK process for analysis work. This process could be created in one time or multiple times"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Analysis > ADVC > Make Process > Static"
macro _link: "[AdvcStaticProcess](../../macro/analysis/AdvcStaticProcess)"
---

## Description

Create ADVC RDNLK process for analysis work. This process could be created in one time or multiple times.

## Syntax

```psj
Analysis.ADVC.MakeProcess.RDNLK(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strName`

- The process name of ADVC - Static process.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iGeomNonlinear`

- The Geometry nonlinear option:
  - If _iGeomNonlinear=0_: None
  - If _iGeomNonlinear=1_: Total Lagrange - Consider the geometric nonlinearity due to total Lagrange method
  - If _iGeomNonlinear=2_: Updated Lagrange - Consider the geometric nonlinearity due to updated Lagrange method
  - If _iGeomNonlinear=3_: Linear
  - If _iGeomNonlinear=4_: NonLinear

<!-- @since:5.1.0 @type:ADVC _STRUCT _TIME _STEP @optional @default:ADVC _STRUCT _TIME _STEP -->
### `advcStructTimeStep`

- The setting of Structure Static parameters such as Time Step, Output Timing Definition.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bConvergence`

- The to be enable/disable the Convergence parameters setting option.
- If _True_: Enable setting option to modify the Convergence parameters
- If _False_: Disable setting option to modify the Convergence parameters

<!-- @since:5.1.0 @type:ADVC _CONVERGENCE @optional @default:ADVC _CONVERGENCE -->
### `advcConvergence`

- The Convergence parameters setting.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bContact`

- The to modify the Contact iterator parameters setting option.
  - If _True_: Enable setting option to modify the Contact iterator parameters
  - If _False_: Disable setting option to modify the Contact iterator parameters

<!-- @since:5.1.0 @type:ADVC _CONTACT _ITER @optional @default:ADVC _CONTACT _ITER -->
### `advcContactIter`

- The Contact iterator parameters setting.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bAutoIncrement`

- The to modify the Auto Increment parameters setting option.
  - If _True_: Enable setting option to modify the Auto Increment parameters
  - If _False_: Disable setting option to modify the Auto Increment parameters

<!-- @since:5.1.0 @type:ADVC _AUTO _INCREMENT @optional @default:ADVC _AUTO _INCREMENT -->
### `advcAutoIncrement`

- The Auto Increment parameters setting.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStabilizationFactor`

- The Stabilization factor.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- The ADVC Static process in Assembly Tree to modify it. This option uses only for editing process purpose.

<!-- @since:5.1.0 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNode`

- The list of nodes that assigned loads in the model.

<!-- @since:5.1.0 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadCaseNode`

- The list of nodes that assigned load cases in the model.

<!-- @since:5.1.0 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNodeContact`

- The list of nodes that assigned contacts in the model.

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The list of output request for the result type such as Displacement, Stress, Strain,...

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iRefType`

- The result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strRefPath`

- The path of reference result.

<!-- @since:5.1.0 @type:List[ADVC _REF _STRESS _RESULT] @optional @default:[] -->
### `listAdvcRefStressResult`

- The list of data of Reference Result.

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bCrackGrowth`

- Whether set crack growth parameters.

### `CrackGrowthParam`

- A \_ [ADVC\_CRACK\_GROWTH](./../../data-type/psj-command/parameter-types/ADVC _CRACK _GROWTH)\_ specifying the list of data of Reference Result.

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
