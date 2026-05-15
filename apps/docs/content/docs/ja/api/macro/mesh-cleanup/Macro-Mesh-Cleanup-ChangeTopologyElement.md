---
title: "ChangeTopologyElement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change Topology Element

## Syntax

```psj
ChangeTopologyElement(int[] taElemKey, int[] taFaceKey, int[] taBodyKey, bool bCreateNewBody)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Element key cursor(\[Element ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Face key cursor(\[Face ID])

<!-- @since:5.0.1 -->
### 3. Int\[]

Part key cursor(\[Part ID])

<!-- @since:5.0.1 -->
### 4. Bool

Create new part bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeTopologyElement([2357, 2214, 2213, 2358], [], [1], 1)
```
