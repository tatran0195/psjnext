---
title: "Analysis.ADVC.MakeProcess.EigenValue()"
description: "Create a Structure - Eigenvalue analysis as an ADVC process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Structure > EigenValue"
macro _link: "[AdvcEigenProcess](../../macro/analysis/AdvcEigenProcess)"
---

## Description

Create a Structure - Eigenvalue analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.EigenValue(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The process name of Structure - Eigenvalue analysis.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bEigenValue`

- The to be enable/disable the Eigenvalue parameters option.

<!-- @since:5.0.1 @type:ADVC _NORMAL _MODAL @optional @default:ADVC _NORMAL _MODAL -->
### `advcNormalModal`

- The parameters setting for the Eigenvalue analysis such as Eigen Num of Modes, Eigenvalue Parameter.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The ADVC Eigenvalue process in Assembly Tree to modify it. This option uses only for editing process purpose.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNode`

- The load node.
- If this argument is specified, the `listLoadCaseNode` will be empty.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadCaseNode`

- The loadcase node.
- If this argument is specified, the `listLoadNode` will be empty.

<!-- @since:5.0.1 @type:List[ADVC _LOAD _NODE] @optional @default:[] -->
### `listLoadNodeContact`

- The load node contact.
- This argument uses the instance of [ADVC\_LOAD\_NODE](./../../data-type/psj-command/parameter-types/ADVC _LOAD _NODE) and won't be duplicated with `listLoadNode` or `listLoadCaseNode`

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilOutputParamList`

- The list of output parameters.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRefType`

- The result reference type.
  - If _iRefType=0_: Temperature Load
  - If _iRefType=1_: Stress

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The path of reference result.

<!-- @since:5.0.1 @type:List[ADVC _REF _STRESS _RESULT] @optional @default:[] -->
### `listAdvcRefStressResult`

- The advc reference stress result.

## Return Code

A _Cursor_ specifying the created/modified Structure - Eigenvalue analysis as an ADVC process.

## Sample Code

```psj {31}
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

creating _status = Analysis.ADVC.MakeProcess.EigenValue(strName="Process _0")

JPT.Debugger(creating _status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx", 
                        strName="Job _1", 
                        crlProcessSequence=[ADVCProcessEigen(1)], 
                        crlTargets=[Part(1)], 
                        bAutoAssignDummyProp=True, 
                        crDummyPropMaterial=Material(1), 
                        listLoadNodeContact=[], 
                        iUiPrecision=6, 
                        bExportGeometryID=True)
```
