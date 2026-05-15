---
title: "Tools.CustomNote.Create()"
description: "Create a custom note"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > CustomNote > Create"
macro _link: ""
---

## Description

Create a custom note.

## Syntax

```psj
Tools.CustomNote.Create(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strNoteName

- Specify note name.
- The default value is "CustomNote\_1".

<!-- @since:5.1.0 @optional -->
### dlNotePosition

- Specify position where the created note indicates.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.1.0 @optional -->
### iTargetEntityType

- Specify target entity type.
  - 0: None
  - 1: Node
  - 2 :1D Element
  - 3: 2D Element
  - 4 :3D Element
  - 5: Face Point
  - 6: Edge Point
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crTarget

- Specify target entity.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crParentCollection

- Specify custom note collection to store the custom note.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### strParentName

- Specify name of newly created custom note collection.
- The default value is "".

<!-- @since:5.1.0 @required -->
### listContent

- Specify content of custom note.

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

<!-- @since:5.1.0 @optional -->
### strImagePath

- Specify image path.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify a custom note to modify.
- The default value is 0:0.

## Return Code

A _Cursor_ specifying created custom note.

## Sample Code

```pj {5-16}
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Tools.CustomNote.Create(
    strNoteName="CustomNote _1", 
    dlNotePosition=[0.0029, 0.0063, 0.01], 
    iTargetEntityType=5, 
    crTarget=Elem(1022), 
    strParentName="Collection _1", 
    listContent=["Top Face"], 
    iFontSize=18, 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=2763429, 
    iArrowColor=2763429)
```
