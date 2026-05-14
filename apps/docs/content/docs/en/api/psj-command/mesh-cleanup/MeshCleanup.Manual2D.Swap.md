---
title: "MeshCleanup.Manual2D.Swap()"
description: "Swap Element Edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > Swap"
---

## Description

Swap Element Edge

## Syntax

```psj
MeshCleanup.Manual2D.Swap(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplElemEdge`

- The element edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3}
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

MeshCleanup.Manual2D.Swap(crplElemEdge=[CursorPair(Node(17), Node(18))])
```
