---
title: "Utility.MeasureDistanceBy2Edges()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Utility > MeasureDistanceBy2Edges"
macro_link: "[MeasureDistanceBy2Edges](../../macro/utility/MeasureDistanceBy2Edges)"
---

## Description

Unknown Description

## Syntax

```psj
Utility.MeasureDistanceBy2Edges(crEdgeFirst, crEdgeLast, iPrecision=6)
```

## Inputs

### `crEdgeFirst` @type(Cursor) @required

- The edge first.

### `crEdgeLast` @type(Cursor) @required

- The edge last.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A _Double_ of distance between two edges.

## Sample Code

```psj
Geometry.Part.Cube()

distance = Utility.MeasureDistanceBy2Edges(crEdgeFirst=Edge(20), crEdgeLast=Edge(18))
print('Distance = ' + str(distance))
```
