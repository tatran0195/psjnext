---
title: "Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode()"
description: "Create a Measure Note for Measure > Distance > Plane(Elem)-Node function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Distance > CreateMeasureNote > PlaneElemToNode"
macro_link: "[CreateMeasureNoteDistanceByPlaneElem_Node]"
---

## Description

Create a Measure Note for Measure > Distance > Plane(Elem)-Node function

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crNode` @type(Cursor) @required

- A node.

### `crElement` @type(Cursor) @required

- An element.

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
Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode(
  strNoteName="Distance1", 
  crNode=Node(185), 
  crElement=Elem(544))
```
