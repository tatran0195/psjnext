---
title: "HexModeling.SolidElemInterface()"
description: "make solid element interface"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > SolidElemInterface"
---

## Description

Make solid element interface

## Syntax

```psj
HexModeling.SolidElemInterface(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bFlip

- Specify the flip.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlElms

- Specify the elms.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, iLayer=5, vecSweepDirection=[0.0, 0.0, 1.0])
HexModeling.SolidElemInterface(crlFaces=[Face(26)])
```
