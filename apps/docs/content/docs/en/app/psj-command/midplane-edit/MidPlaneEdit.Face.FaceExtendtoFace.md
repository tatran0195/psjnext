---
title: "MidPlaneEdit.Face.FaceExtendtoFace()"
description: "add face by face extend to face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > Face > FaceExtendtoFace"
---

## Description

Add face by face extend to face

## Syntax

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```

## Inputs

### `crlExtFaces` @type(List\[Cursor]) @required

- The extend faces.

### `crlRefFaces` @type(List\[Cursor]) @required

- The reference faces.

### `bMergeFace` @type(Boolean) @required

- The merge face.

### `bMergeEdge` @type(Boolean) @required

- The merge edge.

### `dMergeEdgeAngle` @type(Double) @required

- The merge edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```
