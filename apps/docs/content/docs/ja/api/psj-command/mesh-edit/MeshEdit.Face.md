---
title: "MeshEdit.Face()"
description: "Make Mesh deformation"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > Face"
---

## Description

Make Mesh deformation

## Syntax

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### crlFaceFixed

- Specify the face fixed.

<!-- @since:5.0.1 @optional -->
### iOffsetType

- Specify the offset type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dlOffset

- Specify the offset.
- The default value is \[1.0, 0.0, 0.0].

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDistType

- Specify the dist type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDistStrong

- Specify the dist strong.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dDistWeak

- Specify the dist weak.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### iNodeIdPick

- Specify the node ID pick.
- The default value is -1.

<!-- @since:5.0.1 @optional -->
### dlPickForMacro

- Specify the pick for macro.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```
