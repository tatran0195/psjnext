---
title: "Geometry.Edge.ExtendLine()"
description: "Extend the specified edges to the specified boundary"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Extend Line"
macro_link: "[ImprintExtendLine](../../macro/geometry/ImprintExtendLine)"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'iEnableBreakFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Extend the specified edges to the specified boundary.

## Syntax

```psj
Geometry.Edge.ExtendLine(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edge to be extended.

### `iMethod` @type(Integer) @default(0)

- The extend method.
  - I&#x66;_&#x69;Method = 0_, following the direction of the last segments of the given Edge.
  - I&#x66;_&#x69;Method = 1_, attempting to retain the curvature direction of the given Edge.

### `iEnd` @type(Integer) @default(0)

- The end position to extend the edge.
  - I&#x66;_&#x69;End=0_, extend from its endpoints to the closest edge.
  - I&#x66;_&#x69;End=1_, extend the given edge to boundary edges.

### `iNoFittingPoints` @type(Integer) @default(3)

- Number of fitting points. This argument is to be used when th&#x65;_&#x69;Method=1_.

### `iDiv` @type(Integer) @default(2)

- Division segments. This argument is to be used when th&#x65;_&#x69;Method=1_.

### `bBreakFace` @type(Boolean) @default(True) @since(5.1.0)

- Whether to break the face which the given edge lies on where possible.

### `iEnableBreakFace` @type(Integer) @default(1) @deprecated @until(5.1.0)

- Whether to break the face which the given edge lies on. Possible values are 0 and 1.

## Return Code

A _List of Cursor_ specifying the extended edges.?

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=6215639)

Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(453), Node(461))])

extended_edges = Geometry.Edge.ExtendLine(crlEdges=[Edge(27)], iEnd=1)

JPT.Debugger(extended_edges)
```
