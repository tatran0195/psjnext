---
title: "Geometry.BreakEntity.Edge()"
description: "Break an edge into separate units at the given points or specified angle"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Break Entity > Edge"
---

## Description

Break an edge into separate units at the given points or specified angle.

## Syntax

```psj
Geometry.BreakEntity.Edge(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify parts that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify faces that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlEdges

- Specify edges to be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the nodes at which edges pass through will be divided. This argument will be ignored if _bAutoByAngle = False_.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bAutoByAngle

- Specify whether to divide by edge angle.
  - If _True_, edge will be divided at the position where its angle is not greater than the given _dEdgeAngle_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the angle in degrees between line segments. If _bAutoByAngle_ is not specified, this argument is ignored.
- The default value is 60.0.

## Return Code

A _List of Cursor_ specifying the edges after the function is executed.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6215639)

edges = Geometry.BreakEntity.Edge(crlNodes=[Node(86, 83)])

JPT.Debugger(edges)
```
