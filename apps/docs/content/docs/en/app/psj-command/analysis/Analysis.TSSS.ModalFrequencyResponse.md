---
title: 'Analysis.TSSS.ModalFrequencyResponse()'
description: 'Export the Input Deck for TechnoStar SunShine Modal Frequency Response analysis (SOL 111)'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > SunShine > Modal Frequency Response(SOL 111)'
---

<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export the Input Deck for TechnoStar SunShine Modal Frequency Response analysis (SOL 111).

## Syntax

```psj
Analysis.TSSS.ModalFrequencyResponse(...)
```

## Inputs

### `strName` @type(String) @default("Job_1")

- The job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.

### `strDescription` @type(String) @default("")

- The description of TechnoStar SunShine solver job.

### `crlTargets` @type(List\[Cursor]) @default(\[] (all parts in the model))

- The list of target part.

### `nastranAnalysis` @type(NASTRAN_ANALYSIS) @default(NASTRAN_ANALYSIS)

- The TechnoStar Sunshine solver input parameter.

### `crEdit` @type(Cursor) @default(None)

- The created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), wher&#x65;_&#x49;&#x44;_&#x69;s the ID of the solver job had been created. If it is lef&#x74;_&#x4E;one_, a new TechnoStar solver job will be created.

### `strPath` @type(String) @required

- The export location for bdf file.

### `iModelCheckAnswer` @type(Integer) @default(0)

- The model checking option.

### `iDeleteSlaveNodesAnswer` @type(Integer) @default(0)

- The deleting slave nodes option.

### `iRigidMethod` @type(Integer) @since(5.1.0)

- Export RIGID card.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {52,53,54}
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

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=1000000.0,
                                    crlTargets=[Face(21,
                                                     23)])

input_param = NASTRAN_ANALYSIS(iSolverType=6,
                               iGridFormatType=1,
                               dEpsilon=DFLT_DBL,
                               iMaxNumOfIter=DFLT_INT,
                               iNumberOfThreads=1,
                               iMemory=2,
                               iNcpu=1,
                               iSolNo=111,
                               nastranFreqTimestep=NASTRAN_FREQ_TIMESTEP(iDampingType=1),
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueAcceleration=DFLT_INT,
                                                                           iValueVelocity=DFLT_INT,
                                                                           iTypeDisplacement=9,
                                                                           iTypeStress=0,
                                                                           iTypeStrain=0),
                               nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True))

export_status = Analysis.TSSS.ModalFrequencyResponse(nastranAnalysis = input_param,
                                                     strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                               "/TechnoStar/Test.bdf")

JPT.Debugger(export_status)
```
