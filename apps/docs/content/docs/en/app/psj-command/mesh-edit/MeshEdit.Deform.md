---
title: "MeshEdit.Deform()"
description: "Deform mesh by specifying source and destination face pairs."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > Deform"
macro_link: "[GeometryDeform](../../macro/mesh-edit/GeometryDeform)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["geometry deformation","Deform mesh by specifying source and destination face pairs."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Deform mesh by specifying source and destination face pairs.

## Syntax

```psj
MeshEdit.Deform(...)
```

## Inputs

### `crlFaceSrcObverse` @type(List\[Cursor]) @default(\[])

- The source faces (obverse).

### `crlFaceDstReverse` @type(List\[Cursor]) @default(\[])

- The destination faces (reverse).

### `crlFaceSrcReverse` @type(List\[Cursor]) @default(\[])

- The source faces (reverse).

### `crlFaceDstObverse` @type(List\[Cursor]) @default(\[])

- The destination faces (obverse).

### `crlFaceFixed` @type(List\[Cursor]) @default(\[])

- The fixed faces.

### `dDistEffect` @type(Double) @default(0.02)

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
  strName="Cube_2",
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
