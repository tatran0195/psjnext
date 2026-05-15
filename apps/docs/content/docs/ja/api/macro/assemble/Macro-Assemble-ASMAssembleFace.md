---
title: "ASMAssembleFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Assemble multiple parts in a model

## Syntax

```psj
ASMAssembleFace(int[] taBodyKey, int[] taFaceKey, double tolerance, bool fitEdge, bool meshSetting)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Part key cursor(\[Part ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Face key cursor(\[Face ID])

<!-- @since:5.0.1 -->
### 3. Double

Mating tolerance

<!-- @since:5.0.1 -->
### 4. Bool

Imprint fit edge bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Mesh setting bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ASMAssembleFace([], [22, 47], 0.001, 0, 1)
```
