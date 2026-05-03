---
title: "Assembly.RightClick.ChangeMeshLineColor()"
description: "Change the color of the mesh line of the selected part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Change Single Color > Mesh Line"
---

## Description

Change the color of the mesh line of the selected part.

## Syntax

```psj
Assembly.RightClick.ChangeMeshLineColor(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face which mesh line color will be changed.

### `iColor` @type(Integer) @default(0)

- The color.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

changed_status = Assembly.RightClick.ChangeMeshLineColor(crlFaces=[Face(21, 
                                                                        22, 
                                                                        23, 
                                                                        24, 
                                                                        25, 
                                                                        26)], 
                                                         iColor=10535167)

JPT.Debugger(changed_status)
```
