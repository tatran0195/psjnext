---
title: "MidPlaneEdit.AddItems.Face.EFProject()"
description: "Creat new face by project edge to destination face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > AddItems > Face > EFProject"
---

## Description

Creat new face by project edge to destination face

## Syntax

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMergeFace`

- The merge face.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMergeEdge`

- The merge edge.

<!-- @since:5.0.1 @type:Double @required -->
### `dMergeEdgeAngle`

- The merge edge angle.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bMultiEF`

- The multi edge and face .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```
