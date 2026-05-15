---
title: "BoundaryConditions.InitialTemperature.WholeMapping()"
description: "Create initial temperature whole mapping"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > WholeMapping"
---

## Description

Create initial temperature whole mapping.

## Syntax

```psj
BoundaryConditions.InitialTemperature.WholeMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "TemperatureInitsWholeMapping1".

<!-- @since:5.0.1 @optional -->
### iMapSourceType

- Specify the map source type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iMappingMethod

- Specify the mapping method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iIsubcase

- Specify the isubcase.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.1.0 @optional -->
### crTargets

- Specify the mapping targets.
- The default value is \[]].

<!-- @since:5.1.0 @optional -->
### iMappingFromStepNo

- Specify the step number.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iLocalUnit

- Specify the unit of temperature.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```pj {17-22}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(
    crlParts=[Part(1)], 
    bTet10=True, 
    dGradingFactor=1.05, 
    dStretchLimit=0.1, 
    iSpeedVsQual=1, 
    iRegion=1, 
    bSafeMode=False, 
    iParallel=16, 
    bInternalMeshOnly=False, 
    PartColor=65280)

# Assume nastran result include temperature more than 6 steps is at C:/Temp/transient.op2

BoundaryConditions.InitialTemperature.WholeMapping(
    strName="TemperatureInitsWholeMapping _3", 
    crlTargets=[Part(1)], 
    strPath="C:/Temp/transient.op2",
    iMappingFromStepNo=5, 
    iLocalUnit=1)
```
