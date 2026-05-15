---
title: "ImportAnsysResult()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import Ansys result file.

## Syntax

```psj
ImportAnsysResult(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying ansys result file path.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying import type.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportAnsysResult("path/to/the/file", 1, 60.0, 60.0)
```
