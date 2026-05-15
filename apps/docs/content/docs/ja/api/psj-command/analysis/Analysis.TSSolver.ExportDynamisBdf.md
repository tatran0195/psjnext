---
title: "Analysis.TSSolver.ExportDynamisBdf()"
description: "Export the TechnoStar Dynamis solver file in bdf format"
version _introduced: "5.0.1"
available _versions: "all"
macro _link: "[ExportDynamisBdf](../../macro/analysis/ExportDynamisBdf)"
---

## Description

Export the TechnoStar Dynamis solver file in bdf format.

## Syntax

```psj
Analysis.TSSolver.ExportDynamisBdf(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strPath

- Specify the export location for bdf file.

<!-- @since:5.0.1 @required -->
### crJob

- Specify the_[Analysis.TSSolver.Job](Analysis.TSSolver.Job)_.

## Return Code

A _Cursor_ specifying the exported TS-Solver Dynamis BDF file.

## Sample Code

```psj {51,52,53}
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

dynamic _param = NASTRAN _ANALYSIS(iSolverType=3, 
                                 iGridFormatType=1, 
                                 dEpsilon=DFLT _DBL,
                                 iMaxNumOfIter=DFLT _INT, 
                                 iMemory=DFLT _INT, iNcpu=1, 
                                 iSolNo=101,
                                 nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iValueBcresults=DFLT _INT,
                                                                             iValueBgresults=DFLT _INT, 
                                                                             iTypeStrain=0),
                                 nastranNonlinear=NASTRAN _NONLINEAR(iKMETHOD=3, 
                                                                    iMAXITER=1, 
                                                                    bUseEPSW=True))

Analysis.TSSolver.Job(nastranAnalysis = dynamic _param)

export _status = Analysis.TSSolver.ExportDynamisBdf(strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                             "/TechnoStar/Test.bdf", 
                                                   crJob = DynamisJob(1))

JPT.Debugger(export _status)
```
