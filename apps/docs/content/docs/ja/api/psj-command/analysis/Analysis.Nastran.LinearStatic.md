---
title: "Analysis.Nastran.LinearStatic()"
description: "Export the input file for Nastran Structure Linear Static anlysis (SOL 101)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Nastran > LinearStatic"
---

## Description

Export the input file for Nastran Structure Linear Static anlysis (SOL 101).

## Syntax

```psj
Analysis.Nastran.LinearStatic(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the job name of Nastran analysis.
- The default value is "Job\_1".

<!-- @since:5.0.1 @optional -->
### strDescription

- Specify the description of Nastran analysis job.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify list of target parts.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### nastranAnalysis

- Specify the Nastran analysis input parameter.
- The default value is _[NASTRAN\_ANALYSIS](./../../data-type/psj-command/parameter-types/NASTRAN _ANALYSIS)_.

<!-- @since:5.0.1 @optional -->
### bDummyPropAutoAssign

- Specify whether to enable or disable the auto dummy properties creation option.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iDummyPropMaterialID

- Specify the material ID which is used for dummy property assignment.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the export path for bdf file.

<!-- @since:5.0.1 @optional -->
### iModelCheckAnswer

- Specify the model checking option.
  - 0: disable model checking option used for seeking dummy properties.
  - 1: enable model checking option used for seeking dummy properties.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDeleteSlaveNodesAnswer

- Specify the deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.
- The default value is 0.

## Return Code

A _Cursor_ specifying the created job.

## Sample Code

```psj {50,51,52}
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

nastran _param = NASTRAN _ANALYSIS(iSolverType=1, 
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

exported _job = Analysis.Nastran.LinearStatic(nastranAnalysis = nastran _param, 
                                             strPath=re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                     "/TechnoStar/Test.bdf")

JPT.Debugger(exported _job)
```
