---
title: "MeshEdit.MoveNode.MoveNodeOffset()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > MoveNodeOffset"
---

## Description

Unknown Description

## Syntax

```psj
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNodes, crCoord)
```

## Inputs

<!-- @since:5.0.1 @type:Double @required -->
### `dDeltaX`

- The delta x.

<!-- @since:5.0.1 @type:Double @required -->
### `dDeltaY`

- The delta y.

<!-- @since:5.0.1 @type:Double @required -->
### `dDeltaZ`

- The delta z.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crCoord`

- The coordinate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNodes, crCoord)
```
