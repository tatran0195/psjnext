---
title: "Geometry.Edge.PerpendicularLineToEdge()"
description: "Create an edge perpendicular to the selected edges through a specified point on the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Perpendicular Line To Edge"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create a perpendicular line on the given faces and through a specified point. The created lines can be started from the specified point or extend to the closest edge object","Create an edge perpendicular to the selected edges through a specified point on the selected faces"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create an edge perpendicular to the selected edges through a specified point on the selected faces. The created edges can be started from the specified point or extend to the closest edge.

## Syntax

```psj
Geometry.Edge.PerpendicularLineToEdge(...)
```

## Inputs

### `crNode` @type(Cursor) @default(None)

- The start node of new edge. I&#x66;_&#x62;Aut&#x6F;_&#x6F;r scale is specified, this argument is ignored.

### `crEdge` @type(Cursor) @default(None)

- The edge that the new edge should be extended up to. I&#x66;_&#x62;Aut&#x6F;_&#x6F;r scale is specified, this argument is ignored.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

### `bExtend` @type(Boolean) @default(True)

- Whether to extend the new edge through the given node up to the closest edge object.

### `bAuto` @type(Boolean) @default(False)

- Whether to specify the node and edge automatically from the pair of edges where the angle between them is equal or greater than the angl&#x65;_&#x64;LimitAngl&#x65;_&#x73;pecified. The node in-between will be selected automatically, an imprinting line will be made from that node to the opposite edge of the given faces.

### `dLimitAngle` @type(Double) @default(135.0)

- The angle in degrees to limit the angle within which Edge entities should be considered. This argument is to be used when th&#x65;_&#x62;Aut&#x6F;_&#x69;&#x73;_&#x54;rue_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cylinder()

created_edges = Geometry.Edge.PerpendicularLineToEdge(crNode=Node(250), 
                                                      crEdge=Edge(1), 
                                                      crlFaces=[Face(5)])
JPT.Debugger(created_edges)
```
