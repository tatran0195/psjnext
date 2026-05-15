---
title: "Geometry.Face.SmoothFace()"
description: "Create geometric face from given boundaries set by selected edges."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Face > SmoothFace"
macro _link: "CreateSmoothFaceGUI"
---

## Description

Create geometric face from given boundaries set by selected edges.
This function can create curved surface if selected edges are curved.

## Syntax

```psj
Geometry.Face.SmoothFace(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify boundary edges.

<!-- @since:5.1.0 @optional -->
### iElementGeneration

- Specify element type.
  - 0: TRI
  - 1: QUAD
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dGradation

- Specify gradation factor.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bFaceSmooth

- Specify connection continuity.
  - _False_: G0
  - _True_: G1
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### crlTargetParts

- Specify a part that the created face belongs to. If _crlTargetParts_ is empty then creating the new part.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bInterpolation

- Specify whether to make facet sizes or mesh sizes uniform.
- The default value is _False_.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {9}
Geometry.Part.Sphere()
Geometry.Edge.Angle(
    [CursorPair(Node(146), Node(147)), 
    CursorPair(Node(148), Node(168)), 
    CursorPair(Node(267), Node(268)), 
    CursorPair(Node(224), Node(244))])
Geometry.DeleteEntity.Face(crlFaces=[Face(2)])

created _face = Geometry.Face.SmoothFace(crlTargets=[Edge(3)])
JPT.Debugger(created _face)
```
