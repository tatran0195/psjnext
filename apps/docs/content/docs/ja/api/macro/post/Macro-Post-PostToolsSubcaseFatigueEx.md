---
title: "PostToolsSubcaseFatigueEx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Subcase - Fatigue.

## Syntax

```psj
PostToolsSubcaseFatigueEx(int AnaType, string Name, bool FromMaterial, float Qb, float Qw, float Qy, float Angle, string SubcaseName, int SubcaseID, Smap[] SubcaseMap, cursor[] target)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Analysis type.

<!-- @since:5.0.1 -->
### 2. string

Name

<!-- @since:5.0.1 -->
### 3. bool

From Material flag.

<!-- @since:5.0.1 -->
### 4. float

Qy

<!-- @since:5.0.1 -->
### 5. float

Qb

<!-- @since:5.0.1 -->
### 6. float

Qw

<!-- @since:5.0.1 -->
### 7. float

Angle

<!-- @since:5.0.1 -->
### 8. string

New Subcase name.

<!-- @since:5.0.1 -->
### 9. int

New subcase ID

<!-- @since:5.0.1 -->
### 10. SubcaseItem \[]

Target subcases. SubcaseItem contents are:

1. int - ID,
1. string - name,
1. double - coefficient,
1. bool - status.

<!-- @since:5.0.1 -->
### 11. cursor \[]

Target.

## Return Code

Nothing.

## Sample Code

```psj
PostToolsSubcaseFatigueEx(1, "Subcase Fatigue", 0, 270, 130, 165, 15, "Subcase Fatigue", 104, [(0, [(0, "Process= 0-Step=0, Time=1.000000e-02", 1,1), (1, "Process= 0-Step=1, Time=2.000000e-02", 1,1), (2, "Process= 0-Step=2, Time=3.000000e-02", 1,1), (3, "Process= 0-Step=3, Time=4.000000e-02", 1,1), (4, "Process= 0-Step=4, Time=5.000000e-02", 1,0), (5, "Process= 0-Step=5, Time=6.000000e-02", 1,0)])], [3:1])
```
