---
title: "JPT.PreviewBCForceGeneral()"
description: "Show preview result of applying general force on target"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show preview result of applying general force on target.

## Syntax

```psj
JPT.PreviewBCForceGeneral(...)
```

## Inputs

<!-- @since:5.0.1 @type:DItemVector @required -->
### `DItemVector`

- The object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying force.
- This targets can be Face, Edge or Node.

<!-- @since:5.0.1 @type:List[Double] @required -->
### `dlForce`

- The value of Force in 3 directions.

<!-- @since:5.0.1 @type:List[Double] @required -->
### `dlMoment`

- The value of Moment in 3 directions.

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

```psj {10}
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
JPT.PreviewBCForceGeneral(selFace,[0.0,10.0,10.0],[0.0,0.0,0.0],0,color,0.8)
JPT.ViewFitToModel()
```
