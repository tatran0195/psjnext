---
title: "Tools.Measure.Distance.TwoEdges()"
description: "Measure the distance between two edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > TwoEdges"
---

## Description

Measure the distance of two edges.

## Syntax

```psj
Tools.Measure.Distance.TwoEdges(...)
```

## Inputs

### `crEdge1` @type(Cursor) @required

- The first edge to measure distance.

### `crEdge2` @type(Cursor) @required

- The second edge to measure distance.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of distance can be measured.

## Return Code

A _Double_ specifying the distance between two edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoEdges(crEdge1=Edge(20), 
                                           crEdge2=Edge(18))

JPT.Debugger(distance)
```
