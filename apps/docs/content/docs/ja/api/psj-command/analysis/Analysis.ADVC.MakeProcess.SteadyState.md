---
title: "Analysis.ADVC.MakeProcess.SteadyState()"
description: "Create a Heat Transfer - Steady State analysis as an ADVC process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > Make Process > Steady State"
macro _link: "[AdvcSSHProcess](../../macro/analysis/AdvcSSHProcess)"
---

## Description

Create a Heat Transfer - Steady State analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.SteadyState(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the process name of Heat Transfer - Steady State analysis.

<!-- @since:5.0.1 @optional -->
### advcHeatTimeStep

- Specify the setting of Heat Transfer - Steady State parameters such as End Condition, Incrementation, Output Timing Definition.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify to modify the Convergence parameters setting option:
  - If _True_: Enable setting option to modify the Convergence parameters
  - If _False_: Disable setting option to modify the Convergence parameters
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### advcConvergence

- Specify the Convergence parameters setting.
- The default value is ADVC\_CONVERGENCE().

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the ADVC Heat Steady process in Assembly Tree to modify it. This option uses only for editing process purpose.
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

- Specify the list of output request for the result type such as Displacement, Stress, Strain,...
- The default value is \[].

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

creating _status = Analysis.ADVC.MakeProcess.SteadyState(strName="Process _0")

JPT.Debugger(creating _status)
```
