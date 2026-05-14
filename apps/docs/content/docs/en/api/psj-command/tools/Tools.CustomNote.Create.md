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

<!-- @since:5.1.0 @type:String @optional @default:"CustomNote _1" -->
### `strNoteName`

- The note name.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlNotePosition`

- The position where the created note indicates.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTargetEntityType`

- The target entity type.
  - 0: None
  - 1: Node
  - 2 :1D Element
  - 3: 2D Element
  - 4 :3D Element
  - 5: Face Point
  - 6: Edge Point

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTarget`

- The target entity.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crParentCollection`

- The custom note collection to store the custom note.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strParentName`

- The name of newly created custom note collection.

<!-- @since:5.1.0 @type:List[String] @required -->
### `listContent`

- The content of custom note.

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

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strImagePath`

- The image path.

<!-- @since:5.1.0 @type:Cursor @optional @default:0:0 -->
### `crEdit`

- A custom note to modify.

## Return Code

A _Cursor_ specifying created custom note.

## Sample Code

```psj {5-16}
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
