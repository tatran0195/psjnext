---
title: "Assembly.RightClick.ChangeBodyColor()"
description: "Change the color of the selected part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Change Random Color > Surface"
---

## Description

Change the color of the selected part.

## Syntax

```psj
Assembly.RightClick.ChangeBodyColor(...)
```

## Inputs

### `listPartColorPair` @type(List\[PART\_COLOR\_PAIR]) @default(\[])

- A list which contains part and its color.

### `bResetFaceColor` @type(Boolean) @default(False)

- Whether or not reset face color.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

adding_status = Assembly.RightClick.ChangeBodyColor(listPartColorPair=[PART_COLOR_PAIR(crPart=Part(1),
                                                                                       iColor=6409934)])

JPT.Debugger(adding_status)
```
