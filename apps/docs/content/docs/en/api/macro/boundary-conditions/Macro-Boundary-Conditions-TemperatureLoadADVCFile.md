---
title: "TemperatureLoadADVCFile()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create temperature load by advc file

## Syntax

```psj
TemperatureLoadADVCFile(string strName, string strFilePathName, cursor crTable, cursor[] taTarget, cursor crEdit)
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

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TemperatureLoadGeneral("TemperatureLoadsConstant1", 303.15, 0:0, [6:21], 0:0, 0)
```
