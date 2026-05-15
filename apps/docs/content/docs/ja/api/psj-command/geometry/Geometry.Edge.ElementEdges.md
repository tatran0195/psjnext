---
title: "Geometry.Edge.ElementEdges()"
description: "Create edges from the selected element edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Element Edges"
macro _link: "[CreateEdgeByElemEdge](../../macro/geometry/CreateEdgeByElemEdge)"
---

## Description

Create edges from the selected element edges.

## Syntax

```psj
Geometry.Edge.ElementEdges(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crplElemEdges

- Specify the element edges to be converted to edge.

<!-- @since:5.0.1 @optional -->
### bBreakEdge

- Specify whether to break the faces which the given element edges lie on where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _edges = Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(443), Node(452)), 
                                                          CursorPair(Node(444), Node(445)), 
                                                          CursorPair(Node(454), Node(463))])
JPT.Debugger(created _edges)
```
