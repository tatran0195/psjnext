---
title: "ContactClearance()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create contact clearance

## Syntax

```psj
ContactClearance(string strName, double dClearanceVal, int iLocalUnit,
    int iSolverType, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Structural name

<!-- @since:5.0.1 -->
### 2. Double

Clearance value

<!-- @since:5.0.1 -->
### 3. Int

Input Unit

- 0: Mm
- 1: M
- 2: Ft
- 3: In
- 4: Cm

<!-- @since:5.0.1 -->
### 4. Int

Solver type

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
ContactClearance("ContactClearance1", 0.002, 0, 0, [10:452, 6:26], 0:0)
```
