---
title: "Assemble _Faces()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create assemble faces

## Syntax

```psj
Assemble _Faces(int[] id _mating _faces _list, double tol, int at _pos, double snap _tol, bool fit _edge)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

List id mating faces. Not empty

<!-- @since:5.0.1 -->
### 2. Double

Tolerance to find mating faces

<!-- @since:5.0.1 -->
### 3. Int

Connect position: 0 is mid-position, 1 is master position

<!-- @since:5.0.1 -->
### 4. Double

Snap tolerance to boundary edges

<!-- @since:5.0.1 -->
### 5. Bool

Fit edge: to keep circle edge shape: flag 0 : false, 1 : true

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Assemble _Faces([24, 49], 0.00022232, 1, 5e-05, 0)
```
