---
title: "Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis()"
description: "Create a Measure Note for Measure > Angle > 2 Nodes Axis function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Angle > CreateMeasureNote > TwoNodesAxis"
macro _link: "[CreateMeasureNoteAngleBy2Nodes _Axis]"
---

## Description

Create a Measure Note for Measure > Angle > 2 Nodes Axis function.

## Syntax

```psj
Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strNoteName

- Specify the name of the created note.

<!-- @since:5.1.0 @required -->
### crFirstNode

- Specify the first node.

<!-- @since:5.1.0 @required -->
### crSecondNode

- Specify the second node.

<!-- @since:5.1.0 @optional -->
### iAxis

- Specify an axis.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify a local coordinate.
- The default value is _None_.

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

A _CursorStr_ specifying created note.

## Sample Code

```psj {7-10}
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis(
    strNoteName="Angle1", 
    crFirstNode=Node(107), 
    crSecondNode=Node(259))
```
