---
title: "Analysis.Nastran.ModalFrequencyResponse()"
description: "Export the input file for Nastran Modal Frequency Response Analysis (SOL 111)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > Nastran > Modal Frequency Response(SOL 111)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export the input file for Nastran Modal Frequency Response Analysis (SOL 111).

## Syntax

```psj
Analysis.Nastran.ModalFrequencyResponse(...)
```

## Inputs

### `strName` @type(String) @default("Job\_1")

- The job name of Nastran analysis.

### `strDescription` @type(String) @default("")

- The description of Nastran analysis job.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of target parts.

### `nastranAnalysis` @type(NASTRAN\_ANALYSIS) @default(NASTRAN\_ANALYSIS)

- The Nastran analysis input parameter.

### `bDummyPropAutoAssign` @type(Boolean) @default(False)

- Whether to enable or disable the auto dummy properties creation option.

### `iDummyPropMaterialID` @type(Integer) @default(0)

- The material ID which using for dummy property assignment.

### `crEdit` @type(Cursor) @default(None)

- An existing Nastran job.
  - If this parameter is used, the specified job will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new job will be created.

### `strPath` @type(String) @default("")

- The export path for bdf file.

### `iModelCheckAnswer` @type(Integer) @default(0)

- The model checking option.
  - 0: disable model checking option used for seeking dummy property.
  - 1: enable model checking option used for seeking dummy property.

### `iDeleteSlaveNodesAnswer` @type(Integer) @default(0)

- The deleting slave nodes option.
  - 0: disable the deleting slave nodes checking option.
  - 1: enable the deleting slave nodes checking option.

## Return Code

A _Cursor_ specifying the newly created or the modified Nastran job.

## Sample Code

```psj {21}
Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)], bTet10=True, dGradingFactor=1.05,
     dStretchLimit=0.1, iSpeedVsQual=1, iRegion=1, bSafeMode=False,
     iParallel=12, bInternalMeshOnly=False, iPartColor=65280)

Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
     Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Solid(crMaterial=Material(1), dDynaRemeshVal1=DFLT_DBL,
     dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL, crlTargets=[Part(1)], iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(25)])
BoundaryConditions.Pressure.General(dPressure=10.0, dlDirection=[0.0, 0.0, -1.0],
     crlTargets=[Face(26)])

nastran_param = NASTRAN_ANALYSIS(iSolverType=1, iGridFormatType=1, dEpsilon=DFLT_DBL,
     iMaxNumOfIter=DFLT_INT, iMemory=DFLT_INT, iNcpu=1, iSolNo=111,
     nastranFreqTimestep=NASTRAN_FREQ_TIMESTEP(iDampingType=1),
     nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueSdisplacement=DFLT_INT,
     iValueAcceleration=DFLT_INT, iValueVelocity=DFLT_INT, iTypeStress=0, iTypeStrain=0),
     nastranSettings=NASTRAN_SETTINGS(iMEFFMASS=2))
Analysis.Nastran.ModalTransientResponse(nastranAnalysis= nastran_param, strPath="D:/Job_1.bdf")
```
