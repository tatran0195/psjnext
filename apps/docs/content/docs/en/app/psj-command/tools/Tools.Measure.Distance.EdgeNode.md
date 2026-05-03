---
title: "Tools.Measure.Distance.EdgeNode()"
description: "Measure Distance From Node to Edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > EdgeNode"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure Distance From Node to Edge

## Syntax

```psj
Tools.Measure.Distance.EdgeNode(crEdge, crNode, iPrecision=6)
```

## Inputs

### `crEdge` @type(Cursor) @required

- The edge.

### `crNode` @type(Cursor) @required

- The node.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A _Double_ specifying the distance between edge - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.EdgeNode(crEdge=Edge(20), crNode=Node(85), iPrecision=15)
print(dist)
```
