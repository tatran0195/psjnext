---
title: "ExportDynamisBdf()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export Dynamis bdf file

## Syntax

```psj
ExportDynamisBdf(string strPath, TCursor job)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

bdf file path

<!-- @since:5.0.1 -->
### 2. Cursor

job cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportDynamisBdf("D:/TS-Solver.bdf", 148:2)
```
