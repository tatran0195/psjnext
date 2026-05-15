---
title: "MidPlaneEdit.Face.FaceExtendtoFace()"
description: "add face by face extend to face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > Face > FaceExtendtoFace"
---

## Description

Add face by face extend to face

## Syntax

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlExtFaces

- Specify the extend faces.

<!-- @since:5.0.1 @required -->
### crlRefFaces

- Specify the reference faces.

<!-- @since:5.0.1 @required -->
### bMergeFace

- Specify the merge face.

<!-- @since:5.0.1 @required -->
### bMergeEdge

- Specify the merge edge.

<!-- @since:5.0.1 @required -->
### dMergeEdgeAngle

- Specify the merge edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.FaceExtendtoFace(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
```
