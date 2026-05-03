---
title: "Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode()"
description: "Create a Measure Note for Measure > Distance >  Plane(3Nodes)-Node function"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > Distance > CreateMeasureNote > Plane3NodesToNode"
macro_link: "[CreateMeasureNoteDistanceByPlane3Nodes_Node]"
---

## Description

Create a Measure Note for Measure > Distance >  Plane(3Nodes)-Node function

## Syntax

```psj
Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode(...)
```

## Inputs

### `strNoteName` @type(String) @required

- The name of the created note.

### `crFirstNode` @type(Cursor) @required

- The first node.

### `crSecondNode` @type(Cursor) @required

- The second node.

### `crThirdNode` @type(Cursor) @required

- The third node.

### `crFourthNode` @type(Cursor) @required

- The fourth node.

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

```psj{7-12}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode(
    strNoteName="Distance1", 
    crFirstNode=Node(35), 
    crSecondNode=Node(223), 
    crThirdNode=Node(437), 
    crFourthNode=Node(339))
```
