---
title: "CmdImportTSVBdfPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Nastran BDF file to Post Document

## Syntax

```psj
CmdImportTSVBdfPost(string FilePath, int importType, float faceAngle, float edgeAngle, int readLoadAndConst, int readConnection)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

File path

<!-- @since:5.0.1 -->
### 2. int

Import type. Set to 0.

<!-- @since:5.0.1 -->
### 3. float

Face Angle

<!-- @since:5.0.1 -->
### 4. float

Edge Angle

<!-- @since:5.0.1 -->
### 5. bool

Read Load and Constraint flag

<!-- @since:5.0.1 -->
### 6. bool

Read Connection flag

## Return Code

Nothing.

## Sample Code

```psj
CmdImportTSVBdfPost("C:/temp/sample.bdf", 1, 1.0472, 1.0472, 0, 0)
```
