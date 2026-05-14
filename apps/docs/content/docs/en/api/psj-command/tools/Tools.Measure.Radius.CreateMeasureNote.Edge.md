---
title: "Tools.Measure.Radius.CreateMeasureNote.Edge()"
description: "Create a Measure Note for Measure > Radius > Edge function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > Radius > CreateMeasureNote > Edge"
macro _link: "[CreateMeasureNoteRadiusByEdge]"
---

## Description

Create a Measure Note for Measure > Radius > Edge function.

## Syntax

```psj
Tools.Measure.Radius.CreateMeasureNote.Edge(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:Cursor @required -->
### `crEdge`

- An edge.

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

```psj {7-9}
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.Edge(
  strNoteName="Radius1", 
  crEdge=Edge(1))
```
