---
title: "FixedConstraint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create fixed constraint

## Syntax

```psj
FixedConstraint(string name, int dof, Cursor crCoord, int functionType, int USETType,
    bool bAbqOpt,Cursor crTable, Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. Int

dof

<!-- @since:5.0.1 -->
### 3. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 4. Int

function type (0: Constraint, 1: Support, 2: USET)

<!-- @since:5.0.1 -->
### 5. Int

USET type (0: None, 1: U1, 2: U2, 3: U3, 4: U4, 5: U5, 6: U6)

<!-- @since:5.0.1 -->
### 6. Bool

Fixed Abaqus option bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Cursor

table

<!-- @since:5.0.1 -->
### 8. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 9. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
FixedConstraint("Constraint1", 7, 0:0, 0, 0, 0:0, [6:26], 0:0)
```
