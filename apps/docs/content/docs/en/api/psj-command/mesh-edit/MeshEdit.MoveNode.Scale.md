---
title: "MeshEdit.MoveNode.Scale()"
description: "Move node scale"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Scale"
---

## Description

Move node scale

## Syntax

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodesOrigin`

- The node original.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Position @optional @default:[10.0, 10.0, 10.0] -->
### `posDeltaXYZ`

- The delta x y z.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```
