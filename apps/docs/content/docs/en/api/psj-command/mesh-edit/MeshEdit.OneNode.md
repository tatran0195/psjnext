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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaceFixed`

- The face fixed.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bOffsetvector`

- The offsetvector.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 1, 0] -->
### `dlOffset`

- The offset.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dOffset`

- The offset.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDistType`

- The dist type.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dDistStrong`

- The dist strong.

<!-- @since:5.0.1 @type:Double @optional @default:20 -->
### `dDistWeak`

- The dist weak.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.OneNode(crlNodes=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDistType=0, dDistStrong=10, dDistWeak=20)
```
