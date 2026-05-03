---
title: "MeshEdit.MoveNode.Offset()"
description: "MeshEdit MoveNode MoveNodeOffset"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > Offset"
---

## Description

MeshEdit MoveNode MoveNodeOffset

## Syntax

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```

## Inputs

### `dDeltaX` @type(Double) @default(0.0)

- The delta x.

### `dDeltaY` @type(Double) @default(0.0)

- The delta y.

### `dDeltaZ` @type(Double) @default(0.0)

- The delta z.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNodes=[])
```
