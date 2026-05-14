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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceMove`

- The face move.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceFixed`

- The face fixed.

<!-- @since:5.0.1 @type:Double @optional @default:3.00 -->
### `dMove`

- The move.

<!-- @since:5.0.1 @type:Double @optional @default:10.00 -->
### `dDistStrong`

- The dist strong.

<!-- @since:5.0.1 @type:Double @optional @default:20.00 -->
### `dDistWeak`

- The dist weak.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```
