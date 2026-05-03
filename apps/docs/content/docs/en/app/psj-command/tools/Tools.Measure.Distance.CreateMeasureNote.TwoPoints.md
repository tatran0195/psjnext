---
title: "Tools.Measure.Distance.CreateMeasureNote.TwoPoints()"
description: "Create a Measure Note for Measure > Distance > Two Points function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Distance > CreateMeasureNote > TwoPoints"
macro_link: "[CreateMeasureNoteDistanceBy2Points]"
---

## Description

Create a Measure Note for Measure > Distance > Two Points function.

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `dlFirstPoint` @type(List\[Double]) @required

- The first point.

### `dlSecondPoint` @type(List\[Double]) @required

- The second point.

### `crCoordinate` @type(Cursor) @default(None)

- A local coordinate.

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

```psj{7-10}
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
