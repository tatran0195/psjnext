---
title: "BoundaryConditions.InitialTemperature.ADVC()"
description: "Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Initial Temperature > ADVC file"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Read the temperature result output from format of Adventure Cluster solver and defines it as the initial temperature.

## Syntax

```psj
BoundaryConditions.InitialTemperature.ADVC(...)
```

## Inputs

### `strName` @type(String) @default("InitialTemperature1")

- The initial temperature name.

### `strFilePathName` @type(String) @required

- The ADVC temperature result file path.

### `iLocalTemperatureUnit` @type(Ingeter) @default(0) @since(5.1.0)

- The local temperature.

### `bUseDefault` @type(Boolean) @default(False)

- Whether enable or disable the default temperature.

### `crlTargets` @type(List\[Cursor]) @required

- List of target part for initial temperature.

### `crEdit` @type(Cursor) @default(None)

- An existing initial temperature.
  - If this parameter is used, the specified initial temperature will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new initial temperature will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {61-66}
import os

temp_folder = os.environ["Temp"] + "/TechnoStar"

if os.path.isdir(temp_folder):
    pass
else:
    os.mkdir(temp_folder)

Geometry.Part.Cube(iPartColor=6473570)
BoundaryConditions.BoundaryTemperature.Constant(dFTemp=293.15, 
                                                crlTargets=[Part(1)])
Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  200000.0), 
                                 (POISSONS_RATIO, 
                                  0.3)])])
Properties.Shell(crlTargets=[Part(1)], 
                 strName="Shell Property 1", 
                 iPropertyColor=16131973, 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT_DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT_DBL, 
                 dThickRatio=DFLT_DBL, 
                 dNSM=DFLT_DBL, 
                 dFiberDist1=DFLT_DBL, 
                 dFiberDist2=DFLT_DBL, 
                 dPlateOff=DFLT_DBL, 
                 iItgPts=DFLT_INT)
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05))
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1), 
                                      listLoadNode=[ADVC_LOAD_NODE(cr=LbcTempBoundary(1))])
Analysis.ADVC.MakeProcess.SteadyState(strName="ADVC_DEFAULT_PROCESS", 
                                      advcHeatTimeStep=ADVC_HEAT_TIME_STEP(dMaxdt=1.0, 
                                                                           dMindt=1e-05), 
                                      crEdit=ADVCProcessSSH(1))
Analysis.ADVC.HeatTransfer(strPath=temp_folder + "/test.adx", 
                           strName="Job_1", 
                           crlProcessSequence=[ADVCProcessSSH(1)], 
                           crlTargets=[Part(1)], 
                           bAutoAssignDummyProp=True, 
                           crDummyPropMaterial=Material(1), 
                           listLoadNodeContact=[], 
                           iUiPrecision=6, 
                           bExportGeometryID=True)

JPT.Exec('New Document()')

Geometry.Part.Cube()

created_bcs = BoundaryConditions.InitialTemperature.ADVC(
    strName="InitialTemperature_1",
    iLocalTemperatureUnit=1, 
    strFilePathName = temp_folder \
                      + "/test.adx", 
    crlTargets=[Part(1)])

JPT.Debugger(created_bcs)
```
