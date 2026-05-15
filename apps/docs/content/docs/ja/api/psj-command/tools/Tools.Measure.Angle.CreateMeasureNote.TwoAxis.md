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

<!-- @since:5.1.0 @required -->
### strNoteName

- Specify the name of the created note.

<!-- @since:5.1.0 @required -->
### iAxis

- Specify an axis.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify coordinate of the axis.
- The default value is _None_.

<!-- @since:5.1.0 @required -->
### crCoordinateRef

- Specify reference coordinate of the reference axis.

<!-- @since:5.1.0 @required -->
### iAxisRef

- Specify a reference axis.

<!-- @since:5.1.0 @optional -->
### iFontSize

- Specify font size.
- The default value is 16.

<!-- @since:5.1.0 @optional -->
### iFontColor

- Specify font color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bBold

- Specify bold type or not.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iBackgroundColor

- Specify background color.
- The default value is 16777215.

<!-- @since:5.1.0 @optional -->
### iOutlineWidth

- Specify outline width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iOutlineColor

- Specify outline color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowWidth

- Specify arrow width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iArrowColor

- Specify arrow color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowType

- Specify arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTitleType

- Specify title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```pj {9-14}
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
