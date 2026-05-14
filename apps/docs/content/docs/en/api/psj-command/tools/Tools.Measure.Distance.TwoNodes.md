---
title: "Tools.Measure.Distance.TwoNodes()"
description: "Measure distance between two nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > TwoNodes"
---

## Description

Measure distance between two nodes.

## Syntax

```psj
Tools.Measure.Distance.TwoNodes(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode1`

- The first node to measure distance.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crNode2`

- The second node to measure distance.

<!-- @since:5.0.1 @type:String @optional @default:"All" -->
### `strTarget`

- The target projection axis, or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - If _strTarget="X"_: Return the distance value along the X axis.
  - If _strTarget="Y"_: Return the distance value along the Y axis.
  - If _strTarget="Z"_: Return the distance value along the Z axis.
  - If _strTarget="Dist"_: Return the angle value on in 3D space.
  - If _strTarget="All"_: Return all the 4 distance values in a list, in order "Dist", "X", "Y", "Z".

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The number of digit after floating point. The greater`iPrecision` could be, the more accuracy of distance can be measured.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate reference system in which the distance will refer to measure.

## Return Code

A _List of Double_ specifying the distance between two nodes.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoNodes(crNode1=Node(454), 
                                           crNode2=Node(472), 
                                           strTarget="Dist")

JPT.Debugger(distance)

print _str = ", ".join([str(value) for value in distance])
print(print _str)
```
