---
title: "JPT.PreviewBCForceNormal()"
description: "Show preview result of applying normal force on target"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show preview result of applying normal force on target.

## Syntax

```psj
JPT.PreviewBCForceNormal(...)
```

## Inputs

### `DElemForNormal` @type(DElem) @required

- Object specifying 2D element information.
- This element will be used to calculate normal vector for force direction.

### `DItemVector` @type(DItemVector) @required

- Object o&#x72;_&#x4C;ist of[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_&#x6F;bjects storing the information of targets for applying force.
- This targets can be Face, Edge or Node.

### `iArrowDir` @type(Integer) @default(0)

- The display arrow direction.
  - 0: Start at node.
  - 1: End at node.

### `iColor` @type(Integer) @default(255)

- The color of the previewed entity.

### `dTransparency` @type(Double) @default(0.5)

- The transparency of the previewed entity.
- The range of`dTransparency`= \[0.0, 1.0]

## Return Code

This utility function does not have output value.

## Sample Code

```psj {12}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
normalElem = JPT.GetEntitiesByID(JPT.DItemType.ELEM, 1065)
normalElem = JPT.CastDItemToDElem(normalElem[0])
JPT.PreviewBCForceNormal(normalElem,selFace,0,color,0.8)
JPT.ViewFitToModel()
```
