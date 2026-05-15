---
title: "Analysis.ADVC.MakeProcess.Creep()"
description: "Create a Structure - Creep analysis as an ADVC process"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ADVC > MakeProcess > Creep"
macro _link: "[AdvcCreepProcess](../../macro/analysis/AdvcCreepProcess)"
---

## Description

Create a Structure - Creep analysis as an ADVC process.

## Syntax

```psj
Analysis.ADVC.MakeProcess.Creep()
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the process name of Structure - Creep analysis.

<!-- @since:5.0.1 @optional -->
### iGeomNonlinear

- Specify the geometry nonlinear.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### advcStructTimeStep

- Specify the struct time step.
- The default value is ADVC\_STRUCT\_TIME\_STEP().

<!-- @since:5.0.1 @optional -->
### bConvergence

- Specify the convergence.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### advcConvergence

- Specify the convergence.
- The default value is ADVC\_CONVERGENCE().

<!-- @since:5.0.1 @optional -->
### bContact

- Specify the contact.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### advcContactIter

- Specify the contact iterator.
- The default value is ADVC\_CONTACT\_ITER().

<!-- @since:5.0.1 @optional -->
### bAutoIncrement

- Specify the auto increment.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### advcAutoIncrement

- Specify the auto increment.
- The default value is ADVC\_AUTO\_INCREMENT().

<!-- @since:5.0.1 @optional -->
### dStabilizationFactor

- Specify the stabilization factor.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### bThetaDefined

- Specify the theta defined.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dTheta

- Specify the theta.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

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

<!-- @since:5.0.1 @optional -->
### iRefType

- Specify the reference type.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### strRefPath

- Specify the reference path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listAdvcRefStressResult

- Specify the advc reference stress result.
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

A _Cursor_ specifying the created/modified Structure - Creep analysis as an ADVC process.

## Sample Code

```psj {0}
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
```
