---
title: "MidPlaneEdit.AddItems.Face.EFProject()"
description: "Creat new face by project edge to destination face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > AddItems > Face > EFProject"
---

## Description

Creat new face by project edge to destination face

## Syntax

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `bMergeFace` @type(Boolean) @required

- The merge face.

### `bMergeEdge` @type(Boolean) @required

- The merge edge.

### `dMergeEdgeAngle` @type(Double) @required

- The merge edge angle.

### `bMultiEF` @type(Boolean) @required

- The multi edge and face .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFProject(crlEdges, crlFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
```
