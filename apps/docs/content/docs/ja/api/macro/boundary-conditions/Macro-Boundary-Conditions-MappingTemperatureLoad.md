---
title: "MappingTemperatureLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mapping pressure

## Syntax

```psj
MappingTemperatureLoad(String name, Cursor[] target, int pos, int conflictMode,
    int component, int srcType, int mappedComponentIndex,double rltScale,
    double[3] tOffset, double[3] tRotateAngle, double tScale, String path, Cursor editObj )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of mapping temperature

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

component number, 1 for temperature

<!-- @since:5.0.1 -->
### 6. Int

source data type, 0: fluent, 1: starCD, 2:text

<!-- @since:5.0.1 -->
### 7. Int

temperature data index in file

<!-- @since:5.0.1 -->
### 8. Double

scale for result data

<!-- @since:5.0.1 -->
### 9. Double\[3]

transform offset vector

<!-- @since:5.0.1 -->
### 10. Double\[3]

rotate angle vector

<!-- @since:5.0.1 -->
### 11. Double

transform scale

<!-- @since:5.0.1 -->
### 12. String

data source file

<!-- @since:5.0.1 -->
### 13. Cursor

used for edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MappingTemperatureLoad("Mapping", [], 2, 0, 1, 0, 0, 1, [0, 0, 0], [0, 0, 0], 1, "D:\Fluent.dat", 0:0)
```
