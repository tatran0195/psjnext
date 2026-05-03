---
title: "MeshEdit.ChangePattern()"
description: "Change the mesh pattern of faces."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > ChangePattern"
macro_link: "[GeomEditChangePattern](../../macro/mesh-edit/GeomEditChangePattern)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Element ChangePattern","Change the mesh pattern of faces."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Change the mesh pattern of faces.

## Syntax

```psj
MeshEdit.ChangePattern(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The target faces.

### `iPatternType` @type(Integer) @default(0)

- The pattern type.
  - 0: Standard
  - 1: Union Jack

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
JPT.Exec('ViewShowMesh(1)')
JPT.ViewFitToModel()

# Change pattern
MeshEdit.ChangePattern(crlFaces=[Face(22)], iPatternType=1)
```
