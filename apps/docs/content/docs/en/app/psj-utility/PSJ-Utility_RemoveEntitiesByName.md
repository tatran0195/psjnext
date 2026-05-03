---
title: "JPT.RemoveEntitiesByName()"
description: "Remove entities by using the inputted name"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Remove entities by using the inputted name.

## Syntax

```psj
JPT.RemoveEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

### `DTableType` @type(Enum) @required

- Th&#x65;_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_&#x6F;f entity in Jupiter.

### `itemName` @type(String) @required

- The name of the target entity to be removed.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Remove all the parts with their name have the "_" character inside
JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
```
