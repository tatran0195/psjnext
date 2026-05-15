---
title: "ForceQuadratic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Force (Quadratic)

## Syntax

```psj
ForceQuadratic(String name, double totalForce, double a, double b, Cursor crCoordinate,
    int angleBase, double angleRange, int arrowDir, Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. Double

total force

<!-- @since:5.0.1 -->
### 3. Double

a

<!-- @since:5.0.1 -->
### 4. Double

b

<!-- @since:5.0.1 -->
### 5. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 6. Int

angle base

<!-- @since:5.0.1 -->
### 7. Double

angle range

<!-- @since:5.0.1 -->
### 8. Int

arrorDir (0: Start at node, 1: End at node)

<!-- @since:5.0.1 -->
### 9. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 10. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ForceQuadratic("Force2", 1, 2, 3, 0:0, 0, 1.5708, 0, [6:22], 0:0)
```
