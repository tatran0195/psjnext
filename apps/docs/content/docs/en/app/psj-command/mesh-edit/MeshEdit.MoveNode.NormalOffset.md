---
title: "MeshEdit.MoveNode.NormalOffset()"
description: "Move node(s) in Normal Direction of plane"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > NormalOffset"
---

## Description

Move node(s) in Normal Direction of plane

## Syntax

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```

## Inputs

### `dMagnitude` @type(Double) @default(0.0)

- The magnitude.

### `ilNodeList` @type(List\[Integer]) @default(\[])

- The node list.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```
