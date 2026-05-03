---
title: "MeshEdit.SurfaceMesh()"
description: "Command for converting solid mesh of specified parts to surface mesh."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > SurfaceMesh"
macro_link: "[ElementConv_Surface](../../macro/mesh-edit/ElementConv_Surface)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Element Conversion","Command for converting solid mesh of specified parts to surface mesh."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Command for converting solid mesh of specified parts to surface mesh.

## Syntax

```psj
MeshEdit.SurfaceMesh(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The target parts.

### `iType` @type(Integer) @default(1)

- The surface element conversion type.
  - 0: To Linear (Tri3/Quad4)
  - 1: To Quadratic (Tri6/Quad8)
  - 2: Tri3
  - 7: Split (Tri6to4Tri3s/Quad8to4Quad4s)

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
Meshing.AdjustCircleVertex(
  crlParts=[Part(1)],
  bInModeSurfaceMesh=True
)
Meshing.SetMeshAttribute(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  )
)
Meshing.SurfaceMeshing(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  ),
  iThreadNum=16
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Quad8
MeshEdit.SurfaceMesh(crlParts=[Part(1)])
```
