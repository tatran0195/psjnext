---
title: "Tools.Measure.Angle.ProjectedNode()"
description: "Measure the projection angle onto the coordinate system plane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > ProjectedNode"
---

## Description

Measure the projection angle onto the coordinate system plane.

## Syntax

```psj
Tools.Measure.Angle.ProjectedNode(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crNode

- Specify the node.

<!-- @since:5.0.1 @optional -->
### strTarget

- Specify the target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - If _strTarget="XY"_: Return the angle that will project on plane Oxy.
  - If _strTarget="YZ"_: Return the angle that will project on plane Oyz.
  - If _strTarget="ZX"_: Return the angle that will project on plane Ozx.
  - If _strTarget="Angle"_: Return the angle in 3D space.
  - If _strTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".
- The default value is "All".

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

<!-- @since:5.1.0 @optional -->
### crCoord

- Specify the coordinate system.
- The default value is _None_.

## Return Code

A _List of Double_ specifying the projected angles.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube _2", iPartColor=7697908)
angle = Tools.Measure.Angle.ProjectedNode(crNode=Node(461))
JPT.Debugger(angle)
```
