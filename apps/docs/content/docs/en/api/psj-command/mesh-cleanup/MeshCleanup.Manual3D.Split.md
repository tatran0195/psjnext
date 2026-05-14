---
title: "MeshCleanup.Manual3D.Split()"
description: "Merge two Quad elements into one Quad element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > Split"
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor Pair List @required -->
### `crplElemEdge`

- The element edge.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Double @optional @default:0.5 -->
### `dRatioDistance`

- The ratio distance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```
