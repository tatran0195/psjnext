---
title: 'Analysis.TSSolver.NonlinearFrequency()'
description: 'Export the Input Deck for TechnoStar Nonlinear Frequency analysis (SOL 126)'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > TS-Solver > Nonlinear Frequency (SOL 126)'
---

## Description

Export the Input Deck for TechnoStar Nonlinear Frequency analysis (SOL 126).

## Syntax

```psj
Analysis.TSSolver.NonlinearFrequency(...)
```

## Inputs

### `strName` @type(String) @default("Job_1")

- The job name of TechnoStar solver. Output set by this name will be saved in the Assembly tree.

### `strDescription` @type(String) @default("")

- The description of TechnoStar solver job.

### `crlTargets` @type(List\[Cursor]) @default(\[] (all parts in the model))

- The list of target part.

### `nastranAnalysis` @type(NASTRAN_ANALYSIS()) @default(NASTRAN_ANALYSIS())

- The TechnoStar solver input parameter.

### `crEdit` @type(Cursor) @default(None)

- The created TechnoStar solver job. If this parameter is used, the value will be DynamisJob(_ID_), wher&#x65;_&#x49;&#x44;_&#x69;s the ID of the solver job had been created. If it is lef&#x74;_&#x4E;one_, a new TechnoStar solver job will be created.

### `strPath` @type(String) @required

- The export location for bdf file.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {66,67,68}
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

input_param = NASTRAN_ANALYSIS(iSolverType=3,
                               iGridFormatType=1,
                               dEpsilon=DFLT_DBL,
                               iMaxNumOfIter=DFLT_INT,
                               iMemory=1024,
                               iSolNo=126,
                               nastranEigen126=NASTRAN_EIGEN126(dModalStartFreq=0.0,
                                                                dModalEndFreq=100.0,
                                                                iModalNoOfModes=3,
                                                                dMLDSStartFreq=0.0,
                                                                dMLDSEndFreq=100.0,
                                                                iMLDSNoOfModes=3),
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeDisplacement=50,
                                                                           iTypeSpcforces=50,
                                                                           iTypeStress=50,
                                                                           iTypeStrainenergy=50,
                                                                           iTypeAcceleration=50),
                               nastranSettings=NASTRAN_SETTINGS(strK6ROT="100"),
                               nastranNonlinear=NASTRAN_NONLINEAR(iNINC=DFLT_INT,
                                                                  bUseEPSU=True,
                                                                  bUseEPSP=True,
                                                                  bUseEPSW=True,
                                                                  dEPSU=0.001,
                                                                  dEPSP=0.001,
                                                                  dEPSW=0.001),
                               nastranSubcase=[NASTRAN_SUBCASE(iId=1,
                                                               strTitle="Subcase1"),
                                               NASTRAN_SUBCASE(iId=2,
                                                               strTitle="Subcase2")])

export_status = Analysis.TSSolver.NonlinearFrequency(nastranAnalysis = input_param,
                                                     strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                               "/TechnoStar/Test.bdf")

JPT.Debugger(export_status)
```
