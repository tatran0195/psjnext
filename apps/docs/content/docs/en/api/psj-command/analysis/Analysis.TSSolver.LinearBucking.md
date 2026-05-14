---
title: "Analysis.TSSolver.LinearBucking()"
description: "Export the Input Deck for TechnoStar solver Linear Buckling analysis (SOL 105)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > TS-Solver > Linear Buckling(SOL 105)"
---

## Description

Export the Input Deck for TechnoStar solver Linear Buckling analysis (SOL 105).

## Syntax

```psj
Analysis.TSSolver.LinearBucking(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Job _1" -->
### `strName`

- The job name of TechnoStar solver. Output set by this name will be saved in the Assembly tree.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDescription`

- The description of TechnoStar solver job.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] (all parts in the model) -->
### `crlTargets`

- The list of target part.

<!-- @since:5.0.1 @type:NASTRAN _ANALYSIS @optional @default:NASTRAN _ANALYSIS -->
### `nastranAnalysis`

- The TechnoStar solver input parameter.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The created TechnoStar solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The export location for bdf file.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {49,50,51}
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

input _param = NASTRAN _ANALYSIS(iSolverType=3, 
                               iGridFormatType=1, 
                               dEpsilon=DFLT _DBL,
                               iMaxNumOfIter=DFLT _INT, 
                               iMemory=1024, 
                               iSolNo=105,
                               nastranEigen=NASTRAN _EIGEN(dStartFreq=0.0, 
                                                          dEndFreq=100.0, 
                                                          iNoOfModes=3),
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStress=0, 
                                                                           iTypeStrain=0),
                               nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True))

export _status = Analysis.TSSolver.LinearBucking(nastranAnalysis = input _param, 
                                                strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                          "/TechnoStar/Test.bdf")

JPT.Debugger(export _status)
```
