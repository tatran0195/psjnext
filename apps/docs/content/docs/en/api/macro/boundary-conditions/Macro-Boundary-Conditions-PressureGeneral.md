---
title: "PressureGeneral()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pressure general

## Syntax

```psj
PressureGeneral(string strName, double pressure, int distrbute, cursor crTable,
    double phase, double delay, cursor phaseTable, string formulaValue, cursor crCoord,
    cursor[] dirPressCoord, string formulaDirX, string formulaDirY, string formulaDirZ,
    int arrowDir, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Pressure general name

<!-- @since:5.0.1 -->
### 2. Double

Pressure value

<!-- @since:5.0.1 -->
### 3. Int

N/A distribution method

- 0: Per selected entity
- 1: Per node
- 2: Total of select

<!-- @since:5.0.1 -->
### 4. Cursor

Table field data cursor(81:FieldData ID)

<!-- @since:5.0.1 -->
### 5. Double

Phase value

<!-- @since:5.0.1 -->
### 6. Double

delay value

<!-- @since:5.0.1 -->
### 7. Cursor

Table phase field data cursor

<!-- @since:5.0.1 -->
### 8. String

Formula value

<!-- @since:5.0.1 -->
### 9. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 10. Cursor\[]

Pressure direction R, Theta, Z

<!-- @since:5.0.1 -->
### 11. String

Formula X direction

<!-- @since:5.0.1 -->
### 12. String

Formula Y direction

<!-- @since:5.0.1 -->
### 13. String

Formula Z direction

<!-- @since:5.0.1 -->
### 14. Int

Arrow direction

- 0: Start at node
- 1: End at node

<!-- @since:5.0.1 -->
### 15. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 16. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PressureGeneral("Pressure1", 5000, 0, 81:1, 0.0174533, 2, 81:3, "", 27:1, [1, 2, 3], "", "", "", 1, [6:5, 11:700, 11:699], 0:0)
```
