---
title: "HexModeling.Layer()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Layer"
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction.

## Syntax

```psj
HexModeling.Layer(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dFrontWidth

- Specify the front width.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dBackWidth

- Specify the back width.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFrontLayers

- Specify the front layers.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iBackLayers

- Specify the back layers.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iBaseFaceType

- Specify the base face type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSeparate

- Specify the separate.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Layer(crlFaces=[26], dFrontWidth=0.001, dBackWidth=0.0015, iFrontLayers=3, 
                iBackLayers=2, iBaseFaceType=1)
```
