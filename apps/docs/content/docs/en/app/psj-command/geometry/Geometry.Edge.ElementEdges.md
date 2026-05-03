---
title: "Geometry.Edge.ElementEdges()"
description: "Create edges from the selected element edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Element Edges"
macro_link: "[CreateEdgeByElemEdge](../../macro/geometry/CreateEdgeByElemEdge)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create edges by selecting individual element edges","Create edges from the selected element edges"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create edges from the selected element edges.

## Syntax

```psj
Geometry.Edge.ElementEdges(...)
```

## Inputs

### `crplElemEdges` @type(List\[Pairs of Cursor]) @required

- The element edges to be converted to edge.

### `bBreakEdge` @type(Boolean) @default(True)

- Whether to break the faces which the given element edges lie on where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_edges = Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(443), Node(452)), 
                                                          CursorPair(Node(444), Node(445)), 
                                                          CursorPair(Node(454), Node(463))])
JPT.Debugger(created_edges)
```
