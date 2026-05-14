---
title: "MeshCleanup.Manual2D.CreateElement()"
description: "Create a Tri/Quad element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > CreateElement"
---

## Description

Create a Tri/Quad element.

## Syntax

```psj
MeshCleanup.Manual2D.CreateElement()
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElemType`

- The element type.
  - 0: Tri element
  - 1: Quad element

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crParentEntity`

- The face to which the created element will belong.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-4}
Geometry.Part.Cube(iPartColor=6409934)
MeshCleanup.Manual2D.DeleteElement(crlElems=[Elem(1028)])
element = MeshCleanup.Manual2D.CreateElement(crParentEntity=Face(26), 
                                            crlNodes=[Node(470, 469, 461)])
JPT.Debugger(element)
```
