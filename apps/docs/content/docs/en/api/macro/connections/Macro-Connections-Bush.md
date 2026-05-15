---
title: "Bush()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create bush connection

## Syntax

```psj
Bush(int iMethod, string strName, cursor[] vcrMasterTarget, cursor[] vcrSlaveTarget,
    cursor crCoord, double dTol, bool bBushGrounded, int iOriMode, bool iEqual,
    double[3] oriVector, double[] dStiffness, double[] dDampCoef, double[] dDampConst,
    double dRotStrain, double dTransStrain, double dRotStress, double dTransStress, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Bush method creation

- 1: 2 Nodes
- 16: Any Entities
- 21: One to one (Nodes with tolerance)

<!-- @since:5.0.1 -->
### 2. String

Bush name

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target master entities cursor

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Target slave entities cursor

<!-- @since:5.0.1 -->
### 5. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 6. Double

Connection tolerance to find node pair

<!-- @since:5.0.1 -->
### 7. Bool

Bush grounded bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Int

Orientation mode

- 0: Orientation vector
- 1: Coordinate system

<!-- @since:5.0.1 -->
### 9. Bool

Equal 1:1 bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 10. Double\[3]

Orientation vector

<!-- @since:5.0.1 -->
### 11. Double\[]

Stiffness value

<!-- @since:5.0.1 -->
### 12. Double\[]

Damping coefficient value

<!-- @since:5.0.1 -->
### 13. Double\[]

Damping constant value

<!-- @since:5.0.1 -->
### 14. Double

Strain recovery rotation

<!-- @since:5.0.1 -->
### 15. Double

Strain recovery translation

<!-- @since:5.0.1 -->
### 16. Double

Stress recovery rotation

<!-- @since:5.0.1 -->
### 17. Double

Stress recovery translation

<!-- @since:5.0.1 -->
### 18. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Bush(16, "BUSH _1", [10:48, 10:46], [], 0:0, 0.003, 1, 0, 1, [0, 1, 0],
    [1000, 2000, 3000, 0.004, 0.005, 0.006], [1000, 2000, 3000, 0.004, 0.005, 0.006],
    [1, 2, 3, 4, 5, 6], 4, 3, 2, 1, 0:0)
```
