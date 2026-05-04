---
title: 'Analysis.Nastran.Transient()'
description: 'Export the input file for Nastran Transient Heat Transfer analysis (SOL 159)'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > Nastran > Transient'
---

## Description

Export the input file for Nastran Transient Heat Transfer analysis (SOL 159).

## Syntax

```psj
Analysis.Nastran.Transient(...)
```

## Inputs

### `strName` @type(String) @default("Job_1")

- The job name of Nastran analysis.

### `strDescription` @type(String) @default("")

- The description of Nastran analysis job.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- List of target parts.

### `nastranAnalysis` @type(NASTRAN_ANALYSIS) @default(NASTRAN_ANALYSIS)

- The Nastran analysis input parameter.

### `bDummyPropAutoAssign` @type(Boolean) @default(False)

- Whether to enable or disable the auto dummy properties creation option.

### `iDummyPropMaterialID` @type(Integer) @default(0)

- The material ID used for dummy property assignment.

### `crEdit` @type(Cursor) @default(None)

- An existing Nastran job.
    - If this parameter is used, the specified job will be modified.
    - If it is lef&#x74;_&#x4E;one_, a new job will be created.

### `strPath` @type(String) @required

- The export path for bdf file.

### `iModelCheckAnswer` @type(Integer) @default(0)

- The model checking option.
    - 0: disable model checking option used for seeking dummy properties.
    - 1: enable model checking option used for seeking dummy properties.

### `iDeleteSlaveNodesAnswer` @type(Integer) @default(0)

- The deleting slave nodes option.
    - 0: disable the deleting slave nodes checking option.
    - 1: enable the deleting slave nodes checking option.

## Return Code

A _Cursor_ specifying the created job.

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

nastran_param = NASTRAN_ANALYSIS(iSolverType=1,
                                 iGridFormatType=1,
                                 dEpsilon=DFLT_DBL,
                                 iMaxNumOfIter=DFLT_INT,
                                 iMemory=DFLT_INT,
                                 iNcpu=1,
                                 iSolNo=159,
                                 nastranFreqTimestep=NASTRAN_FREQ_TIMESTEP(iDampingType=2,
                                                                           iModalDampingTableId=0),
                                 nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeThermal=1),
                                 nastranNonlinear=NASTRAN_NONLINEAR(iKMETHOD=3,
                                                                    iMAXITER=1,
                                                                    bUseEPSW=True))

exported_job = Analysis.Nastran.Transient(nastranAnalysis = nastran_param,
                                          iDummyPropMaterialID=1,
                                          strPath=re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                  "/TechnoStar/Test.bdf")

JPT.Debugger(exported_job)
```
