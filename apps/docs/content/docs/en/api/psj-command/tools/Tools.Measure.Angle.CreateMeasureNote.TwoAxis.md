---
title: "Tools.Measure.Angle.CreateMeasureNote.TwoAxis()"
description: "Create a Measure Note for Measure > Angle > 2 Axes function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Angle > CreateMeasureNote > TwoAxis"
macro _link: "[CreateMeasureNoteAngleBy2Axis]"
---

## Description

Create a Measure Note for Measure > Angle > 2 Axes function

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:Integer @required -->
### `iAxis`

- An axis.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate of the axis.

<!-- @since:5.1.0 @type:Cursor @required -->
### `crCoordinateRef`

- The reference coordinate of the reference axis.

<!-- @since:5.1.0 @type:Integer @required -->
### `iAxisRef`

- A reference axis.

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

```psj {9-14}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Coordinates.ThreeNode(strName="CRect _1", crlNodes=[Node(6, 437, 472)])
Tools.Coordinates.ThreeNode(strName="CRect _2", crlNodes=[Node(370, 186, 170)])
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(
  strNoteName="Angle1", 
  iAxis=0, 
  crCoordinateRef=Coord(2),
  iAxisRef=0, 
  crCoordinate=Coord(1))
```
