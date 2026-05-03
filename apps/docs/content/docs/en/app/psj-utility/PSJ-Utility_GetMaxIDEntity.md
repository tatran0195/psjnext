---
title: "JPT.GetMaxIDEntity()"
description: "Get the maximum ID of the inputted DItemType"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the maximum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMaxIDEntity(DItemType)
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

# Get the maximum ID of the created parts
iMaxID = JPT.GetMaxIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMaxID) # 3
```
