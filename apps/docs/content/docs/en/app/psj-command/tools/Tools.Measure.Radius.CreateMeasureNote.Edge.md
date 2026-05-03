---
title: "Tools.Measure.Radius.CreateMeasureNote.Edge()"
description: "Create a Measure Note for Measure > Radius > Edge function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Radius > CreateMeasureNote > Edge"
macro_link: "[CreateMeasureNoteRadiusByEdge]"
---

## Description

Create a Measure Note for Measure > Radius > Edge function.

## Syntax

```psj
Tools.Measure.Radius.CreateMeasureNote.Edge(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crEdge` @type(Cursor) @required

- An edge.

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

```psj{7-9}
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.Edge(
  strNoteName="Radius1", 
  crEdge=Edge(1))
```
