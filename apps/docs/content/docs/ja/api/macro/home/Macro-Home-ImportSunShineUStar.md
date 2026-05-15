---
title: "ImportSunShineUStar()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import a SunShine UStar file (\*.op2) to the Jupiter Database.

## Syntax

```psj
ImportSunShineUStar(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle, bool bReadLoadAndConstraint, bool bReadConnection, bool bCreateResultsAtMidNode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying the path to the SunShine UStar file.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying import type.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether or not read load and contraint.

<!-- @since:5.1.0 -->
### 6. bool

- A Boolean specifying whether or not read connection.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether or not create results at mid node.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportSunShineUStar("path/to/the/file", 1, 60.0, 60.0, 0, 0, 0)
```
