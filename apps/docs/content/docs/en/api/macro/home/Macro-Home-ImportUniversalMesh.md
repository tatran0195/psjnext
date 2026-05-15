---
title: "ImportUniversalMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import an Universal file (\*.unv) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
ImportUniversalMesh(str[] strlPaths, doubledFaceAngle, double dEdgeAngle)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str\[]

- A List of String specifying a list of the Universal files (\*.unv file) which will be used for importing.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the angle tolerance in order to determine the face division.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the edge division.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportUniversalMesh(["path/to/the/file"], 60.0, 60.0)
```
