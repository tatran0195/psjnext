---
title: "Geometry.Edge.ProjectLine()"
description: "Create new edges by projecting the selected edges onto the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Project Line"
---

## Description

Create new edges by projecting the selected edges onto the selected faces.

## Syntax

```psj
Geometry.Edge.ProjectLine(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edges to be projected.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify two nodes to define the projection direction. This argument must be specified if _iType=1_.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the method to be used to project onto target faces.
  - If _iType=0_, project along to the face normal direction for the target faces.
  - If _iType=1_, project along to the direction defined by two nodes specified by the _crlNodes_.
  - If _iType=2_, project onto the face closest to the selected edge.
- The default value is 0.

### `bCheckGap`

- A _Boolean_ whether to limit the projection distance to the input value.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dGap

- Specify the gap value. This argument is to be used when _bCheckGap=True_.
- The default value is 0.0.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=13064794)
line = Geometry.Edge.Line(dllPoints=[[0.004444444444444444, 0.01, 0.01], [0.007777777777777778, 0, 0.01]], 
                          crlFaces=[Face(26)])

project _lines = Geometry.Edge.ProjectLine(crlEdges=line, crlFaces=[Face(25)])
JPT.Debugger(project _lines)
```
