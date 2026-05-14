---
title: "JPT.PreviewBCForceNormal()"
description: "Show preview result of applying normal force on target"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of applying normal force on target.

## Syntax

```psj
JPT.PreviewBCForceNormal(...)
```

## Inputs

<!-- @since:5.0.1 @type:DElem @required -->
### `DElemForNormal`

- The object specifying 2D element information.
- This element will be used to calculate normal vector for force direction.

<!-- @since:5.0.1 @type:DItemVector @required -->
### `DItemVector`

- The object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying force.
- This targets can be Face, Edge or Node.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iArrowDir`

- The display arrow direction.
  - 0: Start at node.
  - 1: End at node.

<!-- @since:5.0.1 @type:Integer @optional @default:255 -->
### `iColor`

- The color of the previewed entity.

<!-- @since:5.0.1 @type:Double @optional @default:0.5 -->
### `dTransparency`

- The transparency of the previewed entity.
- The range of `dTransparency` = \[0.0, 1.0]

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
