---
title: "RenumberE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

RenumberE

## Syntax

```psj
RenumberE(renumberItem[] Item, bool AssignProperty, bool SurfaceCornerFirst)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. RenumberItem\[]

RenumberItem is a list:

- Cursor Target
- int Begin
- int NodeOrElem
- int Counter
- int Increasement
- int Order
- int Method
- Cursor CoordinateReference
- int\[] CoordinateOrder
- int\[] Offset
- double\[] CoordinateTolerance
- int ConflictStrategy
- int Solver
- bool Enable

<!-- @since:5.0.1 -->
### 2. Bool

Property Assigned flag True = 1, False =0

<!-- @since:5.0.1 -->
### 3. Bool

Surface Corner first flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RenumberE([(3:1, 1, 0, 7743, 0, 0, 0, 0:0, [0, 0, 0], [10000, 100, 1], [0.1, 0.1, 0.1], 0, 0, 1)], 1, 0)
```
