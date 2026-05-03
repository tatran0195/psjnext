---
title: "Analysis.ModifyLbcToStep()"
description: "Add/Modify Loads, Boundary Conditions, etc. of an Abaqus step"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ModifyLbcToStep"
---

## Description

Add/Modify Loads, Boundary Conditions, etc. of an Abaqus step.

## Syntax

```psj
Analysis.ModifyLbcToStep(...)
```

## Inputs

### `listAbaqusLbcStepInfo` @type(ABAQUS\_LBC\_STEP\_INFO) @default(\[])

- &#xNAN;_&#x6C;is&#x74;_&#x73;pecifying the list of Abaqus steps from load boundary condition information.

## Return Code

A _Boolean_ specifying the status of the creating/modifying process:

- _True_: The specified step has been modified/created successfully.
- _False_: The specified step cannot be modified/created.

## Sample Code

```psj {49,50,51,52,53,54,55}
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
                        Elastic([(YOUNGS_MODULUS, 30000.0),
                                 (POISSONS_RATIO, 0.18)])])

Properties.Solid(crlTargets=[Part(1)],
                 strName="Solid Property 1",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=1000000.0,
                                    crlTargets=[Face(21,
                                                     23)])

Analysis.AbaqusStep.StaticStep(strName="Step1",
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

creating_status = Analysis.ModifyLbcToStep(listAbaqusLbcStepInfo=[ABAQUS_LBC_STEP_INFO(crStep=AbaqStepsStructStatic(1),
                                                                                       crLbc=LbcConstraint(1),
                                                                                       iCurflag=2),
                                                                  ABAQUS_LBC_STEP_INFO(crStep=AbaqStepsStructStatic(1),
                                                                                       crLbc=LbcGPressure(1),
                                                                                       iCurflag=3,
                                                                                       iPreflag=2)])

JPT.Debugger(creating_status)
```
