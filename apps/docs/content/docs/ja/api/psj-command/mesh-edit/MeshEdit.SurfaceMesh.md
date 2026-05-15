---
title: "MeshEdit.SurfaceMesh()"
description: "Command for converting solid mesh of specified parts to surface mesh."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > SurfaceMesh"
macro _link: "[ElementConv _Surface](../../macro/mesh-edit/ElementConv _Surface)"
---

## Description

Command for converting solid mesh of specified parts to surface mesh.

## Syntax

```psj
MeshEdit.SurfaceMesh(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the target parts.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iType

- Specify the surface element conversion type.
  - 0: To Linear (Tri3/Quad4)
  - 1: To Quadratic (Tri6/Quad8)
  - 2: Tri3
  - 7: Split (Tri6to4Tri3s/Quad8to4Quad4s)
- The default value is 1.

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
  surfaceMesh=SURFACE _MESH(
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
  surfaceMesh=SURFACE _MESH(
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
