---
title: "Analysis.TSSolver.NonlinearFrequency()"
description: "Export the Input Deck for TechnoStar Nonlinear Frequency analysis (SOL 126)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > TS-Solver > Nonlinear Frequency (SOL 126)"
---

## Description

Export the Input Deck for TechnoStar Nonlinear Frequency analysis (SOL 126).

## Syntax

```psj
Analysis.TSSolver.NonlinearFrequency(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the job name of TechnoStar solver. Output set by this name will be saved in the Assembly tree.
- The default value is "Job\_1".

<!-- @since:5.0.1 @optional -->
### strDescription

- Specify the description of TechnoStar solver job.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of target part.
- The default value is \[] (all parts in the model).

<!-- @since:5.0.1 @optional -->
### nastranAnalysis

- Specify the TechnoStar solver input parameter.
- The default value is [NASTRAN\_ANALYSIS()](./../../data-type/psj-command/parameter-types/NASTRAN _ANALYSIS).

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the created TechnoStar solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the export location for bdf file.

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

input _param = NASTRAN _ANALYSIS(iSolverType=3, 
                               iGridFormatType=1, 
                               dEpsilon=DFLT _DBL,
                               iMaxNumOfIter=DFLT _INT, 
                               iMemory=1024, 
                               iSolNo=126,
                               nastranEigen126=NASTRAN _EIGEN126(dModalStartFreq=0.0, 
                                                                dModalEndFreq=100.0, 
                                                                iModalNoOfModes=3,
                                                                dMLDSStartFreq=0.0, 
                                                                dMLDSEndFreq=100.0, 
                                                                iMLDSNoOfModes=3),
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeDisplacement=50, 
                                                                           iTypeSpcforces=50,
                                                                           iTypeStress=50, 
                                                                           iTypeStrainenergy=50, 
                                                                           iTypeAcceleration=50),
                               nastranSettings=NASTRAN _SETTINGS(strK6ROT="100"),
                               nastranNonlinear=NASTRAN _NONLINEAR(iNINC=DFLT _INT, 
                                                                  bUseEPSU=True, 
                                                                  bUseEPSP=True, 
                                                                  bUseEPSW=True,
                                                                  dEPSU=0.001, 
                                                                  dEPSP=0.001, 
                                                                  dEPSW=0.001),
                               nastranSubcase=[NASTRAN _SUBCASE(iId=1, 
                                                               strTitle="Subcase1"),
                                               NASTRAN _SUBCASE(iId=2, 
                                                               strTitle="Subcase2")])

export _status = Analysis.TSSolver.NonlinearFrequency(nastranAnalysis = input _param, 
                                                     strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                               "/TechnoStar/Test.bdf")

JPT.Debugger(export _status)
```
