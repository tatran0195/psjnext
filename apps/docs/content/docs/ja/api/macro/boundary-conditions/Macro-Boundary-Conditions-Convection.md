---
title: "Convection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create convection

## Syntax

```psj
Convection(string strName, double dExtTemp, cursor crTimeTempTbl, double dCoef,
    cursor crTimeCoefTbl, cursor crTempCoefTbl, cursor crTargets, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Convection name

<!-- @since:5.0.1 -->
### 2. Double

External temperature

<!-- @since:5.0.1 -->
### 3. Cursor

Time temperature table cursor(\[81:FieldData ID])

<!-- @since:5.0.1 -->
### 4. Double

Convection coefficient value

<!-- @since:5.0.1 -->
### 5. Cursor

Time dependent coefficient table

<!-- @since:5.0.1 -->
### 6. Cursor

Time temperature dependent coefficient table

<!-- @since:5.0.1 -->
### 7. Cursor\[]

Target Entities

<!-- @since:5.0.1 -->
### 8. Cursor

Cursor edit

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Convection("Convection _1", 373.15, 81:1, 2000, 81:1, 81:1, [6:3, 11:764], 0:0)
```
