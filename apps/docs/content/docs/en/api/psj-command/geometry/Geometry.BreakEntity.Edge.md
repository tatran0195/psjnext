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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The parts that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The faces that the edges connecting to the faces will be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEdges`

- The edges to be divided. Either _crlParts_, _crlFaces_, or _crlEdges_ must be specified when _bAutoByAngle = True_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The nodes at which edges pass through will be divided. This argument will be ignored if _bAutoByAngle = False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAutoByAngle`

- Whether to divide by edge angle.
  - If _True_, edge will be divided at the position where its angle is not greater than the given _dEdgeAngle_.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dEdgeAngle`

- The angle in degrees between line segments. If _bAutoByAngle_ is not specified, this argument is ignored.

## Return Code

A _List of Cursor_ specifying the edges after the function is executed.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6215639)

edges = Geometry.BreakEntity.Edge(crlNodes=[Node(86, 83)])

JPT.Debugger(edges)
```
