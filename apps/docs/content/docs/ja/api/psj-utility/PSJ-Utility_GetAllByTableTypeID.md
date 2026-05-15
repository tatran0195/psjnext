---
title: "JPT.GetAllByTableTypeID()"
description: "Get all the information of all entities by inputting DTableType"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all entities by inputting _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.

## Syntax

```psj
JPT.GetAllByTableTypeID(DTableType)
```

## Inputs

<!-- @since:5.1.0 @required -->
### DTableType

- Specify _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the target entities.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the found entities by inputted ID.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Select all parts and store their information to a list of DItem
listDTableParts = JPT.GetAllByTableTypeID(JPT.DTableType.DTABLE _BODY) # ID = 5
JPT.Debugger(listDTableParts)
```
