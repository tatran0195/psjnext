---
title: "ImportAnsys()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Ansys file

## Syntax

```psj
ImportAnsys(string[] vecPath, double faceAngle, double edgeAngle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String\[]

Path directory

<!-- @since:5.0.1 -->
### 2. Double

Face angle

<!-- @since:5.0.1 -->
### 3. Double

Edge angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportAnsys(["D:/Test.dat"], 1.0472, 1.0472)
```
