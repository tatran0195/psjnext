---
title: "Tools.Measure.Angle.CreateMeasureNote.ProjectedNode()"
description: "Create a Measure Note for Measure > Angle > Projected Node"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Angle > CreateMeasureNote > ProjectedNode"
macro_link: "[CreateMeasureNoteAngleByProjected_Node]"
---

## Description

Create a Measure Note for Measure > Angle > Projected Node function.

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.ProjectedNode(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crNode` @type(Cursor) @required

- A node.

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

```psj{8-11}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Coordinates.ThreeNode(strName="CRect_1", crlNodes=[Node(444, 317, 185)])
Tools.Measure.Angle.CreateMeasureNote.ProjectedNode(
    strNoteName="Angle1", 
    crNode=Node(346), 
    crCoordinate=Coord(1))
```
