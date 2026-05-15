---
title: "Assembly.RightClick.ChangeEntityColor()"
description: "Change color of a specific entity/a list of entities (By ID)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "None"
---

## Description

Change color of a specific entity/a list of entities (By ID).

## Syntax

```psj
Assembly.RightClick.ChangeEntityColor(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEntities

- Specify a list of entitiy/entities that its/theirs color will be changed.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color for entities.
- The default value is 0.

## Return Code

A _String_ specifying whether the color of the inputted entity/entities is changed or not:

- **1**: The color of the inputted entity/entities is changed successfully.
- **0**: The color of the inputted entity/entities cannot be changed.

## Sample Code

```psj {2}
Geometry.Part.Cube()
changed _color = Assembly.RightClick.ChangeEntityColor(crlEntities=[Face(26, 24, 22)], iColor=16777088)
JPT.Debugger(changed _color)
```
