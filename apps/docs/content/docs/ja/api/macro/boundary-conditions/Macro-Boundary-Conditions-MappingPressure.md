---
title: "MappingPressure()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mapping pressure

## Syntax

```psj
MappingPressure(string name, Cursor[] target, int pos, int conflictMode, int component,
    int srcType, int mappedComponentIndex, double dSclFact, double[3] transitionVct, double[3] rotVct,
    double coordScl, double dSearchRange, int iInputUnit, string strDataScrFile, Cursor editCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of mapping pressure

<!-- @since:5.0.1 -->
### 2. Cursor\[]

mapping target entities

<!-- @since:5.0.1 -->
### 3. Int

mapping position, 0: surface node, 1:solid node, 2:surface element, 3: solid element

<!-- @since:5.0.1 -->
### 4. Int

how to deal conflict case

<!-- @since:5.0.1 -->
### 5. Int

component number, 1 for pressure

<!-- @since:5.0.1 -->
### 6. Int

source data type, 0: fluent, 1: starCD, 2:text

<!-- @since:5.0.1 -->
### 7. Int

pressure data index in file

<!-- @since:5.0.1 -->
### 8. Double

Scale factor for mapping pressure

<!-- @since:5.0.1 -->
### 9. Double\[3]

Transition vector

<!-- @since:5.0.1 -->
### 10. Double\[3]

Rotation vector

<!-- @since:5.0.1 -->
### 11. Double

Coordinate scale value

<!-- @since:5.0.1 -->
### 12. Double

Search range

- 0: Auto search range
- Value: Tolerance search range

<!-- @since:5.0.1 -->
### 13. Int

Input Unit

- 0: MPa
- 1: Pa
- 2: kPa
- 3: kgf/mm^2
- 4: lbf/ft^2
- 5: tf/m^2
- 6: GPa

<!-- @since:5.0.1 -->
### 14. string

pressure data index in file

<!-- @since:5.0.1 -->
### 15. Cursor

Edit mapping pressure

## Return Code

- "0": The function cannot be executed

## Sample Code

```psj
MappingPressure("MappingPressure1", [6:30, 6:22], 2, 0, 1, 1, -1, 1, [0, 0, 0],
    [0, 0, 0], 1, 0, 0, "D:/Fluent.dat", 0:0)
```
