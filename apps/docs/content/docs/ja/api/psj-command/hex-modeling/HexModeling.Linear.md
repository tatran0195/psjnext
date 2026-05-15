---
title: "HexModeling.Linear()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Linear"
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction.

## Syntax

```psj
HexModeling.Linear(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dLength

- Specify the length.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the layer.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### vecSweepDirection

- Specify the sweep direction.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bInterfaceElemFlag

- Specify the interface element flag.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iLinearMethod

- Specify the linear method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bDeleteOriginalParts

- Specify the delete original parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bDeleteTargetParts

- Specify the delete target parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iMethodBias

- Specify the method bias.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFactor

- Specify the factor.
- The default value is 2.0.

<!-- @since:5.0.1 @optional -->
### iProgression

- Specify the progression.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, vecSweepDirection=[0.0, 0.0, 1.0])
```
