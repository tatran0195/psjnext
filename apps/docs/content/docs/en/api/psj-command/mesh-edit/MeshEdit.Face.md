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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaceFixed`

- The face fixed.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOffsetType`

- The offset type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Double List @optional @default:[1.0, 0.0, 0.0] -->
### `dlOffset`

- The offset.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
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

<!-- @since:5.0.1 @type:Integer @optional @default:-1 -->
### `iNodeIdPick`

- The node ID pick.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlPickForMacro`

- The pick for macro.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.Face(crlFaces, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])
```
