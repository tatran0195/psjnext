---
title: "MeshEdit.MoveNode.AlongCylinder()"
description: "Move node along cylinder surface"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > AlongCylinder"
---

## Description

Move node along cylinder surface

## Syntax

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dIrX`

- The direction x.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dIrY`

- The direction y.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dIrZ`

- The direction z.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dCircleX`

- The circle x.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dCircleY`

- The circle y.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dCircleZ`

- The circle z.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dRadius`

- The radius.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dHeight`

- The height.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.AlongCylinder(crlFaces=[], crlNodes=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```
