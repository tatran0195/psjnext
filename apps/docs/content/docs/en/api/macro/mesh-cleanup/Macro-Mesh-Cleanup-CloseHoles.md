---
title: "CloseHoles()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Close Holes

## Syntax

```psj
CloseHoles(Cursor[] edge _list, double area _min, double area _max, bool merge _faces, bool merge _edges)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Edge List

<!-- @since:5.0.1 -->
### 2. Double

Area Min

<!-- @since:5.0.1 -->
### 3. Double

Area Max

<!-- @since:5.0.1 -->
### 4. Bool

Merge Faces. True=1, False=0

<!-- @since:5.0.1 -->
### 5. Bool

Merge Edges. True=1, False=0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CloseHoles([5:31, 5:35, 5:39, 5:45], 0, 0.54321, 0, 0)
```
