---
title: "Tools.Measure.Angle.ProjectedNode()"
description: "Measure the projection angle onto the coordinate system plane"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Angle > ProjectedNode"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["measure angle on projected node","Measure the projection angle onto the coordinate system plane"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure the projection angle onto the coordinate system plane.

## Syntax

```psj
Tools.Measure.Angle.ProjectedNode(...)
```

## Inputs

### `crNode` @type(Cursor) @required

- The node.

### `strTarget` @type(String) @default("All")

- The target projection plane (2D), or the three-dimensional space (3D) to refer to measure. This parameter can be one of the following:
  - I&#x66;_&#x73;trTarget="XY"_: Return the angle that will project on plane Oxy.
  - I&#x66;_&#x73;trTarget="YZ"_: Return the angle that will project on plane Oyz.
  - I&#x66;_&#x73;trTarget="ZX"_: Return the angle that will project on plane Ozx.
  - I&#x66;_&#x73;trTarget="Angle"_: Return the angle in 3D space.
  - I&#x66;_&#x73;trTarget="All"_: Return all the 4 angle values in a list, in order "Angle", "XY", "YZ", "ZX".

### `iPrecision` @type(Integer) @default(6)

- The precision.

### `crCoord` @type(Cursor) @default(None) @since(5.1.0)

- The coordinate system.

## Return Code

A _List of Double_ specifying the projected angles.

## Sample Code

```psj {2}
Geometry.Part.Cube(strName="Cube_2", iPartColor=7697908)
angle = Tools.Measure.Angle.ProjectedNode(crNode=Node(461))
JPT.Debugger(angle)
```
