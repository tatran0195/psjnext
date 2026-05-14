---
title: "Tools.Measure.Angle.TwoEdges()"
description: "Measure the angle created by 2 edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > TwoEdges"
---

## Description

Measure the angle created by 2 edges.

## Syntax

```psj
Tools.Measure.Angle.TwoEdges(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdge1`

- The first edge to measure the angle.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdge2`

- The second edge to measure the angle.

<!-- @since:5.0.1 @type:String @optional @default:"All" -->
### `strTarget`

- The target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - If _strTarget="XY"_: Return the angle that will project on plane Oxy.
  - If _strTarget="YZ"_: Return the angle that will project on plane Oyz.
  - If _strTarget="ZX"_: Return the angle that will project on plane Ozx.
  - If _strTarget="Angle"_: Return the angle in 3D space.
  - If _strTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate reference system in which the angle will refer to measure.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of angle can be measured.

## Return Code

A _List of Double_ specifying the angles between edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoEdges(crEdge1=Edge(19), 
                                     crEdge2=Edge(18))

JPT.Debugger(angle)
```
