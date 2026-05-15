---
title: "CmdImportTSVBdfPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import a Nastran mesh file to the Jupiter Database as Post document to add result to the mesh.

## Syntax

```psj
CmdImportTSVBdfPost(str strPath, int iImportType, double dFaceAngle, double dEdgeAngle, bool bReadLoadAndConstraint, bool bReadConnection, bool bReadNX)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying a Nastran files which will be used for importing.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying import type.

<!-- @since:5.1.0 -->
### 3. double

- An Integer specifying import type. Here is set to always 1.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether or not to read loads and constraint.

<!-- @since:5.1.0 -->
### 6. bool

- A Boolean specifying whether or not to read connections.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether or not to read NX.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdImportTSVBdfPost("path/to/the/file", 1, 60.0, 60.0, 1, 1, 1)
```
