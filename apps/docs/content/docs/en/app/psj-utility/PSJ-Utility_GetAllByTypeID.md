---
title: "JPT.GetAllByTypeID()"
description: "Get all the information of all entities by inputting DItemType"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all the information of all entities by inputting _[DItemType](../data-type/psj-command/DItem-types)_.

## Syntax

```psj
JPT.GetAllByTypeID(DItemType)
```

## Inputs

### `DItemType` @type(Enum) @required

- &#xNAN;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f the target entities.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the found entities by inputted ID.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select all parts and store their information to a list of DItem
listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY) # ID = 3
JPT.Debugger(listDItemParts)
```
