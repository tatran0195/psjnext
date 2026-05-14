---
title: "JPT.GetSharedElements()"
description: "Get all information of the shared elements"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all information of the shared elements.

## Syntax

```psj
JPT.GetSharedElements(DItemVector)
```

## Inputs

<!-- @since:5.0.1 @type:DItemVector @required -->
### `DItemVector`

- The object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to get the shared elements.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared elements.

## Sample Code

```psj {14}
# Prepare model
Geometry.Part.Cube(iPartColor=6217822)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6908379)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=7138924)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=15753968)
JPT.ViewFitToModel()

# Create shared faces
JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')

# Get the information of all shared elements
listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
listSharedElems = JPT.GetSharedElements(listParts)
JPT.Debugger(listSharedElems)
```
