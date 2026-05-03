---
title: "Geometry.Edge.PerpendicularCylinderLine()"
description: "Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Perpendicular Cylinder Line"
macro_link: "[ImprintPerpendicularCylinderLineS](../../macro/geometry/ImprintPerpendicularCylinderLineS)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create a perpendicular line to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value","Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value.

## Syntax

```psj
Geometry.Edge.PerpendicularCylinderLine(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- The couple nodes, which the first node is the start node where the perpendicular line will be drawn, the second node is used to determine the offset direction (in case of user want to offset).

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted. The selected face could be curved surface or circular surface.

### `iMethod` @type(Integer) @default(0)

- The Imprint method. The method will be represented by the value according to order of selection in the combobox method.
  - I&#x66;_&#x69;Method=0_: Center Angle - The angle at the cylindrical center of a perpendicular position
  - I&#x66;_&#x69;Method=1_: Arc length - The distance on the circumference of a perpendicular position

### `dOffset` @type(Double) @default(0.0)

- The offset value. The offset value would be an angle degrees or length of an arc of a circle in millimeters, which is depended on selection method.

### `bOppositeSide` @type(Boolean) @default(False)

- Whether the opposite side option is checked or not. This argument will allow to imprint 2 lines in both side of selected face.
  - I&#x66;_&#x54;rue_, Jupiter will create 2 lines in both sides of the curved surface of the cylinder. In case of the selection face is a circular face, the imprinted line will continuously go through the center node and cut the edge at a node that opposites to the start node.
  - I&#x66;_&#x46;alse_, Jupiter will create only 1 line that defined by start node.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cylinder(iPartColor=5093709)

created_edges = Geometry.Edge.PerpendicularCylinderLine(crlNodes=[Node(19, 157)], 
                                                crlFaces=[Face(5)],
                                                dOffset=1.0, 
                                                bOppositeSide=True)
JPT.Debugger(created_edges)
```
