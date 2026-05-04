---
title: 'Analysis.ADVC.MakeProcess.EigenValue()'
description: 'Create a Structure - Eigenvalue analysis as an ADVC process'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > Structure > EigenValue'
macro_link: '[AdvcEigenProcess](../../macro/analysis/AdvcEigenProcess)'
---

## Description

Create a Structure - Eigenvalue analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.EigenValue(...)
```

## Inputs

### `strName` @type(String) @required

- The process name of Structure - Eigenvalue analysis.

### `bEigenValue` @type(Boolean) @default(False)

- To be enable/disable the Eigenvalue parameters option.

### `advcNormalModal` @type(ADVC_NORMAL_MODAL) @default(ADVC_NORMAL_MODAL)

- The parameters setting for the Eigenvalue analysis such as Eigen Num of Modes, Eigenvalue Parameter.

### `crEdit` @type(Cursor) @default(None)

- The ADVC Eigenvalue process in Assembly Tree to modify it. This option uses only for editing process purpose.

### `listLoadNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The load node.
- If this argument is specified, the`listLoadCaseNode`will be empty.

### `listLoadCaseNode` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The loadcase node.
- If this argument is specified, the`listLoadNode`will be empty.

### `listLoadNodeContact` @type(List\[ADVC_LOAD_NODE]) @default(\[])

- The load node contact.
- This argument uses the instance of[ADVC_LOAD_NODE](./../../data-type/psj-command/parameter-types/ADVC_LOAD_NODE)and won't be duplicated with`listLoadNode`or`listLoadCaseNode`

### `ilOutputParamList` @type(List\[Integer]) @default(\[])

- The list of output parameters.

### `iRefType` @type(Integer) @default(0)

- The result reference type.
    - I&#x66;_&#x69;RefType=0_: Temperature Load
    - I&#x66;_&#x69;RefType=1_: Stress

### `strRefPath` @type(String) @default("")

- The path of reference result.

### `listAdvcRefStressResult` @type(List\[ADVC_REF_STRESS_RESULT]) @default(\[])

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

creating_status = Analysis.ADVC.MakeProcess.EigenValue(strName="Process_0")

JPT.Debugger(creating_status)

Analysis.ADVC.Structure(strPath=environ["Temp"] + \
                                "/TechnoStar/Test.adx",
                        strName="Job_1",
                        crlProcessSequence=[ADVCProcessEigen(1)],
                        crlTargets=[Part(1)],
                        bAutoAssignDummyProp=True,
                        crDummyPropMaterial=Material(1),
                        listLoadNodeContact=[],
                        iUiPrecision=6,
                        bExportGeometryID=True)
```
