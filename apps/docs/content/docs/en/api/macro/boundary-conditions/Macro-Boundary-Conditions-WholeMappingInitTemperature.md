---
title: "WholeMappingInitTemperature()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create initial temperature by whole mapping

## Syntax

```psj
WholeMappingInitTemperature(cursor[] targetpParts, string strName, int iMappingSrcType, string strPath, int iMappingMethod, int iMappingFromStepNo, int iLocalUnit, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Target parts

<!-- @since:5.1.0 -->
### 2. String

Temperature load name

<!-- @since:5.1.0 -->
### 3. Int

Result type

- 0: Nastran
- 1: Abaqus
- 2: ADVC format2
- 3: CSV

<!-- @since:5.1.0 -->
### 4. String

directory file path name

<!-- @since:5.1.0 -->
### 5. Int

Mapping method type

<!-- @since:5.1.0 -->
### 6. Int

Mapping step (subcase) value

<!-- @since:5.1.0 -->
### 7. Int

Unit of Temperature

<!-- @since:5.1.0 -->
### 8. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
WholeMappingInitTemperature([], "TemperatureInitsWholeMapping _1", 0, "C:/Temp/transient.op2", 0, 0, 1, 0:0)
```
