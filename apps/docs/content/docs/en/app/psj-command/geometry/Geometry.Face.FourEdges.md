---
title: "Geometry.Face.FourEdges()"
description: "Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Face > Edges2 (4 Edges)"
macro_link: "[CreateFaceFromFourEdges](../../macro/geometry/CreateFaceFromFourEdges)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops.

## Syntax

```psj
Geometry.Face.FourEdges(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- Four edges that bound the new face. The edges must form a closed profile and must not contain multiple loops.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {5}
Geometry.Part.Cube()

Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

created_face = Geometry.Face.FourEdges(crlEdges=[Edge(17, 18, 19, 20)])

JPT.Debugger(created_face)
```
