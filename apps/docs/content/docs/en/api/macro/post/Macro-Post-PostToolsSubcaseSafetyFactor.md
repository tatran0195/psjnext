---
title: "PostToolsSubcaseSafetyFactor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Subcase - Safety Factor.

## Syntax

```psj
PostToolsSubcaseSafetyFactor(int AnaType, int RltSet, SubcaseItem[] SubCases, SafetyItem[] SafetyItems, int ThresholdType, string RltName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Analysis type.

<!-- @since:5.0.1 -->
### 2. int

Result Set.

<!-- @since:5.0.1 -->
### 3. SubcaseItem \[]

Target subcases. SubcaseItem contents are:

1. int - ID,
1. string - name,
1. double - coefficient,
1. bool - status.

<!-- @since:5.0.1 -->
### 4. SafetyItem \[]

Target item. SafetyItem contents are:

1. cursor - parts,
1. double - threshold.

<!-- @since:5.0.1 -->
### 5. int

Threshold Type

<!-- @since:5.0.1 -->
### 6. string

Result name.

## Return Code

Nothing.

## Sample Code

```psj
PostToolsSubcaseSafetyFactor(1, 0, [(0, "Step=0, Time=1.000000e-02", 1,1), (1, "Step=1, Time=2.000000e-02", 1,1), (2, "Step=2, Time=3.000000e-02", 1,1)], [(3:1, 0)], 0, "Safety Yield")
```
