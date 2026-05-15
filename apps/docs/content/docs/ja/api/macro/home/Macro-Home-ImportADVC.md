---
title: "ImportADVC()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import ADVC result file.

## Syntax

```psj
ImportADVC(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle, bool bADVCProcessNameRule, bool bDisplayNAResult, str strSelectResultFilePath)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying ADVC result folder path.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying import type:

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether or not ADVC process IDs defined on the ADVC side are displayed.

<!-- @since:5.1.0 -->
### 6. bool

- A Boolean specifying whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

<!-- @since:5.1.0 -->
### 7. str

- A String specifying result file path.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportADVC("path/to/the/file", 1, 60.0, 60.0, 1, 1, "")
```
