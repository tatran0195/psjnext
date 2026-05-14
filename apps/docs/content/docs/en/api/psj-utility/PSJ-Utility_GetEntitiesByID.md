---
title: "JPT.GetEntitiesByID()"
description: "Get information of the inputted entity ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get information of the inputted entity ID.

## Syntax

```psj
JPT.GetEntitiesByID(DItemType, itemID)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

<!-- @since:5.0.1 @type:Integer @required -->
### `itemID`

- The ID of the target entity.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entity has the inputted ID.

Note that the inputted entity is the first element of this list.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the information of the part with ID = 2 and store it to a list
listParts = JPT.GetEntitiesByID(JPT.DItemType.BODY, 2)

# Print the information of the part
JPT.Debugger(listParts[0])
```
