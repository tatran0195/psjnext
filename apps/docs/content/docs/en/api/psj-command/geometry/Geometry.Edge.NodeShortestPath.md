---
title: "Geometry.Edge.NodeShortestPath()"
description: "Create an edge by converting the element edges on the shortest path between two nodes into edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > 2 Nodes Shortest Path"
---

## Description

Create an edge using the shortest path of element edges between two nodes.

## Syntax

```psj
Geometry.Edge.NodeShortestPath(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crFirstNode`

- The first node.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crSecondNode`

- The second node.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the face which the shortest edges lie on where possible.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableBreakFace`

- Whether to break the target face into multiple bodies where possible. Possible values are 0 and 1.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube(iPartColor=6215639)

created _edges = Geometry.Edge.NodeShortestPath(crFirstNode=Node(79), 
                                               crSecondNode=Node(91), 
                                               bBreakFace=0)
JPT.Debugger(created _edges)
```
