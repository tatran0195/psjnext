---
title: "Geometry.Edge.OffsetLine()"
description: "Create new edges by offsetting specified edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Offset Line"
macro_link: "[ImprintOffsetLineS](../../macro/geometry/ImprintOffsetLineS)"
---
<!-- REVIEW FLAGS — requires human review
   [param_decorator_changed] Param 'dOffsetDistance' @type changed from 'Double' to 'List[Double]' in v5.1.0
     context: {"param":"dOffsetDistance","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"Double","toType":"List[Double]"}
   [param_decorator_changed] Param 'dOffsetDistance' @default changed from '0.0' to '[]' in v5.1.0
     context: {"param":"dOffsetDistance","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"[]"}
   [param_removed_unexpectedly] Param 'dlOffsetDistance' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'bAutoCollapse' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create new edges by offsetting specified edges.

## Syntax

```psj
Geometry.Edge.OffsetLine(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `crlEdges` @type(List\[Cursor]) @required

- The edges to be offset.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

### `dOffsetDistance` @type(List\[Double]) @default(\[])

- The offset distance.

### `iLayerNumber` @type(Integer) @default(1)

- The number of layers to be offset.

### `bMerge` @type(Boolean) @default(True)

- Whether or not to merge the offset edges when the angle between them is bigger than 150 degrees.

### `bExtend` @type(Boolean) @default(True)

- Whether to extend the offset edges to the nearest boundary edges.

### `iOffsetMethod` @type(Integer) @default(0)

- How to create offset edges.
  - I&#x66;_&#x69;OffsetMethod=0_, create multiple offset layers using the offset distance and the number of layers.
  - I&#x66;_&#x69;OffsetMethod=1_, create single offset layer using the layer offset distance.

### `dOffsetDistance` @type(List\[Double]) @default(\[])

- The layer offset distance.

### `iImprintMethod` @type(Integer) @default(2)

- Imprint method.
  - I&#x66;_&#x69;ImprintMethod=0_, offset edges will be imprinted onto the face side that has the longest edges.
  - I&#x66;_&#x69;ImprintMethod=1_, offset edges will be imprinted onto the face side that has the shortest edges.
  - I&#x66;_&#x69;ImprintMethod=2_, offset edges will be imprinted onto both face sides.

### `dlOffsetDistance` @type(List\[Double]) @default(\[]) @deprecated @until(5.1.0)

- The layer offset distance.

### `bAutoCollapse` @type(Boolean) @default(False) @deprecated @until(5.1.0)

- Whether to collapse automatically.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube(iPartColor=6484066)

offset_lines = Geometry.Edge.OffsetLine(crlFaces=[Face(22)], 
                                        crlEdges=[Edge(19)], 
                                        dOffsetDistance=0.001, 
                                        iLayerNumber=6)

JPT.Debugger(offset_lines)
```
