---
title: "TemperatureLoadGeneral()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create temperature load by constant value

## Syntax

```psj
TemperatureLoadGeneral(string strName, double dTemperature, cursor crTable,
    cursor[] taTarget, cursor crEdit, bool bUseAsMaterialReferenceTemp)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name of temperature load

<!-- @since:5.0.1 -->
### 2. Double

Temperature value

<!-- @since:5.0.1 -->
### 3. Cursor

Select table

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Targets

<!-- @since:5.0.1 -->
### 5. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 6. Bool

Use as material reference temperature bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TemperatureLoadGeneral("TemperatureLoadsConstant1", 303.15, 0:0, [6:21], 0:0, 0)
```
