---
title: "JPT.ListDoubleToMacroVector()"
description: "Convert a list of 3 double values to a vector3d (Macro string type)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert a _List_ of 3 _Double_ values to a Vector3D (Macro string type).

## Syntax

```psj
JPT.ListDoubleToMacroVector(doubleValue1, doubleValue2, doubleValue3)
```

## Inputs

<!-- @since:5.0.1 @type:Double @required -->
### `doubleValue1`

- The first value which will be used for converting.

<!-- @since:5.0.1 @type:Double @required -->
### `doubleValue2`

- The second value which will be used for converting.

<!-- @since:5.0.1 @type:Double @required -->
### `doubleValue3`

- The third value which will be used for converting.

## Return Code

A _String_ specifying the converted Vector3D (Macro string type).

## Sample Code

```psj {6}
# Convert a list of 3 double values to a vector3d (Macro string type)
inputValue1 = 0.001
inputValue2 = 2.1
inputValue3 = 5.5
# Return a string object with value = [0.001,2.1,5.5]
JPT.Debugger(JPT.ListDoubleToMacroVector(inputValue1, inputValue2, inputValue3))
```
