---
title: "Tools.Measure.Angle.CreateMeasureNote.TwoAxis()"
description: "Create a Measure Note for Measure > Angle > 2 Axes function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Angle > CreateMeasureNote > TwoAxis"
macro_link: "[CreateMeasureNoteAngleBy2Axis]"
---

## Description

Create a Measure Note for Measure > Angle > 2 Axes function

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `iAxis` @type(Integer) @required

- An axis.

### `crCoordinate` @type(Cursor) @default(None)

- Coordinate of the axis.

### `crCoordinateRef` @type(Cursor) @required

- Reference coordinate of the reference axis.

### `iAxisRef` @type(Integer) @required

- A reference axis.

### `iFontSize` @type(Integer) @default(16)

- Font size.

### `iFontColor` @type(Integer) @default(0)

- Font color.

### `bBold` @type(Boolean) @default(False)

- Bold type or not.

### `iBackgroundColor` @type(Integer) @default(16777215)

- Background color.

### `iOutlineWidth` @type(Integer) @default(1)

- Outline width.

### `iOutlineColor` @type(Integer) @default(0)

- Outline color.

### `iArrowWidth` @type(Integer) @default(1)

- Arrow width.

### `iArrowColor` @type(Integer) @default(0)

- Arrow color.

### `iArrowType` @type(Integer) @default(1)

- Arrow type.
  - 0: None.
  - 1: Arrow.

### `iTitleType` @type(Integer) @default(1)

- Title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

## Return Code

A _CursorStr_ specifying created note.

## Sample Code

```psj{9-14}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Coordinates.ThreeNode(strName="CRect_1", crlNodes=[Node(6, 437, 472)])
Tools.Coordinates.ThreeNode(strName="CRect_2", crlNodes=[Node(370, 186, 170)])
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
