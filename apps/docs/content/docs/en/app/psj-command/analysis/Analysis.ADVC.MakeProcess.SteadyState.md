---
title: 'Analysis.ADVC.MakeProcess.SteadyState()'
description: 'Create a Heat Transfer - Steady State analysis as an ADVC process'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > Make Process > Steady State'
macro_link: '[AdvcSSHProcess](../../macro/analysis/AdvcSSHProcess)'
---

## Description

Create a Heat Transfer - Steady State analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.SteadyState(...)
```

## Inputs

### `strName` @type(String) @required

- The process name of Heat Transfer - Steady State analysis.

### `advcHeatTimeStep` @type(ADVC_HEAT_TIME_STEP) @default(\[])

- The setting of Heat Transfer - Steady State parameters such as End Condition, Incrementation, Output Timing Definition.

### `bConvergence` @type(Boolean) @default(False)

- To modify the Convergence parameters setting option:
    - I&#x66;_&#x54;rue_: Enable setting option to modify the Convergence parameters
    - I&#x66;_&#x46;alse_: Disable setting option to modify the Convergence parameters

### `advcConvergence` @type(ADVC_CONVERGENCE) @default(ADVC_CONVERGENCE())

- The Convergence parameters setting.

### `crEdit` @type(Cursor) @default(None)

- The ADVC Heat Steady process in Assembly Tree to modify it. This option uses only for editing process purpose.

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

- The list of output request for the result type such as Displacement, Stress, Strain,...

## Return Code

A _Cursor_ specifying the created or the modified ADVC Steady State process.

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

creating_status = Analysis.ADVC.MakeProcess.SteadyState(strName="Process_0")

JPT.Debugger(creating_status)
```
