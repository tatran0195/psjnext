---
title: "Analysis.NastranJob()"
description: "Create a Nastran Analysis Job"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > NastranJob"
macro_link: "[NastranJob](../../macro/analysis/NastranJob)"
---

## Description

Create a Nastran Analysis Job.

## Syntax

```psj
Analysis.NastranJob(...)
```

## Inputs

### `strName` @type(String) @default("Job\_1")

- The job name of Nastran analysis.

### `strDescription` @type(String) @default("")

- The description of Nastran analysis job.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- List of target parts.

### `nastranAnalysis` @type(NASTRAN\_ANALYSIS) @default(NASTRAN\_ANALYSIS)

- The Nastran analysis input parameter.

### `bDummyPropAutoAssign` @type(Boolean) @default(False)

- Whether to enable or disable the auto dummy properties creation option.

### `iDummyPropMaterialID` @type(Integer) @default(0)

- The material ID which is used for dummy property assignment.

### `crEdit` @type(Cursor) @default(None)

- An existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new job will be created.

## Return Code

A _Cursor_ specifying the created job.

## Sample Code

```psj {52,53}
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

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, 
                                    dlDirection=[0.0, 
                                                 0.0, 
                                                 -1.0],
                                    crlTargets=[Face(26)])

nastran_param = NASTRAN_ANALYSIS(iSolverType=1, 
                                 iGridFormatType=1, 
                                 dEpsilon=DFLT_DBL,
                                 iMaxNumOfIter=DFLT_INT, 
                                 iMemory=DFLT_INT, 
                                 iNcpu=1, 
                                 iSolNo=101,
                                 nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueBcresults=DFLT_INT, 
                                                                             iValueBgresults=DFLT_INT, 
                                                                             iTypeStrain=0),
                                 nastranNonlinear=NASTRAN_NONLINEAR(iKMETHOD=3, 
                                                                    iMAXITER=1, 
                                                                    bUseEPSW=True))

exported_job = Analysis.NastranJob(nastranAnalysis = nastran_param, 
                                   iDummyPropMaterialID=5)

JPT.Debugger(exported_job)
```
