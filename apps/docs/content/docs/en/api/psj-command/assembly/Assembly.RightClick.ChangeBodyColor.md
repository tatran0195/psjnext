---
title: "Assembly.RightClick.ChangeBodyColor()"
description: "Change the color of the selected part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Change Random Color > Surface"
---

## Description

Change the color of the selected part.

## Syntax

```psj
Assembly.RightClick.ChangeBodyColor(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[PART _COLOR _PAIR] @optional @default:[] -->
### `listPartColorPair`

- A list which contains part and its color.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bResetFaceColor`

- Whether or not reset face color.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

adding _status = Assembly.RightClick.ChangeBodyColor(listPartColorPair=[PART _COLOR _PAIR(crPart=Part(1),
                                                                                       iColor=6409934)])

JPT.Debugger(adding _status)
```
