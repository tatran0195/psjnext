---
title: "InitialDynamic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Initial Condition

## Syntax

```psj
InitialDynamic(string m _strName,int m _Type,double[] fVel,BOOL bSelNodeSet,Cursor crNodeSet,
    Cursor crTable,Cursor curCoord,Cursor[] m _taTarget,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Condition name

<!-- @since:5.0.1 -->
### 2. Int

Condition Type\[0-displacement 1-velocity 2-rotation angle 3-angular velocity]

<!-- @since:5.0.1 -->
### 3. Double\[]

Condition value

<!-- @since:5.0.1 -->
### 4. Bool

selected node set

<!-- @since:5.0.1 -->
### 5. Cursor

selected node set cursor

<!-- @since:5.0.1 -->
### 6. Cursor

selected table cursor

<!-- @since:5.0.1 -->
### 7. Cursor

coordinate cursor

<!-- @since:5.0.1 -->
### 8. Cursor\[]

selected entity

<!-- @since:5.0.1 -->
### 9. Cursor

edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
InitialDynamic("InitialAngularVelocity1", 3, [1, 2, 3], 0, 0:0, 0:0, 0:0, [3:1], 0:0)
```
