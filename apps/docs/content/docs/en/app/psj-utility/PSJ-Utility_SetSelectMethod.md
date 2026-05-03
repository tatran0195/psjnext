---
title: "JPT.SetSelectMethod()"
description: "Change the selection method in Jupiter to the specified one"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Change the selection method in Jupiter to the specified one.

## Syntax

```psj
JPT.SetSelectMethod(selectMethodType)
```

## Inputs

### `selectMethodType` @type(Enum) @required

- Th&#x65;_[SelectMethodType](../data-type/psj-utility/pre-utility/enumeration-types/select-method-types)_&#x64;escribing the selection method.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,5,8,11}
# Select method to Body selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_BODY)

# Select method to Face selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_FACE)

# Select method to Edge selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_EDGE)

# Select method to Node selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_NODE)
```
