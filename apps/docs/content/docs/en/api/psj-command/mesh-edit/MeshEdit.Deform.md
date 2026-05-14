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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceSrcObverse`

- The source faces (obverse).

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceDstReverse`

- The destination faces (reverse).

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceSrcReverse`

- The source faces (reverse).

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceDstObverse`

- The destination faces (obverse).

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceFixed`

- The fixed faces.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dDistEffect`

- The deformation influence distance.

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
