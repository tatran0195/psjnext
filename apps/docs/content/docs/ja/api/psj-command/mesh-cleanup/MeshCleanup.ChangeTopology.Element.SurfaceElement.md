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

<!-- @since:5.0.1 @required -->
### ilElement

- Specify the element.

<!-- @since:5.0.1 @required -->
### ilFace

- Specify the face.

<!-- @since:5.0.1 @required -->
### ilPart

- Specify the part.

<!-- @since:5.0.1 @required -->
### iCreateNewPart

- Specify the create new part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement, ilFace, ilPart, iCreateNewPart)
```
