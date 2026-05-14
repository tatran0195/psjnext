---
title: "MeshCleanup.Manual2D.Split()"
description: "manual cleanup by split"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > Split"
---

## Description

Manual cleanup by split

## Syntax

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor Pair List @required -->
### `crplElemEdge`

- The element edge.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dRatio`

- The ratio.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeRef`

- The node reference.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crProjectPart`

- The project part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```
