---
title: "Geometry.BreakEntity.Edge()"
description: "Break an edge into separate units at the given points or specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Break Entity > Edge"
---

## Description

Break an edge into separate units at the given points or specified angle.

## Syntax

```psj
Geometry.BreakEntity.Edge(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- Parts that the edges connecting to the faces will be divided. Eithe&#x72;_&#x63;rlParts_,_crlFaces_, o&#x72;_&#x63;rlEdge&#x73;_&#x6D;ust be specified whe&#x6E;_&#x62;AutoByAngle = True_.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- Faces that the edges connecting to the faces will be divided. Eithe&#x72;_&#x63;rlParts_,_crlFaces_, o&#x72;_&#x63;rlEdge&#x73;_&#x6D;ust be specified whe&#x6E;_&#x62;AutoByAngle = True_.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- Edges to be divided. Eithe&#x72;_&#x63;rlParts_,_crlFaces_, o&#x72;_&#x63;rlEdge&#x73;_&#x6D;ust be specified whe&#x6E;_&#x62;AutoByAngle = True_.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The nodes at which edges pass through will be divided. This argument will be ignored i&#x66;_&#x62;AutoByAngle = False_.

### `bAutoByAngle` @type(Boolean) @default(False)

- Whether to divide by edge angle.
  - I&#x66;_&#x54;rue_, edge will be divided at the position where its angle is not greater than the give&#x6E;_&#x64;EdgeAngle_.

### `dEdgeAngle` @type(Double) @default(60.0)

- The angle in degrees between line segments. I&#x66;_&#x62;AutoByAngl&#x65;_&#x69;s not specified, this argument is ignored.

## Return Code

A _List of Cursor_ specifying the edges after the function is executed.

## Sample Code

```psj {3}
Geometry.Part.Cube(iPartColor=6215639)

edges = Geometry.BreakEntity.Edge(crlNodes=[Node(86, 83)])

JPT.Debugger(edges)
```
