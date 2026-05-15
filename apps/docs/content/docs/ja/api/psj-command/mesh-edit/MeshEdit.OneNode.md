---
title: "MeshEdit.OneNode()"
description: "morphing one node"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > OneNode"
---

## Description

Morphing one node

## Syntax

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceFixed

- Specify the face fixed.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bOffsetvector

- Specify the offsetvector.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dlOffset

- Specify the offset.
- The default value is \[0, 1, 0].

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset.
- The default value is 1.0.

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

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```
