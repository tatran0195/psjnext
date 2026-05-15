---
title: "Macro-Calculation-PostToolsSubcasePeakHoldEx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases.

## Syntax

```psj
PostToolsSubcasePeakHoldEx(int iAnalysisType, bool bFatigue, double dQb, double dQw, double dQy, str strSubcaseName, int iSubcaseID, map mapPeakHoldSubcases)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the analysis type.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether to use the fatigue calculation.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the tension strength of the material.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the material fatigue limit.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the yield stress of the material.

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the name of new subcase to be created.

<!-- @since:5.1.0 -->
### 7. int

- An Integer specifying the ID of new subcase to be created.

<!-- @since:5.1.0 -->
### 8. map

- A Map of _[PEAKHOLD\_SUBCASE\_MAP](../../data-type/psj-command/parameter-types/PEAKHOLD _SUBCASE _MAP)_ specifying the selected subcases to create peakhold results.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostToolsSubcasePeakHoldEx(1, 1, 270.0, 130.0, 165.0, "Subcase 1 Peak Hold", 1, [(1, [(1, "", 1, 1), (2, "", 1, 1), (3, "", 1, 1), (4, "", 1, 1), (5, "", 1, 1)])])
```
