---
title: "JPT.MacroTCursorToDItem()"
description: "Convert cursor (Macro string type) to a DItem object"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert cursor (Macro string type) to a _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Syntax

```psj
JPT.MacroTCursorToDItem(cursor)
```

## Inputs

### `cursor` @type(String) @required

- The cursor (Macro string type).

## Return Code

A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Convert to DItem and get all the information of the created Cube_1
dItem = JPT.Debugger(JPT.MacroTCursorToDItem("3:1"))
JPT.Debugger(dItem)
```
