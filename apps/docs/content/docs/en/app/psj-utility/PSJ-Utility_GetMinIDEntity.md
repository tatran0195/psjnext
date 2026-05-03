---
title: "JPT.GetMinIDEntity()"
description: "Get the minimum ID of the inputted DItemType"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the minimum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMinIDEntity(DItemType)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x6F;f entity in Jupiter.

## Return Code

A _Integer_ specifying the maximum ID of the inputted DItemType.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the minimum ID of the created parts
iMinID = JPT.GetMinIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMinID) # 1
```
