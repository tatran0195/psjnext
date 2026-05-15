---
title: "Analysis.Nastran.LinearBuckling()"
description: "Export the input file for Nastran Linear Buckling Analysis (SOL 105)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Nastran > LinearBuckling"
---

## Description

Export the input file for Nastran Linear Buckling Analysis (SOL 105).

## Syntax

```psj
Analysis.Nastran.LinearBuckling(...)
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

- Specify the list of target parts.
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

- Specify the material ID which using for dummy property assignment.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the export path for bdf file.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iModelCheckAnswer

- Specify the model checking option.
  - 0: disable model checking option used for seeking dummy property.
  - 1: enable model checking option used for seeking dummy property.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDeleteSlaveNodesAnswer

- Specify the deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.
- The default value is 0.

## Return Code

A _Cursor_ specifying the newly created or the modified Nastran job.

## Sample Code

```psj {19}
Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, dGradingFactor=1.05,
     dStretchLimit=0.1, iSpeedVsQual=1, iRegion=1, bSafeMode=False,
     iParallel=12, bInternalMeshOnly=False, iPartColor=65280)

Properties.Material.Add("Structural _Steel", [Density([(DENSITY, 7.85e-09)]),
     Elastic([(YOUNGS _MODULUS, 200000.0), (POISSONS _RATIO, 0.3)])])
Properties.Solid(crMaterial=Material(1), dDynaRemeshVal1=DFLT _DBL,
     dDynaRemeshVal2=DFLT _DBL, dDispHG=DFLT _DBL, crlTargets=[Part(1)], iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, dlDirection=[0.0, 0.0, -1.0],
     crlTargets=[Face(26)])

nastran _param = NASTRAN _ANALYSIS(iSolverType=1, iGridFormatType=1, dEpsilon=DFLT _DBL,
     iMaxNumOfIter=DFLT _INT, iMemory=DFLT _INT, iNcpu=1, iSolNo=105,
    nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStress=0, iTypeStrain=0),
    nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True))
Analysis.Nastran.LinearBuckling(nastranAnalysis= nastran _param,strPath="D:/Job _1.bdf")
```
