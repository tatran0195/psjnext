---
title: "BoundaryConditions.VirtualFluidMass()"
description: "Create a virtual fluid mass."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "BoundaryConditions > VirtualFluidMass"
macro_link: ""
---

## Description

Create a virtual fluid mass.

## Syntax

```psj
BoundaryConditions.VirtualFluidMass(...)
```

## Inputs

### `crEdit` @type(Cursor) @default(None)

- Existing virtual fluid mass.

### `strName` @type(String) @default("FluidVolume\_1")

- The name.

### `crlTargetFaces` @type(List\[Cursor]) @default(\[])

- The target faces.

### `crlTargetElems` @type(List\[Cursor]) @default(\[])

- The target elements.

### `crlTargetGroups` @type(List\[Cursor]) @default(\[])

- The target groups.

### `iWettedSideType` @type(Integer) @default(0)

- Wetted side.

### `crlNegativeSideTargets` @type(List\[Cursor]) @default(\[])

- Negative side targets.

### `dFluidDensity` @type(Double) @default(0.0)

- Fluid density.

### `iFluidDensityUnit` @type(Integer) @default(0)

- Unit of fluid density.

### `crCoordinate` @type(Cursor) @default(None)

- Local coordinate.

### `dFluidHeight` @type(Double) @default(0.0)

- Coordinate of fluid.

### `iFluidHeightUnit` @type(Integer) @default(0)

- Unit of coordinate of fluid.

### `iPlaneOfSymmetry1` @type(Integer) @default(2)

- Planes of symmetry 1.

### `iPlaneOfSymmetry2` @type(Integer) @default(2)

- Planes of symmetry 2.

## Return Code

This function does not have return value.

## Sample Code

```psj {18-21}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    strName="Cube_2", 
    iPartColor=14903267)
    
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
    iPartColor=65280)

BoundaryConditions.VirtualFluidMass(
    crlTargetFaces=[Face(26, 24, 22, 23, 21)], 
    crlNegativeSideTargets=[Face(24, 22, 23, 21)],
    dFluidDensity=1000000000000000.0)
```
