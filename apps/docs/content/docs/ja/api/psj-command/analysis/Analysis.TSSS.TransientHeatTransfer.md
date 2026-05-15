---
title: "Analysis.TSSS.TransientHeatTransfer()"
description: "Export the Input Deck for TechnoStar SunShine Transient Heat Transfer analysis (SOL 159)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > SunShine > Transient Heat Transfer(SOL 159)"
---

## Description

Export the Input Deck for TechnoStar SunShine Transient Heat Transfer analysis (SOL 159).

## Syntax

```psj
Analysis.TSSS.TransientHeatTransfer(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.
- The default value is "Job\_1".

<!-- @since:5.0.1 @optional -->
### strDescription

- Specify the description of TechnoStar SunShine solver job.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of target part.
- The default value is \[] (all parts in the model).

<!-- @since:5.0.1 @optional -->
### nastranAnalysis

- Specify the TechnoStar Sunshine solver input parameter.
- The default value is _[NASTRAN\_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN _ANALYSIS)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the export location for bdf file.

<!-- @since:5.0.1 @optional -->
### iModelCheckAnswer

- Specify the model checking option.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDeleteSlaveNodesAnswer

- Specify the deleting slave nodes option.
- The default value is 0.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {50,51,52}
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

BoundaryConditions.BoundaryTemperature.Constant(dFTemp=373.15, 
                                                crlTargets=[Face(24)])
BoundaryConditions.HeatFlux.SurfaceFlux(strName="SurfaceHeatFlux1", 
                                        dFflux=150000.0,
                                        iDistributionMethod=1, 
                                        crTable=None, 
                                        crlTargets=[Face(23)])

input _param = NASTRAN _ANALYSIS(iSolverType=6, 
                               iGridFormatType=1, 
                               dEpsilon=1e-13,
                               iMaxNumOfIter=500, 
                               iNumberOfThreads=1, 
                               iMemory=2, 
                               iNcpu=1, 
                               iSolNo=159,
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeThermal=1),
                               nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True))

export _status = Analysis.TSSS.TransientHeatTransfer(nastranAnalysis = input _param, 
                                                    strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                              "/TechnoStar/Test.bdf")

JPT.Debugger(export _status)
```
