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

<!-- @since:5.1.0 @required -->
### crlEdges

- Specify the target edges.

<!-- @since:5.1.0 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.1.0 @optional -->
### iNumLine

- Specify the number of lines.
- The default value is 1

<!-- @since:5.1.0 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bExtend

- Specify whether to extend the offset edges to the nearest boundary edges.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6484066)

between _lines = Geometry.Edge.LineInBetween(crlEdges=[Edge(20, 18)], crlFaces=[Face(26)], numLine=2)

JPT.Debugger(between _lines)
```
