---
title: "Geometry.Edge.PerpendicularCylinderLine()"
description: "Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Perpendicular Cylinder Line"
macro _link: "[ImprintPerpendicularCylinderLineS](../../macro/geometry/ImprintPerpendicularCylinderLineS)"
---

## Description

Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value.

## Syntax

```psj
Geometry.Edge.PerpendicularCylinderLine(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the couple nodes, which the first node is the start node where the perpendicular line will be drawn, the second node is used to determine the offset direction (in case of user want to offset).

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the edges are imprinted. The selected face could be curved surface or circular surface.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the Imprint method. The method will be represented by the value according to order of selection in the combobox method.
  - If _iMethod=0_: Center Angle - The angle at the cylindrical center of a perpendicular position
  - If _iMethod=1_: Arc length - The distance on the circumference of a perpendicular position
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset value. The offset value would be an angle degrees or length of an arc of a circle in millimeters, which is depended on selection method.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bOppositeSide

- Specify whether the opposite side option is checked or not. This argument will allow to imprint 2 lines in both side of selected face.
  - If _True_, Jupiter will create 2 lines in both sides of the curved surface of the cylinder. In case of the selection face is a circular face, the imprinted line will continuously go through the center node and cut the edge at a node that opposites to the start node.
  - If _False_, Jupiter will create only 1 line that defined by start node.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cylinder(iPartColor=5093709)

created _edges = Geometry.Edge.PerpendicularCylinderLine(crlNodes=[Node(19, 157)], 
                                                crlFaces=[Face(5)],
                                                dOffset=1.0, 
                                                bOppositeSide=True)
JPT.Debugger(created _edges)
```
