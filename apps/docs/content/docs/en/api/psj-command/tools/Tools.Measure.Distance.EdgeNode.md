---
title: "Tools.Measure.Distance.EdgeNode()"
description: "Measure Distance From Node to Edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > EdgeNode"
---

## Description

Measure Distance From Node to Edge

## Syntax

```psj
Tools.Measure.Distance.EdgeNode(crEdge, crNode, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdge`

- The edge.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode`

- The node.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A _Double_ specifying the distance between edge - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.EdgeNode(crEdge=Edge(20), crNode=Node(85), iPrecision=15)
print(dist)
```
