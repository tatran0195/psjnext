---
title: "Analysis.Nastran.ModalTransientResponse()"
description: "Export the input file for Nastran Modal Transient Response Analysis (SOL 112)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Nastran > Modal Transient Response(SOL 112)"
---

## Description

Export the input file for Nastran Modal Transient Response Analysis (SOL 112).

## Syntax

```psj
Analysis.Nastran.ModalTransientResponse(...)
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

- The material ID which using for dummy property assignment.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The export path for bdf file.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iModelCheckAnswer`

- The model checking option.
  - 0: disable model checking option used for seeking dummy property.
  - 1: enable model checking option used for seeking dummy property.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDeleteSlaveNodesAnswer`

- The deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.

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
     iMaxNumOfIter=DFLT _INT, iMemory=DFLT _INT, iNcpu=1, iSolNo=112,
    nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iTypeStress=0, iTypeStrain=0),
    nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True))
Analysis.Nastran.ModalTransientResponse(nastranAnalysis= nastran _param,strPath="D:/Job _1.bdf")
```
