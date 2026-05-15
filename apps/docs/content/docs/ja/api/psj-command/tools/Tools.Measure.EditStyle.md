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

<!-- @since:5.1.0 @required -->
### crlMeasureNote

- Specify measure notes.

<!-- @since:5.1.0 @optional -->
### iFontSize

- Specify font size.
- The default value is 16.

<!-- @since:5.1.0 @optional -->
### iFontColor

- Specify font color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bBold

- Specify bold type or not.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iBackgroundColor

- Specify background color.
- The default value is 16777215.

<!-- @since:5.1.0 @optional -->
### iOutlineWidth

- Specify outline width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iOutlineColor

- Specify outline color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowWidth

- Specify arrow width.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iArrowColor

- Specify arrow color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iArrowType

- Specify arrow type.
  - 0: None.
  - 1: Arrow.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTitleType

- Specify title type.
  - 0: None.
  - 1: Measure type.
  - 2: Name of note.
- The default value is 1.

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
