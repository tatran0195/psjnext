---
title: "MeshEdit.MoveNode.Absolute()"
description: "move node absolute"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > Absolute"
---

## Description

Move node absolute

## Syntax

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```

## Inputs

### `dDeltaX` @type(Double) @default(0.0)

- The delta x.

### `dDeltaY` @type(Double) @default(0.0)

- The delta y.

### `dDeltaZ` @type(Double) @default(0.0)

- The delta z.

### `b1stCoord` @type(B1ST\_COORD) @default(True)

- The coordinate.

### `b2ndCoord` @type(B2ND\_COORD) @default(True)

- The coordinate.

### `b3rdCoord` @type(B3RD\_COORD) @default(True)

- The coordinate.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNodes=[], crCoord=None)
```
