---
title: "JPT.PreviewTranslation()"
description: "Show preview result of body translation"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of body translation.

## Syntax

```psj
JPT.PreviewTranslation(...)
```

## Inputs

### `DBodyVector`

- A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be moved.

<!-- @since:5.0.1 @required -->
### dlTranslationVector

- Specify the translation vector defining the direction and magnitude of the translation.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color of the previewed entity.
- The default value is 255.

<!-- @since:5.0.1 @optional -->
### dTransparency

- Specify the transparency of the previewed entity.
- The range of `dTransparency` = \[0.0, 1.0]
- The default value is 0.5.

<!-- @since:5.0.1 @optional -->
### DCoord

- Specify Local Coordinate System.
- The default value is None (Global Coordinate System).

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
JPT.PreviewTranslation(parts,[0.02,0.01,0.01],color,1,coord[0])
JPT.ViewFitToModel()
```
