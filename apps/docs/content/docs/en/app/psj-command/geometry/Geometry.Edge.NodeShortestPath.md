---
title: "Geometry.Edge.NodeShortestPath()"
description: "Create an edge by converting the element edges on the shortest path between two nodes into edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > 2 Nodes Shortest Path"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create an edge using the shortest path between two nodes","Create an edge by converting the element edges on the shortest path between two nodes into edge"]}
   [param_removed_unexpectedly] Param 'iEnableBreakFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create an edge using the shortest path of element edges between two nodes.

## Syntax

```psj
Geometry.Edge.NodeShortestPath(...)
```

## Inputs

### `crFirstNode` @type(Cursor) @required

- The first node.

### `crSecondNode` @type(Cursor) @required

- The second node.

### `bBreakFace` @type(Boolean) @default(True) @since(5.1.0)

- Whether to break the face which the shortest edges lie on where possible.

### `iEnableBreakFace` @type(Integer) @default(1) @deprecated @until(5.1.0)

- Whether to break the target face into multiple bodies where possible. Possible values are 0 and 1.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.NodeShortestPath(crFirstNode=Node(79), 
                                               crSecondNode=Node(91), 
                                               bBreakFace=0)
JPT.Debugger(created_edges)
```
