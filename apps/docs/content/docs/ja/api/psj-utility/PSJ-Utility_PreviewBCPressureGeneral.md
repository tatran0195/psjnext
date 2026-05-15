---
title: "JPT.PreviewBCPressureGeneral()"
description: "Show preview result of applying general pressure on target"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of applying general pressure on target.

## Syntax

```psj
JPT.PreviewBCPressureGeneral(...)
```

## Inputs

### `DItemVector`

- A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying pressure.
- This targets can be Face, Edge or Node.

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify the display arrow direction.
  - 0: Start at node.
  - 1: End at node.
- The default value is 0.

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

```psj {10}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
JPT.PreviewBCPressureGeneral(selFace,1,color,0.8)
JPT.ViewFitToModel()
```
