---
title: "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge()"
description: "Create new face by extend free edge to a destination face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > AddItems > Face > EFExtendFreeEdge"
---

## Description

Create new face by extend free edge to a destination face

## Syntax

```psj
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdges, crlFaces, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
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

<!-- @since:5.0.1 @type:Boolean @required -->
### `bUseNeighDir`

- The use neighborhood edge direction.

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
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdges, crlFaces, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
```
