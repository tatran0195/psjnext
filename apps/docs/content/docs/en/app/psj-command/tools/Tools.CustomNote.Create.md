---
title: "Tools.CustomNote.Create()"
description: "Create a custom note"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > CustomNote > Create"
macro_link: ""
---

## Description

Create a custom note.

## Syntax

```psj
Tools.CustomNote.Create(...)
```

## Inputs

### `strNoteName` @type(String) @default("CustomNote\_1")

- Note name.

### `dlNotePosition` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Position where the created note indicates.

### `iTargetEntityType` @type(Integer) @default(0)

- Target entity type.
  - 0: None
  - 1: Node
  - 2 :1D Element
  - 3: 2D Element
  - 4 :3D Element
  - 5: Face Point
  - 6: Edge Point

### `crTarget` @type(Cursor) @default(None)

- Target entity.

### `crParentCollection` @type(Cursor) @default(None)

- Custom note collection to store the custom note.

### `strParentName` @type(String) @default("")

- Name of newly created custom note collection.

### `listContent` @type(List\[String]) @required

- Content of custom note.

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

### `strImagePath` @type(String) @default("")

- Image path.

### `crEdit` @type(Cursor) @default(0:0)

- A custom note to modify.

## Return Code

A _Cursor_ specifying created custom note.

## Sample Code

```psj{5-16}
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0029, 0.0063, 0.01], 
    iTargetEntityType=5, 
    crTarget=Elem(1022), 
    strParentName="Collection_1", 
    listContent=["Top Face"], 
    iFontSize=18, 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=2763429, 
    iArrowColor=2763429)
```
