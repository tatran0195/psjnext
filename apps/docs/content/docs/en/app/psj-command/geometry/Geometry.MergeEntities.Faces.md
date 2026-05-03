---
title: "Geometry.MergeEntities.Faces()"
description: "Merge the selected faces into a single face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Merge Entities > Faces"
---

## Description

Merge the selected faces into a single face.

## Syntax

```psj
Geometry.MergeEntities.Faces(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The faces using for merging.

### `bMergeEdge` @type(Boolean) @default(True)

- Whether to merge edges between faces to be a continuously edges or not.

### `bRemoveNonBoundEdge` @type(Boolean) @default(True)

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
merged_faces = Geometry.MergeEntities.Faces(crlFaces=[Face(26, 28)])
JPT.Debugger(merged_faces)
```
