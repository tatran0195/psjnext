---
title: "MeshEdit.MoveNode.Point()"
description: "Move node(s) to an Face(Edge) Point position"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > Point"
---

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```

## Inputs

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dX`

- The x.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dY`

- The y.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dZ`

- The z.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilNodeList`

- The node list.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```
