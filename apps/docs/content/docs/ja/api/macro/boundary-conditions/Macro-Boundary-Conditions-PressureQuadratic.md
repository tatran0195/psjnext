---
title: "PressureQuadratic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pressure quadratic

## Syntax

```psj
PressureQuadratic(string name, double a, double b, Cursor crCoordinate, double angleRange,
    int pressureDirectionMode, Vector pressureDirection, Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. double

a

<!-- @since:5.0.1 -->
### 3. double

b

<!-- @since:5.0.1 -->
### 4. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 5. double

angle range

<!-- @since:5.0.1 -->
### 6. int

direction mode (0: normal, 1: direction)

<!-- @since:5.0.1 -->
### 7. Vector

pressure direction

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
PressureQuadratic("PressureQuadratic1", 1e+06, 2e+06, 0:0, 0.523599, 0, [0, 0, 0], [6:23], 0:0)
```
