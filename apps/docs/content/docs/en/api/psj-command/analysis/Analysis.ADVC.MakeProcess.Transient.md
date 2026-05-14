---
title: "Analysis.ADVC.MakeProcess.Transient()"
description: "Create ADVC Heat Transfer for Transient process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Heat Transfer > Make Process"
macro _link: "[AdvcTHProcess](../../macro/analysis/AdvcTHProcess)"
---

## Description

Create ADVC Heat Transfer for Transient process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Transient(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name of the new process.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEndType`

- The end connection type. The possible values that it can take are 0, 1, and 2. Each of these numbers corresponds to "Max Time", "Steady Rate", "Both".

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dMaxTime`

- The maximum time. This argument is to be used when _iEndType=1_ or _iEndType=2_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSteadyRate`

- The steady rate. This argument is to be used when _iEndType=2_ or _iEndType=2_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFixedOrAuto`

- The incrementation type.
- If _iFixedOrAuto=0_: Use the fixed dt time value _dFixedDt_.
- If _iFixedOrAuto=1_: Auto calculate the dt time value base on these parameters _dMaxChange_, _dInitDt_, _dMaxDt_, _dMinDt_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxChange`

- The maximum change of temperature. This argument is to be used when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInitDt`

- The initial dt time. This argument is to be used when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDefineMaxDt`

- Whether to use the maximum dt time to calculate the incrementation when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxDt`

- The maximum dt time. This argument is to be used when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDefineMinDt`

- Whether to use the minimum dt time to calculate the incrementation when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMinDt`

- The minimum dt time. This argument is to be used when _iFixedOrAuto=1_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFixedDt`

- The fixed dt time value. This argument is to be used when _iFixedOrAuto=0_.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iOutputLast`

- The output last.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iOutputInterval`

- The output interval.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iRestartLast`

- The restart last.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iRestartInterval`

- The restart interval.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOutputTimeInterval`

- The output time interval.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dRestartTimeInterval`

- The restart time interval.

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iOutputInit`

- The output initial.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iListOutputInterval`

- The list output interval.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bConvergence`

- The convergence.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgTol`

- The convergence tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgNrTol`

- The convergence of Newton-Raphson method tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgDispTol`

- The convergence of displacement tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgNrDispTol`

- The convergence of Newton-Raphson method displacement tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgDispLimitTol`

- The convergence of displacement limit tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCgTotalDispLimitTol`

- The convergence of total displacement limit tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNewtonTol`

- The Newton tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNewtonDispTol`

- The Newton displacement tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNewtonDispLimitTol`

- The Newton displacement limit tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNewtonTotalDispLimitTol`

- The Newton total displacement limit tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iCgloopMax`

- The convergence of loop maximum.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iNewtonMax`

- The Newton maximum.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dHtNlLoopTol`

- The heat transfer nl loop tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iHtNlLoopMax`

- The heat transfer nl loop maximum.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing ADVC process to be modified. If the default value is specified, a new process will be created, otherwise the specified ADVC process will be modified.

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

creating _status = Analysis.ADVC.MakeProcess.Transient(strName="Process _0", 
                                                      dSteadyRate=DFLT _DBL, 
                                                      listLoadNode=[],
                                                      listLoadCaseNode=[], 
                                                      listLoadNodeContact=[])

JPT.Debugger(creating _status)
```
