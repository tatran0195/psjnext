---
title: "BoundaryConditions.InitialTemperature.WholeMapping()"
description: "Create initial temperature whole mapping"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialTemperature > WholeMapping"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create initial temperature whole mapping.

## Syntax

```psj
BoundaryConditions.InitialTemperature.WholeMapping(...)
```

## Inputs

### `strName` @type(String) @default("TemperatureInitsWholeMapping1")

- The name.

### `iMapSourceType` @type(Integer) @default(0)

- The map source type.

### `strPath` @type(String) @default("")

- The path.

### `iMappingMethod` @type(Integer) @default(0)

- The mapping method.

### `iIsubcase` @type(Integer) @default(0)

- The isubcase.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `crTargets` @type(List\[Cursor]) @default(\[]]) @since(5.1.0)

- The mapping targets.

### `iMappingFromStepNo` @type(Integer) @default(0) @since(5.1.0)

- The step number.

### `iLocalUnit` @type(Integer) @default(0) @since(5.1.0)

- The unit of temperature.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{17-22}
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
    strName="TemperatureInitsWholeMapping_3", 
    crlTargets=[Part(1)], 
    strPath="C:/Temp/transient.op2",
    iMappingFromStepNo=5, 
    iLocalUnit=1)
```
