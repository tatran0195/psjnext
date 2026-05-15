---
title: "JPT.MacroListTCursorToListDItem()"
description: "Convert a cursor list (Macro string type) to a DItemVector"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert a cursor list (Macro string type) to a _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_.

## Syntax

```psj
JPT.MacroListTCursorToListDItem(cursorList)
```

## Inputs

<!-- @since:5.0.1 @required -->
### cursorList

- Specify the cursor list (Macro string type).

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the converted items.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube()

# Convert a cursor list (Macro string type) to a DItemVector
## Create a list of Node cursor
strCursorNode1 = "10:467"
strCursorNode2 = "10:477"
strCursorNode3 = "10:483"
listCursorNode = f"[{strCursorNode1}, {strCursorNode2}, {strCursorNode3}]"
## Convert cursor list to list of DItem
JPT.Debugger(JPT.MacroListTCursorToListDItem(listCursorNode))
```
