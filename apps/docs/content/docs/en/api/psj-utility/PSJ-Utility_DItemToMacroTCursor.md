---
title: "JPT.DItemToMacroTCursor()"
description: "Convert DItem object to Cursor (Macro string type)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _Cursor_ (Macro string type).

## Syntax

```psj
JPT.DItemToMacroTCursor(DItem)
```

## Inputs

<!-- @since:5.0.1 @type:DItem @required -->
### `DItem`

- The object to be converted.

## Return Code

A _String_ containing all the converted items.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert one of them to List of Cursor (Macro string type)
## Get all Nodes from model
listNodes = [JPT.CastToDItem(node) for node in JPT.GetAllNodes()] # List of DItem objects
## Get 1 Node from the created list
node = listNodes[0] # DItem object
## Return Node to a string object, for example, return value = 10:772
JPT.Debugger(JPT.DItemToMacroTCursor(node))
```
