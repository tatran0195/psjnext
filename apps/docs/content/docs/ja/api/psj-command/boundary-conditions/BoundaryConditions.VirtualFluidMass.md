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

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify existing virtual fluid mass.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name.
- The default value is "FluidVolume\_1".

<!-- @since:5.1.0 @optional -->
### crlTargetFaces

- Specify the target faces.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlTargetElems

- Specify the target elements.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlTargetGroups

- Specify the target groups.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iWettedSideType

- Specify wetted side.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crlNegativeSideTargets

- Specify negative side targets.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dFluidDensity

- Specify fluid density.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iFluidDensityUnit

- Specify unit of fluid density.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify local coordinate.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### dFluidHeight

- Specify coordinate of fluid.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iFluidHeightUnit

- Specify unit of coordinate of fluid.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iPlaneOfSymmetry1

- Specify planes of symmetry 1.
- The default value is 2.

<!-- @since:5.1.0 @optional -->
### iPlaneOfSymmetry2

- Specify planes of symmetry 2.
- The default value is 2.

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
