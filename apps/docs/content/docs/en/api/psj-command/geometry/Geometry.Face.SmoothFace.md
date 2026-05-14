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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The boundary edges.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iElementGeneration`

- The element type.
  - 0: TRI
  - 1: QUAD

<!-- @since:5.1.0 @type:Double @optional @default:1 -->
### `dGradation`

- The gradation factor.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bFaceSmooth`

- The connection continuity.
  - _False_: G0
  - _True_: G1

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargetParts`

- A part that the created face belongs to. If _crlTargetParts_ is empty then creating the new part.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bInterpolation`

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

created _face = Geometry.Face.SmoothFace(crlTargets=[Edge(3)])
JPT.Debugger(created _face)
```
