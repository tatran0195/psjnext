---
title: "Tools.CustomNote.EditStyle()"
description: "Edit style of indicated custom notes."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > CustomNote > EditStyle"
macro_link: "EditCustomNoteStyle"
---

## Description

Edit style of indicated custom notes.

## Syntax

```psj
Tools.CustomNote.EditStyle(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- Custom notes or collections to edit style.

### `iFontSize` @type(Integer) @default(16)

- Font size.

### `iFontColor` @type(Integer) @default(0)

- Font color.

### `bBold` @type(Boolean) @default(False)

- Font bold.

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

- Type of arrow.
  - 0 : None
  - 1 : Arrow

### `iAlignment` @type(Integer) @default(0)

- Alignment.
  - 0: Left
  - 1: Center
  - 2: Right

## Return Code

A _Boolean_ specifying edit custom note style works successfully or not.

## Sample Code

```psj{22-26}
Geometry.Part.Cube(strName="Cube_1", iPartColor=6409934)

Tools.CustomNote(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.01, 0.01],
    iTargetEntityType=1, crTarget=Node(8), 
    strParentName="Collection_1", 
    listContent=["My Custom Note 1"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote(
    strNoteName="CustomNote_2", 
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
