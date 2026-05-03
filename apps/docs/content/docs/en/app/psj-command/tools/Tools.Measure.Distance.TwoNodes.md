---
title: "Tools.Measure.Distance.TwoNodes()"
description: "Measure distance between two nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > TwoNodes"
---

## Description

Measure distance between two nodes.

## Syntax

```psj
Tools.Measure.Distance.TwoNodes(...)
```

## Inputs

### `crNode1` @type(Cursor) @required

- The first node to measure distance.

### `crNode2` @type(Cursor) @required

- The second node to measure distance.

### `strTarget` @type(String) @default("All")

- The target projection axis, or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - I&#x66;_&#x73;trTarget="X"_: Return the distance value along the X axis.
  - I&#x66;_&#x73;trTarget="Y"_: Return the distance value along the Y axis.
  - I&#x66;_&#x73;trTarget="Z"_: Return the distance value along the Z axis.
  - I&#x66;_&#x73;trTarget="Dist"_: Return the angle value on in 3D space.
  - I&#x66;_&#x73;trTarget="All"_: Return all the 4 distance values in a list, in order "Dist", "X", "Y", "Z".

### `iPrecision` @type(Integer) @default(6)

- The number of digit after floating point. The greater`iPrecision`could be, the more accuracy of distance can be measured.

### `crCoord` @type(Cursor) @default(None)

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

print_str = ", ".join([str(value) for value in distance])
print(print_str)
```
