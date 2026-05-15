---
title: "RBarOneToMany()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create one-to-many RBAR (rigid elements) connection

## Syntax

```psj
RBarOneToMany(string strName, cursor[] taMasterTarget, cursor[] taSlaveTarget, int iMethod, int ulDofs, double dTol,
            cursor crCoord, bool bUpdateDispCS, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

RBAR name

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Target master entities cursor

<!-- @since:5.1.0 -->
### 3. Cursor\[]

Target slave entities cursor

<!-- @since:5.1.0 -->
### 4. Int

Rbe2 method creation

- 16: One to many

<!-- @since:5.1.0 -->
### 5. Int

Reference DOFs attribute

<!-- @since:5.1.0 -->
### 6. Double

Search area tolerance

<!-- @since:5.1.0 -->
### 7. Cursor

Whether use local coordinate or not: True = 27:\*, False = 0:0

<!-- @since:5.1.0 -->
### 8. Bool

Update displacement coordinate system, bool flag: True = 1, False = 0

<!-- @since:5.1.0 -->
### 9. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RBarOneToMany("RBar _1", [10:493], [10:6, 10:2, 10:3], 16, 63, 0, 0:0, 1, 0:0)
```
