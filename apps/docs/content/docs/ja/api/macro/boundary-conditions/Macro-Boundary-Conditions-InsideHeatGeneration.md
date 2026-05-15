---
title: "InsideHeatGeneration()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create inside heat generation

## Syntax

```psj
InsideHeatGeneration(string strName, double dInsideFlux, cursor crTable, cursor[] crTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Inside heat generation name

<!-- @since:5.0.1 -->
### 2. Double

Inside flux value

<!-- @since:5.0.1 -->
### 3. Cursor

Table field data cursor

<!-- @since:5.0.1 -->
### 4. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 5. Cursor

Edit Cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
InsideHeatGeneration("InsideHeatGeneration3", 0.001, 81:1, [3:1], 0:0)
```
