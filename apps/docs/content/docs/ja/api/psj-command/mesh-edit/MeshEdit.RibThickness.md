---
title: "MeshEdit.RibThickness()"
description: "Mesh Edit Morphing Rib Thickness"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > RibThickness"
---

## Description

Mesh Edit Morphing Rib Thickness

## Syntax

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaceMove

- Specify the face move.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaceFixed

- Specify the face fixed.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMove

- Specify the move.
- The default value is 3.00.

<!-- @since:5.0.1 @optional -->
### dDistStrong

- Specify the dist strong.
- The default value is 10.00.

<!-- @since:5.0.1 @optional -->
### dDistWeak

- Specify the dist weak.
- The default value is 20.00.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```
