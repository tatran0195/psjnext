---
title: "Analysis.TSSS.LinearStatic()"
description: "Export the Input Deck for TechnoStar SunShine Linear Static analysis (SOL 101)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > SunShine > Linear Static(SOL 101)"
macro _link: "[TSSS _LinearStatic]"
---

## Description

Export the Input Deck for TechnoStar SunShine Linear Static analysis (SOL 101).

## Syntax

```psj
Analysis.TSSS.LinearStatic(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the job name of TechnoStar SunShine solver. Output set by this name will be saved in the Assembly tree.
- The default value is "Job\_1".

<!-- @since:5.0.1 @optional -->
### strDescription

- Specify the description of TechnoStar SunShine solver job.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of target part.
- The default value is \[] (all parts in the model).

<!-- @since:5.0.1 @optional -->
### nastranAnalysis

- Specify the TechnoStar Sunshine solver input parameter.
- The default value is _[NASTRAN\_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN _ANALYSIS)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the created TechnoStar SunShine solver job. If this parameter is used, the value will be DynamisJob(_ID_), where _ID_ is the ID of the solver job had been created. If it is left _None_, a new TechnoStar solver job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the export location for bdf file.

<!-- @since:5.0.1 @optional -->
### iModelCheckAnswer

- Specify the model checking option.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDeleteSlaveNodesAnswer

- Specify the deleting slave nodes option.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitTempType

- Specify the initial temperature load type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bUSTARCalculation\_b

- Specify enable UStar calculation.

<!-- @since:5.1.0 @optional -->
### iMethod

- Specify method.
  - 0 : Default
  - 1 : ORIGINAL

<!-- @since:5.1.0 @optional -->
### bDomainWithDSize\_b

- Specify whether domain with Dsize.
-

<!-- @since:5.1.0 @optional -->
### iDSize

- Specify value of Dsize.
-

<!-- @since:5.1.0 @optional -->
### bEPS\_b

- Specify enable EPS.
-

<!-- @since:5.1.0 @optional -->
### dEPS

- Specify EPS value.
-

<!-- @since:5.1.0 @optional -->
### iGroupKey

- Specify group id.

<!-- @since:5.1.0 @optional -->
### iRigidMethod

- Specify export RIGID card.

## Return Code

A _Cursor_ specifying the exported job.

## Sample Code

```psj {50-53}
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

input _param = NASTRAN _ANALYSIS(iSolverType=6,
                               iGridFormatType=1,
                               dEpsilon=DFLT _DBL,
                               iMaxNumOfIter=DFLT _INT,
                               iNumberOfThreads=1,
                               iMemory=2,
                               iNcpu=1,
                               iSolNo=101,
                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStrain=0),
                               nastranNonlinear=NASTRAN _NONLINEAR(iMAXITER=DFLT _INT,
                                                                  bUseEPSW=True,
                                                                  dEPSU=DFLT _DBL,
                                                                  dEPSP=DFLT _DBL))

export _status = Analysis.TSSS.LinearStatic(nastranAnalysis = input _param,
                                           strPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                         "/TechnoStar/Test.bdf",
                                           iInitTempType=2)

JPT.Debugger(export _status)
```
