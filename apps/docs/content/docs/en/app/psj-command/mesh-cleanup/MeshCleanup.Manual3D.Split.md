---
title: "MeshCleanup.Manual3D.Split()"
description: "Merge two Quad elements into one Quad element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > Split"
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```

## Inputs

### `crplElemEdge` @type(Cursor Pair List) @required

- The element edge.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `dRatioDistance` @type(Double) @default(0.5)

- The ratio distance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Split(crplElemEdge, crlNodes=[], dRatioDistance=0.5)
```
