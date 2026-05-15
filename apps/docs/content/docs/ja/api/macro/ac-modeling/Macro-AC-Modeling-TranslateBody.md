---
title: "TranslateBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Translate Body

## Syntax

```psj
TranslateBody(cursor[] body, double[3] trans _vector, cursor coordinate, bool create _new,
    bool copy _lbc, int copy _count)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Body List

<!-- @since:5.0.1 -->
### 2. double\[3]

Translation Vector

<!-- @since:5.0.1 -->
### 3. Cursor

Reference Coordinate

<!-- @since:5.0.1 -->
### 4. Bool

Create New Body 1=Yes, 0=No

<!-- @since:5.0.1 -->
### 5. Bool

Copy LBC 1=Yes, 0=No

<!-- @since:5.0.1 -->
### 6. Int

Copy Count

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TranslateBody([3:2], [[0.002, 0, 0]], 0:0, 0, 0, 0)
```
