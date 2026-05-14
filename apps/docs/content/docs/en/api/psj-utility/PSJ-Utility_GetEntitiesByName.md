---
title: "JPT.GetEntitiesByName()"
description: "Get information of the inputted entity name"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get information of the inputted entity name.

## Syntax

```psj
JPT.GetEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

<!-- @since:5.0.1 @type:DTableType @required -->
### `DTableType`

- The _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @type:String @required -->
### `itemName`

- The name of the target entity.

<!-- @since:5.0.1 @type:BoolType @required -->
### `BoolType`

- The _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entities have the inputted name.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the information of the part with name = "_" and store it to a list
listParts = JPT.GetEntitiesByName(JPT.DTableType.DTABLE _BODY, "_", JPT.BoolType.FALSE _VAL)
print(listParts[0].name) # Cube _1
print(listParts[2].name) # Cube _3
print(listParts[2].id) # 3
```
