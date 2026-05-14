---
title: "Tools.Measure.Distance.Edge()"
description: "Measure the edge length"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > Edge"
---

## Description

Measure the edge length.

## Syntax

```psj
Tools.Measure.Distance.Edge(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdge`

- The edge to measure the distance.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of distance can be measured.

## Return Code

A _Double_ specifying the length of the specified edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

length = Tools.Measure.Distance.Edge(crEdge=Edge(15))

JPT.Debugger(length)
```
