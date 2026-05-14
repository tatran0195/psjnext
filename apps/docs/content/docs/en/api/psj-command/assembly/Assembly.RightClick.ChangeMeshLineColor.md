---
title: "Assembly.RightClick.ChangeMeshLineColor()"
description: "Change the color of the mesh line of the selected part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Change Single Color > Mesh Line"
---

## Description

Change the color of the mesh line of the selected part.

## Syntax

```psj
Assembly.RightClick.ChangeMeshLineColor(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face which mesh line color will be changed.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The color.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

changed _status = Assembly.RightClick.ChangeMeshLineColor(crlFaces=[Face(21, 
                                                                        22, 
                                                                        23, 
                                                                        24, 
                                                                        25, 
                                                                        26)], 
                                                         iColor=10535167)

JPT.Debugger(changed _status)
```
