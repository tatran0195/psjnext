---
title: "JPT.PreviewRotate()"
description: "Show preview result of body rotation"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of body rotation.

## Syntax

```psj
JPT.PreviewRotate(...)
```

## Inputs

<!-- @since:5.0.1 @type:DBodyVector @required -->
### `DBodyVector`

- The object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be rotated.

<!-- @since:5.0.1 @type:List @required -->
### `posCenter`

- The center position of rotation.

<!-- @since:5.0.1 @type:List @required -->
### `vecAxis`

- The axis of rotation.

<!-- @since:5.0.1 @type:Double @required -->
### `dAngle`

- The rotation angle in degree.

<!-- @since:5.0.1 @type:Integer @optional @default:255 -->
### `iColor`

- The color of the previewed entity.

<!-- @since:5.0.1 @type:Double @optional @default:0.5 -->
### `dTransparency`

- The transparency of the previewed entity.
- The range of `dTransparency` = \[0.0, 1.0]

<!-- @since:5.0.1 @type:DCoord @optional @default:None (Global Coordinate System) -->
### `DCoord`

- The object specifying Local Coordinate System.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {13}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube _2", iPartColor=13259210)
Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
coord = JPT.GetAllCoordinates()
JPT.PreviewRotate(parts,[0,0,0],[0,1,0],45,color,0.8,coord[0])
JPT.ViewFitToModel()
```
