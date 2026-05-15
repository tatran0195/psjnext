---
title: "CmdImportTSVPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Result or Mesh file to Post Document

## Syntax

```psj
CmdImportTSVPost(string FilePath, int solverType, int importType, float faceAngle, float edgeAngle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

File path

<!-- @since:5.0.1 -->
### 2. int

_[Solver type](../../data-type/psj-utility/post-utility/enumeration-types/post-job-type.md)_.

<!-- @since:5.0.1 -->
### 3. int

Import type

<!-- @since:5.0.1 -->
### 4. float

Face Angle

<!-- @since:5.0.1 -->
### 5. float

Edge Angle

## Return Code

Nothing.

## Sample Code

```psj
CmdImportTSVPost("C:/Temp/sample.dat", 9, 1, 1.0472, 1.0472)
```
