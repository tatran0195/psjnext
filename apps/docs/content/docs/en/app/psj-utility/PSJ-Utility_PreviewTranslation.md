---
title: "JPT.PreviewTranslation()"
description: "Show preview result of body translation"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show preview result of body translation.

## Syntax

```psj
JPT.PreviewTranslation(...)
```

## Inputs

### `DBodyVector` @type(DBodyVector) @required

- Object o&#x72;_&#x4C;ist of[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_&#x6F;bjects storing the information of parts to be moved.

### `dlTranslationVector` @type(List\[Double]) @required

- The translation vector defining the direction and magnitude of the translation.

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
JPT.PreviewTranslation(parts,[0.02,0.01,0.01],color,1,coord[0])
JPT.ViewFitToModel()
```
