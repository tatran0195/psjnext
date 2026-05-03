---
title: "MeshEdit.MoveNode.Point()"
description: "Move node(s) to an Face(Edge) Point position"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > Point"
---

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```

## Inputs

### `dX` @type(Double) @default(0.0)

- The x.

### `dY` @type(Double) @default(0.0)

- The y.

### `dZ` @type(Double) @default(0.0)

- The z.

### `ilNodeList` @type(List\[Integer]) @default(\[])

- The node list.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```
