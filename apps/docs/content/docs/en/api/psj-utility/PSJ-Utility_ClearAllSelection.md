---
title: "JPT.ClearAllSelection()"
description: "Clear all the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Clear all the selected entities.

## Syntax

```psj
JPT.ClearAllSelection()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, True)

# Deselect all the selected entities
JPT.ClearAllSelection()
```
