---
title: "JPT.SelectionByID()"
description: "Select an entity by using its ID"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Select an entity by using its ID.

## Syntax

```psj
JPT.SelectionByID(DItemType, entityID, BoolType)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f entity in Jupiter.

### `entityID` @type(Integer) @required

- ID of the selecting entity.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the selection mode:
  - _True_: Select the inputted entity with its ID.
  - _False_: Deselect the inputted entity with its ID.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, JPT.BoolType.TRUE_VAL)
```
