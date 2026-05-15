---
title: "JPT.RemoveEntitiesByName()"
description: "Remove entities by using the inputted name"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove entities by using the inputted name.

## Syntax

```psj
JPT.RemoveEntitiesByName(DTableType, itemName, BoolType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DTableType

- Specify the_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @required -->
### itemName

- Specify the name of the target entity to be removed.

<!-- @since:5.0.1 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
  - _False_: Approximate match.
  - _True_: Exact match.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Remove all the parts with their name have the "_" character inside
JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE _BODY, "_", JPT.BoolType.FALSE _VAL)
```
