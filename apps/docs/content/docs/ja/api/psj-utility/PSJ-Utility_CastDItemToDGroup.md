---
title: "JPT.CastDItemToDGroup()"
description: "Convert DItem object to DGroup object"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ object to get the information of the selected group.

## Syntax

```psj
JPT.CastDItemToDGroup(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ object (Group with relating information).

## Sample Code

```psj {12}
# Prepare model
Geometry.Part.Cube()
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
JPT.ViewFitToModel()

# Get Group object as DItem object from the created list of DItem objects
listDItemGroups = JPT.GetAllByTypeID(JPT.DItemType.GROUP)
dItemGroup = listDItemGroups[0]
JPT.Debugger(dItemGroup)

# Convert from the above DItem object to DGroup object
dGroup = JPT.CastDItemToDGroup(dItemGroup)
JPT.Debugger(dGroup)
```
