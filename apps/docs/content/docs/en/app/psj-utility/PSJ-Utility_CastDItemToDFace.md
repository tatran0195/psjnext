---
title: "JPT.CastDItemToDFace()"
description: "Convert DItem object to DFace object"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ object to get the information of the selected (Inputted) face(s).

## Syntax

```psj
JPT.CastDItemToDFace(DItemObject)
```

## Inputs

### `DItemObject` @type(DItem) @required

- Object which will be used to convert.

## Return Code

A _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ object (Face with relating information).

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Face object as DItem object from the created list of DItem objects
listDItemFaces = JPT.GetAllByTypeID(JPT.DItemType.FACE)
dItemFace = listDItemFaces[0]
JPT.Debugger(dItemFace)

# Convert from the above DItem object to DFace object
dFace = JPT.CastDItemToDFace(dItemFace)
JPT.Debugger(dFace)
```
