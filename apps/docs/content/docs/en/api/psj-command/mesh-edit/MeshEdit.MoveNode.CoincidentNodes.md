---
title: "MeshEdit.MoveNode.CoincidentNodes()"
description: "Coincident Nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > CoincidentNodes"
---

## Description

Coincident Nodes

## Syntax

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDesOrder`

- The des order.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```
