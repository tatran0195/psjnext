---
title: "ForceSine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Force (Sine)

## Syntax

```psj
ForceSine(String name, double totalForce, double a, Cursor crCoordinate, int angleBase,
    double angleRange, int arrowDir, int distributeInAxis, Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. double

total force

<!-- @since:5.0.1 -->
### 3. Double

a

<!-- @since:5.0.1 -->
### 4. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 5. Int

angle base

<!-- @since:5.0.1 -->
### 6. Double

angle range

<!-- @since:5.0.1 -->
### 7. Int

arrorDir (0: Start at node, 1: End at node)

<!-- @since:5.0.1 -->
### 8. Int

distributed in axis (0: false, 1: true)

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
ForceSine("Force3", 1, 2, 0:0, 0, 1.5708, 0, 0, [6:22], 0:0)
```
