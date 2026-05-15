---
title: "Tools.Measure.Distance.TwoEdges()"
description: "Measure the distance between two edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > TwoEdges"
---

## Description

Measure the distance of two edges.

## Syntax

```psj
Tools.Measure.Distance.TwoEdges(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crEdge1

- Specify the first edge to measure distance.

<!-- @since:5.0.1 @required -->
### crEdge2

- Specify the second edge to measure distance.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the number of digit after floating point. The greater`iPrecision` could be, the more accuracy of distance can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the distance between two edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoEdges(crEdge1=Edge(20), 
                                           crEdge2=Edge(18))

JPT.Debugger(distance)
```
