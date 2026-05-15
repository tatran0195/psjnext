---
title: "WholeMappingTemperatureLoad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create temperature load

## Syntax

```psj
WholeMapping(string strName, int iMappingSrcType, string strPath, int iMappingMethod,
    int iMappingFromStepNo, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Temperature load name

<!-- @since:5.0.1 -->
### 2. Int

Result type

- 0: Nastran
- 1: Abaqus
- 2: ADVC format2
- 3: CSV

<!-- @since:5.0.1 -->
### 3. String

directory file path name

<!-- @since:5.0.1 -->
### 4. Int

Mapping method type

<!-- @since:5.0.1 -->
### 5. Int

Mapping step (subcase) value

<!-- @since:5.0.1 -->
### 6. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
WholeMappingTemperatureLoad("TemperatureLoadsWholeMapping1", 3, "D:/CFD _Large _ForWholeMapping.csv", 0, 0, 0:0)
```
