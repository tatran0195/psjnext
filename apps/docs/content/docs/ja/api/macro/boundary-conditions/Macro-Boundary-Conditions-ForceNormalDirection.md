---
title: "ForceNormalDirection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Force (normal direction)

## Syntax

```psj
ForceNormalDirection(string name, vector force, int arrowDir, int distributionMethod,
    cursor crCoordinate, cursor[] targets, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. Vector

force

<!-- @since:5.0.1 -->
### 3. int

arrorDir (0: Start at node, 1: End at node)

<!-- @since:5.0.1 -->
### 4. int

distributionMethod (0: Per selected entity, 1: Per node, 2: Total of select)

<!-- @since:5.0.1 -->
### 5. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 6. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 7. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ForceNormalDirection("Force3", [0, -1, 0], 0, 0, 0:0, [6:21], 0:0)
```
