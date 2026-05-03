---
title: "HexModeling.Layer()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Layer"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["sweep by layer","Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction.

## Syntax

```psj
HexModeling.Layer(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dFrontWidth` @type(Double) @default(0.0)

- The front width.

### `dBackWidth` @type(Double) @default(0.0)

- The back width.

### `iFrontLayers` @type(Integer) @default(1)

- The front layers.

### `iBackLayers` @type(Integer) @default(0)

- The back layers.

### `iBaseFaceType` @type(Integer) @default(0)

- The base face type.

### `iSeparate` @type(Integer) @default(0)

- The separate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-9}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Layer(crlFaces=[26], dFrontWidth=0.001, dBackWidth=0.0015, iFrontLayers=3, 
                iBackLayers=2, iBaseFaceType=1)
```
