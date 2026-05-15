---
title: "Analysis.ExportAdx()"
description: "Export the ADVENTURECluster solver file in adx format with the existing Job in Assembly Tree. By pointing out the desired ADVC Job in Assembly Tree, exporting could be done multiple times with user's setting"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > Export Adx"
macro _link: "[ExportAdx](../../macro/analysis/ExportAdx)"
---

## Description

Export the ADVENTURECluster solver file in adx format with the existing Job in Assembly Tree. By pointing out the desired ADVC Job in Assembly Tree, exporting could be done multiple times with user's setting.

## Syntax

```psj
Analysis.ExportAdx(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crJob

- Specify the ADVC analysis Job in Assembly Tree by using identification number (ID number) of the Job.

<!-- @since:5.0.1 @required -->
### strPath

- Specify the destination path file to export. The destination path should be different from C Drive (C:/) due to Window would deny saving any files to C Drive directly (It is recommended to save in User's Drive such as D Drive, E Drive,...)

<!-- @since:5.0.1 @optional -->
### iNumType

- Specify the numeric format type. This argument would allow numeric setting type of adx file.
  - If _iNumType=0_: Real Type - The numerical values in real number format (123.456).
  - If _iNumType=1_: Power Type - The numerical values in exponential/scientific format (1.234E-005).
  - If _iNumType=2_: Auto Type - The numerical values would show in both above types depending on value of model
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iUiWidth

- Specify the limitation number of digits before the point of the number. This option allows to control number digits of value in exported ADX file.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### iUiPrecision

- Specify the limitation number of digits after the point of the number. This option allows to control number digits of value in exported ADX file.
- The default value is 1.

## Return Code

- An _Boolean_ specifying the status of the exporting process:
  - _True_: The ADVC (\*.adx) file has been exported successfully.
  - _False_: The ADVC (\*.adx) file cannot be exported.

## Sample Code

```psj {71-74}
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

Analysis.ADVC.MakeProcess.Static(strName="ADVC _DEFAULT _PROCESS",
                                 advcStructTimeStep=ADVC _STRUCT _TIME _STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT _DBL,
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.MakeProcess.Static(strName="ADVC _DEFAULT _PROCESS",
                                 advcStructTimeStep=ADVC _STRUCT _TIME _STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT _DBL,
                                 crEdit=ADVCProcessStatic(1),
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.MakeProcess.Static(strName="ADVC _DEFAULT _PROCESS",
                                 advcStructTimeStep=ADVC _STRUCT _TIME _STEP(dMaxDt=1.0,
                                                                          dMinDt=1e-05),
                                 dStabilizationFactor=DFLT _DBL,
                                 crEdit=ADVCProcessStatic(1),
                                 listLoadNode=[],
                                 listLoadCaseNode=[],
                                 listLoadNodeContact=[],
                                 listAdvcRefStressResult=[])

Analysis.ADVC.Structure(strPath="D:/Job _1.adx",
                        strName="Job _1",
                        crlProcessSequence=[ADVCProcessStatic(1)],
                        crlTargets=[Part(1)],
                        bAutoAssignDummyProp=True,
                        listLoadNodeContact=[],
                        iNumType=2,
                        iUiPrecision=5)

exported _status = Analysis.ExportAdx(crJob=ADVCJob(1),
                                     strPath="D:/Job _2.adx",
                                     iNumType=2,
                                     iUiPrecision=5)

JPT.Debugger(exported _status)
```
