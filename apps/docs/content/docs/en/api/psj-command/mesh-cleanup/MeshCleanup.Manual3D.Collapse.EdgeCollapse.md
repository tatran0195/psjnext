---
title: "MeshCleanup.Manual3D.Collapse.EdgeCollapse()"
description: "collapse"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > Collapse > EdgeCollapse"
---

## Description

Collapse

## Syntax

```psj
MeshCleanup.Manual3D.Collapse.EdgeCollapse(crplElemEdge=[], crlNodes=[])
```

## Inputs

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplElemEdge`

- The element edge.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Collapse.EdgeCollapse(crplElemEdge=[], crlNodes=[])
```
