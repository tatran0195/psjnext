---
title: "ImportGeomBDF()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Geometry bdf file

## Syntax

```psj
ImportGeomBDF(string[] vecPath, bool use _unit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Path directory

<!-- @since:5.0.1 -->
### 2. Bool

Use unit True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportGeomBDF(["D:/test.bdf"], 1)
```
