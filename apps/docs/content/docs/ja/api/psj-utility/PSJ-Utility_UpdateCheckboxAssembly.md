---
title: "JPT.UpdateCheckboxAssembly()"
description: "Set state of checkbox of item in Assembly Tree"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the state of checkbox of item in Assembly Tree.

## Syntax

```psj
JPT.UpdateCheckboxAssembly(DItemType, entityID, BoolType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DItemType

- Specify the_[DItemType](../data-type/psj-command/DItem-types)_ of the entity.

<!-- @since:5.0.1 @required -->
### entityID

- Specify the ID of the target entity.

<!-- @since:5.0.1 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the state of checkbox:
  - _True_: Check the checkbox of item in Assembly Tree.
  - _False_: Uncheck the checkbox of item in Assembly Tree.

:::tip
You also can input **1** instead of inputting JPT.BoolType.TRUE\_VAL,
or input **0** instead of inputting JPT.BoolType.FALSE\_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {10-11}
# prepare model...
JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube _1", 7105764, 0:0)')
JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube _2", 6409934, 0:0)')
JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube _3", 13259210, 0:0)')

parts = JPT.GetAllParts()

# update checkbox from assembly tree
for part in parts:
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 1) # turn on checkbox
    JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 0) # turn off checkbox
```
