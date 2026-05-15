---
title: "ExportAdx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export ADX file

## Syntax

```psj
ExportAdx(cursor crJobAdx, string strPath, int NumType, int Width, int Precision)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

cursor of job exported

<!-- @since:5.0.1 -->
### 2. String

path of adx file

<!-- @since:5.0.1 -->
### 3. Int

number of type

<!-- @since:5.0.1 -->
### 4. Int

width

<!-- @since:5.0.1 -->
### 5. Int

precision

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportAdx(130:1, "D:/ADVC.adx", 2, 10, 5)
```
