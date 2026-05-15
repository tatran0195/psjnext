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

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify custom notes or collections to edit style.
- The default value is \[].

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

- Specify font bold.
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

- Specify type of arrow.
  - 0 : None
  - 1 : Arrow
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iAlignment

- Specify alignment.
  - 0: Left
  - 1: Center
  - 2: Right
- The default value is 0.

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
