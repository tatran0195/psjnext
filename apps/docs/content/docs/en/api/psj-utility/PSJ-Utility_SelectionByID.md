---
title: "JPT.SelectionByID()"
description: "Select an entity by using its ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Select an entity by using its ID.

## Syntax

```psj
JPT.SelectionByID(DItemType, entityID, BoolType)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @type:Integer @required -->
### `entityID`

- The ID of the selecting entity.

<!-- @since:5.0.1 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, JPT.BoolType.TRUE _VAL)
```
