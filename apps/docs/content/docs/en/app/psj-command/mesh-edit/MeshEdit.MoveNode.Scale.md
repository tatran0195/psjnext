---
title: "MeshEdit.MoveNode.Scale()"
description: "Move node scale"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > Scale"
---

## Description

Move node scale

## Syntax

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crlNodesOrigin` @type(List\[Cursor]) @default(\[])

- The node original.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `posDeltaXYZ` @type(Position) @default(\[10.0, 10.0, 10.0])

- The delta x y z.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Scale(crlNodes=[], crlNodesOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```
