---
title: "JPT.SelectionByIDs()"
description: "Select entities by using their list of IDs"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Select entities by using their list of IDs.

## Syntax

```psj
JPT.SelectionByIDs(DItemType, entityIDs, BoolType)
```

## Inputs

<!-- @since:5.1.0 @required -->
### DItemType

- Specify the_[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.1.0 @required -->
### entityIDs

- Specify the list of ID of the selecting entites.

<!-- @since:5.1.0 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
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

# Select face with IDs = [50, 51, 52]
JPT.SelectionByIDs(JPT.DItemType.FACE, [50, 51, 52], JPT.BoolType.TRUE _VAL)
```
