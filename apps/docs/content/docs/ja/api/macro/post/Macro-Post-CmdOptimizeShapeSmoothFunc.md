---
title: "CmdOptimizeShapeSmoothFunc()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Smoothing topology optimization result

## Syntax

```psj
CmdOptimizeShapeSmoothFunc(cursor [], cursor [], double tol, int nlayer, int cycle, double factor, double meshSize, bool keep)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor\[]

Designed parts

<!-- @since:5.1.0 -->
### 2. cursor\[]

Non-designed parts

<!-- @since:5.1.0 -->
### 3. double

Tolerance of density

<!-- @since:5.1.0 -->
### 4. int

Number of remove layer

<!-- @since:5.1.0 -->

#### 5. int

Number of looping

<!-- @since:5.1.0 -->

#### 6. double

factor

<!-- @since:5.1.0 -->

#### 7. double

Mesh size

<!-- @since:5.1.0 -->
### 8. bool

Keep shared nodes

## Return Code

Nothing.

## Sample Code

```psj
CmdOptimizeShapeSmoothFunc([3:1], [], 0.670000, 1, 50, 0.300000, 0.002845, 0)
```
