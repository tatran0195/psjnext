---
title: "JPT.GetMinIDEntity()"
description: "Get the minimum ID of the inputted DItemType"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the minimum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMinIDEntity(DItemType)
```

## Inputs

<!-- @since:5.0.1 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

## Return Code

A _Integer_ specifying the maximum ID of the inputted DItemType.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the minimum ID of the created parts
iMinID = JPT.GetMinIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMinID) # 1
```
