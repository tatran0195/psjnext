---
title: "Assembly.RightClick.ChangeEdgeColor()"
description: "Change the color of the edges of selected part"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assemble Window > Right Click > Change Single Color > Feature Edge Ribbon: Assemble Window > Right Click > Change Single Color > Feature Edge(Default) Ribbon: Assemble Window > Right Click > Change Random Color > Feature Edge Ribbon: Assemble Window > Right Click > Change Random Color > Feature Edge(Default)"
---

## Description

Change the color of the edges of selected part.

## Syntax

```psj
Assembly.RightClick.ChangeEdgeColor(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Parts to change edge color.

### `iColor` @type(Integer) @default(0)

- Edge color to change.

### `bRandom` @type(Boolean) @default(False)

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
