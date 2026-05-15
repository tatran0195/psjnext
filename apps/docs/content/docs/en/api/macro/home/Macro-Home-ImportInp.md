---
title: "ImportInp()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Abaqus INP file

## Syntax

```psj
ImportInp(string[] m _vecPath,double m _faceAngle,double m _edgeAngle, int iImportType)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Multiple files Path

<!-- @since:5.0.1 -->
### 2. Double

Face angle

<!-- @since:5.0.1 -->
### 3. Double

Edge angle

<!-- @since:5.0.1 -->
### 4. Int

Import type

- 0: Standard Abaqus Inp
- 1: Standard Abaqus Inp by Property

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportInp(["D:/Test.inp"], 1.0472, 1.0472, 1)
```
