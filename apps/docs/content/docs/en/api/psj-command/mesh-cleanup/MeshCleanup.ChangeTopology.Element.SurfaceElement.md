---
title: "MeshCleanup.ChangeTopology.Element.SurfaceElement()"
description: "Assign the selected element to a different part."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > ChangeTopology > Element > SurfaceElement"
---

## Description

Assign the selected element to a different part.

## Syntax

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```

## Inputs

<!-- @since:5.0.1 @type:List[Integer] @required -->
### `ilElement`

- The element.

<!-- @since:5.0.1 @type:List[Integer] @required -->
### `ilFace`

- The face.

<!-- @since:5.0.1 @type:List[Integer] @required -->
### `ilPart`

- The part.

<!-- @since:5.0.1 @type:Integer @required -->
### `iCreateNewPart`

- The create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```
