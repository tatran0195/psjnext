---
title: "JPT.ShowHideEntitiesByID()"
description: "Show or Hide an entity by inputted its ID"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show or Hide an entity by inputted its ID.

## Syntax

```psj
JPT.ShowHideEntitiesByID(DTableType, itemID, BoolType)
```

## Inputs

### `DTableType` @type(Enum) @required

- Th&#x65;_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_&#x6F;f the entities which will be shown/hidden.

### `itemID` @type(Integer) @required

- The ID of the target entity.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the display mode:
  - _False_: Hide the inputted part.
  - _True_: Show the inputted part.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Hide all parts
JPT.ShowHideAllParts(JPT.BoolType.FALSE_VAL)

# Show Cube_1
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)
```
