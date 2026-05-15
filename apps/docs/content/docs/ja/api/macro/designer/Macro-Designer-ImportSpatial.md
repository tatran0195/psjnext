---
title: "ImportSpatial()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import CAD file by Spatial interface

## Syntax

```psj
ImportSpatial(String[] vecPath, double surface _plane _tolerance, double surface _plane _angle,
    double max _facet _width, int isNXDirect)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

multiple CAD file paths

<!-- @since:5.0.1 -->
### 2. Double

surface plane tolerance option

<!-- @since:5.0.1 -->
### 3. Double

surface plane angle option

<!-- @since:5.0.1 -->
### 4. Double

max facet width option

<!-- @since:5.0.1 -->
### 5. Int

flag of NXDirect

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportSpatial(["D:/assy1.sat"], 0.002, 30, 0, 0)
```
