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

<!-- @since:5.0.1 @type:String @optional @default:"TemperatureInitsWholeMapping1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMapSourceType`

- The map source type.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappingMethod`

- The mapping method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iIsubcase`

- The isubcase.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[]] -->
### `crTargets`

- The mapping targets.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMappingFromStepNo`

- The step number.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLocalUnit`

- The unit of temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {17-22}
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
