---
title: "Geometry.Face.FourEdges()"
description: "Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Face > Edges2 (4 Edges)"
macro _link: "[CreateFaceFromFourEdges](../../macro/geometry/CreateFaceFromFourEdges)"
---

## Description

Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops.

## Syntax

```psj
Geometry.Face.FourEdges(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify four edges that bound the new face. The edges must form a closed profile and must not contain multiple loops.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {5}
Geometry.Part.Cube()

Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

created _face = Geometry.Face.FourEdges(crlEdges=[Edge(17, 18, 19, 20)])

JPT.Debugger(created _face)
```
