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
ImportBdf(String[] vecPath, int importType, double faceAngle, double edgeAngle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

multiple bdf file paths

<!-- @since:5.0.1 -->
### 2. Int

Import type

<!-- @since:5.0.1 -->
### 3. Double

face angle (radian)

<!-- @since:5.0.1 -->
### 4. Double

edge angle (radian)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportBdf(["D:/test.bdf"], 2, 1.0472, 1.0472)
```
