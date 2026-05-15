---
title: "Pressure2Nodes()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pressure 2 nodes

## Syntax

```psj
Pressure2Nodes(string strName, cursor crNodeA, double dPressureA, int iNodeAUnit,
    cursor crNodeB, double dPressureB, int iNodeBUnit, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Pressure 2 nodes name

<!-- @since:5.0.1 -->
### 2. Cursor

Node A key cursor(10:Node ID)

<!-- @since:5.0.1 -->
### 3. Double

Pressure A value

<!-- @since:5.0.1 -->
### 4. Int

Node A unit type

<!-- @since:5.0.1 -->
### 5. Cursor

Node B key cursor(10:Node ID)

<!-- @since:5.0.1 -->
### 6. Double

Pressure B value

<!-- @since:5.0.1 -->
### 7. Int

Node B unit type

<!-- @since:5.0.1 -->
### 8. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 9. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Pressure2Nodes("PressureLinear1", 10:351, 2000, 0, 10:350, 4000, 0, 2, [6:5, 11:553, 11:554, 10:351, 10:350], 0:0)
```
