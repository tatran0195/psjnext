---
title: "BoundaryConditions.VirtualFluidMass()"
description: "Create a virtual fluid mass."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "BoundaryConditions > VirtualFluidMass"
macro _link: ""
---

## Description

Create a virtual fluid mass.

## Syntax

```psj
BoundaryConditions.VirtualFluidMass(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing virtual fluid mass.

<!-- @since:5.1.0 @type:String @optional @default:"FluidVolume _1" -->
### `strName`

- The name.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargetFaces`

- The target faces.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargetElems`

- The target elements.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargetGroups`

- The target groups.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iWettedSideType`

- The wetted side.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlNegativeSideTargets`

- The negative side targets.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFluidDensity`

- The fluid density.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFluidDensityUnit`

- The unit of fluid density.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The local coordinate.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFluidHeight`

- The coordinate of fluid.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFluidHeightUnit`

- The unit of coordinate of fluid.

<!-- @since:5.1.0 @type:Integer @optional @default:2 -->
### `iPlaneOfSymmetry1`

- The planes of symmetry 1.

<!-- @since:5.1.0 @type:Integer @optional @default:2 -->
### `iPlaneOfSymmetry2`

- The planes of symmetry 2.

## Return Code

This function does not have return value.

## Sample Code

```psj {18-21}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    strName="Cube _2", 
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
