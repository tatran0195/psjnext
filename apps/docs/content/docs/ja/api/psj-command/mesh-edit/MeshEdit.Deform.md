---
title: "MeshEdit.Deform()"
description: "Deform mesh by specifying source and destination face pairs."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > Deform"
macro _link: "[GeometryDeform](../../macro/mesh-edit/GeometryDeform)"
---

## Description

Deform mesh by specifying source and destination face pairs.

## Syntax

```psj
MeshEdit.Deform(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaceSrcObverse

- Specify the source faces (obverse).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceDstReverse

- Specify the destination faces (reverse).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceSrcReverse

- Specify the source faces (reverse).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceDstObverse

- Specify the destination faces (obverse).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceFixed

- Specify the fixed faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dDistEffect

- Specify the deformation influence distance.
- The default value is 0.02.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(
  dlLength=[0.01, 0.01, 0.001],
  ilAxialNodes=[10, 10, 3],
  iPartColor=7463537
)
Geometry.Part.Cube(
  dlOrigin=[0.0, 0.0, 0.002],
  strName="Cube _2",
  iPartColor=7961077
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Deform mesh
MeshEdit.Deform(
  crlFaceSrcObverse=[Face(26)],
  crlFaceDstObverse=[Face(51)],
  crlFaceFixed=[Face(25)]
)
```
