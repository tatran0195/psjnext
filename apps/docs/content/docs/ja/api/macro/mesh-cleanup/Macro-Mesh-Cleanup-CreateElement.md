---
title: "CreateElement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create element based on nodes

## Syntax

```psj
CreateElement(int iElemType, int iParentEntity, int[] viNodeKey)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Create element type

- 0: TRI3
- 1: QUAD4

<!-- @since:5.0.1 -->
### 2. Int

Parent face key cursor(Face ID)

<!-- @since:5.0.1 -->
### 3. Int\[]

Node key cursor(\[Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateElement(0, 24, [85, 489, 83])
```
