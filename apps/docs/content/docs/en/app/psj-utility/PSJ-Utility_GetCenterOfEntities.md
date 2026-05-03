---
title: "JPT.GetCenterOfEntities()"
description: "Get center coordinate of selected entities"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get center coordinate of selected entities.

## Syntax

```psj
JPT.GetCenterOfEntities(DItemVector)
```

## Inputs

### `DItemVector` @type(DItemVector) @required

- Object o&#x72;_&#x4C;ist of[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_&#x6F;bjects specifying the targets to get center coordinates.

## Return Code

A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ object or _List of Double_ value containing the coordinate values \[x, y, z] of the center of the inputted entities.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the center coordinate of the inputted entities
listParts = JPT.GetAllByTypeID(3)
JPT.Debugger(JPT.GetCenterOfEntities(listParts))
```
