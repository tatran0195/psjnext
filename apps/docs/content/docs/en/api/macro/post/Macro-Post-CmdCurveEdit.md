---
title: "CmdCurveEdit()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Edit Line Format.

## Syntax

```psj
CmdCurveEdit(int dxCurve, string Name, color col, int LineType, int SymbolType, int Thick, int SymbolThick, bool 13OCT)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Post job.

<!-- @since:5.0.1 -->
### 2. string

Title

<!-- @since:5.0.1 -->
### 3. color

Line Color

<!-- @since:5.0.1 -->
### 4. int

Dash Line Type

<!-- @since:5.0.1 -->
### 5. int

Marker Type

<!-- @since:5.0.1 -->
### 6. int

Line Weight

<!-- @since:5.0.1 -->
### 7. int

Marker Size

<!-- @since:5.0.1 -->
### 8. bool

1/3 OCT flag

## Return Code

Nothing.

## Sample Code

```psj
CmdCurveEdit(1, "Curve1", 16711935, 0, 0, 1, 4, 0)
```
