---
title: "Tools.Measure.Angle.TwoEdges()"
description: "Measure the angle created by 2 edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Angle > TwoEdges"
---

## Description

Measure the angle created by 2 edges.

## Syntax

```psj
Tools.Measure.Angle.TwoEdges(...)
```

## Inputs

### `crEdge1` @type(Cursor) @required

- The first edge to measure the angle.

### `crEdge2` @type(Cursor) @required

- The second edge to measure the angle.

### `strTarget` @type(String) @default("All")

- The target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - I&#x66;_&#x73;trTarget="XY"_: Return the angle that will project on plane Oxy.
  - I&#x66;_&#x73;trTarget="YZ"_: Return the angle that will project on plane Oyz.
  - I&#x66;_&#x73;trTarget="ZX"_: Return the angle that will project on plane Ozx.
  - I&#x66;_&#x73;trTarget="Angle"_: Return the angle in 3D space.
  - I&#x66;_&#x73;trTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".

### `crCoord` @type(Cursor) @default(None)

- The coordinate reference system in which the angle will refer to measure.

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of angle can be measured.

## Return Code

A _List of Double_ specifying the angles between edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoEdges(crEdge1=Edge(19), 
                                     crEdge2=Edge(18))

JPT.Debugger(angle)
```
