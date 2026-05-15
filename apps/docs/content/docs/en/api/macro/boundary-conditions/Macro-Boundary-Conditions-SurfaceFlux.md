---
title: "SurfaceFlux()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create surface flux

## Syntax

```psj
SurfaceFlux(string strName, double dFlux, int iDistributionMethod, cursor crTable, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Surface flux name

<!-- @since:5.0.1 -->
### 2. Double

Surface flux value

<!-- @since:5.0.1 -->
### 3. Int

Input unit type\*

- 0: MW/mm^2
- 1: W/m^2
- 2:MiuW/mm^2
- 3: kcal/mm^2\*h
- 4: Lbf/ft\*s
- 5: Lbf/in\*s

<!-- @since:5.0.1 -->
### 4. Cursor

Table field data cursor(81:FieldData ID)

<!-- @since:5.0.1 -->
### 5. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 6. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SurfaceFlux("SurfaceHeatFlux1", 1000, 1, 81:4, [6:3, 11:693], 0:0)
```
