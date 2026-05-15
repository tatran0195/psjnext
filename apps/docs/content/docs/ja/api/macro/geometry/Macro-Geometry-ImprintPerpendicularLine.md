---
title: "ImprintPerpendicularLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Perpendicular line

## Syntax

```psj
ImprintPerpendicularLine(cursor[] nodes, cursor[] faces, double offset, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Double

Insert offset value

<!-- @since:5.0.1 -->
### 4. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintPerpendicularLine([10:218, 10:190], [6:22], 0.002, 1)
```
