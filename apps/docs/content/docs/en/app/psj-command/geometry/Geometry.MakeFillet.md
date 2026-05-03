---
title: "Geometry.MakeFillet()"
description: "Create face-face fillet"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Make Fillet"
---

## Description

This method creates a smooth transition surface between two adjacent faces, which need to share at least one edge.

## Syntax

```psj
Geometry.MakeFillet(crlEdges, dRadius=1.0)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- Shared edges between adjacent faces.

### `dRadius` @type(Double) @default(1.0)

- The radius applied to the entire given edges.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.MakeFillet(crlEdges=[Edge(17, 19)])
```
