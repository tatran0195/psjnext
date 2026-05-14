---
title: "Geometry.Edge.LineInBetween()"
description: "Create edges between two selected edges"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Edge > LineInBetween"
macro _link: ""
---

## Description

Create edges between two selected edges.

## Syntax

```psj
Geometry.Edge.LineInBetween(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlEdges`

- The target edges.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlFaces`

- The target faces on which the edges are imprinted.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iNumLine`

- The number of lines.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the given faces where possible.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bExtend`

- Whether to extend the offset edges to the nearest boundary edges.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6484066)

between _lines = Geometry.Edge.LineInBetween(crlEdges=[Edge(20, 18)], crlFaces=[Face(26)], numLine=2)

JPT.Debugger(between _lines)
```
