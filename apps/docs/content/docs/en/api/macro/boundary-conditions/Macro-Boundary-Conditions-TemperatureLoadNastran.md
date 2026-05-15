---
title: "TemperatureLoadNastran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create temperature load by Nastran punch file

## Syntax

```psj
TemperatureLoadNastran(string strName, string strFilePathName, cursor crTable,
    cursor[] taTarget, cursor crEdit, bool bUseAsMaterialReferenceTemp)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of temperature load

<!-- @since:5.0.1 -->
### 2. String

file path

<!-- @since:5.0.1 -->
### 3. Cursor

select table

<!-- @since:5.0.1 -->
### 4. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 5. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 6. Bool

if use as material reference temperature

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TemperatureLoadNastran("TemperatureLoadsPunch1", "D:/1 _heat.pch", 0:0, [], 0:0, 0)
```
