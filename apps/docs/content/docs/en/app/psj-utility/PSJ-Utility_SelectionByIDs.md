---
title: "JPT.SelectionByIDs()"
description: "Select entities by using their list of IDs"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Select entities by using their list of IDs.

## Syntax

```psj
JPT.SelectionByIDs(DItemType, entityIDs, BoolType)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f entity in Jupiter.

### `entityIDs` @type(List\[Integer]) @required

- The list of ID of the selecting entites.

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

# Select face with IDs = [50, 51, 52]
JPT.SelectionByIDs(JPT.DItemType.FACE, [50, 51, 52], JPT.BoolType.TRUE_VAL)
```
