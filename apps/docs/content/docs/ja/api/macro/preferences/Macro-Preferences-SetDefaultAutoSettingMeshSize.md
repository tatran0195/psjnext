---
title: "SetDefaultAutoSettingMeshSize()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Turn ON/OFF Data Validation.

## Syntax

```psj
SetDefaultAutoSettingMeshSize(int Selection, float Maximum, float Minimum)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Select setting type

- 0: Average
- 1: Minimum
- 2: Maximum

<!-- @since:5.1.0 -->
### 2. float

Coefficent for Maximum mesh size.

<!-- @since:5.1.0 -->
### 3. float

Coefficent for Minimum mesh size.

## Return Code

No return code.

## Sample Code

```psj
SetDefaultAutoSettingMeshSize(1, 2, 0.2)
```
