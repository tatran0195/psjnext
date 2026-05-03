---
title: "JPT.GetEntitiesByName()"
description: "Get information of the inputted entity name"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get information of the inputted entity name.

## Syntax

```psj
JPT.GetEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

### `DTableType` @type(Enum) @required

- Th&#x65;_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_&#x6F;f entity in Jupiter.

### `itemName` @type(String) @required

- The name of the target entity.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entities have the inputted name.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the part with name = "_" and store it to a list
listParts = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
print(listParts[0].name) # Cube_1
print(listParts[2].name) # Cube_3
print(listParts[2].id) # 3
```
