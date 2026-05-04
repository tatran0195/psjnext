---
title: 'Analysis.TSSolver.SteadyStateHeatTransfer()'
description: 'Export the Input Deck for TechnoStar Steady State Heat Transfer analysis (SOL 153)'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > TS-Solver > Steady State Heat Transfer(SOL 153)'
---

## Description

Export the Input Deck for TechnoStar Steady State Heat Transfer analysis (SOL 153).

## Syntax

```psj
Analysis.TSSolver.SteadyStateHeatTransfer(...)
```

## Inputs

### `strName` @type(String) @default("Job_1")

- The job name of TechnoStar solver. Output set by this name will be saved in the Assembly tree.

### `strDescription` @type(String) @default("")

- The description of TechnoStar solver job.

### `crlTargets` @type(List\[Cursor]) @default(\[] (all parts in the model))

- The list of target part.

### `nastranAnalysis` @type(NASTRAN_ANALYSIS) @default(NASTRAN_ANALYSIS)

- The TechnoStar solver input parameter.

### `crEdit` @type(Cursor) @default(None)

- The created TechnoStar solver job. If this parameter is used, the value will be DynamisJob(_ID_), wher&#x65;_&#x49;&#x44;_&#x69;s the ID of the solver job had been created. If it is lef&#x74;_&#x4E;one_, a new TechnoStar solver job will be created.

### `strPath` @type(String) @required

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
                        Elastic([(YOUNGS_MODULUS, 30000.0),
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

BoundaryConditions.BoundaryTemperature.Constant(dFTemp=373.15,
                                                crlTargets=[Face(24)])
BoundaryConditions.HeatFlux.SurfaceFlux(strName="SurfaceHeatFlux1",
                                        dFflux=150000.0,
                                        iDistributionMethod=1,
                                        crTable=None,
                                        crlTargets=[Face(23)])

input_param = NASTRAN_ANALYSIS(iSolverType=3,
                               iGridFormatType=1,
                               bUseCASI=True,
                               dEpsilon=1e-13,
                               iMaxNumOfIter=500,
                               iMemory=1024,
                               iSolNo=153,
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeThermal=1,
                                                                           iTypeFlux=6))

export_status = Analysis.TSSolver.SteadyStateHeatTransfer(nastranAnalysis = input_param,
                                                          strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                                    "/TechnoStar/Test.bdf")

JPT.Debugger(export_status)
```
