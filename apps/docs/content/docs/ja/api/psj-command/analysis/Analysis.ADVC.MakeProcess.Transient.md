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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the new process.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iEndType

- Specify the end connection type. The possible values that it can take are 0, 1, and 2. Each of these numbers corresponds to "Max Time", "Steady Rate", "Both".
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dMaxTime

- Specify the maximum time. This argument is to be used when _iEndType=1_ or _iEndType=2_.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dSteadyRate

- Specify the steady rate. This argument is to be used when _iEndType=2_ or _iEndType=2_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFixedOrAuto

- Specify the incrementation type.
- If _iFixedOrAuto=0_: Use the fixed dt time value _dFixedDt_.
- If _iFixedOrAuto=1_: Auto calculate the dt time value base on these parameters _dMaxChange_, _dInitDt_, _dMaxDt_, _dMinDt_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxChange

- Specify the maximum change of temperature. This argument is to be used when _iFixedOrAuto=1_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dInitDt

- Specify the initial dt time. This argument is to be used when _iFixedOrAuto=1_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iDefineMaxDt

- Specify whether to use the maximum dt time to calculate the incrementation when _iFixedOrAuto=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxDt

- Specify the maximum dt time. This argument is to be used when _iFixedOrAuto=1_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iDefineMinDt

- Specify whether to use the minimum dt time to calculate the incrementation when _iFixedOrAuto=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMinDt

- Specify the minimum dt time. This argument is to be used when _iFixedOrAuto=1_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFixedDt

- Specify the fixed dt time value. This argument is to be used when _iFixedOrAuto=0_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iOutputLast

- Specify the output last.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iOutputInterval

- Specify the output interval.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iRestartLast

- Specify the restart last.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iRestartInterval

- Specify the restart interval.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### dOutputTimeInterval

- Specify the output time interval.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dRestartTimeInterval

- Specify the restart time interval.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iOutputInit

- Specify the output initial.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### iListOutputInterval

- Specify the list output interval.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify the convergence.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dCgTol

- Specify the convergence tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCgNrTol

- Specify the convergence of Newton-Raphson method tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCgDispTol

- Specify the convergence of displacement tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCgNrDispTol

- Specify the convergence of Newton-Raphson method displacement tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCgDispLimitTol

- Specify the convergence of displacement limit tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCgTotalDispLimitTol

- Specify the convergence of total displacement limit tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNewtonTol

- Specify the Newton tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNewtonDispTol

- Specify the Newton displacement tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNewtonDispLimitTol

- Specify the Newton displacement limit tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNewtonTotalDispLimitTol

- Specify the Newton total displacement limit tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iCgloopMax

- Specify the convergence of loop maximum.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### iNewtonMax

- Specify the Newton maximum.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### dHtNlLoopTol

- Specify the heat transfer nl loop tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iHtNlLoopMax

- Specify the heat transfer nl loop maximum.
- The default value is DFLT\_INT.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existing ADVC process to be modified. If the default value is specified, a new process will be created, otherwise the specified ADVC process will be modified.
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

- Specify the output param list.
- The default value is \[].

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
