---
title: "Geometry.MergeEntities.Faces()"
description: "Merge the selected faces into a single face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Merge Entities > Faces"
---

## Description

Merge the selected faces into a single face.

## Syntax

```psj
Geometry.MergeEntities.Faces(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The faces using for merging.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMergeEdge`

- Whether to merge edges between faces to be a continuously edges or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRemoveNonBoundEdge`

- Whether to remove the edges which are not a boundary edge.

## Return Code

A _List of Cursor_ specifying a list of faces after executing the function.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Geometry.Edge.Line(dllPoints=[[0.005, 0, 0.01],
                              [0.006, 0.01, 0.01]],
                   crlFaces=[Face(26)])
Geometry.Edge.Line(dllPoints=[[0.002, 0.002, 0.01],
                              [0.003, 0.005, 0.01]],
                   crlFaces=[Face(26)])
merged _faces = Geometry.MergeEntities.Faces(crlFaces=[Face(26, 28)])
JPT.Debugger(merged _faces)
```
