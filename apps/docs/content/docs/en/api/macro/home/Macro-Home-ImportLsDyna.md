---
title: "ImportLsDyna()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Import Ls-Dyna file

## Syntax

```psj
ImportLsDyna(string[] m _vecPath,double m _faceAngle,double m _edgeAngle)
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

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportLsDyna(["D:/Test.k"], 1.0472, 1.0472)
```
