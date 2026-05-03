---
title: "Analysis.Abaqus()"
description: "Create an Abaqus job"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > Abaqus"
macro_link: "[CreateAbaqusJob](../../macro/analysis/CreateAbaqusJob)"
---

## Description

Create an Abaqus job.

## Syntax

```psj
Analysis.Abaqus(...)
```

## Inputs

### `strName` @type(String) @required

- The Abaqus job name.

### `abaqusAnalysis` @type(JOB\_ABAQUS\_DATA) @default(JOB\_ABAQUS\_DATA)

- The Abaqus Analysis input parameter.

### `crlStepSequence` @type(List\[Cursor]) @default(\[])

- The list of Abaqus step defined in sequence.

### `crEdit` @type(Cursor) @default(None)

- An existing Abaqus job.
  - If this parameter is used, the specified job will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new job will be created.

## Return Code

A _Cursor_ specifying the created jobs.

## Sample Code

```psj {28,29}
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

created_job = Analysis.Abaqus("Job_1", 
                              abaqusAnalysis=JOB_ABAQUS_DATA(iUnit=1))

JPT.Debugger(created_job)
```
