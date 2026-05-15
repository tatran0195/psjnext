---
title: "HexBoxMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Box hex mesh creator for parts

## Syntax

```psj
HexBoxMesh(int[] taBodyKey, double dMeshSize, string sMaterialName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Body ID

<!-- @since:5.0.1 -->
### 2. Double

Box mesh size

<!-- @since:5.0.1 -->
### 3. String

Material Name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexBoxMesh([1], 0.002, "Magnesium _Alloy")
```
