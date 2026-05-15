---
title: "ASMSeparateShell()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Separate assembled faces in a shell model

## Syntax

```psj
ASMSeparateShell(int iType, int[] taKeyEntity, bool bCreateGroup)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Type option:

- 1: Parts
- 2: Edges

<!-- @since:5.0.1 -->
### 2. Int\[]

Entity cursor(\[Entity ID]) -> depend on Picked Type

<!-- @since:5.0.1 -->
### 3. Bool

Create group

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ASMSeparateShell(1, [4, 1], 0)
```
