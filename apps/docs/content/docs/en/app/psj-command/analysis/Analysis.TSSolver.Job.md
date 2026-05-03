---
title: "Analysis.TSSolver.Job()"
description: "Create TechnoStar Solver Job which is necessary for Analysis.TSSolver.ExportDynamisBdf"
version_introduced: "5.0.1"
available_versions: "all"
macro_link: "[DynamisJob](../../macro/analysis/DynamisJob)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create TechnoStar Solver Job which is necessary for _[Analysis.TSSolver.ExportDynamisBdf](Analysis.TSSolver.ExportDynamisBdf)_.

## Syntax

```psj
Analysis.TSSolver.Job(...)
```

## Inputs

### `strName` @type(String) @default("Job\_1")

- The job name of TechnoStar solver. Output set by this name will be saved in the Assembly tree.

### `strDescription` @type(String) @default("")

- The description of TechnoStar solver job.

### `crlTargets` @type(List\[Cursor]) @default(\[] (all parts in the model))

- The list of target part.

### `nastranAnalysis` @type(NASTRAN\_ANALYSIS) @default(NASTRAN\_ANALYSIS)

- The TechnoStar solver input parameter.

### `crEdit` @type(Cursor) @default(None)

- The created TechnoStar solver job. If this parameter is used, the value will be DynamisJob(_ID_), wher&#x65;_&#x49;&#x44;_&#x69;s the ID of the solver job had been created. If it is lef&#x74;_&#x4E;one_, a new TechnoStar solver job will be created.

## Return Code

A _Cursor_ specifying the created jobs.

## Sample Code

```psj {49}
Geometry.Part.Cube(iPartColor=5619133)
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
                 iPropertyColor=12275404, 
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

dynamic_param = NASTRAN_ANALYSIS(iSolverType=3, 
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

created_job = Analysis.TSSolver.LinearStatic(nastranAnalysis = dynamic_param)

JPT.Debugger(created_job)
```
