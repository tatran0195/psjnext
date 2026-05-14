---
title: "Analysis.Nastran.NormalModes()"
description: "Export the input file for Nastran structure normal modes analysis (SOL 103)."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Nastran > Normal Modes(SOL 103)"
---

## Description

Export the input file for Nastran structure normal modes analysis (SOL 103).

## Syntax

```psj
Analysis.Nastran.NormalModes(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Job _1" -->
### `strName`

- The job name of Nastran analysis.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strDescription`

- The description of Nastran analysis job.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of target parts.

<!-- @since:5.0.1 @type:NASTRAN _ANALYSIS @optional @default:NASTRAN _ANALYSIS -->
### `nastranAnalysis`

- The Nastran analysis input parameter.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDummyPropAutoAssign`

- Whether to enable or disable the auto dummy properties creation option.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDummyPropMaterialID`

- The material ID used for dummy property assignment.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The export path for bdf file.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iModelCheckAnswer`

- The model checking option.
  - 0: disable model checking option used for seeking dummy properties.
  - 1: enable model checking option used for seeking dummy properties.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDeleteSlaveNodesAnswer`

- The deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.

## Return Code

A _Cursor_ specifying the created job.

## Sample Code

```psj {55,56,57}
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
                                 iSolNo=103, 
                                 nastranEigen=NASTRAN _EIGEN(dStartFreq=5.0, 
                                                            dEndFreq=50.0, 
                                                            iNoOfModes=10),
                                 nastranFreqTimestep=NASTRAN _FREQ _TIMESTEP(iDampingType=2, 
                                                                           iModalDampingTableId=0),
                                 nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStress=0, 
                                                                             iTypeStrain=0), 
                                 nastranSettings=NASTRAN _SETTINGS(iMEFFMASS=2),
                                 nastranNonlinear=NASTRAN _NONLINEAR(iKMETHOD=3, 
                                                                    iMAXITER=1, 
                                                                    bUseEPSW=True))

exported _job = Analysis.Nastran.NormalModes(nastranAnalysis = nastran _param, 
                                            strPath=re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                    "/TechnoStar/Test.bdf")

JPT.Debugger(exported _job)
```
