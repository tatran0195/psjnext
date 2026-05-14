---
title: "Geometry.Face.Elements()"
description: "Create faces from the selected elements"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Face > Elements"
macro _link: "[CreateFaceByElem](../../macro/geometry/CreateFaceByElem)"
---

## Description

Create faces from the selected elements.

## Syntax

```psj
Geometry.Face.Elements(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The surface elements to be moved to the new surface.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSharedFace`

- Whether to create a shared face. If _bSharedFace=True_, the _crlElems_ argument must specify shared elements.

## Return Code

A _List of Cursor_ specifying the new created faces.

## Sample Code

```psj {3,4,5,6,7,8,9,10}
Geometry.Part.Cube()

created _face = Geometry.Face.Elements(crlElems=[Elem(1008,
                                                    1007,
                                                    989,
                                                    990,
                                                    1005,
                                                    1006,
                                                    988,
                                                    987)])

JPT.Debugger(created _face)
```
