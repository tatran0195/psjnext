---
title: "Tools.Measure.Distance.CreateMeasureNote.TwoPoints()"
description: "Create a Measure Note for Measure > Distance > Two Points function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Distance > CreateMeasureNote > TwoPoints"
macro _link: "[CreateMeasureNoteDistanceBy2Points]"
---

## Description

Create a Measure Note for Measure > Distance > Two Points function.

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlFirstPoint`

- The first point.

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlSecondPoint`

- The second point.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- A local coordinate.

<!-- @since:5.1.0 @type:Integer @optional @default:16 -->
### `iFontSize`

- The font size.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFontColor`

- The font color.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBold`

- The bold type or not.

<!-- @since:5.1.0 @type:Integer @optional @default:16777215 -->
### `iBackgroundColor`

- The background color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iOutlineWidth`

- The outline width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOutlineColor`

- The outline color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowWidth`

- The arrow width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iArrowColor`

- The arrow color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowType`

- The arrow type.
  - 0: None.
  - 1: Arrow.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTitleType`

- The title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj {7-10}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(
  strNoteName="Distance1", 
  dlFirstPoint=[0.007, 0.0036, 0.01], 
  dlSecondPoint=[0.001, 0.005, 0.01])
```
