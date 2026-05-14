---
title: "Geometry.Edge.ExtendLine()"
description: "Extend the specified edges to the specified boundary"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Extend Line"
macro _link: "[ImprintExtendLine](../../macro/geometry/ImprintExtendLine)"
---

## Description

Extend the specified edges to the specified boundary.

## Syntax

```psj
Geometry.Edge.ExtendLine(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edge to be extended.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The extend method.
  - If _iMethod = 0_, following the direction of the last segments of the given Edge.
  - If _iMethod = 1_, attempting to retain the curvature direction of the given Edge.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnd`

- The end position to extend the edge.
  - If _iEnd=0_, extend from its endpoints to the closest edge.
  - If _iEnd=1_, extend the given edge to boundary edges.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iNoFittingPoints`

- The number of fitting points. This argument is to be used when the _iMethod=1_.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iDiv`

- The division segments. This argument is to be used when the _iMethod=1_.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the face which the given edge lies on where possible.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableBreakFace`

- Whether to break the face which the given edge lies on. Possible values are 0 and 1.

## Return Code

A _List of Cursor_ specifying the extended edges.?

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6215639)

Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(453), Node(461))])

extended _edges = Geometry.Edge.ExtendLine(crlEdges=[Edge(27)], iEnd=1)

JPT.Debugger(extended _edges)
```
