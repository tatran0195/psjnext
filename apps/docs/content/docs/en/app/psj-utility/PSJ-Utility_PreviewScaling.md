---
title: "JPT.PreviewScaling()"
description: "Show preview result of body scaling"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show preview result of body scaling.

## Syntax

```psj
JPT.PreviewScaling(...)
```

## Inputs

### `DBodyVector` @type(DBodyVector) @required

- Object o&#x72;_&#x4C;ist of[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_&#x6F;bjects storing the information of parts to be scaled.

### `dlScaleVector` @type(List\[Double]) @required

- The scale vector. It defines how much scaling is used in each direction.

### `dlScaleCenter` @type(List\[Double]) @required

- The scale center position. It defines a point where the scaling should be started.

### `iColor` @type(Integer) @default(255)

- The color of the previewed entity.

### `dTransparency` @type(Double) @default(0.5)

- The transparency of the previewed entity.
- The range of`dTransparency`= \[0.0, 1.0]

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2.1,1.1,1.1],[0,0,0],color,0.2)
JPT.ViewFitToModel()
```
