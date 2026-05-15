---
title: "ImportBdf()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Nastran bdf file

## Syntax

```psj
ImportBdf(string[] vecPath, int importType, double faceAngle, double edgeAngle,
    bool readNameComment, int createDup1DElemAnswer)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Path directory

<!-- @since:5.0.1 -->
### 2. Int

Import type

- 0: Standard Nastran BDF
- 1: 1D2D3D-Part
- 2: 1D-Edge; 2D-Face; 3D-Part

<!-- @since:5.0.1 -->
### 3. Double

Face angle (radian)

<!-- @since:5.0.1 -->
### 4. Double

Edge angle (radian)

<!-- @since:5.0.1 -->
### 5. Bool

Read Name Comments for Jupiter True=1, False=0

<!-- @since:5.0.1 -->
### 6. Int

Create Dup 1D Element Answer

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportBdf(["D:/Test.bdf"], 2, 1.0472, 1.0472, 0, -1)
```
