---
title: "MeshEdit.MoveNode.CoincidentNodes()"
description: "Coincident Nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > CoincidentNodes"
---

## Description

Coincident Nodes

## Syntax

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `dTol` @type(Double) @default(0.01)

- The tolerance.

### `bDesOrder` @type(Boolean) @default(False)

- The des order.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.CoincidentNodes(crlNodes=[], dTol=0.01, bDesOrder=False)
```
