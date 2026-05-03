---
title: "HexModeling.Linear()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Linear"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Linear hex mesh creation","Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction.

## Syntax

```psj
HexModeling.Linear(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dLength` @type(Double) @default(10)

- The length.

### `iLayer` @type(Integer) @default(10)

- The layer.

### `vecSweepDirection` @type(Vector) @default(\[])

- The sweep direction.

### `bInterfaceElemFlag` @type(Boolean) @default(False)

- The interface element flag.

### `iLinearMethod` @type(Integer) @default(0)

- The linear method.

### `bDeleteOriginalParts` @type(Boolean) @default(False)

- The delete original parts.

### `bDeleteTargetParts` @type(Boolean) @default(False)

- The delete target parts.

### `iMethodBias` @type(Integer) @default(0)

- The method bias.

### `dFactor` @type(Double) @default(2.0)

- The factor.

### `iProgression` @type(Integer) @default(0)

- The progression.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, vecSweepDirection=[0.0, 0.0, 1.0])
```
