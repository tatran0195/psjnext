---
title: "JPT.GetCountByType()"
description: "Get total number of entities by inputting DItemType"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get total number of entities by inputting _[DItemType](../data-type/psj-command/DItem-types)_.

## Syntax

```psj
JPT.GetCountByType(DItemType)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x74;hat wants to count the total number.

## Return Code

An _Integer_ specifying the total number of the inputted type.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Count the total number of bodies existing on the current Jupiter
iPartCount = JPT.GetCountByType(JPT.DItemType.BODY)
print(iPartCount) # 3
```
