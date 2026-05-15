---
title: "DYNAMIC _FREQ _ANALYSIS _LOADCASE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a load case for Gururi analysis.

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _LOADCASE(int AnalysisType, cursor ParentAnalysis, string Name, double Factor, int NewID, cursor[] SelectedLoad, double[] TargetFactor, cursor Edit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

Choose type of analysis.

<!-- @since:5.1.0 -->
### 2. Cursor

A Cursor specifying the parent analysis.

<!-- @since:5.1.0 -->
### 3. String

Name of the load case.

<!-- @since:5.1.0 -->
### 4. Double

A Double specifying the factor of load case.

<!-- @since:5.1.0 -->
### 5. Int

New ID of the load case.

<!-- @since:5.1.0 -->
### 6. Cursor\[]

A Cursor List specifying the selected load.

<!-- @since:5.1.0 -->
### 7. Double\[]

A Double List specifying the target factor.

<!-- @since:5.1.0 -->
### 8. Cursor

A Cursor specifying an existing load case condition.

## Return Code

A Cursor specifying the created gururi load case.

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _LOADCASE(1, 3:1, "LoadCase _1", 1.0, 1, [], [1.0], 0:0)
```
