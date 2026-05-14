---
title: "MeshEdit.MoveNode.Offset()"
description: "MeshEdit MoveNode MoveNodeOffset"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Offset"
---

## Description

MeshEdit MoveNode MoveNodeOffset

## Syntax

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDeltaX`

- The delta x.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDeltaY`

- The delta y.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDeltaZ`

- The delta z.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```
