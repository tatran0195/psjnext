---
title: "ImportInpToPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import an Abaqus mesh file (\*.inp) to the Jupiter Database (Mesh, boundary conditions, etc.) as Post document to add result to the mesh.

## Syntax

```psj
ImportInpToPost(str strPath, double dFaceAngle, double dEdgeAngle, int iImportType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying specifying an Abaqus file (\*.inp file) which will be used for importing.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 -->
### 4. int

- A interger specifying the type of

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportInpToPost("path/to/the/file", 60.0, 60.0, 1)
```
