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

<!-- @since:5.0.1 @required -->
### crEdge

- Specify the edge.

<!-- @since:5.0.1 @required -->
### crNode

- Specify the node.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between edge - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.EdgeNode(crEdge=Edge(20), crNode=Node(85), iPrecision=15)
print(dist)
```
