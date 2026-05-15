---
title: "Analysis.ExportAbaqus()"
description: "Export Abaqus (*.inp) file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ExportAbaqus"
macro _link: "[ExportAbaqusInp](../../macro/analysis/ExportAbaqusInp)"
---

## Description

Export Abaqus (\*.inp) file.

## Syntax

```psj
Analysis.ExportAbaqus(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crAbaJob

- Specify the created Abaqus job using[Analysis.Abaqus()](Analysis.Abaqus) function.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the list of parts will be exported.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### strInpPath

- Specify the destination path file to export.
- The default value is "".

## Return Code

A _Boolean_ specifying the status of the exporting process:

- _True_: The Abaqus (\*.inp) file has been exported successfully.
- _False_: The Abaqus (\*.inp) file cannot be exported.

## Sample Code

```psj {56-58}
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

Analysis.AbaqusStep.StaticStep(strName="Step1",
                               iAutomatic=1,
                               iMaxInc=100,
                               dInitSize=1.0,
                               dMinSize=1e-05,
                               dMaxSize=1.0,
                               iAllowIter=8,
                               dAdjustFactor=1.0,
                               iMaxContactIteration=30,
                               dDampingFactor=0.0002,
                               iUseAdaptive=1,
                               dMaxRationOfEnergyStrain=0.05,
                               dTimePeriod=1.0,
                               iRamp=1,
                               iExtrapolateMethod=1,
                               strlFullPlasticRegion=[""])

Analysis.Abaqus(strName="Job _1", abaqusAnalysis=JOB _ABAQUS _DATA(iSurfDefType=1,
                iUnit=1, bExportNodeElemGroup=True, bDeleteFloatingNodes=True, bExportFaceElemGroup=True,
                bLoadCase=True, crDummyMat=Material(1)))
export _status = Analysis.ExportAbaqus(crAbaJob=AbaqusJob(1),
                                      strInpPath=re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                                 "/TechnoStar/Example _Export _Abaqus _PSJ _Command.inp")

print("Exported to INP file successfully!") \
    if export _status == True \
    else print("Error is occurred! Can't export INP file")
```
