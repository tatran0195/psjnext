---
title: "JPT.DItemToMacroTCursorPair()"
description: "Convert pair of DItem objects to Cursor pair (Macro string type)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert pair of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to _Cursor_ pair (Macro string type).

## Syntax

```psj
JPT.DItemToMacroTCursorPair(DItem1, DItem2)
```

## Inputs

### `DItem1`

- The first _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.

### `DItem2`

- The second _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.

## Return Code

A _String_ containing all the converted items.

## Sample Code

```psj {14}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert a pair of them to cursor pair (Macro string type)
## Get all Nodes from model
listNodes = JPT.GetAllNodes() # List of DNode objects
## Get 2 Nodes and convert them to DItem object
dItemNode1 = JPT.CastToDItem(listNodes[0]) # The first DItem object
dItemNode2 = JPT.CastToDItem(listNodes[1]) # The second DItem object
## Return 2 DItems to a string object, for example, return value = 10:772-10:251
JPT.Debugger(JPT.DItemToMacroTCursorPair(dItemNode1, dItemNode2))
```
