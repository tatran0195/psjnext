---
title: "MC _Intersection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Intersection

## Syntax

```psj
MC _Intersection(cursor[] crBody, double dTol, int iDispType, int iNoLayer, bool bErrText)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double

Number of edges tolerance

<!-- @since:5.0.1 -->
### 3. Int

Display intersection type

- 0: Body intersection only
- 1: All intersection
- 2: Between bodies intersection

<!-- @since:5.0.1 -->
### 4. Int

Number of intersection layer

<!-- @since:5.0.1 -->
### 5. Bool

Error text bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC _Intersection([3:1], 0, 0, 1, 0)
```
