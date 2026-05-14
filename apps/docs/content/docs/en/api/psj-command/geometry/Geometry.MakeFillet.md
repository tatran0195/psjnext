---
title: "Geometry.MakeFillet()"
description: "Create face-face fillet"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Make Fillet"
---

## Description

This method creates a smooth transition surface between two adjacent faces, which need to share at least one edge.

## Syntax

```psj
Geometry.MakeFillet(crlEdges, dRadius=1.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The shared edges between adjacent faces.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dRadius`

- The radius applied to the entire given edges.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.MakeFillet(crlEdges=[Edge(17, 19)])
```
