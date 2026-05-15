---
title: "Utility.MeasureDistanceBy2Edges()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Utility > MeasureDistanceBy2Edges"
macro _link: "[MeasureDistanceBy2Edges](../../macro/utility/MeasureDistanceBy2Edges)"
---

## Description

Unknown Description

## Syntax

```psj
Utility.MeasureDistanceBy2Edges(crEdgeFirst, crEdgeLast, iPrecision=6)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crEdgeFirst

- Specify the edge first.

<!-- @since:5.0.1 @required -->
### crEdgeLast

- Specify the edge last.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

## Return Code

A _Double_ of distance between two edges.

## Sample Code

```psj
Geometry.Part.Cube()

distance = Utility.MeasureDistanceBy2Edges(crEdgeFirst=Edge(20), crEdgeLast=Edge(18))
print('Distance = ' + str(distance))
```
