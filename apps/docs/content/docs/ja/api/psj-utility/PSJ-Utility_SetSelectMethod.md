---
title: "JPT.SetSelectMethod()"
description: "Change the selection method in Jupiter to the specified one"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change the selection method in Jupiter to the specified one.

## Syntax

```psj
JPT.SetSelectMethod(selectMethodType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### selectMethodType

- Specify the_[SelectMethodType](../data-type/psj-utility/pre-utility/enumeration-types/select-method-types)_ describing the selection method.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,5,8,11}
# Select method to Body selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD _BODY)

# Select method to Face selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD _FACE)

# Select method to Edge selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD _EDGE)

# Select method to Node selection
JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD _NODE)
```
