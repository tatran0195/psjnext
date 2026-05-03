---
title: "MeshEdit.MoveNode.MoveNodeOffset()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > MoveNodeOffset"
---

## Description

Unknown Description

## Syntax

```psj
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNodes, crCoord)
```

## Inputs

### `dDeltaX` @type(Double) @required

- The delta x.

### `dDeltaY` @type(Double) @required

- The delta y.

### `dDeltaZ` @type(Double) @required

- The delta z.

### `crlNodes` @type(List\[Cursor]) @required

- The node.

### `crCoord` @type(Cursor) @required

- The coordinate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNodes, crCoord)
```
