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
### dMergeEdgeAngle

- Specify the merge edge angle.

<!-- @since:5.0.1 @required -->
### bMultiEF

- Specify the multi edge and face .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```
