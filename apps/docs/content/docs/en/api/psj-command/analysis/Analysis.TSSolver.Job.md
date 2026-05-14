---
title: "Analysis.TSSolver.Job()"
description: "Create TechnoStar Solver Job which is necessary for Analysis.TSSolver.ExportDynamisBdf"
version _introduced: "5.0.1"
available _versions: "all"
macro _link: "[DynamisJob](../../macro/analysis/DynamisJob)"
---

## Description

Create TechnoStar Solver Job which is necessary for _[Analysis.TSSolver.ExportDynamisBdf](Analysis.TSSolver.ExportDynamisBdf)_.

## Syntax

```psj
Analysis.TSSolver.Job(...)
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
                        Elastic([(YOUNGS _MODULUS, 30000.0), 
                                 (POISSONS _RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)], 
                 strName="Solid Property 1", 
                 iPropertyColor=12275404, 
                 crMaterial=Material(1), 
                 iCordM=-2, 
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL, 
                 dDispHG=DFLT _DBL, 
                 iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, 
                                    dlDirection=[0.0, 
                                                 0.0, 
                                                 -1.0],
                                    crlTargets=[Face(26)])

dynamic _param = NASTRAN _ANALYSIS(iSolverType=3, 
                                 iGridFormatType=1, 
                                 dEpsilon=DFLT _DBL,
                                 iMaxNumOfIter=DFLT _INT, 
                                 iMemory=DFLT _INT, 
                                 iNcpu=1, 
                                 iSolNo=101,
                                 nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iValueBcresults=DFLT _INT, 
                                                                             iValueBgresults=DFLT _INT,
                                                                             iTypeStrain=0), 
                                 nastranNonlinear=NASTRAN _NONLINEAR(iKMETHOD=3, 
                                                                    iMAXITER=1, 
                                                                    bUseEPSW=True))

created _job = Analysis.TSSolver.LinearStatic(nastranAnalysis = dynamic _param)

JPT.Debugger(created _job)
```
