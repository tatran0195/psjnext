---
title: "MeshEdit.AdjustOrientation()"
description: "Adjust the orientation (normal direction) of parts, faces, or elements."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > AdjustOrientation"
macro_link: "[GeomEditAdjustOrientation](../../macro/mesh-edit/GeomEditAdjustOrientation)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Adjust Orientation","Adjust the orientation (normal direction) of parts, faces, or elements."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Adjust the orientation (normal direction) of parts, faces, or elements.

## Syntax

```psj
MeshEdit.AdjustOrientation(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The target parts.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The target faces.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The target elements.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
MainWindow.RightClick.FlipElement(crlTargets=[Face(26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(699, 702, 684, 701)])

# Adjust orientation
MeshEdit.AdjustOrientation(crlParts=[Part(1)], crlElems=[Elem(322)])
```
