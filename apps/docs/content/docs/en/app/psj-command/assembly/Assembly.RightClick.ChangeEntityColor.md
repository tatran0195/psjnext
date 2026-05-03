---
title: "Assembly.RightClick.ChangeEntityColor()"
description: "Change color of a specific entity/a list of entities (By ID)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "None"
---

## Description

Change color of a specific entity/a list of entities (By ID).

## Syntax

```psj
Assembly.RightClick.ChangeEntityColor(...)
```

## Inputs

### `crlEntities` @type(List\[Cursor]) @required

- A list of entitiy/entities that its/theirs color will be changed.

### `iColor` @type(Integer) @default(0)

- The color for entities.

## Return Code

A _String_ specifying whether the color of the inputted entity/entities is changed or not:

- **1**: The color of the inputted entity/entities is changed successfully.
- **0**: The color of the inputted entity/entities cannot be changed.

## Sample Code

```psj {2}
Geometry.Part.Cube()
changed_color = Assembly.RightClick.ChangeEntityColor(crlEntities=[Face(26, 24, 22)], iColor=16777088)
JPT.Debugger(changed_color)
```
