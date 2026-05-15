---
title: "Tools.Measure.Radius.Edge()"
description: "Measure arc radius of the specified edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Radius > Edge"
---

## Description

Measure arc radius of the specified edge.

## Syntax

```psj
Tools.Measure.Radius.Edge(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crEdge

- Specify the edge to measure the arc radius. The selected edge should be a curved edge, not to be a straight edge.

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the number of digit after floating point. The greater`iPrecision` could be, the more accuracy of arc radius can be measured.
- The default value is 6.

## Return Code

A _Double_ specifying the arc radius value.

## Sample Code

```psj {3}
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.Edge(crEdge=Edge(1))

JPT.Debugger(radius)
```
