---
title: "Tools.Measure.CreateMeasureNoteForce()"
description: "Create a Measure Note for Measure > Force function"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Measure > CreateMeasureNoteForce"
macro _link: "[CreateMeasureNoteForce]"
---

## Description

Create a Measure Note for Measure > Force function.

## Syntax

```psj
Tools.Measure.CreateMeasureNoteForce(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strNoteName`

- The name of the created note.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The target entities.

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

```psj {4-6}
#Please load result contains force result here.
#Input IDs of nodes to measure.
n1=1
n2=2
n3=3

Tools.Measure.CreateMeasureNoteForce(
        strNoteName="Force1", 
        crlTargets=[Node(n1, n2, n3)])
```
