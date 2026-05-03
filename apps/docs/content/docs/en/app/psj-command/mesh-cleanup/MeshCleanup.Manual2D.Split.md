---
title: "MeshCleanup.Manual2D.Split()"
description: "manual cleanup by split"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > Split"
---

## Description

Manual cleanup by split

## Syntax

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```

## Inputs

### `crplElemEdge` @type(Cursor Pair List) @required

- The element edge.

### `dRatio` @type(Double) @default(0.0)

- The ratio.

### `crNodeRef` @type(Cursor) @default(None)

- The node reference.

### `crProjectPart` @type(Cursor) @default(None)

- The project part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```
