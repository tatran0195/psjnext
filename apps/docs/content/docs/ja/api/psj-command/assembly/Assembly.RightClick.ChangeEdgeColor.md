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

<!-- @since:5.1.0 @required -->
### crlParts

- Specify parts to change edge color.

<!-- @since:5.1.0 @optional -->
### iColor

- Specify edge color to change.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bRandom

- Specify whether assign random color. It ignores iColor setting.
- The default value is _False_.

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
