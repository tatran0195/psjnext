---
title: "Geometry.Edge.PerpendicularLineOfEdge()"
description: "Create an edge perpendicular to the line defined by two nodes in the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Perpendicular Line Of Edge"
macro_link: "[ImprintPerpendicularLine](../../macro/geometry/ImprintPerpendicularLine)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create a perpendicular edge through a line defined by two nodes. The first selected node will be start point of new line","Create an edge perpendicular to the line defined by two nodes in the selected faces"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a perpendicular edge to the line defined by two nodes in the selected facs.

## Syntax

```psj
Geometry.Edge.PerpendicularLineOfEdge(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- 2 nodes in order from the screen to determine the direction. The first node is the origin of the offset amount. The imprint line is defined perpendicular to this direction.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `dOffsetDistance` @type(Double) @default(0)

- The offset distance.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edge.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.PerpendicularLineOfEdge(crlNodes=[Node(344, 339)], 
                                                     crlFaces=[Face(24, 
                                                                    22, 
                                                                    26, 
                                                                    25, 
                                                                    21, 
                                                                    23)])
JPT.Debugger(created_edges)
```
