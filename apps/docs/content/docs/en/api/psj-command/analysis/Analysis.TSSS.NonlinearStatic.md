---
title: "Analysis.TSSS.NonlinearStatic()"
description: "Export the Input Deck for TechnoStar SunShine Nonlinear Static analysis (SOL 106)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > SunShine > Nonlinear Static(SOL 106)"
macro _link: "TSSS _NonlinearStatic"
---

## Description

Export the Input Deck for TechnoStar SunShine Nonlinear Static analysis (SOL 106).

## Syntax

```psj
Analysis.TSSS.NonlinearStatic(...)
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

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iRadialReturn`

- The radial return algorithm used in Nonlinear Static Analysis.

<!-- @since:5.0.1 @type:NASTRAN _NONLINEAR @optional @default:[] -->
### `listNastranNonlinear`

- The _list_ specifying the Nastran Nonlinear parameter of TechnoStar SunShine solver.

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

<!-- @since:5.1.0 @type:Integer @optional -->
### `iLGDISP`

- The LGDISP parameter.
- This default value is -1.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iRigidMethod`

- The export RIGID card.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {53,54,55,56}
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
                               iSolNo=106,
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iValueBcresults=DFLT _INT, 
                                                                           iTypeStrain=0,
                                                                           iTypeBcresults=1),
                               nastranNonlinear=NASTRAN _NONLINEAR(iKMETHOD=1, 
                                                                  iMAXITER=10,
                                                                  bUseEPSW=True, 
                                                                  dEPSU=DFLT _DBL, 
                                                                  dEPSP=DFLT _DBL))

export _status = Analysis.TSSS.NonlinearStatic(nastranAnalysis = input _param,
                                              iRadialReturn=1, 
                                              strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                        "/TechnoStar/Test.bdf")

JPT.Debugger(export _status)
```
