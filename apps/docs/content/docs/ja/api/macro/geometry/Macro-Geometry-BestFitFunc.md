---
title: "BestFitFunc()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Align the selected parts based on their geometric features.

## Syntax

```psj
BestFitFunc(Cursor[] crlStaticTarget, Cursor[] crlDynamicTarget, Double dError, Int iMaxCycle, int iAlgorithmsType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

A _List of Cursor_ specifying the target parts for the move operation.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

A _List of Cursor_ specifying the parts to be moved.

<!-- @since:5.1.0 -->
### 3. Double

The total difference in distance between nodes.

<!-- @since:5.1.0 -->
### 4. Int

The number of iterations for the matrix calculation.

<!-- @since:5.1.0 -->
### 5. Int

The algorithms' type (always set to 0).

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BestFitFunc([3:1], [3:2], 1e-08, 400, 0)
```
