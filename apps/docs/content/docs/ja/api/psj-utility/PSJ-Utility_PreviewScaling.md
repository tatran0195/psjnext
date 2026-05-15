---
title: "JPT.PreviewScaling()"
description: "Show preview result of body scaling"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of body scaling.

## Syntax

```psj
JPT.PreviewScaling(...)
```

## Inputs

### `DBodyVector`

- A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be scaled.

<!-- @since:5.0.1 @required -->
### dlScaleVector

- Specify the scale vector. It defines how much scaling is used in each direction.

<!-- @since:5.0.1 @required -->
### dlScaleCenter

- Specify the scale center position. It defines a point where the scaling should be started.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color of the previewed entity.
- The default value is 255.

<!-- @since:5.0.1 @optional -->
### dTransparency

- Specify the transparency of the previewed entity.
- The range of `dTransparency` = \[0.0, 1.0]
- The default value is 0.5.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube _2", iPartColor=13259210)

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2.1,1.1,1.1],[0,0,0],color,0.2)
JPT.ViewFitToModel()
```
