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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The target faces on which the edges are imprinted.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The edges to be offset.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the given faces where possible.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @type:List[Double] @default:[] -->
### `dOffsetDistance`

- The offset distance.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iLayerNumber`

- The number of layers to be offset.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMerge`

- Whether or not to merge the offset edges when the angle between them is bigger than 150 degrees.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bExtend`

- Whether to extend the offset edges to the nearest boundary edges.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOffsetMethod`

- The how to create offset edges.
  - If _iOffsetMethod=0_, create multiple offset layers using the offset distance and the number of layers.
  - If _iOffsetMethod=1_, create single offset layer using the layer offset distance.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 @type:List[Double] @default:[] -->
### `dOffsetDistance`

- The layer offset distance.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iImprintMethod`

- The imprint method.
  - If _iImprintMethod=0_, offset edges will be imprinted onto the face side that has the longest edges.
  - If _iImprintMethod=1_, offset edges will be imprinted onto the face side that has the shortest edges.
  - If _iImprintMethod=2_, offset edges will be imprinted onto both face sides.

<!-- @since:5.0.1 @type:List[Double] @removed:5.1.0 @optional @deprecated @default:[] -->
### `dlOffsetDistance`

- The layer offset distance.

<!-- @since:5.0.1 @type:Boolean @removed:5.1.0 @optional @deprecated @default:False -->
### `bAutoCollapse`

- Whether to collapse automatically.

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
