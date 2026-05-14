---
title: "Tools.Measure.Radius.CreateMeasureNote.ThreeNodes()"
description: "Create a Measure Note for Measure > Radius > 3 Nodes function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Radius > CreateMeasureNote > ThreeNodes"
macro _link: "[CreateMeasureNoteRadiusBy3Nodes]"
---

## Description

Create a Measure Note for Measure > Radius > 3 Nodes function.

## Syntax

```psj
Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:Cursor @required -->
### `crFirstNode`

- The first node.

<!-- @since:5.1.0 @type:Cursor @required -->
### `crSecondNode`

- The second node.

<!-- @since:5.1.0 @type:Cursor @required -->
### `crThirdNode`

- The third node.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- A local coordinate.

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

A _CursorStr_ specifying created note.

## Sample Code

```psj {7-11}
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(
  strNoteName="Radius1", 
  crFirstNode=Node(70), 
  crSecondNode=Node(46), 
  crThirdNode=Node(16))
```
