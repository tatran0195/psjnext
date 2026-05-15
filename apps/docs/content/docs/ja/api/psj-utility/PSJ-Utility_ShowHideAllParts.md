---
title: "JPT.ShowHideAllParts()"
description: "Show or Hide all part existing on the screen"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show or Hide all part existing on the screen.

## Syntax

```psj
JPT.ShowHideAllParts(BoolType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
  - _False_: Hide all parts.
  - _True_: Show all parts.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2")
Geometry.Part.Cube(strName="Cube _3")
JPT.ViewFitToModel()

# Show all parts
JPT.ShowHideAllParts(JPT.BoolType.TRUE _VAL)
```
