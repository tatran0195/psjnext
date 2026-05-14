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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The process name of Structure - Creep analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGeomNonlinear`

- The geometry nonlinear.

<!-- @since:5.0.1 @type:Struct @optional @default:ADVC _STRUCT _TIME _STEP() -->
### `advcStructTimeStep`

- The struct time step.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bConvergence`

- The convergence.

<!-- @since:5.0.1 @type:Struct @optional @default:ADVC _CONVERGENCE() -->
### `advcConvergence`

- The convergence.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bContact`

- The contact.

<!-- @since:5.0.1 @type:Struct @optional @default:ADVC _CONTACT _ITER() -->
### `advcContactIter`

- The contact iterator.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoIncrement`

- The auto increment.

<!-- @since:5.0.1 @type:Struct @optional @default:ADVC _AUTO _INCREMENT() -->
### `advcAutoIncrement`

- The auto increment.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dStabilizationFactor`

- The stabilization factor.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bThetaDefined`

- The theta defined.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTheta`

- The theta.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

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

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iRefType`

- The reference type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strRefPath`

- The reference path.

<!-- @since:5.0.1 @type:List[ADVC _REF _STRESS _RESULT] @optional @default:[] -->
### `listAdvcRefStressResult`

- The advc reference stress result.

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bCrackGrowth`

- Whether set crack growth parameters.

### `CrackGrowthParam`

- A \_ [ADVC\_CRACK\_GROWTH](./../../data-type/psj-command/parameter-types/ADVC _CRACK _GROWTH)\_ specifying the list of data of Reference Result.

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
