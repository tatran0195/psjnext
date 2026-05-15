---
title: "EnforcedDisplacement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create enforced displacement

## Syntax

```psj
EnforcedDisplacement(string strName, int dwDof, double dTransR, double dTransTheta,
    double dTransZ, double dRotR, double dRotTheta, double dRotZ, cursor crCoord,
    int iArrowDir, cursor crTable, cursor crNodeSet, double dPhase, double dDelay,
    cursor crPhaseTable, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Enforced displacement name

<!-- @since:5.0.1 -->
### 2. Int

Reference DOFs attribute

<!-- @since:5.0.1 -->
### 3. Double

Translation R

<!-- @since:5.0.1 -->
### 4. Double

Translation Theta

<!-- @since:5.0.1 -->
### 5. Double

Translation Z

<!-- @since:5.0.1 -->
### 6. Double

Rotate R

<!-- @since:5.0.1 -->
### 7. Double

Rotate Theta

<!-- @since:5.0.1 -->
### 8. Double

Rotate Z

<!-- @since:5.0.1 -->
### 9. Cursor

Whether use local coordinate or not True = 27:, False = 0:0

<!-- @since:5.0.1 -->
### 10. Int

Arrow direction

- 0: Start at node
- 1: End at node

<!-- @since:5.0.1 -->
### 11. Cursor

Table field data cursor(81:FieldData ID)

<!-- @since:5.0.1 -->
### 12. Cursor

Table node set

<!-- @since:5.0.1 -->
### 13. Double

Phase value

<!-- @since:5.0.1 -->
### 14. Double

Delay value

<!-- @since:5.0.1 -->
### 15. Cursor

Phase table cursor

<!-- @since:5.0.1 -->
### 16. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 17. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EnforcedDisplacement("EnforcedDisplacement1", 63, 0.001, 0.002, 0.003, 1, 2, 3, 27:1,
    0, 81:1, 0:0, 1, 1, 0:0, [6:3, 5:1, 10:70], 0:0)
```
