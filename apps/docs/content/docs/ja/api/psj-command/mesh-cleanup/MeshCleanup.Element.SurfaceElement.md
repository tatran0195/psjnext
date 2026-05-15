---
title: "MeshCleanup.Element.SurfaceElement()"
description: "Change Topology Element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Element > SurfaceElement"
---

## Description

Change Topology Element

## Syntax

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### ilElement

- Specify the element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilFace

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilPart

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iCreateNewPart

- Specify the create new part.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)
```
