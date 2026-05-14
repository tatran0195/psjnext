---
title: "Tools.CustomNote.EditStyle()"
description: "Edit style of indicated custom notes."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > CustomNote > EditStyle"
macro _link: "EditCustomNoteStyle"
---

## Description

Edit style of indicated custom notes.

## Syntax

```psj
Tools.CustomNote.EditStyle(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The custom notes or collections to edit style.

<!-- @since:5.1.0 @type:Integer @optional @default:16 -->
### `iFontSize`

- The font size.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iFontColor`

- The font color.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBold`

- The font bold.

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

- The type of arrow.
  - 0 : None
  - 1 : Arrow

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAlignment`

- The alignment.
  - 0: Left
  - 1: Center
  - 2: Right

## Return Code

A _Boolean_ specifying edit custom note style works successfully or not.

## Sample Code

```psj {22-26}
Geometry.Part.Cube(strName="Cube _1", iPartColor=6409934)

Tools.CustomNote(
    strNoteName="CustomNote _1", 
    dlNotePosition=[0.0, 0.01, 0.01],
    iTargetEntityType=1, crTarget=Node(8), 
    strParentName="Collection _1", 
    listContent=["My Custom Note 1"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote(
    strNoteName="CustomNote _2", 
    dlNotePosition=[0.01, 0.01, 0.01], 
    iTargetEntityType=1, 
    crTarget=Node(7), c
    rParentCollection=CustomNoteCollection(1), 
    listContent=["My Custom Note 2"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote.EditStyle(
    crlTargets=[CustomNoteCollection(1)], 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=25600, 
    iArrowColor=8421376)
```
