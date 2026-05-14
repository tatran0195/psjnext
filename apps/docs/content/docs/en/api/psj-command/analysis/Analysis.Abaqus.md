---
title: "Analysis.Abaqus()"
description: "Create an Abaqus job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Abaqus"
macro _link: "[CreateAbaqusJob](../../macro/analysis/CreateAbaqusJob)"
---

## Description

Create an Abaqus job.

## Syntax

```psj
Analysis.Abaqus(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The Abaqus job name.

<!-- @since:5.0.1 @type:JOB _ABAQUS _DATA @optional @default:JOB _ABAQUS _DATA -->
### `abaqusAnalysis`

- The Abaqus Analysis input parameter.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlStepSequence`

- The list of Abaqus step defined in sequence.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Abaqus job.
  - If this parameter is used, the specified job will be modified.
  - If it is left _None_, a new job will be created.

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

created _job = Analysis.Abaqus("Job _1", 
                              abaqusAnalysis=JOB _ABAQUS _DATA(iUnit=1))

JPT.Debugger(created _job)
```
