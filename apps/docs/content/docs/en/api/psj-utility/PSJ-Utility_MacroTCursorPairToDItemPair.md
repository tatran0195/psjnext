---
title: "JPT.MacroTCursorPairToDItemPair()"
description: "Convert cursor pair (Macro string type) to a pair of DItem object"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert cursor pair (Macro string type) to a pair of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Syntax

```psj
JPT.MacroTCursorPairToDItemPair(cursorPair)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `cursorPair`

- The cursor pair (Macro string type).

## Return Code

A _[DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ object.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=7730934)
JPT.ViewFitToModel()

# Get all the information of the 2 created cubes
dItemPair = JPT.Debugger(JPT.MacroTCursorPairToDItemPair("3:1-3:2"))
JPT.Debugger(dItemPair.firstDItem)
JPT.Debugger(dItemPair.secondDItem)
```
