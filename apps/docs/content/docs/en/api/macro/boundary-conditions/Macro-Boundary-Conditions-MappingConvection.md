---
title: "MappingConvection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mapping pressure

## Syntax

```psj
MappingConvection(String name, Cursor[] Target, int Position, int ViewCp, int Cp,
    int SourceType, int[6] MappedCpIndex, int[6] MappedCpIndex, double RScale,
    double[3] Offset, double[3] Rotate, double TScale, double seachRange, int HTCunit,
    int tempUnit, String path, Cursor editMapping)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name of mapping convection

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target list

<!-- @since:5.0.1 -->
### 3. Int

mapping position, 0: surface node, 1:solid node, 2:surface element, 3: solid element

<!-- @since:5.0.1 -->
### 4. Int

View component (Cp)

<!-- @since:5.0.1 -->
### 5. Int

component number, 2 for convection

<!-- @since:5.0.1 -->
### 6. Int

source data type, 0: fluent, 1: starCD, 2:text

<!-- @since:5.0.1 -->
### 7. Int\[6]

Mapped Cp Index List

<!-- @since:5.0.1 -->
### 8. Int\[6]

Mapped Cp Index List

<!-- @since:5.0.1 -->
### 9. Double

Rscale

<!-- @since:5.0.1 -->
### 10. Double\[3]

Offset List

<!-- @since:5.0.1 -->
### 11. Double\[3]

Rotate List

<!-- @since:5.0.1 -->
### 12. Double

Tscale

<!-- @since:5.0.1 -->
### 13. Double

Search range

<!-- @since:5.0.1 -->
### 14. Int

HTC Unit

<!-- @since:5.0.1 -->
### 15. Int

Temperature unit

<!-- @since:5.0.1 -->
### 16. String

Path

<!-- @since:5.0.1 -->
### 17. Cursor

Edit mapping convection

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MappingConvection("MappingConvection2", [6:23], 2, 0, 2, 2, 0, 1, 1, [0, 0, 0],
    [1, 0, 0], 1, 0, 0, 1, "D:/wj-block-cold.csv", 0:0)
```
