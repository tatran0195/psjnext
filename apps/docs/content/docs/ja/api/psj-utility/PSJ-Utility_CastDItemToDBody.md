---
title: 'JPT.CastDItemToDBody()'
description: 'Convert DItem object to DBody object'
version_introduced: '5.0.1'
available_versions: 'all'
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to
_[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ object to get the information of the selected body.

## Syntax

```psj
JPT.CastDItemToDBody(DItemObject)
```

## Inputs

### `DItemObject` @type(DItem) @required

- Object which will be used to convert.

## Return Code

A _[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ object (Part with relating information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Part object as DItem object from the created list of DItem objects
listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
dItemPart = listDItemParts[0]
JPT.Debugger(dItemPart)

# Convert from the above DItem object to DBody object
dBodyPart = JPT.CastDItemToDBody(dItemPart)
JPT.Debugger(dBodyPart)
```
