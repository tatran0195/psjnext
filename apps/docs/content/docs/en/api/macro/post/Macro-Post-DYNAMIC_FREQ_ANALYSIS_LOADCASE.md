---
title: "DYNAMIC _FREQ _ANALYSIS _LOADCASE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Load Case of Frequency Analysis

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _LOADCASE(int AnalysisType, cursor ParentAnalysis, string Name, double Factor, int newID, cursor[] SelLoad, double[] targetFactor, cursor EditTarget)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Analysis type

<!-- @since:5.0.1 -->
### 2. cursor

Parent analysis

<!-- @since:5.0.1 -->
### 3. string

Name

<!-- @since:5.0.1 -->
### 4. double

Coefficient

<!-- @since:5.0.1 -->
### 5. int

ID

<!-- @since:5.0.1 -->
### 6. cursor\[]

Selected Loads

<!-- @since:5.0.1 -->
### 7. double\[]

Coefficients of each selected load.

<!-- @since:5.0.1 -->
### 8. cursor

Target load case when modify.

## Return Code

Nothing.

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _LOADCASE(1, 195:1, "LoadCase1", 3, 2, [197:3, 197:4], [1, 4], 0:0)
```
