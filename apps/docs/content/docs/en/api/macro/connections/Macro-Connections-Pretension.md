---
title: "Pretension()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create pretension

## Syntax

```psj
Pretension(string strName, int iDir, double dValue, bool bFixLength, cursor crTable,
    cursor crCoord, int iLocalUnit, cursor[] taFace, cursor crEdit, bool bIfCreate2ADVCStatic)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Pretension name

<!-- @since:5.0.1 -->
### 2. Int

Pretension direction

- 0: UX
- 1: UY
- 2: UZ

<!-- @since:5.0.1 -->
### 3. Double

Pretension force value

<!-- @since:5.0.1 -->
### 4. Bool

Bolt FixLength bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Cursor

Table cursor

<!-- @since:5.0.1 -->
### 6. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 7. Int

unit index

<!-- @since:5.0.1 -->
### 8. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 9. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 10. Bool

Create 2 ADVC Static bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Pretension("BoltLoad007", 2, 0.05, 1, 0:0, 27:1, 0, [6:180, 6:178], 0:0, 0)
```
