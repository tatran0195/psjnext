---
title: "Geometry.Edge.PerpendicularLineOfEdge()"
description: "Create an edge perpendicular to the line defined by two nodes in the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Perpendicular Line Of Edge"
macro _link: "[ImprintPerpendicularLine](../../macro/geometry/ImprintPerpendicularLine)"
---

## Description

Create a perpendicular edge to the line defined by two nodes in the selected facs.

## Syntax

```psj
Geometry.Edge.PerpendicularLineOfEdge(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify 2 nodes in order from the screen to determine the direction. The first node is the origin of the offset amount. The imprint line is defined perpendicular to this direction.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.0.1 @optional -->
### dOffsetDistance

- Specify the offset distance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edge.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube(iPartColor=6215639)

created _edges = Geometry.Edge.PerpendicularLineOfEdge(crlNodes=[Node(344, 339)], 
                                                     crlFaces=[Face(24, 
                                                                    22, 
                                                                    26, 
                                                                    25, 
                                                                    21, 
                                                                    23)])
JPT.Debugger(created _edges)
```
