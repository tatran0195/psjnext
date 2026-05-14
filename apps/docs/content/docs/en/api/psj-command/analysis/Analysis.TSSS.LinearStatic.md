---
title: "Analysis.TSSS.LinearStatic()"
description: "Export the Input Deck for TechnoStar SunShine Linear Static analysis (SOL 101)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > SunShine > Linear Static(SOL 101)"
macro _link: "[TSSS _LinearStatic]"
---

## Description

Export the Input Deck for TechnoStar SunShine Linear Static analysis (SOL 101).

## Syntax

```psj
Analysis.TSSS.LinearStatic(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Job _1" -->
### `strName`

- The job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDescription`

- The description of TechnoStar SunShine solver job.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] (all parts in the model) -->
### `crlTargets`

- The list of target part.

<!-- @since:5.0.1 @type:NASTRAN _ANALYSIS @optional @default:NASTRAN _ANALYSIS -->
### `nastranAnalysis`

- The TechnoStar Sunshine solver input parameter.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The export location for bdf file.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iModelCheckAnswer`

- The model checking option.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDeleteSlaveNodesAnswer`

- The deleting slave nodes option.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInitTempType`

- The initial temperature load type.

<!-- @since:5.1.0 @type:Boolean @optional -->
### `bUSTARCalculation _b`

- The enable UStar calculation.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iMethod`

- The method.
  - 0 : Default
  - 1 : ORIGINAL

<!-- @since:5.1.0 @type:Boolean @optional -->
### `bDomainWithDSize _b`

- Whether domain with Dsize.
-

<!-- @since:5.1.0 @type:Integer @optional -->
### `iDSize`

- The value of Dsize.
-

<!-- @since:5.1.0 @type:Boolean @optional -->
### `bEPS _b`

- The enable EPS.
-

<!-- @since:5.1.0 @type:Double @optional -->
### `dEPS`

- The EPS value.
-

<!-- @since:5.1.0 @type:Integer @optional -->
### `iGroupKey`

- The group id.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iRigidMethod`

- The export RIGID card.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {50-53}
from os import environ
import re

Geometry.Part.Cube()
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
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=1000000.0,
                                    crlTargets=[Face(21,
                                                     23)])

input _param = NASTRAN _ANALYSIS(iSolverType=6,
                               iGridFormatType=1,
                               dEpsilon=DFLT _DBL,
                               iMaxNumOfIter=DFLT _INT,
                               iNumberOfThreads=1,
                               iMemory=2,
                               iNcpu=1,
                               iSolNo=101,
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStrain=0),
                               nastranNonlinear=NASTRAN _NONLINEAR(iMAXITER=DFLT _INT,
                                                                  bUseEPSW=True,
                                                                  dEPSU=DFLT _DBL,
                                                                  dEPSP=DFLT _DBL))

export _status = Analysis.TSSS.LinearStatic(nastranAnalysis = input _param,
                                           strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                         "/TechnoStar/Test.bdf",
                                           iInitTempType=2)

JPT.Debugger(export _status)
```
