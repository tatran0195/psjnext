---
title: "MeshEdit.MoveNode.Absolute()"
description: "move node absolute"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Absolute"
---

## Description

Move node absolute

## Syntax

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
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

<!-- @since:5.0.1 @type:B1ST _COORD @optional @default:True -->
### `b1stCoord`

- The coordinate.

<!-- @since:5.0.1 @type:B2ND _COORD @optional @default:True -->
### `b2ndCoord`

- The coordinate.

<!-- @since:5.0.1 @type:B3RD _COORD @optional @default:True -->
### `b3rdCoord`

- The coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```
