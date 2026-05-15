---
title: "ConnectGap()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create gap connection

## Syntax

```psj
ConnectGap(cursor[] taEntityMaster, cursor[] taEntitySlave, int iMethod, int OrientType,
    cursor crCoord, string strName, double dU0, double dF0, double dKa, double dKb,
    double dKt, double dMar, double dMu1, double dMu2, double[3] orientVec,
    double dTmax, double dRadius, double dTRmin, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target entity master cursor(\[CursorType:CursorType ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target entity slave cursor(\[CursorType:CursorType ID])

<!-- @since:5.0.1 -->
### 3. Int

Method type

- 1: 2 Nodes
- 2: 2 Edges
- 3: 2 Faces

<!-- @since:5.0.1 -->
### 4. Int

Gap orientation by

- 0: Orientation vector
- 1: Coordinate system

<!-- @since:5.0.1 -->
### 5. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 6. String

Name of gap

<!-- @since:5.0.1 -->
### 7. Double

U0 value

<!-- @since:5.0.1 -->
### 8. Double

F0 value

<!-- @since:5.0.1 -->
### 9. Double

KA value

<!-- @since:5.0.1 -->
### 10. Double

KB value

<!-- @since:5.0.1 -->
### 11. Double

KT value

<!-- @since:5.0.1 -->
### 12. Double

Mar value

<!-- @since:5.0.1 -->
### 13. Double

MU1 value

<!-- @since:5.0.1 -->
### 14. Double

MU2 value

<!-- @since:5.0.1 -->
### 15. Double\[3]

Orientation vector coordinate

<!-- @since:5.0.1 -->
### 16. Double

TMax value

<!-- @since:5.0.1 -->
### 17. Double

Radius to find node pair

<!-- @since:5.0.1 -->
### 18. Double

TRmin value

<!-- @since:5.0.1 -->
### 19. Cursor

Used in edit mode to specify edited object

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ConnectGap([6:62], [6:60], 3, 1, 27:1, "GAP _11", 0.001, 1, 1000, 1000, 1000, 1,
    1, 1, [0, 1, 0], 0.002, 0.05, 2, 0:0)
```
