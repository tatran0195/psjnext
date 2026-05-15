---
title: "ImportInpToPost()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import inp mesh as Post document.

## Syntax

```psj
ImportInpToPost(string FilePath, float faceAngle, float edgeAngle, int ImportType)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

File path.

<!-- @since:5.0.1 -->
### 2. float

Face Angle.

<!-- @since:5.0.1 -->
### 3. float

Edge Angle.

<!-- @since:5.0.1 -->
### 4. int

Import Type
0: Standard Abaqus Inp
1: Standard Abaqus Inp by Property

## Return Code

Nothing.

## Sample Code

```psj
ImportInpToPost(["C:/Temp/Data.inp"], 1.0472, 1.0472, 1)
```
