---
title: "BoundaryConditions.InitialTemperature.ADVC()"
description: "Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Initial Temperature > ADVC file"
---

## Description

Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.ADVC(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InitialTemperature1" -->
### `strName`

- The initial temperature name.

<!-- @since:5.0.1 @type:String @required -->
### `strFilePathName`

- The ADVC temperature result file path.

<!-- @since:5.1.0 @type:Ingeter @optional @default:0 -->
### `iLocalTemperatureUnit`

- The local temperature.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseDefault`

- Whether enable or disable the default temperature.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The list of target part for initial temperature.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing initial temperature.
  - If this parameter is used, the specified initial temperature will be modified.
  - If it is left _None_, a new initial temperature will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {61-66}
import os

temp _folder = os.environ["Temp"] + "/TechnoStar"

if os.path.isdir(temp _folder):
    pass
else:
    os.mkdir(temp _folder)

Geometry.Part.Cube(iPartColor=6473570)
BoundaryConditions.BoundaryTemperature.Constant(dFTemp=293.15, 
                                                crlTargets=[Part(1)])
Properties.Material.Add("Structural _Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS _MODULUS, 
                                  200000.0), 
                                 (POISSONS _RATIO, 
                                  0.3)])])
Properties.Shell(crlTargets=[Part(1)], 
                 strName="Shell Property 1", 
                 iPropertyColor=16131973, 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT _DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT _DBL, 
                 dThickRatio=DFLT _DBL, 
                 dNSM=DFLT _DBL, 
                 dFiberDist1=DFLT _DBL, 
                 dFiberDist2=DFLT _DBL, 
                 dPlateOff=DFLT _DBL, 
                 iItgPts=DFLT _INT)
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC _DEFAULT _PROCESS", 
                                      advcHeatTimeStep=ADVC _HEAT _TIME _STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05))
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC _DEFAULT _PROCESS", 
                                      advcHeatTimeStep=ADVC _HEAT _TIME _STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1), 
                                      listLoadNode=[ADVC _LOAD _NODE(cr=LbcTempBoundary(1))])
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC _DEFAULT _PROCESS", 
                                      advcHeatTimeStep=ADVC _HEAT _TIME _STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1))
Analysis.ADVC.HeatTransfer(strPath=temp _folder + "/test.adx", 
                           strName="Job _1", 
                           crlProcessSequence=[ADVCProcessSSH(1)], 
                           crlTargets=[Part(1)], 
                           bAutoAssignDummyProp=True, 
                           crDummyPropMaterial=Material(1), 
                           listLoadNodeContact=[], 
                           iUiPrecision=6, 
                           bExportGeometryID=True)

JPT.Exec('New Document()')

Geometry.Part.Cube()

created _bcs = BoundaryConditions.InitialTemperature.ADVC(
    strName="InitialTemperature _1",
    iLocalTemperatureUnit=1, 
    strFilePathName = temp _folder \
                      + "/test.adx", 
    crlTargets=[Part(1)])

JPT.Debugger(created _bcs)
```
