---
title: "Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges()"
description: "Create a Measure Note for Measure > Angle > 2 Elem Edges function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Angle > CreateMeasureNote > TwoElemEdges"
macro_link: "[CreateMeasureNoteAngleBy2ElemEdges]"
---

## Description

Create a Measure Note for Measure > Angle > 2 Elem Edges function

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crFirstPairFirstNode` @type(Cursor) @required

- The first node of the first element edge.

### `crFirstPairSecondNode` @type(Cursor) @required

- The second node of  the first element edge.

### `crSecondPairFirstNode` @type(Cursor) @required

- The first node of the second element edge.

### `crSecondPairSecondNode` @type(Cursor) @required

- The second node of  the second element edge.

### `crCoordinate` @type(Cursor) @default(None)

- Local coordinate.

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

```psj{7-12}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges(
  strNoteName="Angle1", 
  crFirstPairFirstNode=Node(371), 
  crFirstPairSecondNode=Node(380), 
  crSecondPairFirstNode=Node(379), 
  crSecondPairSecondNode=Node(380))
```
