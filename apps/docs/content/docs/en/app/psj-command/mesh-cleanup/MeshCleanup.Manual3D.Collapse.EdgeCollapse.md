---
title: "MeshCleanup.Manual3D.Collapse.EdgeCollapse()"
description: "collapse"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > Collapse > EdgeCollapse"
---

## Description

Collapse

## Syntax

```psj
MeshCleanup.Manual3D.Collapse.EdgeCollapse(crplElemEdge=[], crlNodes=[])
```

## Inputs

### `crplElemEdge` @type(Cursor Pair List) @default(\[])

- The element edge.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.Collapse.EdgeCollapse(crplElemEdge=[], crlNodes=[])
```
