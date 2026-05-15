---
title: "JPT.ShowHideEntitiesByID()"
description: "Show or Hide an entity by inputted its ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show or Hide an entity by inputted its ID.

## Syntax

```psj
JPT.ShowHideEntitiesByID(DTableType, itemID, BoolType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DTableType

- Specify the_[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be shown/hidden.

<!-- @since:5.0.1 @required -->
### itemID

- Specify the ID of the target entity.

<!-- @since:5.0.1 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
  - _False_: Hide the inputted part.
  - _True_: Show the inputted part.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Hide all parts
JPT.ShowHideAllParts(JPT.BoolType.FALSE _VAL)

# Show Cube _1
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE _BODY, 1, JPT.BoolType.TRUE _VAL)
```
