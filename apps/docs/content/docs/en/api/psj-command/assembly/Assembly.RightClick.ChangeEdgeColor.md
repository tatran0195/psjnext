---
title: "Assembly.RightClick.ChangeEdgeColor()"
description: "Change the color of the edges of selected part"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble Window > Right Click > Change Single Color > Feature Edge Ribbon: Assemble Window > Right Click > Change Single Color > Feature Edge(Default) Ribbon: Assemble Window > Right Click > Change Random Color > Feature Edge Ribbon: Assemble Window > Right Click > Change Random Color > Feature Edge(Default)"
---

## Description

Change the color of the edges of selected part.

## Syntax

```psj
Assembly.RightClick.ChangeEdgeColor(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The parts to change edge color.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iColor`

- The edge color to change.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bRandom`

- Whether assign random color. It ignores iColor setting.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
JPT.ViewFitToModel()
Assembly.RightClick.ChangeEdgeColor(crlParts=[Part(1)], iColor=12583104)
```
