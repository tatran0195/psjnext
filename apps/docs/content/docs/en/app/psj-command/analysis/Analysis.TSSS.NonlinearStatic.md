---
title: "Analysis.TSSS.NonlinearStatic()"
description: "Export the Input Deck for TechnoStar SunShine Nonlinear Static analysis (SOL 106)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > SunShine > Nonlinear Static(SOL 106)"
macro_link: "TSSS_NonlinearStatic"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export the Input Deck for TechnoStar SunShine Nonlinear Static analysis (SOL 106).

## Syntax

```psj
Analysis.TSSS.NonlinearStatic(...)
```

## Inputs

### `strName` @type(String) @default("Job\_1")

- The job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.

### `strDescription` @type(String) @default("")

- The description of TechnoStar SunShine solver job.

### `crlTargets` @type(List\[Cursor]) @default(\[] (all parts in the model))

- The list of target part.

### `nastranAnalysis` @type(NASTRAN\_ANALYSIS) @default(NASTRAN\_ANALYSIS)

- The TechnoStar Sunshine solver input parameter.

### `iRadialReturn` @type(Integer) @default(DFLT\_INT)

- The radial return algorithm used in Nonlinear Static Analysis.

### `listNastranNonlinear` @type(NASTRAN\_NONLINEAR) @default(\[])

- &#xNAN;_&#x6C;is&#x74;_&#x73;pecifying the Nastran Nonlinear parameter of TechnoStar SunShine solver.

### `crEdit` @type(Cursor) @default(None)

- The created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), wher&#x65;_&#x49;&#x44;_&#x69;s the ID of the solver job had been created. If it is lef&#x74;_&#x4E;one_, a new TechnoStar solver job will be created.

### `strPath` @type(String) @required

- The export location for bdf file.

### `iModelCheckAnswer` @type(Integer) @default(0)

- The model checking option.

### `iDeleteSlaveNodesAnswer` @type(Integer) @default(0)

- The deleting slave nodes option.

### `iLGDISP` @type(Integer) @since(5.1.0)

- LGDISP parameter.
- This default value is -1.

### `iRigidMethod` @type(Integer) @since(5.1.0)

- Export RIGID card.

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
                               iSolNo=106,
                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueBcresults=DFLT_INT, 
                                                                           iTypeStrain=0,
                                                                           iTypeBcresults=1),
                               nastranNonlinear=NASTRAN_NONLINEAR(iKMETHOD=1, 
                                                                  iMAXITER=10,
                                                                  bUseEPSW=True, 
                                                                  dEPSU=DFLT_DBL, 
                                                                  dEPSP=DFLT_DBL))

export_status = Analysis.TSSS.NonlinearStatic(nastranAnalysis = input_param,
                                              iRadialReturn=1, 
                                              strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                        "/TechnoStar/Test.bdf")

JPT.Debugger(export_status)
```
