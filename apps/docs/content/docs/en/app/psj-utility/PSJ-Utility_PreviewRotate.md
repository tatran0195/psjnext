---
title: "JPT.PreviewRotate()"
description: "Show preview result of body rotation"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show preview result of body rotation.

## Syntax

```psj
JPT.PreviewRotate(...)
```

## Inputs

### `DBodyVector` @type(DBodyVector) @required

- Object o&#x72;_&#x4C;ist of[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_&#x6F;bjects storing the information of parts to be rotated.

### `posCenter` @type(List) @required

- The center position of rotation.

### `vecAxis` @type(List) @required

- The axis of rotation.

### `dAngle` @type(Double) @required

- The rotation angle in degree.

### `iColor` @type(Integer) @default(255)

- The color of the previewed entity.

### `dTransparency` @type(Double) @default(0.5)

- The transparency of the previewed entity.
- The range of`dTransparency`= \[0.0, 1.0]

### `DCoord` @type(DCoord) @default(None (Global Coordinate System))

- Object specifying Local Coordinate System.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {13}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
coord = JPT.GetAllCoordinates()
JPT.PreviewRotate(parts,[0,0,0],[0,1,0],45,color,0.8,coord[0])
JPT.ViewFitToModel()
```
