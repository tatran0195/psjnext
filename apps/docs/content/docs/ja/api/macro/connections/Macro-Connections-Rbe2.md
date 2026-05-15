---
title: "Rbe2()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create rbe2 connection

## Syntax

```psj
Rbe2(int iMethod, cursor[] taMasterTarget, cursor[] taSlaveTarget, int eType, string strName,
    cursor crCoord, double dTol, int ulDofs, double[3] virtualNodePos, int iSurfaceDef,
    cursor crEdit, bool bUpdateDispCS, bool bCornerOnly, int iDuplicatedMode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Rbe2 method creation

- 16: One to many
- 17: One to one
- 18: To center
- 19: To circle center
- 21: One to one (Nodes with tolerance)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target master entities cursor

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target slave entities cursor

<!-- @since:5.0.1 -->
### 4. Int

RBE2 type = 2

<!-- @since:5.0.1 -->
### 5. String

RBE2 name

<!-- @since:5.0.1 -->
### 6. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 7. Double

Search area tolerance

<!-- @since:5.0.1 -->
### 8. Int

Reference DOFs attribute

<!-- @since:5.0.1 -->
### 9. Double\[3]

used in center of any entities and circle center circumference

<!-- @since:5.0.1 -->
### 10. Int

Surface definition output

- 0: By node set
- 1: By element set

<!-- @since:5.0.1 -->
### 11. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 12. Bool

update display bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 13. Bool

Only corner nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 14. Int

duplicated mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Rbe2(17, [10:224983], [10:157853], 2, "RBE2 _1", 0:0, 0, 63, [0, 0, 0], 0, 0:0, 1, 0, -1)
```
