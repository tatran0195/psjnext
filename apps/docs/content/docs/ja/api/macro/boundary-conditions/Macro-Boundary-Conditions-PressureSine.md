---
title: "PressureSine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pressure sine

## Syntax

```psj
PressureSine(String name, double a, Cursor crCoordinate, double angleRange, int distributionAxis,
    int pressureDirectionMode, int isTotalForceAdjustment, double totalForce, Vector pressureDirection,
    Cursor crCoordinateSystemForDirection, int isCornerNodesDistribution, String formulaForA,
    Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. double

a

<!-- @since:5.0.1 -->
### 3. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 4. double

angle range

<!-- @since:5.0.1 -->
### 5. int

distribution axis

<!-- @since:5.0.1 -->
### 6. int

direction mode (0: normal, 1: direction)

<!-- @since:5.0.1 -->
### 7. int

is total force adjustment

<!-- @since:5.0.1 -->
### 8. double

total force

<!-- @since:5.0.1 -->
### 9. Vector

pressure direction

<!-- @since:5.0.1 -->
### 10. Cursor

coordinate system for direction

<!-- @since:5.0.1 -->
### 11. int

is corner nodes distribution

<!-- @since:5.0.1 -->
### 12. String

formula for A

<!-- @since:5.0.1 -->
### 13. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 14. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PressureSine("PressureSine1", 1e+07, 0:0, 0.523599, 0, 0, 0, 0, [0, 0, 0], 0:0, 0, "", [6:23], 0:0)
```
