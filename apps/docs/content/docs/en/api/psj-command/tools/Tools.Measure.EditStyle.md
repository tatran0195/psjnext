---
title: "Tools.Measure.EditStyle()"
description: "Edit style of the specified measure note"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > EditStyle"
macro _link: "[EditMeasureNoteStyle]"
---

## Description

Edit style of the specified measure note

## Syntax

```psj
Tools.Measure.EditStyle(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlMeasureNote`

- The measure notes.

<!-- @since:5.1.0 @type:Integer @optional @default:16 -->
### `iFontSize`

- The font size.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFontColor`

- The font color.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBold`

- The bold type or not.

<!-- @since:5.1.0 @type:Integer @optional @default:16777215 -->
### `iBackgroundColor`

- The background color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iOutlineWidth`

- The outline width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOutlineColor`

- The outline color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowWidth`

- The arrow width.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iArrowColor`

- The arrow color.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iArrowType`

- The arrow type.
  - 0: None.
  - 1: Arrow.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTitleType`

- The title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.

## Return Code

A _Boolean_ specifying the function succeeded or not.

## Sample Code

```psj {13-21}
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
