---
title: "MeasureTotalLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Measure the Load

## Syntax

```psj
MeasureTotalLoad(cursor[] target items, cursor coordinate, string target string, Integer N)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target Item cursors\[]

<!-- @since:5.0.1 -->
### 2. Cursor

coordinate cursor

<!-- @since:5.0.1 -->
### 3. String

output target string X/Y/Z/Total/ALL

<!-- @since:5.0.1 -->
### 4. Integer N

specify the number of decimal places (0{'<='}N{'<='}30)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeasureTotalLoad([],0:0,"ALL",6)
```
