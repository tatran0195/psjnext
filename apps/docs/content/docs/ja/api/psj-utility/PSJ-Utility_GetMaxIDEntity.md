---
title: "JPT.GetMaxIDEntity()"
description: "Get the maximum ID of the inputted DItemType"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the maximum ID of the inputted DItemType.

## Syntax

```psj
JPT.GetMaxIDEntity(DItemType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### DItemType

- Specify the_[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.

## Return Code

A _Integer_ specifying the maximum ID of the inputted DItemType.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get the maximum ID of the created parts
iMaxID = JPT.GetMaxIDEntity(JPT.DItemType.BODY)
JPT.Debugger(iMaxID) # 3
```
