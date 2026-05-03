---
title: "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge()"
description: "Create new face by extend free edge to a destination face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > AddItems > Face > EFExtendFreeEdge"
---

## Description

Create new face by extend free edge to a destination face

## Syntax

```psj
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdges, crlFaces, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
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

### `bUseNeighDir` @type(Boolean) @required

- The use neighborhood edge direction.

### `dMergeEdgeAngle` @type(Double) @required

- The merge edge angle.

### `bMultiEF` @type(Boolean) @required

- The multi edge and face .

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.AddItems.Face.EFExtendFreeEdge(crlEdges, crlFaces, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
```
