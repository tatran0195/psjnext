---
title: "PositionBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Position Body

## Syntax

```psj
PositionBody(Cursor[] body, Point[6] point, bool create _new, bool copy _lbc)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Body List

<!-- @since:5.0.1 -->
### 2. Point\[6]

Point: \[targetA, targetB, targetC, baseA, baseB, baseC]

<!-- @since:5.0.1 -->
### 3. bool

Create New Body 1=Yes,0=No

<!-- @since:5.0.1 -->
### 4. bool

Copy LBC 1=Yes,0=No

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PositionBody([3:8], [[0.0208889, 0.00111111, 0.01], [0.0208889, 0.00333333, 0.01],
    [0.0186667, 0.00111111, 0.01], [0.00111111, 0.00111111, 0.01], [0.00111111, 0.00333333, 0.01],
    [0.00333333, 0.00111111, 0.01]], 0, 1)
```
