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

<!-- @since:5.0.1 @required -->
### strName

- Specify the process name of Structure - Eigenvalue analysis.

<!-- @since:5.0.1 @optional -->
### bEigenValue

- Specify to be enable/disable the Eigenvalue parameters option.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcNormalModal

- Specify the parameters setting for the Eigenvalue analysis such as Eigen Num of Modes, Eigenvalue Parameter.
- The default value is _[ADVC\_NORMAL\_MODAL](./../../data-type/psj-command/parameter-types/ADVC _NORMAL _MODAL)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the ADVC Eigenvalue process in Assembly Tree to modify it. This option uses only for editing process purpose.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listLoadNode

- Specify the load node.
- If this argument is specified, the `listLoadCaseNode` will be empty.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadCaseNode

- Specify the loadcase node.
- If this argument is specified, the `listLoadNode` will be empty.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listLoadNodeContact

- Specify the load node contact.
- This argument uses the instance of [ADVC\_LOAD\_NODE](./../../data-type/psj-command/parameter-types/ADVC _LOAD _NODE) and won't be duplicated with `listLoadNode` or `listLoadCaseNode`
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilOutputParamList

- Specify the list of output parameters.
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

- Specify the advc reference stress result.
- The default value is \[].

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
