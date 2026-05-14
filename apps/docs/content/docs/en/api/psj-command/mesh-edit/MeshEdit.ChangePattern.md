---
title: "MeshEdit.ChangePattern()"
description: "Change the mesh pattern of faces."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > ChangePattern"
macro _link: "[GeomEditChangePattern](../../macro/mesh-edit/GeomEditChangePattern)"
---

## Description

Change the mesh pattern of faces.

## Syntax

```psj
MeshEdit.ChangePattern(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The target faces.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPatternType`

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
