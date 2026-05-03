---
title: "Geometry.Face.SmoothFace()"
description: "Create geometric face from given boundaries set by selected edges."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Face > SmoothFace"
macro_link: "CreateSmoothFaceGUI"
---

## Description

Create geometric face from given boundaries set by selected edges.
This function can create curved surface if selected edges are curved.

## Syntax

```psj
Geometry.Face.SmoothFace(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- Boundary edges.

### `iElementGeneration` @type(Integer) @default(0)

- Element type.
  - 0: TRI
  - 1: QUAD

### `dGradation` @type(Double) @default(1)

- Gradation factor.

### `bFaceSmooth` @type(Boolean) @default(True)

- Connection continuity.
  - _False_: G0
  - _True_: G1

### `crlTargetParts` @type(List\[Cursor]) @default(\[])

- A part that the created face belongs to. I&#x66;_&#x63;rlTargetPart&#x73;_&#x69;s empty then creating the new part.

### `bInterpolation` @type(Boolean) @default(False)

- Whether to make facet sizes or mesh sizes uniform.

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

created_face = Geometry.Face.SmoothFace(crlTargets=[Edge(3)])
JPT.Debugger(created_face)
```
