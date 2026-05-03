---
title: "JPT.ShowHideAllParts()"
description: "Show or Hide all part existing on the screen"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show or Hide all part existing on the screen.

## Syntax

```psj
JPT.ShowHideAllParts(BoolType)
```

## Inputs

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the display mode:
  - _False_: Hide all parts.
  - _True_: Show all parts.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {8}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Show all parts
JPT.ShowHideAllParts(JPT.BoolType.TRUE_VAL)
```
