---
title: "RBE2OneToOne()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create one-to-one RBE2 (rigid elements) connection

## Syntax

```psj
RBE2OneToOne(int iMethod, cursor[] taMasterTarget, cursor[] taSlaveTarget, int eType, string strName,
    cursor crCoordSys, double dTol, int ulDofs, double[3] virtualNodePos, int iSurfaceDef,
    cursor crEdit, int iEnableUpdateDispCS, int iEnableCornerOnly, int iEnableCheckDuplicate, int iDuplicatedMode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

Rbe2 method creation

- 17: One to one

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Target master entities cursor

<!-- @since:5.1.0 -->
### 3. Cursor\[]

Target slave entities cursor

<!-- @since:5.1.0 -->
### 4. Int

Rbe2 type creation

- RBE2 type = 2

<!-- @since:5.1.0 -->
### 5. String

RBE2 name

<!-- @since:5.1.0 -->
### 6. Cursor

Whether use local coordinate or not: True = 27:\*, False = 0:0

<!-- @since:5.1.0 -->
### 7. Double

Search area tolerance

<!-- @since:5.1.0 -->
### 8. Int

Reference DOFs attribute

<!-- @since:5.1.0 -->
### 9. Double\[3]

Used in center of any entities and circle center circumference

<!-- @since:5.1.0 -->
### 10. Int

Surface definition output

- 0: By node set
- 1: By element set

<!-- @since:5.1.0 -->
### 11. Cursor

Edit cursor

<!-- @since:5.1.0 -->
### 12. Int

Update displacement coordinate system

<!-- @since:5.1.0 -->
### 13. Int

Enable only corner nodes

<!-- @since:5.1.0 -->
### 14. Int

Enable duplication check

<!-- @since:5.1.0 -->
### 15. Int

Duplication mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RBE2OneToOne(17, [10:935], [10:469], 2, "RBE2 _2", 0:0, 0, 63, [0, 0, 0], 0, 0:0, 1, 0, 1, 0)
```
