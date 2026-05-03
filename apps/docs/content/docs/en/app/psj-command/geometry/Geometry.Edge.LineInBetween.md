---
title: "Geometry.Edge.LineInBetween()"
description: "Create edges between two selected edges"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Edge > LineInBetween"
macro_link: ""
---

## Description

Create edges between two selected edges.

## Syntax

```psj
Geometry.Edge.LineInBetween(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The target edges.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `iNumLine` @type(Integer) @default(1)

- The number of lines.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

### `bExtend` @type(Boolean) @default(True)

- Whether to extend the offset edges to the nearest boundary edges.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6484066)

between_lines = Geometry.Edge.LineInBetween(crlEdges=[Edge(20, 18)], crlFaces=[Face(26)], numLine=2)

JPT.Debugger(between_lines)
```
