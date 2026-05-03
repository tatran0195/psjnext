---
title: "HexModeling.SolidElemInterface()"
description: "make solid element interface"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > SolidElemInterface"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Make solid element interface

## Syntax

```psj
HexModeling.SolidElemInterface(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `bFlip` @type(Boolean) @default(False)

- The flip.

### `crlElms` @type(List\[Cursor]) @default(\[])

- The elms.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, iLayer=5, vecSweepDirection=[0.0, 0.0, 1.0])
HexModeling.SolidElemInterface(crlFaces=[Face(26)])
```
