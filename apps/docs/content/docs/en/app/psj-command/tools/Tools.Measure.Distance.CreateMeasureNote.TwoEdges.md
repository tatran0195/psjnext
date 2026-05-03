---
title: "Tools.Measure.Distance.CreateMeasureNote.TwoEdges()"
description: "Create a Measure Note for Measure > Distance > 2Edges function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Distance > CreateMeasureNote > TwoEdges"
macro_link: "[CreateMeasureNoteDistanceBy2Edges]"
---

## Description

Create a Measure Note for Measure > Distance > 2Edges function.

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.TwoEdges(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crFirstEdge` @type(Cursor) @required

- The first edge.

### `crSecondEdge` @type(Cursor) @required

- The second edge.

### `crCoordinate` @type(Cursor) @default(None)

- A local coordinate.

### `iFontSize` @type(Integer) @default(16)

- Specifying

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
Tools.Measure.Distance.CreateMeasureNote.TwoEdges(
    strNoteName="Distance1", 
    crFirstEdge=Edge(11),
    crSecondEdge=Edge(17))
```
