---
title: "ImportPreFrontISTR()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import FrontISTR result file.

## Syntax

```psj
ImportPreFrontISTR(str strPath, double dFaceAngle, double dEdgeAngle)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying FrontISTR file path.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value). Unit: radian.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value). Unit: radian.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportPreFrontISTR("path/to/the/file", 1.04072, .04072)
```
