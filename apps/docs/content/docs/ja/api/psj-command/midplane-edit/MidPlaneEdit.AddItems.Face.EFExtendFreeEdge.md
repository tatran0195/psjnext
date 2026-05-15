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

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edge.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### bMergeFace

- Specify the merge face.

<!-- @since:5.0.1 @required -->
### bMergeEdge

- Specify the merge edge.

<!-- @since:5.0.1 @required -->
### bUseNeighDir

- Specify the use neighborhood edge direction.

<!-- @since:5.0.1 @required -->
### dMergeEdgeAngle

- Specify the merge edge angle.

<!-- @since:5.0.1 @required -->
### bMultiEF

- Specify the multi edge and face .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdges, crlFaces, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
```
