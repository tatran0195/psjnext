---
title: "Geometry.FindFeature.Edge()"
description: "Find and select the specific edges according to their characteristic"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Find Feature > Edges"
---

## Description

Find and select the specific edges according to their characteristic.

## Syntax

```psj
Geometry.FindFeature.Edge(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to find the specific faces. This argument must be specified if th&#x65;_&#x69;EdgeTyp&#x65;_&#x61;rgument value is not equal to 4.

### `iEdgeType` @type(Integer) @default(0)

- The specified type of Edges.
  - I&#x66;_&#x69;EdgeType=0_, find and select the straight edge lines.
  - I&#x66;_&#x69;EdgeType=1_, find and select the edges that form a closed profile.
  - I&#x66;_&#x69;EdgeType=2_, find and select the edges of circular shape.
  - I&#x66;_&#x69;EdgeType=3_, find and select the edges of semi-circular shape.
  - I&#x66;_&#x69;EdgeType=4_, find and select the edges of bolt hole.
  - I&#x66;_&#x69;EdgeType=5_, find and select the concentric edge of the specified edge.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edges used to find the their concentric edges. This argument must be specified i&#x66;_&#x69;EdgeType=5_.

### `dDiameterMin` @type(Double) @default(1.0)

- The minimum diameter of bolt hole.

### `dDiameterMax` @type(Double) @default(2.0)

- The maximum diameter of bolt hole.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The faces used to find the edges of bolt hole. This argument is to be used i&#x66;_&#x69;EdgeType=4_.

## Return Code

A _List Cursor_ of edges if success, or _None_ if fail.

## Sample Code

```psj {2}
cube=Geometry.Part.Cube()
edges = Geometry.FindFeature.Edge(crlParts=[cube])
JPT.Debugger(edges)
```
