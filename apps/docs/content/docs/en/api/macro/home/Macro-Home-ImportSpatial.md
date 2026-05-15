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
ImportSpatial(string[] vecPath, double surface _plane _tolerance, double suface _plane _angle,
    double max _facet _width, int NX _multibody, int healing, int isNXDirect, int setFaceColor,
    String facetParamCsvFile)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Multiple CAD file paths

<!-- @since:5.0.1 -->
### 2. Double

Surface plane tolerance option

<!-- @since:5.0.1 -->
### 3. Double

Suface plane angle option

<!-- @since:5.0.1 -->
### 4. Double

Max facet width option

<!-- @since:5.0.1 -->
### 5. Int

Flag of NX Multibody

<!-- @since:5.0.1 -->
### 6. Int

Flag of healing option

<!-- @since:5.0.1 -->
### 7. Int

Flag of NXDirect

<!-- @since:5.0.1 -->
### 8. Int

Flag of setting face color option

<!-- @since:5.0.1 -->
### 9. String

Facet parameter csv file path

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportSpatial(["D:/Test.sat"], 0, 20, 0.1, 1, 1, 0, 1, "")
```
