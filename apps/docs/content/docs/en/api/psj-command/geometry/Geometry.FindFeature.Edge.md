---
title: "Geometry.FindFeature.Edge()"
description: "Find and select the specific edges according to their characteristic"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Find Feature > Edges"
---

## Description

Find and select the specific edges according to their characteristic.

## Syntax

```psj
Geometry.FindFeature.Edge(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to find the specific faces. This argument must be specified if the _iEdgeType_ argument value is not equal to 4.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEdgeType`

- The specified type of Edges.
  - If _iEdgeType=0_, find and select the straight edge lines.
  - If _iEdgeType=1_, find and select the edges that form a closed profile.
  - If _iEdgeType=2_, find and select the edges of circular shape.
  - If _iEdgeType=3_, find and select the edges of semi-circular shape.
  - If _iEdgeType=4_, find and select the edges of bolt hole.
  - If _iEdgeType=5_, find and select the concentric edge of the specified edge.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdges`

- The edges used to find the their concentric edges. This argument must be specified if _iEdgeType=5_.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dDiameterMin`

- The minimum diameter of bolt hole.

<!-- @since:5.0.1 @type:Double @optional @default:2.0 -->
### `dDiameterMax`

- The maximum diameter of bolt hole.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The faces used to find the edges of bolt hole. This argument is to be used if _iEdgeType=4_.

## Return Code

A _List Cursor_ of edges if success, or _None_ if fail.

## Sample Code

```psj {2}
cube=Geometry.Part.Cube()
edges = Geometry.FindFeature.Edge(crlParts=[cube])
JPT.Debugger(edges)
```
