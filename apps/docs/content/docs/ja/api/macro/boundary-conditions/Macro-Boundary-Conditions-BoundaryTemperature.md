---
title: "BoundaryTemperature()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create boundary temperature

## Syntax

```psj
BoundaryTemparature(string strName, double fTemp, cursor crTable, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Boundary temperature name

<!-- @since:5.0.1 -->
### 2. Double

Temperature value

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
BoundaryTemperature("BoundaryTemperature _1", 373.15, 81:1, [3:1, 6:3], 0:0)
```
