---
title: "CmdImportTSVWAONPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import WAON result file to the Jupiter Database.

## Syntax

```psj
CmdImportTSVWAONPost(str strPath, str strFPMFilePath, str strResultFolderPath, int iImportType, double dFaceAngle, double dEdgeAngle, bool bReadLoadAndConstraint, bool bReadConnection, bool bCreateResultsAtMidNode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying BEM file (.bdf).

<!-- @since:5.1.0 -->
### 2. str

- A String specifying FPM file (.bdf).

<!-- @since:5.1.0 -->
### 3. str

- A String specifying result folder.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying import type. For WAON file, it is always set to 1.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether or not read load and contraint.

<!-- @since:5.1.0 -->
### 8. bool

- A Boolean specifying whether or not read connection.

<!-- @since:5.1.0 -->
### 9. bool

- A Boolean specifying whether or not create results at mid node.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdImportTSVWAONPost("C:/Temp/", "C:/Temp/BEM.bdf", "C:/Temp/FPM.bdf", 1, 60.0, 60.0, 0, 0, 0)
```
