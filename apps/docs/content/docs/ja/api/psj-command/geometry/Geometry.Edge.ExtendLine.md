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

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edge to be extended.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the extend method.
  - If _iMethod = 0_, following the direction of the last segments of the given Edge.
  - If _iMethod = 1_, attempting to retain the curvature direction of the given Edge.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnd

- Specify the end position to extend the edge.
  - If _iEnd=0_, extend from its endpoints to the closest edge.
  - If _iEnd=1_, extend the given edge to boundary edges.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNoFittingPoints

- Specify number of fitting points. This argument is to be used when the _iMethod=1_.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### iDiv

- Specify division segments. This argument is to be used when the _iMethod=1_.
- The default value is 2.

<!-- @since:5.1.0 @optional -->
### bBreakFace

- Specify whether to break the face which the given edge lies on where possible.
- The default value is _True_.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEnableBreakFace

- Specify whether to break the face which the given edge lies on. Possible values are 0 and 1.
- The default value is 1.

## Return Code

A _List of Cursor_ specifying the extended edges.?

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6215639)

Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(453), Node(461))])

extended _edges = Geometry.Edge.ExtendLine(crlEdges=[Edge(27)], iEnd=1)

JPT.Debugger(extended _edges)
```
