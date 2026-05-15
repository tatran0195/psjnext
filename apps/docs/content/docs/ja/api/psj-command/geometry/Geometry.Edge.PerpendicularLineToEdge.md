---
title: "Geometry.Edge.PerpendicularLineToEdge()"
description: "Create an edge perpendicular to the selected edges through a specified point on the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Perpendicular Line To Edge"
---

## Description

Create an edge perpendicular to the selected edges through a specified point on the selected faces. The created edges can be started from the specified point or extend to the closest edge.

## Syntax

```psj
Geometry.Edge.PerpendicularLineToEdge(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crNode

- Specify the start node of new edge. If _bAuto_ or scale is specified, this argument is ignored.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crEdge

- Specify the edge that the new edge should be extended up to. If _bAuto_ or scale is specified, this argument is ignored.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bExtend

- Specify whether to extend the new edge through the given node up to the closest edge object.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bAuto

- Specify whether to specify the node and edge automatically from the pair of edges where the angle between them is equal or greater than the angle _dLimitAngle_ specified. The node in-between will be selected automatically, an imprinting line will be made from that node to the opposite edge of the given faces.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dLimitAngle

- Specify the angle in degrees to limit the angle within which Edge entities should be considered. This argument is to be used when the _bAuto_ is _True_.
- The default value is 135.0.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cylinder()

created _edges = Geometry.Edge.PerpendicularLineToEdge(crNode=Node(250), 
                                                      crEdge=Edge(1), 
                                                      crlFaces=[Face(5)])
JPT.Debugger(created _edges)
```
