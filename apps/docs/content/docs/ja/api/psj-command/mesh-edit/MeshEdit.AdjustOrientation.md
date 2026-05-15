---
title: "MeshEdit.AdjustOrientation()"
description: "Adjust the orientation (normal direction) of parts, faces, or elements."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > AdjustOrientation"
macro _link: "[GeomEditAdjustOrientation](../../macro/mesh-edit/GeomEditAdjustOrientation)"
---

## Description

Adjust the orientation (normal direction) of parts, faces, or elements.

## Syntax

```psj
MeshEdit.AdjustOrientation(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the target parts.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the target faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the target elements.
- The default value is \[].

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
