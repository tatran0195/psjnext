---
title: "ImportMarcMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import a Marc file (.t16, .t19) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
ImportMarcMesh(str strPath, double dFaceAngle, double dEdgeAngle)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying the Marc file (\*.t16, \*.t19 files) which will be used for importing.

<!-- @since:5.1.0 -->
### 2. double

- A double specifying face angle.

<!-- @since:5.1.0 -->
### 3. double

- A double specifying edge angle.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportMarcMesh("path/to/the/file", 60.0, 60.0)
```
