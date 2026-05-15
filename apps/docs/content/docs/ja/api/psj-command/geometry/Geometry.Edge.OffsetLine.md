---
title: "Geometry.Edge.OffsetLine()"
description: "Create new edges by offsetting specified edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Offset Line"
macro _link: "[ImprintOffsetLineS](../../macro/geometry/ImprintOffsetLineS)"
---

## Description

Create new edges by offsetting specified edges.

## Syntax

```psj
Geometry.Edge.OffsetLine(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the edges to be offset.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dOffsetDistance

- Specify the offset distance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLayerNumber

- Specify the number of layers to be offset.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bMerge

- Specify whether or not to merge the offset edges when the angle between them is bigger than 150 degrees.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bExtend

- Specify whether to extend the offset edges to the nearest boundary edges.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iOffsetMethod

- Specify how to create offset edges.
  - If _iOffsetMethod=0_, create multiple offset layers using the offset distance and the number of layers.
  - If _iOffsetMethod=1_, create single offset layer using the layer offset distance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dOffsetDistance

- Specify the layer offset distance.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iImprintMethod

- Specify imprint method.
  - If _iImprintMethod=0_, offset edges will be imprinted onto the face side that has the longest edges.
  - If _iImprintMethod=1_, offset edges will be imprinted onto the face side that has the shortest edges.
  - If _iImprintMethod=2_, offset edges will be imprinted onto both face sides.
- The default value is 2.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dlOffsetDistance

- Specify the layer offset distance.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### bAutoCollapse

- Specify whether to collapse automatically.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube(iPartColor=6484066)

offset _lines = Geometry.Edge.OffsetLine(crlFaces=[Face(22)], 
                                        crlEdges=[Edge(19)], 
                                        dOffsetDistance=0.001, 
                                        iLayerNumber=6)

JPT.Debugger(offset _lines)
```
