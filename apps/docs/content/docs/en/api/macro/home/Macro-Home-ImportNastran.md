---
title: "ImportNastran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import Nastran / Vibro result file.

## Syntax

```psj
ImportNastran(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle, bool bReadLoadAndConstraint, bool bReadConnection, bool bCreateResultsAtMidNode, bool bIsVibro)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying nastran result file path.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying import type.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether or not read load and constraint.

<!-- @since:5.1.0 -->
### 6. bool

- A Boolean specifying whether or not read connection.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether or not create results at mid node.

<!-- @since:5.1.0 -->
### 8. bool

- A Boolean specifying whether or not the file is Vibro Acoustic.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportNastran("path/to/the/file", 1, 60.0, 60.0, 0, 0, 0, 0)
```
