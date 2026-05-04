---
title: 'Analysis.ADVC.MakeProcess.Transient()'
description: 'Create ADVC Heat Transfer for Transient process'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ADVC > Heat Transfer > Make Process'
macro_link: '[AdvcTHProcess](../../macro/analysis/AdvcTHProcess)'
---

## Description

Create ADVC Heat Transfer for Transient process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Transient(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name of the new process.

### `iEndType` @type(Integer) @default(1)

- The end connection type. The possible values that it can take are 0, 1, and 2. Each of these numbers corresponds to "Max Time", "Steady Rate", "Both".

### `dMaxTime` @type(Double) @default(1)

- The maximum time. This argument is to be used whe&#x6E;_&#x69;EndType=&#x31;_&#x6F;&#x72;_&#x69;EndType=2_.

### `dSteadyRate` @type(Double) @default(0.0)

- The steady rate. This argument is to be used whe&#x6E;_&#x69;EndType=&#x32;_&#x6F;&#x72;_&#x69;EndType=2_.

### `iFixedOrAuto` @type(Integer) @default(0)

- The incrementation type.
- I&#x66;_&#x69;FixedOrAuto=0_: Use the fixed dt time valu&#x65;_&#x64;FixedDt_.
- I&#x66;_&#x69;FixedOrAuto=1_: Auto calculate the dt time value base on these parameter&#x73;_&#x64;MaxChange_,_dInitDt_,_dMaxDt_,_dMinDt_.

### `dMaxChange` @type(Double) @default(DFLT_DBL)

- The maximum change of temperature. This argument is to be used whe&#x6E;_&#x69;FixedOrAuto=1_.

### `dInitDt` @type(Double) @default(DFLT_DBL)

- The initial dt time. This argument is to be used whe&#x6E;_&#x69;FixedOrAuto=1_.

### `iDefineMaxDt` @type(Integer) @default(0)

- Whether to use the maximum dt time to calculate the incrementation whe&#x6E;_&#x69;FixedOrAuto=1_.

### `dMaxDt` @type(Double) @default(DFLT_DBL)

- The maximum dt time. This argument is to be used whe&#x6E;_&#x69;FixedOrAuto=1_.

### `iDefineMinDt` @type(Integer) @default(0)

- Whether to use the minimum dt time to calculate the incrementation whe&#x6E;_&#x69;FixedOrAuto=1_.

### `dMinDt` @type(Double) @default(DFLT_DBL)

- The minimum dt time. This argument is to be used whe&#x6E;_&#x69;FixedOrAuto=1_.

### `dFixedDt` @type(Double) @default(DFLT_DBL)

- The fixed dt time value. This argument is to be used whe&#x6E;_&#x69;FixedOrAuto=0_.

### `iOutputLast` @type(Integer) @default(-1)

- The output last.

### `iOutputInterval` @type(Integer) @default(DFLT_INT)

- The output interval.

### `iRestartLast` @type(Integer) @default(-1)

- The restart last.

### `iRestartInterval` @type(Integer) @default(DFLT_INT)

- The restart interval.

### `dOutputTimeInterval` @type(Double) @default(DFLT_DBL)

- The output time interval.

### `dRestartTimeInterval` @type(Double) @default(DFLT_DBL)

- The restart time interval.

### `iOutputInit` @type(Integer) @default(-1)

- The output initial.

### `iListOutputInterval` @type(Integer) @default(DFLT_INT)

- The list output interval.

### `bConvergence` @type(Boolean) @default(False)

- The convergence.

### `dCgTol` @type(Double) @default(DFLT_DBL)

- The convergence tolerance.

### `dCgNrTol` @type(Double) @default(DFLT_DBL)

- The convergence of Newton-Raphson method tolerance.

### `dCgDispTol` @type(Double) @default(DFLT_DBL)

- The convergence of displacement tolerance.

### `dCgNrDispTol` @type(Double) @default(DFLT_DBL)

- The convergence of Newton-Raphson method displacement tolerance.

### `dCgDispLimitTol` @type(Double) @default(DFLT_DBL)

- The convergence of displacement limit tolerance.

### `dCgTotalDispLimitTol` @type(Double) @default(DFLT_DBL)

- The convergence of total displacement limit tolerance.

### `dNewtonTol` @type(Double) @default(DFLT_DBL)

- The Newton tolerance.

### `dNewtonDispTol` @type(Double) @default(DFLT_DBL)

- The Newton displacement tolerance.

### `dNewtonDispLimitTol` @type(Double) @default(DFLT_DBL)

- The Newton displacement limit tolerance.

### `dNewtonTotalDispLimitTol` @type(Double) @default(DFLT_DBL)

- The Newton total displacement limit tolerance.

### `iCgloopMax` @type(Integer) @default(DFLT_INT)

- The convergence of loop maximum.

### `iNewtonMax` @type(Integer) @default(DFLT_INT)

- The Newton maximum.

### `dHtNlLoopTol` @type(Double) @default(DFLT_DBL)

- The heat transfer nl loop tolerance.

### `iHtNlLoopMax` @type(Integer) @default(DFLT_INT)

- The heat transfer nl loop maximum.

### `crEdit` @type(Cursor) @default(None)

- The existing ADVC process to be modified. If the default value is specified, a new process will be created, otherwise the specified ADVC process will be modified.

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

- The output param list.

## Return Code

A _Cursor_ specifying the created or the modified ADVC Transient process.

## Sample Code

```psj {31,32,33,34,35}
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

creating_status = Analysis.ADVC.MakeProcess.Transient(strName="Process_0",
                                                      dSteadyRate=DFLT_DBL,
                                                      listLoadNode=[],
                                                      listLoadCaseNode=[],
                                                      listLoadNodeContact=[])

JPT.Debugger(creating_status)
```
