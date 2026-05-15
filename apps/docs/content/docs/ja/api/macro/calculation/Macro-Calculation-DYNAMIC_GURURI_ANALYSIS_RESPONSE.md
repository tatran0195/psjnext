---
title: "DYNAMIC _GURURI _ANALYSIS _RESPONSE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Output the Gururi result of the response point.

## Syntax

```psj
DYNAMIC _GURURI _ANALYSIS _RESPONSE(cursor ParentAnalysis, cursor Coordinate, bool AllModesUsed, string[] SelectedModesName, bool UseDampingFactor, double DampingFactor, cursor DampingFactorTable, double InputFrequency, double StartPhase, int StepNumber, bool OutputMaximumGururiResult, int PrincipleType, bool AllCase, cursor SelectedLoadCase, cursor Edit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor

A Cursor specifying the parent analysis.

<!-- @since:5.1.0 -->
### 2. Cursor

A Cursor specifying the coordinate.

<!-- @since:5.1.0 -->
### 3. Bool

A Boolean specifying whether to use the all modes used.

<!-- @since:5.1.0 -->
### 4. String\[]

A String List specifying names of the selected modes.

<!-- @since:5.1.0 -->
### 5. Bool

Specify whether to input value of damping factor with double format or table format.

<!-- @since:5.1.0 -->
### 6. Double

A Double specifying value of the damping factor with doule format.

<!-- @since:5.1.0 -->
### 7. Cursor

A Double specifying value of the damping factor with table format.

<!-- @since:5.1.0 -->
### 8. Double

A Double specifying input of the frequency.

<!-- @since:5.1.0 -->
### 9. Double

A Double specifying start of the phase.

<!-- @since:5.1.0 -->
### 10. Int

An Int specifying the number of steps.

<!-- @since:5.1.0 -->
### 11. Bool

A Boolean specifying whether to output the maximum Gururi results.

<!-- @since:5.1.0 -->
### 12. Int

An Int specifying type of principle.

<!-- @since:5.1.0 -->
### 13. Bool

A Boolean specifying whether to use the all cases.

<!-- @since:5.1.0 -->
### 14. Cursor

A Cursor specifying the selected load case.

<!-- @since:5.1.0 -->
### 15. Cursor

A Cursor specifying an existing response condition.

## Return Code

A Cursor specifying the created gururi response condition.

## Sample Code

```psj
DYNAMIC _GURURI _ANALYSIS _RESPONSE(3:1, 2:1, True, [], True, 1.0, 2:1, 0.0, 0.0, 10, True, 3, True, 2:1, 2:1)
```
