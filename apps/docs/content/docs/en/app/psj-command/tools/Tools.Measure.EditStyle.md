---
title: "Tools.Measure.EditStyle()"
description: "Edit style of the specified measure note"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Measure > EditStyle"
macro_link: "[EditMeasureNoteStyle]"
---

## Description

Edit style of the specified measure note

## Syntax

```psj
Tools.Measure.EditStyle(...)
```

## Inputs

### `crlMeasureNote` @type(List\[Cursor]) @required

- Measure notes.

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

A _Boolean_ specifying the function succeeded or not.

## Sample Code

```psj{13-21}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
  strNoteName="Distance1", 
  crFirstNode=Node(473), 
  crSecondNode=Node(439))

#Edit the style of the Measure Note
Tools.Measure.EditStyle(
  crlMeasureNote=[MeasureNote(1)], 
  iFontColor=255, 
  iBackgroundColor=15794175,
  iOutlineWidth=3, 
  iArrowWidth=2, 
  iArrowColor=255, 
  iArrowType=1, 
  iTitleType=1)
```
