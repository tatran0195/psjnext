---
title: "PostToolsSubcasePeakHoldEx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Subcase - Peak Hold.

## Syntax

```psj
PostToolsSubcasePeakHoldEx(int analysisType, bool Fatigue, float Qb, float Qw, float Qy, string SubcaseName, int SubcaseID, map[] SubcaseMap)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Analysis type.

<!-- @since:5.0.1 -->
### 2. bool

Fatigue parameter flag.

<!-- @since:5.0.1 -->
### 3. float

Qy

<!-- @since:5.0.1 -->
### 4. float

Qb

<!-- @since:5.0.1 -->
### 5. float

Qw

<!-- @since:5.0.1 -->

#### 6. string

Name

<!-- @since:5.0.1 -->

#### 7. int

ID

<!-- @since:5.0.1 -->

#### 8. map\[]

Source results.

Map contents are:

1. int - Result Set,
1. SubcaseItem.
   2-1. int - ID
   2-1. string - Name,
   2-2. int - Status,
   2-4. bool - Enabled / Disabled.

## Return Code

Nothing.

## Sample Code

```psj
PostToolsSubcasePeakHoldEx(1, 0, 270, 130, 165, "Subcase 101 Peak Hold", 101, [(0, [(0, "Step=0, Time=1.000000e-02", 1,1), (1, "Step=1, Time=2.000000e-02", 1,1), (2, "Step=2, Time=3.000000e-02", 1,1), (3, "Step=3, Time=4.000000e-02", 1,1), (4, "Step=4, Time=5.000000e-02", 1,1), (5, "Step=5, Time=6.000000e-02", 1,0)])])
```
