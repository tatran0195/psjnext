---
title: "ResultOutputList()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export List.

## Syntax

```psj
ResultOutputList(string FilePath, cursor[] taBody, int ResultType, int Output, bool OutPutType, int Target, bool MidNode, int[] PostResultKeyAnalysis, int[] PostResultKeyResultSet, int[] PostResultKeyTimeStep, int[] PostResultKeyCatType)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Export file path.

<!-- @since:5.0.1 -->
### 2. cursor\[]

Target entity list.

<!-- @since:5.0.1 -->
### 3. int

Result Type.

<!-- @since:5.0.1 -->
### 4. int

Output type.

<!-- @since:5.0.1 -->
### 5. bool

All parts flag.

<!-- @since:5.0.1 -->
### 6. int

Target

<!-- @since:5.0.1 -->
### 7. bool

Mid Node flag.

<!-- @since:5.0.1 -->
### 8. int \[]

Post Result Key Analysis

<!-- @since:5.0.1 -->
### 9. int \[]

Post Result Key Result Set

<!-- @since:5.1.0 -->
### 10. int \[]

Post Result Key Time Step

<!-- @since:5.1.0 -->
### 11. int \[]

Post Result Key Cat Type

## Return Code

Nothing.

## Sample Code

```psj
ResultOutputList("C:/temp/file.csv", [3:7, 3:8, 3:9, 3:2], 7, 0, 0, 0, 1, [1, 1, 1], [0, 0, 0], [0, 2, 4], [0, 0, 0])
```
